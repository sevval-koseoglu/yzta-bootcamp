import re


URL_PATTERN = r"(?:https?://|www\.)[^\s]+"
PHONE_PATTERN = r"(?<!\d)(?:(?:\+90|0)\s*)?5\d{2}[\s.-]*\d{3}[\s.-]*\d{2}[\s.-]*\d{2}(?!\d)"
IBAN_PATTERN = r"TR\d{2}(?:\s?\d{4}){5}\s?\d{2}"


KEYWORD_GROUPS = {
    "urgency": ["acil", "hemen", "24 saat", "son gün", "son şans", "süre doluyor", "gecikmeden"],
    "payment": ["ödeme", "para gönder", "ücret", "havale", "eft", "yatırmanız", "borcunuz"],
    "personal_info": [
        "tc kimlik", "kimlik numarası", "kart numarası", "kart bilgileri",
        "cvv", "şifre", "parola", "doğrulama kodu", "sms kodu",
    ],
    "prize": ["ödül kazandınız", "çekiliş kazandınız", "hediye kazandınız", "ücretsiz hediye"],
    "threat": [
        "hesabınız kapatılacak", "hesabınız bloke", "kartınız bloke",
        "icra işlemi", "yasal işlem", "erişiminiz durdurulacak",
    ],
    "institution": ["kargo", "banka", "e-devlet", "edevlet", "ptt", "vergi dairesi", "belediye"],
}


def normalize_text(text):
    """Türkçe büyük harfleri anahtar kelime aramasına uygun biçimde küçültür."""
    return text.translate(str.maketrans({"I": "ı", "İ": "i"})).lower()


def contains_keyword(text, group):
    return any(keyword in text for keyword in KEYWORD_GROUPS[group])


def analyze_message(text):
    normalized = normalize_text(text)
    compact_text = re.sub(r"\s+", "", text)
    findings = []

    flags = {
        "url": bool(re.search(URL_PATTERN, text, re.IGNORECASE)),
        "phone": bool(re.search(PHONE_PATTERN, text)),
        "iban": bool(re.search(IBAN_PATTERN, compact_text, re.IGNORECASE)),
        **{group: contains_keyword(normalized, group) for group in KEYWORD_GROUPS},
    }

    def add_finding(code, description, points):
        findings.append({"code": code, "description": description, "points": points})

    if flags["url"]:
        add_finding("url", "Mesaj içerisinde dış bağlantı bulunuyor.", 20)
    if flags["phone"]:
        add_finding("phone", "Mesaj içerisinde cep telefonu numarası bulunuyor.", 5)
    if flags["iban"]:
        add_finding("iban", "Mesaj içerisinde IBAN formatına benzeyen bir ifade bulunuyor.", 20)
    if flags["urgency"]:
        add_finding("urgency", "Mesaj hızlı hareket etmeye zorlayan aciliyet ifadeleri içeriyor.", 15)
    if flags["payment"]:
        add_finding("payment", "Mesajda ödeme veya para gönderme talebi bulunuyor.", 15)
    if flags["personal_info"]:
        add_finding("personal_info", "Mesajda kişisel, kart veya doğrulama bilgisi isteniyor.", 25)
    if flags["prize"]:
        add_finding("prize", "Mesajda ödül, hediye veya çekiliş vaadi bulunuyor.", 15)
    if flags["threat"]:
        add_finding("threat", "Mesajda hesap kapatma, bloke veya yasal işlem tehdidi bulunuyor.", 15)

    # Tek başına kurum adı risk sayılmaz; başka sinyallerle birlikte taklit ihtimalini artırır.
    suspicious_context = any(
        flags[key] for key in ("url", "iban", "urgency", "payment", "personal_info", "prize", "threat")
    )
    if flags["institution"] and suspicious_context:
        add_finding("institution_context", "Mesaj bir kurum veya hizmeti taklit ediyor olabilir.", 10)

    # Birlikte görüldüğünde dolandırıcılık ihtimalini belirgin biçimde artıran sinyaller.
    if flags["url"] and flags["payment"]:
        add_finding("url_payment", "Ödeme talebi bir dış bağlantıyla birlikte sunuluyor.", 10)
    if flags["urgency"] and flags["payment"]:
        add_finding("urgency_payment", "Ödeme talebi aciliyet baskısıyla birlikte kullanılıyor.", 10)
    if flags["url"] and flags["personal_info"]:
        add_finding("url_personal_info", "Bağlantı üzerinden hassas bilgi paylaşılması isteniyor olabilir.", 10)

    score = min(sum(item["points"] for item in findings), 100)

    if score >= 60:
        level = "Yüksek Risk"
    elif score >= 25:
        level = "Orta Risk"
    else:
        level = "Düşük Risk"

    return score, level, findings