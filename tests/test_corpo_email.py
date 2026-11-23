"""Regression tests for the report's email summary."""

import unittest

from src.corpo_email import msg_corpo_email


class EmailSummaryTests(unittest.TestCase):
    def test_summary_contains_all_statistics(self):
        result = msg_corpo_email(
            {"Citacoes": 12, "Autor": "Jane Doe", "Tag": "Life"}
        )
        self.assertIn("12", result)
        self.assertIn("Jane Doe", result)
        self.assertIn("Life", result)

    def test_missing_statistic_raises_key_error(self):
        with self.assertRaises(KeyError):
            msg_corpo_email({"Citacoes": 1})


if __name__ == "__main__":
    unittest.main()
