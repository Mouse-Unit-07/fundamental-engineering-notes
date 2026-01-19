# Schematic

- Schematic notes
- Primarily from _Art of Electronics_

## Index

- [Index](#index)
- [Overview](#overview)
- [Be Clear](#be-clear)
- [Don't Fight Convention](#dont-fight-convention)
- [Positive, Negative Supply Voltages](#positive-negative-supply-voltages)
- [Title Area](#title-area)
- [Use Power and Ground Symbols](#use-power-and-ground-symbols)
- [Wire Overlap](#wire-overlap)

## Overview

- Schematics should be unambiguous, and make circuit functions clear

## Be Clear

- Clearly label pin numbers, part values, reference designators, polarities, etc
  - Label pin numbers on the outside of a symbol, and signal names inside
  - All parts should have values/types indicated, as well as reference designators
- Keep functional areas distinct
  - Go ahead and leave empty space on the schematic page if need be
- Use the same symbol for the same device
- Stretch out leads a bit w/ wires before making connections

## Don't Fight Convention

- Conventional layout of op-amps, flip-flops, and other circuits/devices
- Signals flow from left to right
  - Follow whenever possible and when it doesn't sacrifice clarity
- Align wires/components horizontally and vertically
  - Don't place stuff down diagonally

## Positive, Negative Supply Voltages

- Put positive supply voltages towards the top, and negative supply voltages towards the bottom

## Title Area

- There should be a title area near the bottom of the page for:
  - Name of circuit
  - Name of instrument
  - Author, validator name
  - Date
  - Assembly number
  - Revision

## Use Power and Ground Symbols

- As in, don't bring all supply rail or ground wires together

## Wire Overlap

- Use dots to indicate that wires are connected
- Four wires shall not connect at a point
  - So wires can't both cross and connect at the same point
  - Following this closes doors for doubt and potential mistakes including/missing a connection dot
