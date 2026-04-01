"""
Plugin registration for Energy Time Series Expectations.

This file allows Great Expectations to discover and load
the custom expectations defined in this contrib package.
"""

from .energy_time_series_expectations import (
    ExpectTimeSeriesToHaveNoMissingIntervals,
    ExpectDemandToBeWithinCapacityLimits,
)

__all__ = [
    "ExpectTimeSeriesToHaveNoMissingIntervals",
    "ExpectDemandToBeWithinCapacityLimits",
]
