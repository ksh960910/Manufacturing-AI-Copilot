from ultralytics import YOLO

model = YOLO("yolo11n.pt")


def detect_objects(image_path: str) -> list:
    """
    이미지에서 객체를 탐지하여 표준 데이터 형식으로 반환
    """

    results = model(image_path)
    result = results[0]

    detections = []

    for box in result.boxes:

        cls = int(box.cls.item())
        conf = float(box.conf.item())
        bbox = box.xyxy[0].tolist()

        detections.append({
            "class": result.names[cls],
            "confidence": round(conf, 3),
            "bbox": [round(x, 2) for x in bbox]
        })

    return detections