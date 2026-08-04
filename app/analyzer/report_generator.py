from collections import defaultdict


def generate_report(image_name: str, analysis: dict) -> str:
    """
    분석 결과를 Markdown 형태의 PCB Inspection Report로 생성
    """

    summary = analysis["summary"]
    detections = analysis["detections"]

    # 내부 식별자인 class를 기준으로 그룹화
    grouped = defaultdict(list)

    for detection in detections:
        grouped[detection["class"]].append(detection)

    report = []

    report.append("# PCB Inspection Report")
    report.append("")

    report.append(f"**Image:** {image_name}")
    report.append("")

    report.append("## Summary")
    report.append("")
    report.append(f"- Total Defects: {summary['total_defects']}")
    report.append(f"- Highest Severity: {summary['highest_severity']}")
    report.append(f"- Average Confidence: {summary['average_confidence']:.3f}")
    report.append("")

    report.append("### Severity Distribution")

    for severity, count in summary["severity_counts"].items():
        report.append(f"- {severity}: {count}")

    report.append("")

    report.append("### Confidence Distribution")

    for level, count in summary["confidence"].items():
        report.append(f"- {level.capitalize()}: {count}")

    report.append("")

    report.append("---")
    report.append("")

    report.append("## Defect Details")
    report.append("")

    for _, defect_list in grouped.items():

        sample = defect_list[0]

        avg_confidence = (
            sum(d["confidence"] for d in defect_list)
            / len(defect_list)
        )

        report.append(
            f"### {sample['display_name']} ({len(defect_list)})"
        )

        report.append("")

        report.append(
            f"- Severity: {sample['severity']}"
        )

        report.append(
            f"- Average Confidence: {avg_confidence:.3f}"
        )

        report.append("")

        report.append("#### Description")
        report.append("")
        report.append(sample["description"])
        report.append("")

        report.append("#### Possible Causes")
        report.append("")

        for cause in sample["possible_causes"]:
            report.append(f"- {cause}")

        report.append("")

        report.append("#### Recommended Actions")
        report.append("")

        for action in sample["recommended_actions"]:
            report.append(f"- {action}")

        report.append("")

        report.append("---")
        report.append("")

    return "\n".join(report)