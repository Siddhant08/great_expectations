@metric_value(engine="pandas")
def _pandas(cls, data, frequency="30min", **kwargs):
    # Ensure the index is a datetime index
    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("Data must have a DatetimeIndex for time-series metrics.")

    # Drop duplicate timestamps (keep first occurrence)
    data = data[~data.index.duplicated(keep="first")]

    # Sort index to ensure correct ordering
    data = data.sort_index()

    # Edge case: if only one timestamp, no missing intervals
    if len(data.index) < 2:
        return []

    # Generate expected full range
    expected = pd.date_range(
        start=data.index.min(),
        end=data.index.max(),
        freq=frequency,
    )

    # Find missing timestamps
    missing = expected.difference(data.index)

    return list(missing)
