"""Reusable plotting code"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_col_by_sus(df, col, split_name, top_n=None):
    plot_df = df[[col, "sus"]].copy()
    if top_n is not None:
        keep = plot_df[col].value_counts().head(top_n).index
        plot_df = plot_df[plot_df[col].isin(keep)]
    plot_df[col] = plot_df[col].astype(str)
    plot_df["sus_label"] = plot_df["sus"].astype(str)
    sns.countplot(
        data=plot_df,
        x=col,
        hue="sus_label",
        hue_order=["0", "1"],
        order=sorted(plot_df[col].unique(), key=int),
    )
    plt.yscale("log")
    plt.title(f"{col} by sus label ({split_name}, log scale)")
    plt.show()