"""
PCB defect knowledge base.

각 결함(class)에 대한 제조 도메인 지식을 정의
Analyzer와 Report Generator에서 공통으로 사용
"""

DEFECT_KNOWLEDGE = {
    "missing_hole": {
        "display_name": "Missing Hole",
        "description": (
            "A required drilled hole is missing from the PCB."
        ),
        "severity": "High",
        "inspection_priority": "High",
        "possible_causes": [
            "Drilling machine malfunction",
            "Incorrect drill file (NC Drill)",
            "Hole generation process failure",
        ],
        "recommended_actions": [
            "Inspect the drilling machine.",
            "Verify the NC drill file.",
            "Perform a full inspection before shipment.",
        ],
    },

    "mouse_bite": {
        "display_name": "Mouse Bite",
        "description": (
            "Irregular erosion along the edge of a copper trace."
        ),
        "severity": "Medium",
        "inspection_priority": "High",
        "possible_causes": [
            "Over-etching during PCB manufacturing",
            "Excessive etching chemical concentration",
            "Uneven etching time",
        ],
        "recommended_actions": [
            "Inspect the etching process.",
            "Check the chemical concentration.",
            "Review process parameters.",
        ],
    },

    "open_circuit": {
        "display_name": "Open Circuit",
        "description": (
            "A conductive path is broken, causing electrical disconnection."
        ),
        "severity": "Critical",
        "inspection_priority": "High",
        "possible_causes": [
            "Over-etching",
            "Mechanical damage",
            "Copper deposition failure",
        ],
        "recommended_actions": [
            "Inspect conductive traces.",
            "Verify copper deposition quality.",
            "Perform continuity testing.",
        ],
    },

    "short": {
        "display_name": "Short Circuit",
        "description": (
            "Unintended electrical connection between conductive traces."
        ),
        "severity": "Critical",
        "inspection_priority": "High",
        "possible_causes": [
            "Insufficient etching",
            "Copper bridge formation",
            "Manufacturing contamination",
        ],
        "recommended_actions": [
            "Inspect adjacent traces.",
            "Remove conductive bridges.",
            "Repeat electrical testing.",
        ],
    },

    "spur": {
        "display_name": "Spur",
        "description": (
            "Small unwanted copper protrusion extending from a trace."
        ),
        "severity": "Medium",
        "inspection_priority": "Medium",
        "possible_causes": [
            "Incomplete etching",
            "Photoresist residue",
            "Process variation",
        ],
        "recommended_actions": [
            "Review the etching process.",
            "Inspect the photoresist coating.",
            "Remove residual copper.",
        ],
    },

    "spurious_copper": {
        "display_name": "Spurious Copper",
        "description": (
            "Unwanted isolated copper remaining on the PCB surface."
        ),
        "severity": "Medium",
        "inspection_priority": "Medium",
        "possible_causes": [
            "Incomplete copper removal",
            "Photoresist defect",
            "Etching process issue",
        ],
        "recommended_actions": [
            "Inspect the etching quality.",
            "Check photoresist integrity.",
            "Perform optical inspection.",
        ],
    },
}