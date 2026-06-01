import great_expectations as ge
from typing import Tuple, List

def validate_data(df) -> Tuple[bool, List[str]]:
    """
    Validates the dataset using Great Expectations.

    Args:
        df (pd.DataFrame): The DataFrame to validate.

    Returns:
        Tuple[bool, List[str]]: A tuple containing a boolean indicating if the data is valid and a list of validation errors if any.
    """
    # Create a Great Expectations DataFrame
    ge_df = ge.from_pandas(df)
    print("Starting schema validation...")
    # Define expectations
    expectations = [
        ge_df.expect_column_to_not_be_null('CustomerID'),
        ge_df.expect_column_to_exist('Gender'),
        ge_df.expect_column_to_exist('Age'),
        ge_df.expect_column_to_exist('Support Calls'),
        ge_df.expect_column_to_exist('Usage Frequency'),
        ge_df.expect_column_to_exist('Churn'),
        ge_df.expect_column_to_exist('Tenure'),
        ge_df.expect_column_to_exist('Total Spend'),
        ge_df.expect_column_to_exist('Payment Delay'),
        ge_df.expect_column_to_exist('Last Interaction'),
        ge_df.expect_column_to_exist('Subscription Type'),
        ge_df.expect_column_to_exist('Contract Length'),
        ge_df.expect_column_values_to_be_in_set('Churn', [0, 1]),
        ge_df.expect_column_values_to_be_in_set('Gender', ["Male", "Female"]),
        ge_df.expect_column_values_to_be_between('Support Calls', min_value=0),
        ge_df.expect_column_values_to_be_between('CustomerID', min_value=0),
        ge_df.expect_column_values_to_be_between('Age', min_value=0),
        ge_df.expect_column_values_to_be_between('Usage Frequency', min_value=0),
        ge_df.expect_column_values_to_be_between('Tenure',min_value=0),
        ge_df.expect_column_values_to_be_between('Total Spend', min_value=0),
        ge_df.expect_column_values_to_be_of_type('Payment Delay', 'int64'),
        ge_df.expect_column_values_to_be_between('Last Interaction', min_value=0),
        ge_df.expect_column_values_to_be_in_set('Subscription Type', ["Standard", "Basic", "Premium"]),
        ge_df.expect_column_values_to_be_in_set('Contract Length', ["Annual", "Monthly", "Quarterly"])
    ]
    print("Schema validation completed. Now validating data quality...")

    # === RUN VALIDATION SUITE ===
    print("   ⚙️  Running complete validation suite...")
    results = ge_df.validate()

    # === PROCESS RESULTS ===
    # Extract failed expectations for detailed error reporting
    failed_expectations = []
    for r in results["results"]:
        if not r["success"]:
            expectation_type = r["expectation_config"]["expectation_type"]
            failed_expectations.append(expectation_type)

    # Print validation summary
    total_checks = len(results["results"])
    passed_checks = sum(1 for r in results["results"] if r["success"])
    failed_checks = total_checks - passed_checks

    if results["success"]:
        print(f"✅ Data validation PASSED: {passed_checks}/{total_checks} checks successful")
    else:
        print(f"❌ Data validation FAILED: {failed_checks}/{total_checks} checks failed")
        print(f"   Failed expectations: {failed_expectations}")

    return results["success"], failed_expectations