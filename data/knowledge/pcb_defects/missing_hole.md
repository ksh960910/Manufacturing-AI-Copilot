# Missing Hole

## Severity

High

## Description

A required drilled hole is absent from the printed circuit board (PCB). A
missing hole can prevent component mounting, mechanical fastening, or an
electrical interconnection through the board.

## Likely Causes

- Drilling machine malfunction or a broken drill bit.
- Incorrect or incomplete NC drill file.
- Failure during drill-program loading or hole-generation processing.

## Inspection Procedure

1. Compare the detected location with the approved drill drawing and NC drill
   file.
2. Inspect the drilling machine, drill bit condition, and drill-program log.
3. Check boards from the same production lot for the same missing feature.
4. Confirm whether the hole is required for a component, mounting point, or
   plated-through electrical connection.

## Recommended Actions

1. Stop using the affected drill program until it is verified.
2. Verify the NC drill file against the approved manufacturing release.
3. Inspect the drilling machine and replace damaged tooling when necessary.
4. Perform full visual inspection of the affected lot before shipment.

## Shipment Decision

Hold the affected board and lot for review. Release only after the missing
feature has been dispositioned and required hole locations are verified.
