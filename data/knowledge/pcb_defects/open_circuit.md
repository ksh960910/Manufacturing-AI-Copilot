# Open Circuit

## Severity

Critical

## Description

An open circuit is a broken conductive path that causes electrical
disconnection. It can make the finished PCB or an attached component
nonfunctional.

## Likely Causes

- Over-etching of copper traces.
- Mechanical damage during handling, drilling, routing, or depanelization.
- Copper deposition, plating, or adhesion failure.
- Contamination or an imaging defect that interrupted the trace pattern.

## Inspection Procedure

1. Perform continuity testing across the detected conductive path.
2. Inspect the break at magnification for over-etching, damage, or delamination.
3. Check nearby boards from the same lot for repeated trace breaks.
4. Review etching, plating, and handling records for the applicable process
   stage.

## Recommended Actions

1. Place the affected board and associated lot on hold.
2. Perform continuity testing on the affected net and similar critical nets.
3. Inspect copper deposition and etching quality before restarting production.
4. Escalate repeated occurrences to manufacturing and quality engineering.

## Shipment Decision

Do not ship the affected board. Release of the lot requires successful
electrical testing, root-cause review, and documented quality approval.
