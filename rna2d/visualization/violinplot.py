
from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


@dataclass
class Violinplot():
    style:str = "whitegrid"
    sns.set_theme(style=style)

    def plot(self, sns_df:pd.DataFrame, axs:plt.axis, title:str, y_left:bool=True, x_axis:bool=True):
        ax = sns.violinplot(x='INF', y='Method', inner=None, color='grey', data=sns_df, ax=axs, cut=0)
        ax.set(title=title)
        ax.set_ylabel("")
        if not y_left:
            ax.set_ylabel("")
            ax.set_yticklabels("")
        if not x_axis:
            ax.set_xlabel("")
    