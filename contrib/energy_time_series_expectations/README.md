# Energy Time Series Expectations

This contribution provides a set of custom Expectations and example workflows for validating **energy demand time‑series data**, with a focus on substation‑level demand measurements used in electricity distribution networks.

Energy demand data is typically recorded at fixed intervals (e.g., 10‑min, 30‑min, hourly) and is used for forecasting, planning, curtailment analysis, and operational decision‑making. Because downstream analytics depend heavily on data quality, it is essential to detect issues such as missing intervals, sensor flatlines, negative values, or unrealistic demand spikes.

This module introduces domain‑specific Expectations and examples that help data teams validate the integrity of energy time‑series datasets before they are used in modelling or reporting.

---

## What’s Included

### ✔ Custom Expectations
This module provides simple, reusable Expectations tailored to energy demand data, such as:

- **`expect_time_series_to_have_no_missing_intervals`**  
  Ensures timestamps follow a fixed frequency (e.g., 30‑minute intervals).

- **`expect_demand_to_be_within_capacity_limits`**  
  Validates that measured demand does not exceed the known transformer or feeder rating.

- **`expect_time_series_to_follow_daily_cycle`**  
  Checks whether the demand profile exhibits a typical daily pattern (e.g., morning/evening peaks).

These Expectations are designed to be lightweight, interpretable, and easy to integrate into existing Great Expectations workflows.

---

## Example Notebook

The `examples/` folder contains a Jupyter notebook demonstrating how to:

1. Load substation demand time‑series data  
2. Create a Great Expectations Data Context  
3. Apply the custom Expectations  
4. Interpret validation results  
5. Generate Data Docs for reporting  

This example is intended as a practical starting point for energy analysts, data engineers, and data scientists working with operational network data.

---

## Why This Matters

Energy demand time‑series data often suffers from:

- Missing or duplicated timestamps  
- Irregular sampling intervals  
- Negative or impossible values  
- Sudden spikes or drops due to sensor faults  
- Long flatlines indicating stuck meters  
- Values exceeding physical capacity limits  

These issues can significantly distort:

- Load forecasting  
- Curtailment estimation  
- Network planning  
- Constraint analysis  
- ANM/LMS reporting  
- Regulatory submissions  

By validating data quality early, teams can prevent downstream errors and build more reliable analytics pipelines.

---

## How to Use

After installing Great Expectations, import the custom Expectations:

```python
from great_expectations.contrib.energy_time_series_expectations import (
    expect_time_series_to_have_no_missing_intervals,
    expect_demand_to_be_within_capacity_limits,
    expect_time_series_to_follow_daily_cycle,
)
