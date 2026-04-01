import pandas as pd
from great_expectations.validator.validator import Validator
from great_expectations.core.expectation_suite import ExpectationSuite
from great_expectations.datasource.fluent import PandasDatasource

from great_expectations.contrib.energy_time_series_expectations.energy_time_series_expectations import (
    ExpectTimeSeriesToHaveNoMissingIntervals,
)


def test_no_missing_intervals():
    # Create a simple complete time series
    index = pd.date_range("2024-01-01", periods=4, freq="30min")
    df = pd.DataFrame({"value": [1, 2, 3, 4]}, index=index)

    # Build a GE validator
    ds = PandasDatasource(name="pandas")
    batch = ds.get_asset("dummy").add_batch(df)
    validator = Validator(execution_engine=batch.execution_engine, expectation_suite=ExpectationSuite("test"))

    # Run the expectation
    result = ExpectTimeSeriesToHaveNoMissingIntervals().validate(
        configuration={"kwargs": {"frequency": "30min"}},
        metrics={"energy_time_series.missing_intervals": []},
    )

    assert result["success"] is True
