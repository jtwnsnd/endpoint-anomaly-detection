"""Download the BETH process-event CSVs into the repo's data/ folder."""
from pathlib import Path
import shutil
import kagglehub

DATA_DIR = Path(__file__).resolve().parents[2] / "data"
SPLITS = ["labelled_training_data.csv", "labelled_testing_data.csv", "labelled_validation_data.csv"]

def main():
    cache = Path(kagglehub.dataset_download("katehighnam/beth-dataset"))
    DATA_DIR.mkdir(exist_ok=True)
    for name in SPLITS:
        src = next(cache.rglob(name))
        shutil.copy(src, DATA_DIR / name)
        print("copied", name)

if __name__ == "__main__":
    main()