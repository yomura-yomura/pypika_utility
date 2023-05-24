from pypika.functions import Function


_default_timezone = "UTC"


def set_default_timezone(timezone):
    global _default_timezone
    _default_timezone = timezone


class TDTimeParse(Function):
    """
    Date -> Unix Time
    https://docs.treasuredata.com/display/public/PD/Supported+Presto+and+TD+Functions#SupportedPrestoandTDFunctions-TD_TIME_PARSE
    """
    def __init__(self, yyyy_mm_dd, timezone=None):
        if timezone is None:
            timezone = _default_timezone
        super().__init__("TD_TIME_PARSE", yyyy_mm_dd, timezone)


class TDTimeFormat(Function):
    """
    Unix Time -> Date
    """
    def __init__(self, timestamp, yyyy_mm_dd_format, timezone=None):
        if timezone is None:
            timezone = _default_timezone
        super().__init__("TD_TIME_FORMAT", timestamp, yyyy_mm_dd_format, timezone)


class TDTimeRange(Function):
    """
    start_time/end_time: Date / Unix Time
    """
    def __init__(self, timestamp, start_time, end_time, timezone=None):
        if timezone is None:
            timezone = _default_timezone
        super().__init__("TD_TIME_RANGE", timestamp, start_time, end_time, timezone)


class TDDateTrunc(Function):
    """
    https://docs.treasuredata.com/display/public/PD/Supported+Presto+and+TD+Functions#SupportedPrestoandTDFunctions-TD_DATE_TRUNC
    """
    def __init__(self, unit, timestamp, timezone=None):
        if timezone is None:
            timezone = _default_timezone
        assert unit.lower() in ("minute", "hour", "day", "week", "month", "quarter", "year")
        super().__init__("TD_DATE_TRUNC", unit, timestamp, timezone)
