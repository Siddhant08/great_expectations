import pandas as pd
from great_expectations.validator.validator import Validator
from great_expectations.core.expectation_suite import ExpectationSuite
from great_expectations.datasource.fluent import PandasDatasource

from great_expectations.contrib.energy_time_series_expectations.energy_time_series_expectations import (
    ExpectTimeSeriesToHaveNoMissingIntervals,
)


def test_detects_missing_intervals():
    # Create a time series with a missing timestamp
    index = pd.to_datetime([
        "2024-01-01 00:00",
        "2024-01-01 00:30",
        # Missing 01:00
        "2024-01-01 01:30",
    ])
    df = pd.DataFrame({"value": [1, 2, 3]}, index=index)

    # Expected missing timestamp
    expected_missing = [pd.Timestamp("2024-01-01 01:00")]

    # Build a GE validator
    ds = PandasDatasource(name="pandas")
    batch = ds.get_asset("dummy").add_batch(df)
    validator = Validator(execution_engine=batch.execution_engine, expectation_suite=ExpectationSuite("test"))

    # Simulate metric output
    result = ExpectTimeSeriesToHaveNoMissingIntervals().validate(
        configuration={"kwargs": {"frequency": "30min"}},
        metrics={"energy_time_series.missing_intervals": expected_missing},
    )

    assert result["success"] is False
    assert result["result"]["missing_intervals"] == expected_missing
