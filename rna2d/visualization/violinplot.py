
from dataclasses import dataclass

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


@dataclass
class Violinplot():
    style:str = "whitegrid"
    sns.set_theme(style=style)

    def plot(self, sns_df:pd.DataFrame, axs:plt.axis, panel_id: str, title:str, y_left:bool=True, x_axis:bool=True):
        # set custom color palette
        order = sns_df.groupby(['Method', 'Color']).count().sort_values(by=['Color', "Method"], ascending=[True, True]).index
        custom_palette = [sns.color_palette("colorblind", 3)[c] for m, c in order]
        print(len(custom_palette))
        
        ax = sns.violinplot(x='INF', y='Method',  inner=None, data=sns_df,  cut=0, palette=custom_palette)
        # sns set plot values range
        ax.set_xlim(0, 1)
        bottom, top = ax.get_ylim()
        val = 0.0
        ax.set_ylim(bottom + val, top - val)
        
        ax.set(title=title)
        ax.set_ylabel("")
        if not y_left:
            ax.set_ylabel("")
            ax.set_yticklabels("")
        if not x_axis:
            ax.set_xlabel("")
        ax.text(-0.1, 1.1, panel_id, transform=ax.transAxes, 
            size=20, weight='bold')
        # ax.legend_.remove()
    