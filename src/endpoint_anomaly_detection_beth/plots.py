"""Reusable plotting code"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_col_by_sus(df, col, split_name):
    plot_df = df[[col, "sus"]].copy()
    plot_df[col] = plot_df[col].astype(str)
    plot_df["sus_label"] = plot_df["sus"].astype(str)
    sns.countplot(data=plot_df, x=str(col), hue="sus_label")
    plt.yscale("log")
    plt.title(f"{col} by sus label ({split_name}, log scale)")
    plt.show()