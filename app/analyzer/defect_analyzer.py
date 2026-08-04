from collections import Counter

from app.analyzer.knowledge_base import DEFECT_KNOWLEDGE

HIGH_CONFIDENCE_THRESHOLD = 0.8
MEDIUM_CONFIDENCE_THRESHOLD = 0.5

def analyze_defects(detections: list) -> dict:
    """
    Detection 결과를 요약하여 반환한다.

    Args:
        detections (list): detector.py에서 반환한 Detection 결과

    Returns:
        dict: 결함 요약 정보
    """

    class_counts = Counter()
    severity_counts = Counter()

    confidence_counts = {
        'high' : 0,
        'medium' : 0,
        'low' : 0,
    }

    confidences = []
    enriched_detections = []

    for detection in detections:
        cls = detection['class']
        confidence = detection['confidence']

        class_counts[cls] += 1
        confidences.append(detection["confidence"])

        if confidence >= HIGH_CONFIDENCE_THRESHOLD:
            confidence_counts['high']+=1

        elif confidence >=MEDIUM_CONFIDENCE_THRESHOLD:
            confidence_counts['medium']+=1

        else:
            confidence_counts['low']+=1

        knowledge = DEFECT_KNOWLEDGE.get(cls, {})

        severity = knowledge.get('severity', {})

        if severity:
            severity_counts[severity]+=1

        enriched_detection = {
            **detection,
            **knowledge
        }

        enriched_detections.append(enriched_detection)

    SEVERITY_PRIORITY = {
    "Critical": 4,
    "High": 3,
    "Medium": 2,
    "Low": 1,
    }

    highest_severity = None

    if severity_counts:
        highest_severity = max(
            severity_counts.keys(),
            key=lambda x: SEVERITY_PRIORITY[x]
        )

    total_defects = len(detections)

    average_confidence = (
        round(sum(confidences) / total_defects, 3)
        if total_defects > 0
        else 0.0
    )

    summary = {
        'total_defects': total_defects,
        'class_counts' : dict(class_counts),
        'severity_counts' : dict(severity_counts),
        'highest_severity' : highest_severity,
        'confidence' : confidence_counts,
        'average_confidence' : average_confidence,
    }

    return {
        'summary' : summary,
        'detections' : enriched_detections,
    }