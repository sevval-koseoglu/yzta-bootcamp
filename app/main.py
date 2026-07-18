import re
import streamlit as st

st.set_page_config(page_title="Scam Message Detector", page_icon="🛡️", layout="wide")

st.title("Scam Message Detector")
st.write("Türkçe SMS, e-posta ve mesaj içerikleri için temel dolandırıcılık risk analizi.")

message = st.text_area(
    "Analiz edilecek mesajı girin:",
    height=180,
    placeholder="Örnek: Kargonuz beklemede. Teslimat için 24 saat içinde ödeme yapınız..."
)

def analyze_message(text):
    risks = []
    score = 0

    url_pattern = r"(https?://\S+|www\.\S+)"
    phone_pattern = r"(\+90|0)?\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}"
    iban_pattern = r"TR\d{2}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\s?\d{2}"

    urgency_words = ["acil", "hemen", "24 saat", "son gün", "iptal", "bloke"]
    payment_words = ["ödeme", "para", "ücret", "kart", "iban", "havale"]
    institution_words = ["kargo", "banka", "e-devlet", "ptt", "çekiliş", "burs"]

    if re.search(url_pattern, text, re.IGNORECASE):
        risks.append("Mesaj içerisinde bağlantı/link bulunuyor.")
        score += 25

    if re.search(phone_pattern, text):
        risks.append("Mesaj içerisinde telefon numarası bulunuyor.")
        score += 10

    if re.search(iban_pattern, text.replace(" ", ""), re.IGNORECASE):
        risks.append("Mesaj içerisinde IBAN formatına benzeyen ifade bulunuyor.")
        score += 25

    if any(word in text.lower() for word in urgency_words):
        risks.append("Mesajda aciliyet veya baskı oluşturan ifadeler bulunuyor.")
        score += 20

    if any(word in text.lower() for word in payment_words):
        risks.append("Mesajda ödeme veya para talebi bulunuyor.")
        score += 20

    if any(word in text.lower() for word in institution_words):
        risks.append("Mesaj bir kurum veya hizmet taklidi içeriyor olabilir.")
        score += 15

    score = min(score, 100)

    if score >= 70:
        level = "Yüksek Risk"
    elif score >= 40:
        level = "Orta Risk"
    else:
        level = "Düşük Risk"

    return score, level, risks

if st.button("Mesajı Analiz Et"):
    if not message.strip():
        st.warning("Lütfen analiz edilecek bir mesaj girin.")
    else:
        score, level, risks = analyze_message(message)

        st.subheader("Analiz Sonucu")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.metric("Risk Skoru", f"{score}/100")
            st.write(f"**Risk Seviyesi:** {level}")

        with col2:
            st.write("**Şüpheli Noktalar:**")
            if risks:
                for risk in risks:
                    st.write(f"- {risk}")
            else:
                st.write("- Belirgin bir risk sinyali bulunamadı.")

        st.info("Öneri: Şüpheli bağlantılara tıklamayın. İşlemi ilgili kurumun resmi web sitesi veya mobil uygulaması üzerinden kontrol edin.")
