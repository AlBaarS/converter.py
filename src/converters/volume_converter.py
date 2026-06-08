from .base_converter import BaseConverter

class VolumeConverter(BaseConverter):

    conversion_multipliers: dict[str, float] = {
        "nanoliter":       1e9,
        "microliter":      1e6,
        "milliliter":      1e3,
        "centiliter":      1e2,
        "deciliter":       1e1,
        "liter":           1,
        "cubic_meter":     1e-3,
        "cubic_kilometer": 1e-12,
        "fluid_ounce":     33.814038638,
        "cup":             4.2267548297,
        "pint":            2.1133774149,
        "quart":           1.0566887074,
        "gallon":          0.2641721769
    }

    units: dict[str, list[str]] = {
        "nanoliter":       ["nl","nanoliter","nanolitre"],
        "microliter":      ["µl","ul","microleter","microlitre","mm³","mm3","mm^3","cubic millimeter","cubic_millimeter","cubic millimetre","cubic_millimetre"],
        "milliliter":      ["ml","milliliter","millilitre","cm³","cm3","cm^3","cubic centimeter","cubic_centimeter","cubic centimetre","cubic_centimetre"],
        "centiliter":      ["cl","centiliter","centilitre"],
        "deciliter":       ["dl","deciliter","decilitre"],
        "liter":           ["l","liter","litre","dm³","dm3","dm^3","cubic decimeter","cubic_decimeter","cubic decimetre","cubic_decimetre"],
        "cubic_meter":     ["m³","m3","m^3","cubic meter","cubic_meter","cubic metre","cubic_metre"],
        "cubic_kilometer": ["km³","km3","km^3","cubic kilometer","cubic_kilometer","cubic kilometre","cubic_kilometre"],
        "fluid_ounce":     ["fl oz","fl_oz","fluid ounce","fluid_ounce"],
        "cup":             ["cup"],
        "pint":            ["pt","p","pint"],
        "quart":           ["qt","quart"],
        "gallon":          ["gal","gallon"]
    }

    type: str = "volume"
