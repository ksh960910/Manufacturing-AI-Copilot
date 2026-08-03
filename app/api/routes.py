from pathlib import Path

from fastapi import APIRouter, UploadFile, File

from app.vision.detector import detect_objects

router = APIRouter()


@router.post("/detect")
async def detect(file: UploadFile = File(...)):

    temp_dir = Path("temp")
    temp_dir.mkdir(exist_ok=True)

    image_path = temp_dir / file.filename

    try:
        with open(image_path, "wb") as f:
            f.write(await file.read())

        detections = detect_objects(str(image_path))

        return {
            "image": file.filename,
            "total_defects": len(detections),
            "detections": detections
        }
    finally:
        image_path.unlink(missing_ok=True)

        try:
            temp_dir.rmdir()
        except OSError:
            # 다른 요청의 파일이 남아 있으면 폴더는 유지
            pass
