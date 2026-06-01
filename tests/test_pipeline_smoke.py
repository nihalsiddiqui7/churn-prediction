from pathlib import Path
import unittest

from src.data_d.load_data import load_data
from src.data_d.preprocess_data import preprocess_data
from src.features.build_features import feature_engineering
from src.utils.validate import validate_data


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "customer_churn_dataset.csv"


class PipelineSmokeTest(unittest.TestCase):
    def test_pipeline_runs_on_small_sample(self) -> None:
        raw_df = load_data(str(RAW_DATA_PATH)).head(25).copy()

        is_valid, validation_errors = validate_data(raw_df)
        self.assertTrue(is_valid, msg=f"Validation failed: {validation_errors}")

        processed_df = preprocess_data(raw_df.copy(), "Churn")
        expected_processed_columns = [
            "Support Calls",
            "Churn",
            "Total Spend",
            "Payment Delay",
            "Last Interaction",
            "Subscription Type",
            "Contract Length",
        ]
        self.assertEqual(list(processed_df.columns), expected_processed_columns)
        self.assertGreater(len(processed_df), 0)

        engineered_df = feature_engineering(processed_df.copy())
        self.assertGreater(len(engineered_df), 0)
        self.assertNotIn("Subscription Type", engineered_df.columns)
        self.assertNotIn("Contract Length", engineered_df.columns)
        self.assertEqual(
            list(engineered_df.select_dtypes(include=["object"]).columns),
            [],
        )


if __name__ == "__main__":
    unittest.main()