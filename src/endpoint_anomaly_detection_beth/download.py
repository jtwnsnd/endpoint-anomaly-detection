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
        dest = DATA_DIR / name
        shutil.copy(src, dest)
        print(f"Saved {name} to {dest} ({dest.stat().st_size / 1e6:.1f} MB)")

if __name__ == "__main__":
    main()