from ultralytics import YOLO

model = YOLO('yolo11n.pt')

results = model("https://ultralytics.com/images/bus.jpg")

result = results[0]

detections = []

for box in result.boxes:

    cls = int(box.cls.item())
    conf = float(box.conf.item())

    bbox = box.xyxy[0].tolist()

    detection = {
        "class": result.names[cls],
        "confidence": round(conf, 3),
        "bbox": [round(x, 2) for x in bbox]
    }

    print(detection)

    detections.append(detection)


result.save('runs/result.jpg')

print('YOLO inference completed')