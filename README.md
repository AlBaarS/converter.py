```
 ▄▄▄▄  ▄▄▄  ▄▄  ▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  ▄▄▄▄▄▄   ▄▄▄▄  ▄▄ ▄▄ 
██▀▀▀ ██▀██ ███▄██ ██▄██ ██▄▄  ██▄█▄   ██     ██▄█▀ ▀███▀ 
▀████ ▀███▀ ██ ▀██  ▀█▀  ██▄▄▄ ██ ██   ██   ▄ ██      █   
```

A simple command-line tool to convert common units. Supports metric and imperial. Written in python with love ♥

## What is this tool and why do I need it?

Calm down, sheesh. As stated, this is a hobby project. I am mostly creating it for my enjoyment. However, I do use it during my D&D sessions. If we're playing and I want to know how long the hallway in which I am going to cast fireball _actually_ is (in real units), I can just type `convert.py 60 ft to m`, and I will have my answer. It saves me opening a tab, typing in the actual search string, and then waiting for duckduckgo to give me the answer. Instead, I get a near-instant result in my terminal. If that sounds neat to you, well, go ahead and download it!

```
❗Please note ❗
This project uses match-case statements and therefore requires at least Python version 3.10
This project is under active development. Here be dragons. And bugs.
```

## Installation

### Step 1. Download

Clone this project to your machine using git:

```bash
git clone git@github.com:AlBaarS/converter_py.git
# or
git clone https://github.com/AlBaarS/converter_py.git
```

Alternatively, simply download the project as an archive and extract in your preferred location.

Now, you are good to go in principle. You can execute the `convert.py` file as-is, or call it explicitly using python:

```bash
./converter_py/convert.py 200 cm to m
python3 converter_py/convert.py 30 in to ft
```

However, if you want to make your life a bit easier, I recommend creating an alias as described below.

### Step 2. Create an alias (optional)

You can create an alias as follows:

```bash
alias convert.py='python3 /path/to/converter_py/convert.py'
# Tip: put this in your .bashrc (or similar file for your shell) to ensure that it is stored.
```

Now you can call on the converter from any path in your system.

```bash
convert.py 170 lbs to kg
```

## Usage:


### Base syntax
The syntax is simple and intuitive. Simply type the command, the value, the input unit and the output unit as follows:

```
convert.py <input value> <input unit> to <output unit> <optional arguments>
```

Some examples:
```
convert.py 20 pints to liters
convert.py 3ft to m
```
You can use the singular or multitude of a unit (e.g. minute/minutes and foot/feet). Units that consist of two words
can have a whitespace or an underscore (e.g. square feet and square_feet). It also takes UK English spelling into
account (e.g. metre and litre). Furthermore, as demonstrated above, you can use the full names and symbols, or the
approximations thereof (e.g. m², m2 and m^2), and either have a space between the value and the unit or not.

The most important part of the command is the keyword "to". It serves to seperate the input data from the output data,
and can therefore not be ommited.

### Optional arguments
Once you run your command, you will receive output as such:
```
> convert.py 20 pints to liters
9.4635249998384 liters (l)
```

You may want to customize this output. For this purpose, there are two optional arguments:

`round <decimal>`: Specify the number of decimals the output may have. Minimum of 0.

`unitless`: Output the number only, without the unit specification.

The round argument is used as follows:
```
convert.py 5 yards to meters round 2
```

The unitless argument is used as follows:
```
convert.py 20 pints to liters unitless
```

They can be used together in whichever order you prefer
```
convert.py 303 seconds to minutes round 0 unitless
convert.py 50ft to m unitless round 3
```

You can also call `convert.py` with no arguments use the `help` argument to re-read all of this information:
```
convert.py
convert.py help
```

## Current units supported

In alphabetical order:

<details>
<summary>Area</summary>
<br>

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
</details>

<details>
<summary>Distance</summary>
<br>

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
</details>

<details>
<summary>Time</summary>
<br>

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
</details>

<details>
<summary>Volume</summary>
<br>

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
</details>

<details>
<summary>Weight</summary>
<br>

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

</details>

## Future additions:

Within the scope of conversions, I plan to add the following:

- Temperature
- Velocity

I will also add an option to omit the unit from the output, which will make piping output from this tool much easier.

Finally, I am also considering expanding the scope to other simple and common conversions/calculations, like the surface area or volume, speed, and diagonal lines/angles.

## Acknowledgements

ASCII convert.py made on https://patorjk.com/software/taag/ using the ANSI Compact font.

No AI was used to generate/check/whatever code in this project (because screw AI).
