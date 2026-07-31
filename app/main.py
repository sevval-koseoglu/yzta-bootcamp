import streamlit as st

from ai_analyzer import get_ai_interpretation
from analyzer import analyze_message
from history import clear_analyses, get_analyses, get_dashboard_stats, save_analysis

st.set_page_config(page_title="Scam Message Detector", page_icon="🛡️", layout="wide")

st.title("Scam Message Detector")
st.write("Türkçe SMS, e-posta ve mesaj içerikleri için açıklanabilir dolandırıcılık risk analizi.")

analysis_tab, history_tab, dashboard_tab = st.tabs(["Mesaj Analizi", "Analiz Geçmişi", "Dashboard"])

with analysis_tab:

    message = st.text_area(
        "Analiz edilecek mesajı girin:",
        height=180,
        placeholder="Örnek: Kargonuz beklemede. Teslimat için 24 saat içinde ödeme yapınız..."
    )

    use_ai = st.checkbox(
        "Yapay zekâ destekli bağlamsal yorum oluştur",
        value=True,
        help="Mesajdaki telefon, IBAN ve uzun numaralar maskelendikten sonra Gemini ile yorumlanır.",
    )

    if st.button("Mesajı Analiz Et", type="primary"):
        if not message.strip():
            st.warning("Lütfen analiz edilecek bir mesaj girin.")
        else:
            score, level, findings = analyze_message(message)
            save_analysis(message, score, level)

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

            if use_ai:
                st.subheader("Yapay Zekâ Destekli Yorum")
                try:
                    with st.spinner("Mesajın bağlamı değerlendiriliyor..."):
                        ai_interpretation = get_ai_interpretation(
                        message=message,
                        score=score,
                        level=level,
                        findings=findings,
                        )
                    st.markdown(ai_interpretation)
                    st.caption("AI modeli: Gemini 3.5 Flash")
                except ValueError:
                    st.info(
                    "Yapay zekâ yorumu için GEMINI_API_KEY tanımlanmalıdır. "
                    "Kural tabanlı analiz kullanılmaya devam ediyor."
                    )
                except Exception:
                    st.warning(
                    "Yapay zekâ servisine şu anda ulaşılamadı. "
                    "Kural tabanlı analiz kullanılmaya devam ediyor."
                    )

with history_tab:
    st.subheader("Analiz Geçmişi")
    st.caption("Gizlilik için mesajlardaki hassas numaralar maskelenerek saklanır.")
    analyses = get_analyses()
    if analyses:
        st.dataframe(
            [
                {
                    "Tarih": item["created_at"].replace("T", " "),
                    "Mesaj Özeti": item["message_summary"],
                    "Risk Skoru": item["score"],
                    "Risk Seviyesi": item["level"],
                }
                for item in analyses
            ],
            use_container_width=True,
            hide_index=True,
        )
        if st.button("Analiz Geçmişini Temizle"):
            clear_analyses()
            st.rerun()
    else:
        st.info("Henüz kaydedilmiş bir analiz bulunmuyor.")

with dashboard_tab:
    st.subheader("Analiz Dashboard'u")
    stats = get_dashboard_stats()
    metric1, metric2, metric3 = st.columns(3)
    metric1.metric("Toplam Analiz", stats["total"])
    metric2.metric("Ortalama Risk Skoru", f"{stats['average_score']}/100")
    high_ratio = (stats["distribution"]["Yüksek Risk"] / stats["total"] * 100) if stats["total"] else 0
    metric3.metric("Yüksek Risk Oranı", f"%{high_ratio:.1f}")

    if stats["total"]:
        chart_data = {
            "Risk Seviyesi": list(stats["distribution"].keys()),
            "Analiz Sayısı": list(stats["distribution"].values()),
        }
        st.bar_chart(chart_data, x="Risk Seviyesi", y="Analiz Sayısı", color="#d9534f")
        st.write("**Son Analizler**")
        st.dataframe(
            get_analyses(limit=5),
            use_container_width=True,
            hide_index=True,
            column_config={"id": None},
        )
    else:
        st.info("Dashboard verileri, ilk mesaj analizinden sonra burada görüntülenecek.")
