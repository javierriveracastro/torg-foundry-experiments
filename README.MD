# Torg Eternity Basic Targeting

A simple modules that tries to implement some support for targeting in Torg Eternity

## Build Instructions

You will need to have Trasncrypt(https://transcrypt.org/) installed.

Just move to the root directory and run

`transcrypt main.py`

This will transpile the python code into javascipt into the py-src/__target__/ directory.

You should link this directory from pf2-dmg-count as script. In linux:

`ln -s py-src/__target__ torg-basic-targeting/scripts`

Afterwards you only need to run transcrypt after each change or just setup your preferred IDE to do it automatically.
