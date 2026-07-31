import tempfile
import unittest
from pathlib import Path

from history import clear_analyses, create_message_summary, get_analyses, get_dashboard_stats, save_analysis


class AnalysisHistoryTests(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.db_path = Path(self.temp_directory.name) / "test_history.db"

    def tearDown(self):
        self.temp_directory.cleanup()

    def test_sensitive_data_is_masked_in_summary(self):
        summary = create_message_summary(
            "0532 123 45 67 numarasını arayın ve TR12 3456 7890 1234 5678 9012 34 hesabına gönderin."
        )
        self.assertNotIn("0532", summary)
        self.assertNotIn("TR12", summary)
        self.assertIn("[TELEFON MASKELENDİ]", summary)
        self.assertIn("[IBAN MASKELENDİ]", summary)

    def test_analysis_is_saved_and_listed(self):
        save_analysis("Örnek mesaj", 35, "Orta Risk", self.db_path)
        analyses = get_analyses(db_path=self.db_path)
        self.assertEqual(len(analyses), 1)
        self.assertEqual(analyses[0]["score"], 35)
        self.assertEqual(analyses[0]["level"], "Orta Risk")

    def test_dashboard_statistics(self):
        save_analysis("Güvenli", 0, "Düşük Risk", self.db_path)
        save_analysis("Şüpheli", 80, "Yüksek Risk", self.db_path)
        stats = get_dashboard_stats(self.db_path)
        self.assertEqual(stats["total"], 2)
        self.assertEqual(stats["average_score"], 40.0)
        self.assertEqual(stats["distribution"]["Düşük Risk"], 1)
        self.assertEqual(stats["distribution"]["Yüksek Risk"], 1)

    def test_history_can_be_cleared(self):
        save_analysis("Örnek", 0, "Düşük Risk", self.db_path)
        clear_analyses(self.db_path)
        self.assertEqual(get_analyses(db_path=self.db_path), [])


if __name__ == "__main__":
    unittest.main()
