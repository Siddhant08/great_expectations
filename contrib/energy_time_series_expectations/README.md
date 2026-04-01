# Energy Time Series Expectations

This contrib package provides custom Great Expectations Expectations for validating
energy demand and load time‑series data. These Expectations are designed for use
with datasets such as substation load profiles, feeder demand, or other
time‑indexed measurements where completeness and operational limits matter.

## Included Expectations

### `ExpectTimeSeriesToHaveNoMissingIntervals`
Validates that a time series contains no missing timestamps based on a specified
frequency (e.g., 30 minutes). This is useful for ensuring that SCADA or AMI
data is complete before downstream analysis.

**Arguments**
- `frequency` (str): Pandas offset alias such as `"30min"`, `"1H"`, `"15min"`.

**Example**
```python
validator.expect_time_series_to_have_no_missing_intervals(
    frequency="30min"
)
