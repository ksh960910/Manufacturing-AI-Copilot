from pathlib import Path
from ultralytics import YOLO

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = PROJECT_ROOT / 'models' / 'trained' / 'best.pt'

if MODEL_PATH.exists():
    print("Using fine-tuned model")
    model = YOLO(str(MODEL_PATH))
else:
    print("Using pretrained model")
    model = YOLO('yolo11n.pt')

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