# PCB Elements

- PCB elements notes

## Index

- [Index](#index)
- [Component Footprint](#component-footprint)
- [Documentation](#documentation)
- [Electrically Conductive](#electrically-conductive)
- [High-Speed/RF](#high-speedrf)
- [Internal to PCB](#internal-to-pcb)
- [Mechanical/Structural](#mechanicalstructural)
- [Surface Finishes](#surface-finishes)
- [Test/Manufacturing](#testmanufacturing)
- [Thermal Management](#thermal-management)

## Component Footprint

- Courtyard
  - Assembly keep out area
- Component outline
  - Silkscreen outline for easy placement
- Assembly layer markings
  - Pin 1, polarity, etc

## Documentation

- Mechanical drawings
- Drill files
- Netlist
- Assembly drawing
- Layer stack file
- Fabrication notes

## Electrically Conductive

- Copper traces
  - Routed copper paths for signals, power, ground
  - Impedance can be controlled w/ length/width/spacing
- Pads
  - Includes TH (through-hole) and SMD (surface-mount) pads
  - Pads in a crosshair pattern help reduce dissipation of heat to make soldering easier (thermal relief pads)
  - Via-in-pad- good for BGA parts
- Vias
  - TH vias
    - Through all layers connecting top <-> bottom layers
  - Blind vias
    - From an outer layer to an inner layer
  - Buried vias
    - From two inner layers
  - Microvias
    - Laser-drilled vias
  - Tented vias
    - Soldermask-covered vias to prevent solder or any other electrical connection
  - Filled vias
    - Either w/ conductive or non-conductive fill
  - Back drilled vias
    - TH vias that are drilled out to remove any excessive via stubs to ensure signal integrity
- Copper pours/planes
  - Ground planes
  - Power planes
  - Copper pour/floods
  - Polygons (custom-shaped copper areas)
  - Stitching copper- a strategy to reduce EMI

## High-Speed/RF

- Controlled impedance traces
  - Microstrip
    - Refers to traces where the signal conductor is placed on the outer layer of a PCB, w/ ground plane underneath some PCB dielectric
    - Faster signal propagation relative to stripline, but has higher radiation loss
  - Stripline
    - Refers to traces that are sandwiched between two dielectric layers and ground planes
    - The enclosure causes slower signal propagation, but has less radiation loss
  - Differential pairs
  - Coplanar waveguides
- Guard rings
  - Conductive rings of copper around sensitive nodes
- Tuning structures
  - Serpentines for length matching, meanders
- Stitching vias
  - For EMI shielding / RF boundaries
- RF keep outs
  - No copper zones for antennas
- Ground fences
  - For isolation around RF circuitry

## Internal to PCB

- Core layers
  - Dielectric (fiberglass) and internal copper films
- Prepreg
  - Resin bonding layers
- Internal routing
  - Buried traces/vias
- Stitching bars/rails
  - Used to improve return paths

## Mechanical/Structural

- Board outline
  - PCB shape / mechanical dimension constraints
- Cutouts
  - Internal slots, routing clearance holes, ventilation openings
- Mounting holes
  - Can be plated/non-plated
  - For screws, standoffs, mechanical fixtures
- Fiducials
  - Small pads placed on a PCB to help pick & place machines during component placement
  - Those vias at the edge of boards we thought are for connecting planes together
  - Can be global (whole PCB) or local (per footprint or BGA part)
- Keep out areas
  - Mechanical/electrical/height keep out regions
- Edge connectors
  - Gold fingers, keys/notches
- Breakaway features
  - Mouse bites (consecutive holes), v-cut scoring (a wedge in the PCB from both sides)

## Surface Finishes

- Soldermask layer, expansion, tenting
  - The top insulating layer coating the fiberglass to prevent solder from getting on everything
  - Soldermask between pads are called "soldermask dams"
  - Covering vias w/ soldermask is called "tenting"
- Silkscreen/legend
  - Component labels
  - Pin 1 indicators
  - Logos/markings
  - Revision identifiers
- Surface finish (copper plating)
  - Copper to aid solderability
  - Can be made HASL/HASL lead free, ENIG ("electroless nickel immersion gold"), OSP ("organic solderability preservative"), hard gold plating, immersion tin/silver

## Test/Manufacturing

- Test pads/points
  - For bed-of-nails testing
- ICT/JTAG connectors
- Barcodes/QR codes

## Thermal Management

- Thermal vias
  - Arrays of vias under heat-generating ICs to transfer heat to ground/heat sink layers
- Copper polygons / heat spreading areas
  - Large copper regions to dissipate heat
  - Aka, "cooling fingers"/"copper islands"
- Heat slugs/pads
  - Exposed copper pads under ICs- common for QFN packages
