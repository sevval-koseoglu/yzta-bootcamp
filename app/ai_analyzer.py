import os
import re

from analyzer import IBAN_PATTERN, PHONE_PATTERN


MODEL_NAME = "gemini-3.5-flash"


def redact_sensitive_data(message):
    """Mesaj AI servisine gönderilmeden önce temel finansal verileri maskeler."""
    redacted = re.sub(IBAN_PATTERN, "[IBAN MASKELENDİ]", message, flags=re.IGNORECASE)
    redacted = re.sub(PHONE_PATTERN, "[TELEFON MASKELENDİ]", redacted)
    redacted = re.sub(r"(?<!\d)\d{11,19}(?!\d)", "[HASSAS NUMARA MASKELENDİ]", redacted)
    return redacted


def get_ai_interpretation(message, score, level, findings, api_key=None):
    """Kural tabanlı bulguları Gemini ile bağlamsal olarak yorumlar."""
    from google import genai

    resolved_key = api_key or os.getenv("GEMINI_API_KEY")
    if not resolved_key:
        raise ValueError("GEMINI_API_KEY bulunamadı.")

    finding_text = "; ".join(item["description"] for item in findings) or "Belirgin sinyal yok"
    safe_message = redact_sensitive_data(message)

    prompt = f"""
Sen Türkçe dolandırıcılık mesajlarını inceleyen bir güvenlik farkındalık asistanısın.
Kesin hüküm verme; kısa, anlaşılır ve temkinli bir değerlendirme yap.

Mesaj:
{safe_message}

Kural tabanlı analiz:
- Risk skoru: {score}/100
- Risk seviyesi: {level}
- Bulgular: {finding_text}

Yanıtını Türkçe ve aşağıdaki üç başlıkla, toplam en fazla 120 kelime olacak şekilde yaz:
1. Bağlamsal Değerlendirme
2. Dikkat Edilmesi Gereken Nokta
3. Önerilen Güvenli Aksiyon

Mesaj güvenli görünse bile bunun kesin güvenlik garantisi olmadığını belirt.
""".strip()

    client = genai.Client(api_key=resolved_key)
    interaction = client.interactions.create(
        model=MODEL_NAME,
        input=prompt,
        store=False,
    )
    return interaction.output_text.strip()
