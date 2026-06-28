# Import modules
from re import sub

class Help:

    input_command: str

    help_page: str = '''
     ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄  ▄▄ ▄▄ 
    ██▀▀▀ ██▀██ ███▄██ ██▄██ ██▄▄  ██▄█▄   ██     ██▄█▀ ▀███▀ 
    ▀████ ▀███▀ ██ ▀██  ▀█▀  ██▄▄▄ ██ ██   ██   ▄ ██      █   

A simple command-line tool to convert common units. Supports metric and imperial. Written in python with love ♥

------------------------------------------------------------------------------------------------------------------------

# Base syntax
The syntax is simple and intuitive. Simply type the command, the value, the input unit and the output unit as follows:
    convert.py <input value> <input unit> to <output unit> <optional arguments>

Some examples:
    convert.py 20 pints to liters
    convert.py 3ft to m

You can use the singular or multitude of a unit (e.g. minute/minutes and foot/feet). Units that consist of two words
can have a whitespace or an underscore (e.g. square feet and square_feet). It also takes UK English spelling into
account (e.g. metre and litre). Furthermore, as demonstrated above, you can use the full names and symbols, or the
approximations thereof (e.g. m², m2 and m^2), and either have a space between the value and the unit or not.

The most important part of the command is the keyword "to". It serves to seperate the input data from the output data,
and can therefore not be ommited.

------------------------------------------------------------------------------------------------------------------------

# Optional arguments
Once you run your command, you will receive output as such:
> convert.py 20 pints to liters
9.4635249998384 liters (l)
You may want to customize this output. For this purpose, there are two optional arguments:
    round <decimal>: Specify the number of decimals the output may have. Minimum of 0.
    unitless: Output the number only, without the unit specification.

The round argument is used as follows:
    convert.py 5 yards to meters round 2

The unitless argument is used as follows:
    convert.py 20 pints to liters unitless

They can be used together in whichever order you prefer
    convert.py 303 seconds to minutes round 0 unitless
    convert.py 50ft to m unitless round 3

------------------------------------------------------------------------------------------------------------------------

# Available units
Currently, the following conversions can be done:
    area
    distance
    time
    volume
    weight

For a full list of units, you can use the help command followed by one of these definitions (e.g. convert.py help time)
of check the README for a list.
'''

    help_area: str = '''
     ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄  ▄▄ ▄▄ 
    ██▀▀▀ ██▀██ ███▄██ ██▄██ ██▄▄  ██▄█▄   ██     ██▄█▀ ▀███▀ 
    ▀████ ▀███▀ ██ ▀██  ▀█▀  ██▄▄▄ ██ ██   ██   ▄ ██      █  

Available units for area:
- Square nanometer (nm²)
- Square micrometer (µm²)
- Square millimeter (mm²)
- Square centimeter (cm²)
- Square decimeter (dm²)
- Square meter (m²)
- Square decameter (dam²)
- Hectare (ha)/square hectometer (hm²)
- Square kilometer (km²)
- Square inch (in²)
- Square foot (ft²)
- Acre (ac)
- Square mile (mi²)
'''

    help_distance: str = '''
     ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄  ▄▄ ▄▄ 
    ██▀▀▀ ██▀██ ███▄██ ██▄██ ██▄▄  ██▄█▄   ██     ██▄█▀ ▀███▀ 
    ▀████ ▀███▀ ██ ▀██  ▀█▀  ██▄▄▄ ██ ██   ██   ▄ ██      █  

Available units for distance:
- Nanometer (nm)
- Micrometer (µm)
- Millimeter (mm)
- Centimeter (cm)
- Decimeter (dm)
- Meter (m)
- Decameter (dam)
- Hectometer (hm)
- Kilometer (km)
- Inch (in)
- Foot (ft)
- Yard (ac)
- Mile (mi)
- Nautical mile (nmi)
- Lightyear (ly)
'''

    help_time: str = '''
     ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄  ▄▄ ▄▄ 
    ██▀▀▀ ██▀██ ███▄██ ██▄██ ██▄▄  ██▄█▄   ██     ██▄█▀ ▀███▀ 
    ▀████ ▀███▀ ██ ▀██  ▀█▀  ██▄▄▄ ██ ██   ██   ▄ ██      █  

Available units for time:
- Picosecond (ps)
- Nanosecond (ns)
- Microsecond (µs)
- Millisecond (ms)
- Second (s)
- Minute (min)
- Hour (hr)
- Day (d)
- Week (w)
- Month (mo)
- Year (y)
'''

    help_volume: str = '''
     ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄  ▄▄ ▄▄ 
    ██▀▀▀ ██▀██ ███▄██ ██▄██ ██▄▄  ██▄█▄   ██     ██▄█▀ ▀███▀ 
    ▀████ ▀███▀ ██ ▀██  ▀█▀  ██▄▄▄ ██ ██   ██   ▄ ██      █  

Available units for volume:
- Nanoliter (nl)
- Microliter (µl)
- Milliliter (ml)
- Centiliter (cl)
- Deciliter (dl)
- Liter (l)
- Cubic meter (m³)
- Cubic kilometer (km³)
- Fluid ounce (fl oz)
- Cup
- Pint (pt)
- Quart (qt)
- Gallon (gal)
'''

    help_weight: str = '''
     ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄  ▄▄ ▄▄ 
    ██▀▀▀ ██▀██ ███▄██ ██▄██ ██▄▄  ██▄█▄   ██     ██▄█▀ ▀███▀ 
    ▀████ ▀███▀ ██ ▀██  ▀█▀  ██▄▄▄ ██ ██   ██   ▄ ██      █  

Available units for weight:
- Nanogram (ng)
- Microgram (µg)
- Milligram (mg)
- Gram (g)
- Kilogram (kg)
- Ton (metric) (t)
- Ounce (oz)
- Pound (lb)
- Short ton (st)
- Long ton (lt)
'''

    # Builder methods
    def __init__(self, command: str) -> None:
        self.input_command = command

    # Getter methods
    def get_input_command(self) -> str: # pragma: no cover
        return self.input_command

    def get_help_page(self) -> str:     # pragma: no cover
        return self.help_page
    
    def get_help_area(self) -> str:     # pragma: no cover
        return self.help_area
    
    def get_help_distance(self) -> str: # pragma: no cover
        return self.help_distance
    
    def get_help_time(self) -> str:     # pragma: no cover
        return self.help_time
    
    def get_help_volume(self) -> str:   # pragma: no cover
        return self.help_volume
    
    def get_help_weight(self) -> str:   # pragma: no cover
        return self.help_weight
    
    # Functional methods
    def page(self) -> str:
        match sub(r"help|\s", "", self.get_input_command()):
            case "area":
                return self.get_help_area()
            case "distance":
                return self.get_help_distance()
            case "time":
                return self.get_help_time()
            case "volume":
                return self.get_help_volume()
            case "weight":
                return self.get_help_weight()
            case _:
                return self.get_help_page()
