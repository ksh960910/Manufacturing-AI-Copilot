from ultralytics import YOLO

model = YOLO("models/trained/best.pt")

results = model("data/raw/pcb/test/images/01_missing_hole_13_jpg.rf.6cc34a0f55a0a57a56a63584982cbf18.jpg")

print(results[0].boxes)