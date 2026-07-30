from pathlib import Path
import shutil
import os

from dotenv import load_dotenv
from roboflow import Roboflow

PROJECT_ROOT = Path(__file__).resolve().parent.parent

print(PROJECT_ROOT)

DATA_ROOT = PROJECT_ROOT / "data"
RAW_ROOT = DATA_ROOT / "raw"
PCB_ROOT = RAW_ROOT / "pcb"

# Get API key from .env
def get_api_key():

    load_dotenv()

    api_key = os.getenv("ROBOFLOW_API_KEY")

    if api_key is None:
        raise ValueError("ROBOFLOW_API_KEY not found.")

    return api_key

# Download roboflow dataset and set data directory
def download_dataset(api_key):

    rf = Roboflow(api_key=api_key)
    project = rf.workspace("test-yylx4").project("pcb-defect-uqoat")
    dataset = project.version(2).download("yolov11")

    downloaded_path = Path(dataset.location)

    RAW_ROOT.mkdir(parents=True, exist_ok=True)

    shutil.move(str(downloaded_path), str(PCB_ROOT))

def main():

    if PCB_ROOT.exists():
        print("Dataset already exists.")
        return
    else:
        api_key = get_api_key()
        download_dataset(api_key)

        print("Dataset setup completed.")

if __name__=='__main__':
    main()