import pandas as pd
from great_expectations.validator.validator import Validator
from great_expectations.core.expectation_suite import ExpectationSuite
from great_expectations.datasource.fluent import PandasDatasource

from great_expectations.contrib.energy_time_series_expectations.energy_time_series_expectations import (
    ExpectTimeSeriesToHaveNoMissingIntervals,
)


def test_duplicate_timestamps_are_ignored():
    # Duplicate timestamp at 00:30
    index = pd.to_datetime([
        "2024-01-01 00:00",
        "2024-01-01 00:30",
        "2024-01-01 00:30",  # duplicate
        "2024-01-01 01:00",
    ])
    df = pd.DataFrame({"value": [1, 2, 2, 3]}, index=index)

    # No missing intervals expected
    expected_missing = []

    ds = PandasDatasource(name="pandas")
    batch = ds.get_asset("dummy").add_batch(df)
    validator = Validator(execution_engine=batch.execution_engine, expectation_suite=ExpectationSuite("test"))

    result = ExpectTimeSeriesToHaveNoMissingIntervals().validate(
        configuration={"kwargs": {"frequency": "30min"}},
        metrics={"energy_time_series.missing_intervals": expected_missing},
    )

    assert result["success"] is True
    assert result["result"]["missing_intervals"] == expected_missing
