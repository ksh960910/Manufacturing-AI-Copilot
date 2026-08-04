# Electrical Test and Shipment Hold Guideline

## Purpose

This guideline supports investigation of critical PCB defects, especially open
circuits and short circuits, detected by visual inspection.

## When to Apply

Apply this procedure when a visual inspection indicates a broken trace,
unintended copper bridge, or another defect that could affect electrical
continuity or isolation.

## Test Procedure

1. Place the affected board and associated lot on quality hold.
2. Use the approved netlist or test fixture to perform continuity testing for
   suspected open circuits.
3. Perform isolation or resistance testing for suspected short circuits.
4. Inspect the detected area under magnification to confirm the visual finding.
5. Expand testing to comparable nets or boards when the defect may be
   process-related.

## Release Criteria

- No unresolved open circuit or short circuit remains on the board.
- Required continuity and isolation tests pass.
- The defect cause is investigated and corrective action is recorded.
- Quality or manufacturing engineering approves the release decision.

## Shipment Decision

An unresolved open circuit or short circuit requires a shipment hold. The board
and potentially affected lot must not be released until the release criteria
are satisfied.
