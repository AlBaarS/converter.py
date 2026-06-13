from .base_converter import BaseConverter


class WeightConverter(BaseConverter):

    conversion_multipliers: dict[str, float] = {
        "nanogram": 1e12,
        "microgram": 1e9,
        "milligram": 1e6,
        "gram": 1e3,
        "kilogram": 1,
        "metric_ton": 1e-3,
        "ounce": 35.273990723,
        "pound": 2.2046244202,
        "short_ton": 1.1023122e-3,
        "long_ton": 9.842073e-4,
    }

    units: dict[str, list[str]] = {
        "nanogram": ["ng", "nanogram", "nanogramme"],
        "microgram": ["µg", "ug", "microgram", "microgramme"],
        "milligram": ["mg", "milligram", "milligramme"],
        "gram": ["g", "gram", "gramme"],
        "kilogram": ["kg", "kilo", "kilogram", "kilogramme"],
        "metric_ton": ["t", "ton", "tonne", "metric ton", "metric_ton", "metric tonne", "metric_tonne"],
        "ounce": ["oz", "℥", "ounce"],
        "pound": ["lb", "pound"],
        "short_ton": ["st", "s_t", "short ton", "short_ton", "short tonne", "short_tonne"],
        "long_ton": ["lt", "l_t", "long ton", "long_ton", "long tonne", "long_tonne"],
    }

    type: str = "weight"
