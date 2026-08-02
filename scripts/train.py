from pathlib import Path
from ultralytics import YOLO

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_YAML = PROJECT_ROOT / "data" / "raw" / "pcb" / "data.yaml"




def main():

    MODEL = YOLO("yolo11n.pt")

    print(f"Dataset : {DATA_YAML}")
    print("Start YOLO training...")

    MODEL.train(
        data=str(DATA_YAML),
        epochs=1,
        imgsz=640,
        batch=16,
        project=str(PROJECT_ROOT / "models"),
        name="pcb_detector",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()