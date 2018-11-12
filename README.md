# kicad-to-neoden

Commandline script to convert KiCad position files to CSV files for use on NeoDen 4 pick and place machines.

## Usage

`python kicad_to_neoden.py your_position_file_from_kicad.pos`

Works with Python 2 or 3 and outputs a file with the same name as the input but ending with "_neoden.csv"

## What this script does

This script performs the following:
- Filters out all lines beginning with a hash (#)
- Converts 0-359 rotation value into -180 to +180 value
- Truncates measurements to two decimal places and adds "mm"
- Converts "top" to "T" and everything else to "B" (this could be a gotcha if there is anything other than "bottom" output by KiCad)
- Orders output for NeoDen to "Designator,Footprint,Mid X,Mid Y,Layer,Rotation,Comment"

## Syntax example

Input example line:
`R1        4k7           R_0603                     154.2720  -121.1820   90.0000  top`
Output example line:
`R1,4k7,154.27mm,-121.18mm,T,90,R_0603`

