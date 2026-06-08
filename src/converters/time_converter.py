from .base_converter import BaseConverter

class TimeConverter(BaseConverter):

    conversion_multipliers: dict[str, float] = {
        "picosecond":  3.6e15,
        "nanosecond":  3.6e12,
        "microsecond": 3.6e9,
        "millisecond": 3.6e6,
        "second":      3.6e3,
        "minute":      60,
        "hour":        1,
        "day":         1/24,
        "week":        1/168,
        "month":       1.3689254e-3,
        "year":        1.140771e-4
    }

    units: dict[str, list[str]] = {
        "picosecond":  ["ps","picosecond"],
        "nanosecond":  ["ns","nanosecond"],
        "microsecond": ["µs","us","microsecond"],
        "millisecond": ["ms","millisecond"],
        "second":      ["s","sec","second"],
        "minute":      ["min","mn","minute"],
        "hour":        ["hr","hour"],
        "day":         ["d","dy","day"],
        "week":        ["w","wk","week"],
        "month":       ["mo","month"],
        "year":        ["y","yr","year","a"]
    }

    type: str = "time"
