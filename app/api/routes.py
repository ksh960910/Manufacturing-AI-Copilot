from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.vision.detector import detect_objects

router = APIRouter()


@router.post("/detect")
async def detect(file: UploadFile = File(...)):

    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)

    image_path = temp_dir / file.filename

    with open(image_path, "wb") as f:
        f.write(await file.read())

    detections = detect_objects(str(image_path))

    return {
        "image": file.filename,
        "total_defects": len(detections),
        "detections": detections
    }