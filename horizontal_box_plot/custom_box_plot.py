# - Create a custom figure with multiple horizontal boxplots.
# - Created by: Kristin Chang
# - Last updated: May 2025

import matplotlib.pyplot as plt
import numpy as np
from typing import List, Optional, Tuple, Union

def custom_box_plot(
        data: Union[np.ndarray, List[np.ndarray]],
        labels: Union[np.ndarray[str], List[np.ndarray[str]]],
        fig_save_as: Optional[str] = './custom_box_plot.png',
        font_size: Optional[int] = 14,
        box_fill_color: Optional[str] = 'lightgray',
        median_line_color: Optional[str] = 'black',
        median_line_width: Optional[float] = 1,
        marker_style: Optional[str] = 'o',
        marker_color: Optional[str] = 'royalblue',
        marker_alpha: Optional[float] = 0.9,
        marker_size: Optional[float] = 5,
        marker_outline_width: Optional[float] = 0,
        spacing_factor: Optional[float] = 0.5,
        fig_ylabels: Optional[Union[np.ndarray[str], List[np.ndarray[str]]]] = [['Scenario 1'], ['Scenario 2']],
        fig_title: Optional[str] = 'Custom Box Plot',
        xlabel: Optional[str] = 'Values',
        fig_size: Optional[Tuple[int, int]] = (10, 7)
        ):
    """
    Creates a matplotlib figure containing horizontal box subplots.

    Parameters:
    ----------
    data : array
        A single numpy array or ordered list of arrays containing the data.
    labels : array
        A numpy array containing the ordered list of labels (str) for each set of data.
    fig_save_as : str
        Relative path, filename, and filetype to save the figure as.
    font_size : int
        Font size for figure text.
    box_fill_color : str
        Fill color for all boxes in the figure subplots.
    median_line_color : str
        Line color for Median marker.
    median_line_width : float
        Line width for Median marker.
    marker_style : str
        Marker style for individual points. Default is 'o'. Other typical styles include: '.'(point), '^'(triangle up), 's'(square), 'H'(hexagon2).
        See matplotlib docs for more styles: https://matplotlib.org/stable/api/markers_api.html
    marker_color : str
        Fill color for individual point markers. Default is 'royalblue'. Available named colors here: https://matplotlib.org/stable/gallery/color/named_colors.html
    marker_alpha : float
        Transparency value for individual point markers.
    marker_size : float
        Size of individual point markers.
    marker_outline_width : float
        Line width of individual point markers.
    spacing_factor : float
        Adjust vertical spacing between subplot ylabels (e.g., vertical space between each box row).
    fig_ylabels : array
        A numpy array containing the ordered list of labels (str) for each subplot.
    fig_title : str
        Title for the figure.
    xlabel : str
        Label for the figure xaxis.
    fig_size : tuple
        Set the size of the figure as a Tuple. (e.g., (10, 7)).

    Returns:
    ----------
    plt.Figure
        MatPlotLib Figure with single or multiple horizontal box subplots.
    image
        Saves specified image file to fig_save_as destination.
    """

    # Prepare figure
    plt.rcParams['font.size'] = font_size
    number_of_subplots = len(data)
    fig, axs = plt.subplots(number_of_subplots, 1, figsize=fig_size, gridspec_kw={'height_ratios': [1,1]})

    # Generate subplots
    for i in np.arange(0, number_of_subplots):
        plot_scenario(
            axs[i],
            labels[i],
            data[i],
            box_fill_color,
            median_line_color,
            median_line_width,
            marker_style,
            marker_color,
            marker_alpha,
            marker_size,
            marker_outline_width,
            spacing_factor,
            fig_ylabels[i]
            )

    # Add details to figure
    axs[0].set_title(fig_title, pad=15)
    axs[-1].set_xlabel(xlabel, labelpad=15)
    fig.align_ylabels()
    plt.subplots_adjust(hspace=0.25)
    plt.savefig(fig_save_as, bbox_inches='tight')

# ----------
# HELPER FUNCTIONS
# ---------
def plot_scenario(
        ax: plt.Axes,
        labels: Union[np.ndarray[str], List[np.ndarray[str]]],
        data: Union[np.ndarray, List[np.ndarray]],
        box_fill_color: Optional[str] = 'lightgray',
        median_line_color: Optional[str] = 'black',
        median_line_width: Optional[float] = 1,
        marker_style: Optional[str] = 'o',
        marker_color: Optional[str] = 'royalblue',
        marker_alpha: Optional[float] = 0.9,
        marker_size: Optional[float] = 5,
        marker_outline_width: Optional[float] = 0,
        spacing_factor: Optional[float] = 0.5,
        fig_ylabel: Optional[str] = ['Scenario']
        ):

    # Define custom positions to reduce spacing between boxes
    positions = np.arange(1, len(data) + 1) * spacing_factor

    # Create subplot 1
    bp = ax.boxplot(
        data,
        vert=False,
        labels=labels,
        patch_artist=True,
        positions=positions
        )

    for i, dataset in enumerate(data):
        y = positions[i]
        x = dataset
        ax.plot(
            x,
            np.full_like(x,y),
            marker_style,
            color=marker_color,
            alpha=marker_alpha,
            markersize=marker_size,
            markeredgewidth=marker_outline_width
        )

    # Customize elements
    for box in bp['boxes']:
        box.set_facecolor(box_fill_color)

    for median in bp['medians']:
        median.set(linewidth=median_line_width)
        median.set(color=median_line_color)

    # Adjust y-axis labels to match box positions
    ax.set_yticks(positions)
    ax.set_yticklabels(labels)

    # Add labels to plot
    ax.set_ylabel('             '+fig_ylabel+'           ', bbox=dict(edgecolor='black', facecolor='lightgray'), labelpad=20)
    return ax