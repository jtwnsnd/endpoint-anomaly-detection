"""Features for analyzing BETH dataset"""
import pandas as pd
import seaborn as sns
import matplotlib as plt
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"

def load_split(name: str) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / f"labelled_{name}_data.csv")
