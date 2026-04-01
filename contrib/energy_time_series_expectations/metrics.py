"""
Custom metrics for Energy Time Series Expectations.
"""

from great_expectations.expectations.metrics import MetricProvider, metric_value
import pandas as pd


class TimeSeriesMissingIntervals(MetricProvider):
    """
    Computes missing intervals in a time series based on a specified frequency.
    """

    condition_metric_name = "energy_time_series.missing_intervals"

    @metric_value(engine="pandas")
    def _pandas(cls, data, frequency="30min", **kwargs):
        # Ensure the index is a datetime index
        if not isinstance(data.index, pd.DatetimeIndex):
            raise ValueError("Data must have a DatetimeIndex for time-series metrics.")

        # Generate expected full range
        expected = pd.date_range(start=data.index.min(),
                                 end=data.index.max(),
                                 freq=frequency)

        # Find missing timestamps
        missing = expected.difference(data.index)

        return list(missing)
