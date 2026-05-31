from .base_converter import BaseConverter

class DistanceConverter(BaseConverter):

    conversion_multipliers: dict[str, float] = {
        "nanometer":     1e9,
        "micrometer":    1e6,
        "millimeter":    1e3,
        "centimeter":    1e2,
        "decimeter":     1e1,
        "meter":         1,
        "decameter":     1e-1,
        "hectometer":    1e-2,
        "kilometer":     1e-3,
        "inch":          39.37007874,
        "foot":          3.280839895,
        "yard":          1.0936132983,
        "mile":          6.213712e-4,
        "nautical_mile": 5.399568e-4,
        "lightyear":     1.057008707e16
    }

    units: dict[str, list[str]] = {
        "nanometer":     ["nm","nanometer","nanometre"],
        "micrometer":    ["µm","um","micrometer","micrometre"],
        "millimeter":    ["mm","millimeter","millimetre"],
        "centimeter":    ["cm","centimeter","centimetre"],
        "decimeter":     ["dm","decimeter","decimetre"],
        "meter":         ["m","meter","metre"],
        "decameter":     ["dam","decameter","decametre"],
        "hectometer":    ["hm","hectometer","hectometre"],
        "kilometer":     ["km","kilometer","kilometre"],
        "inch":          ["in","inch"],
        "foot":          ["ft","ft.","foot"],
        "yard":          ["yd","yard"],
        "mile":          ["mi","mile"],
        "nautical_mile": ["nmi","nautical mile","nautical_mile"],
        "lightyear":     ["ly","lightyear", "light year","light_year","light-year"]
    }

    type: str = "distance"
