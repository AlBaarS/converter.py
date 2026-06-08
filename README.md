# converter.py

Hobby project to create a converter tool on the command line. Works on Linux, will probably work on Unix/MacOS, might work on Windows (cannot test this myself).

## What is this tool and why do I need it?

Calm down, sheesh. As stated, this is a hobby project. I am mostly creating it for my enjoyment. However, I do use it during my D&D sessions. If we're playing and I want to know how big the room in which I am going to cast fireball _actually_ is (in real units), I can just type `convert.py 60 ft to m`, and I will have my answer. It saves me opening a tab, typing in the actual search string, and then waiting for duckduckgo to give me the answer. Instead, I get a near-instant result in my terminal. If that sounds neat to you, well, go ahead and download it!

```
❗Please note ❗
This project uses built-in type hinting and therefore requires at least Python version 3.9
This project is under development. There are bugs. 
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

## Features:

Convert common units in your terminal of choice using an intuitive syntax:

```bash
# Use symbols, full name, or common abbreviations. Works with a whitespace or an underscore
convert.py 3mi to km
convert.py 20 square meters to square feet
convert.py 30000 pints to cubic_meters
```

You can also round your output to a specified number of decimals:

```bash
convert.py 75 kg to lbs round 2
convert.py 303 seconds to minutes round 0
```

### Current units supported

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
