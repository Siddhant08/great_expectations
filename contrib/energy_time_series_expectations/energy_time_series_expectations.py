from great_expectations.expectations.expectation import Expectation
from great_expectations.expectations.metrics import MetricConfiguration


class ExpectTimeSeriesToHaveNoMissingIntervals(Expectation):
    """
    Validates that a time series has no missing timestamps
    based on a specified frequency (e.g., 30 minutes).
    """

    metric_dependencies = ("energy_time_series.missing_intervals",)
    success_keys = ("frequency",)

    default_kwarg_values = {
        "frequency": "30min",
    }

    def validate_configuration(self, configuration):
        # Basic validation: ensure frequency is provided
        assert "frequency" in configuration.kwargs, "frequency must be supplied"
        return True

    def _validate(
        self,
        configuration,
        metrics,
        runtime_configuration=None,
        execution_engine=None,
    ):
        missing = metrics.get("energy_time_series.missing_intervals")

        success = len(missing) == 0

        return {
            "success": success,
            "result": {
                "missing_intervals": missing,
                "missing_count": len(missing),
            },
        }

    def get_validation_dependencies(self, configuration=None, execution_engine=None, runtime_configuration=None):
        """
        Tell GE which metric to compute and with what parameters.
        """
        deps = super().get_validation_dependencies(
            configuration=configuration,
            execution_engine=execution_engine,
            runtime_configuration=runtime_configuration,
        )

        frequency = configuration.kwargs.get("frequency", "30min")

        deps["metrics"]["energy_time_series.missing_intervals"] = MetricConfiguration(
            metric_name="energy_time_series.missing_intervals",
            metric_domain_kwargs={},
            metric_value_kwargs={"frequency": frequency},
        )

        return deps
