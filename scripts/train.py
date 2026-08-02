import argparse
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_YAML = PROJECT_ROOT / "data" / "raw" / "pcb" / "data.yaml"




def parse_args():
    parser = argparse.ArgumentParser(description="Train a YOLO model for PCB detection.")
    parser.add_argument(
        "--epochs",
        type=int,
        default=100,
        help="Number of training epochs (default: 100).",
    )
    parser.add_argument(
        "--imgsz",
        type=int,
        default=640,
        help="Input image size in pixels (default: 640).",
    )
    parser.add_argument(
        "--batch",
        type=int,
        default=16,
        help="Batch size (default: 16).",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    from ultralytics import YOLO

    MODEL = YOLO("yolo11n.pt")

    print(f"Dataset : {DATA_YAML}")
    print(f"Epochs: {args.epochs}, Image size: {args.imgsz}, Batch size: {args.batch}")
    print("Start YOLO training...")

    MODEL.train(
        data=str(DATA_YAML),
        epochs=args.epochs,
        imgsz=args.imgsz,
        batch=args.batch,
        project=str(PROJECT_ROOT / "models"),
        name="pcb_detector",
        exist_ok=True,
    )


if __name__ == "__main__":
    main()
