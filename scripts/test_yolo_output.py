from app.vision.detector import detect_objects

detections = detect_objects(
    'https://ultralytics.com/iamges/bus.jpg'
)

print(detections)