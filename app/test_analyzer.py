import unittest

from analyzer import analyze_message


class AnalyzeMessageTests(unittest.TestCase):
    def assert_analysis(self, message, expected_score, expected_level):
        score, level, _ = analyze_message(message)
        self.assertEqual(score, expected_score)
        self.assertEqual(level, expected_level)

    def test_safe_meeting_message(self):
        self.assert_analysis(
            "Toplantımız yarın saat 14.00 için planlanmıştır.",
            0,
            "Düşük Risk",
        )

    def test_safe_bank_information(self):
        self.assert_analysis(
            "Banka şubemiz hafta içi 09.00-17.00 saatleri arasında hizmet vermektedir.",
            0,
            "Düşük Risk",
        )

    def test_phone_number_alone_is_low_risk(self):
        self.assert_analysis(
            "Detaylı bilgi için 0532 123 45 67 numarasını arayabilirsiniz.",
            5,
            "Düşük Risk",
        )

    def test_external_link_is_low_risk_by_itself(self):
        self.assert_analysis(
            "Etkinlik programı: https://example.com/program",
            20,
            "Düşük Risk",
        )

    def test_payment_request_alone_is_low_risk(self):
        self.assert_analysis(
            "Ödemenizi havale ile gerçekleştiriniz.",
            15,
            "Düşük Risk",
        )

    def test_iban_and_payment_are_medium_risk(self):
        self.assert_analysis(
            "Ödeme için TR12 3456 7890 1234 5678 9012 34 IBAN adresine havale yapınız.",
            35,
            "Orta Risk",
        )

    def test_prize_message_alone_is_low_risk(self):
        self.assert_analysis(
            "Çekiliş kazandınız, ödülünüzü almak için bize ulaşın.",
            15,
            "Düşük Risk",
        )

    def test_cargo_payment_scam_is_high_risk(self):
        self.assert_analysis(
            "Kargonuz beklemede. 24 saat içinde ödeme yapın: "
            "https://kargo-takip-tr.com/odeme",
            80,
            "Yüksek Risk",
        )

    def test_bank_credential_scam_is_high_risk(self):
        self.assert_analysis(
            "Banka hesabınız bloke edilecek. Hemen https://guvenli-giris.example "
            "bağlantısından kart bilgileri ve SMS kodu girin.",
            95,
            "Yüksek Risk",
        )

    def test_score_never_exceeds_one_hundred(self):
        score, level, _ = analyze_message(
            "Banka hesabınız bloke edilecek. Acil ödeme yapın ve kart bilgileri, "
            "CVV, şifre ve SMS kodunu girin: https://example.com TR12 3456 7890 "
            "1234 5678 9012 34"
        )
        self.assertEqual(score, 100)
        self.assertEqual(level, "Yüksek Risk")

    def test_safe_delivery_information(self):
        self.assert_analysis("Kargonuz bugün 16.00-18.00 arasında teslim edilecektir.", 0, "Düşük Risk")

    def test_safe_appointment_reminder(self):
        self.assert_analysis("Hastane randevunuz 12 Ağustos saat 10.30'dadır.", 0, "Düşük Risk")

    def test_urgent_message_without_other_signal(self):
        self.assert_analysis("Toplantı acil olarak başka bir salona alınmıştır.", 15, "Düşük Risk")

    def test_threat_alone_is_low_risk(self):
        self.assert_analysis("Gecikme durumunda yasal işlem başlatılacaktır.", 15, "Düşük Risk")

    def test_prize_link_is_medium_risk(self):
        self.assert_analysis(
            "Hediye kazandınız, ayrıntılar için https://hediye.example adresini açın.",
            35,
            "Orta Risk",
        )

    def test_fake_scholarship_payment_is_high_risk(self):
        self.assert_analysis(
            "Burs başvurunuz onaylandı. 24 saat içinde kayıt ücreti ödeme yapın: https://burs.example",
            70,
            "Yüksek Risk",
        )

    def test_fake_government_credentials_is_high_risk(self):
        self.assert_analysis(
            "E-devlet erişiminiz durdurulacak. Hemen https://edevlet.example üzerinden şifrenizi girin.",
            95,
            "Yüksek Risk",
        )

    def test_fake_tax_payment_is_high_risk(self):
        self.assert_analysis(
            "Vergi dairesi borcunuz için son gün. Ödeme yapın: https://vergi.example",
            80,
            "Yüksek Risk",
        )

    def test_iban_without_payment_request_is_low_risk(self):
        self.assert_analysis("Kayıtlı IBAN: TR12 3456 7890 1234 5678 9012 34", 20, "Düşük Risk")

    def test_uppercase_turkish_keywords_are_detected(self):
        self.assert_analysis("ACİL ÖDEME YAPIN", 40, "Orta Risk")


if __name__ == "__main__":
    unittest.main()
