"""
Energy Time Series Expectations

This module contains custom Expectations for validating
energy demand time-series data such as substation load profiles.
These Expectations are placeholders and will be implemented
in later steps of the contribution.
"""

from great_expectations.expectations.expectation import Expectation


class ExpectTimeSeriesToHaveNoMissingIntervals(Expectation):
    """
    Placeholder Expectation:
    Checks that a time-series has no missing timestamps
    based on a specified frequency (e.g., 30 minutes).
    """

    metric_dependencies = ()
    success_keys = ("frequency",)

    default_kwarg_values = {
        "frequency": "30min",
    }

    def validate_configuration(self, configuration):
        return True

    def _validate(self, configuration, metrics, runtime_configuration=None, execution_engine=None):
        return {
            "success": True,
            "result": {"details": "Placeholder expectation — logic to be added later."},
        }


class ExpectDemandToBeWithinCapacityLimits(Expectation):
    """
    Placeholder Expectation:
    Ensures that demand values do not exceed a specified
    transformer or feeder capacity limit.
    """

    metric_dependencies = ()
    success_keys = ("max_capacity",)

    default_kwarg_values = {
        "max_capacity": 10000,
    }

    def validate_configuration(self, configuration):
        return True

    def _validate(self, configuration, metrics, runtime_configuration=None, execution_engine=None):
        return {
            "success": True,
            "result": {"details": "Placeholder expectation — logic to be added later."},
        }
