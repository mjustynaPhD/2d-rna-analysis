
from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


@dataclass
class Violinplot():
    style:str = "whitegrid"
    sns.set_theme(style=style)

    def plot(self, sns_df:pd.DataFrame, axs:plt.axis, panel_id: str, title:str, y_left:bool=True, x_axis:bool=True):
        ax = sns.violinplot(x='INF', y='Method', inner=None, hue='Color', data=sns_df, ax=axs, cut=0, palette='colorblind')
        # sns set plot values range
        ax.set_xlim(0, 1)
        
        ax.set(title=title)
        ax.set_ylabel("")
        if not y_left:
            ax.set_ylabel("")
            ax.set_yticklabels("")
        if not x_axis:
            ax.set_xlabel("")
        ax.text(-0.1, 1.1, panel_id, transform=ax.transAxes, 
            size=20, weight='bold')
        ax.legend_.remove()
    