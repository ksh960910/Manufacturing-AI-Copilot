from ultralytics import YOLO


def main():
    model = YOLO("yolo11n.pt")

    model.train(
        data="data/raw/pcb/data.yaml",
        epochs=1,
        imgsz=640,
        batch=16,
        project="runs",
        name="pcb_detector"
    )

if __name__ == "__main__":
    main()