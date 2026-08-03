from collections import Counter


def analyze_defects(detections: list) -> dict:
    """
    Detection 결과를 요약하여 반환한다.

    Args:
        detections (list): detector.py에서 반환한 Detection 결과

    Returns:
        dict: 결함 요약 정보
    """

    class_counts = Counter()
    confidences = []

    for detection in detections:
        class_counts[detection["class"]] += 1
        confidences.append(detection["confidence"])

    total_defects = len(detections)

    average_confidence = (
        round(sum(confidences) / total_defects, 3)
        if total_defects > 0
        else 0.0
    )

    return {
        "total_defects": total_defects,
        "class_counts": dict(class_counts),
        "average_confidence": average_confidence,
    }