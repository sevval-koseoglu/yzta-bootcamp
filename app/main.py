import streamlit as st

from analyzer import analyze_message

st.set_page_config(page_title="Scam Message Detector", page_icon="🛡️", layout="wide")

st.title("Scam Message Detector")
st.write("Türkçe SMS, e-posta ve mesaj içerikleri için açıklanabilir dolandırıcılık risk analizi.")

message = st.text_area(
    "Analiz edilecek mesajı girin:",
    height=180,
    placeholder="Örnek: Kargonuz beklemede. Teslimat için 24 saat içinde ödeme yapınız..."
)

if st.button("Mesajı Analiz Et"):
    if not message.strip():
        st.warning("Lütfen analiz edilecek bir mesaj girin.")
    else:
        score, level, findings = analyze_message(message)

        st.subheader("Analiz Sonucu")

        if level == "Yüksek Risk":
            st.error("Bu mesaj birden fazla güçlü dolandırıcılık sinyali içeriyor.")
        elif level == "Orta Risk":
            st.warning("Bu mesaj bazı şüpheli sinyaller içeriyor. İşlem yapmadan önce doğrulayın.")
        else:
            st.success("Mesajda belirgin veya güçlü bir dolandırıcılık sinyali bulunamadı.")

        col1, col2 = st.columns([1, 2])

        with col1:
            st.metric("Risk Skoru", f"{score}/100")
            st.write(f"**Risk Seviyesi:** {level}")
            st.progress(score / 100)

        with col2:
            st.write("**Şüpheli Noktalar:**")
            if findings:
                for finding in findings:
                    st.write(f"- {finding['description']} (+{finding['points']} puan)")
            else:
                st.write("- Belirgin bir risk sinyali bulunamadı.")

        st.subheader("Güvenli Aksiyon Önerisi")
        if level == "Yüksek Risk":
            st.error(
                "Bağlantıya tıklamayın, ödeme yapmayın ve kişisel bilgi paylaşmayın. "
                "Mesajdaki iletişim bilgilerini kullanmadan ilgili kurumun resmi web sitesi "
                "veya mobil uygulaması üzerinden durumu kontrol edin."
            )
        elif level == "Orta Risk":
            st.warning(
                "Mesajı gönderen kişi veya kurumu bağımsız bir kanaldan doğrulayın. "
                "Doğrulama tamamlanana kadar bağlantıya tıklamayın ve ödeme yapmayın."
            )
        else:
            st.info(
                "Belirgin bir risk sinyali bulunmadı. Yine de tanımadığınız göndericilerden "
                "gelen bağlantı ve dosyalara karşı dikkatli olun."
            )

        st.caption(
            "Bu araç farkındalık amacıyla hazırlanmıştır ve kesin güvenlik kararı vermez. "
            "Şüphe durumunda ilgili kurumla resmi kanallardan iletişime geçin."
        )