import matplotlib.pyplot as plt

def plot_timetable(df):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Remove axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    # Define table
    table = ax.table(
        cellText=df.values, colLabels=df.columns, cellLoc="center", loc="center"
    )

    # Auto scale the column widths
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    # table.scale(1.2, 1.2)

    plt.show()