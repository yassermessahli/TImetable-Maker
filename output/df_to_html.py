import pandas as pd


def df_to_html(df: pd.DataFrame, file_path: str, change_dict: dict = None):
    """
    Converts a Pandas DataFrame to an HTML file.

    :param df: The DataFrame to convert
    :param file_path: The path to save the HTML file
    """
    # only show index of columns ( day and group ) and do not show time
    html = df.to_html(
        index=True,
        index_names=True,
        header=True,
        classes="table table-bordered",
        na_rep="/",
    )

    # replace things in change_dict
    for key, value in change_dict.items():
        html = html.replace(key, value)

    # wrap the hole thing inside html tag and add head and body tags
    # add styles from "style.css" file
    html = f"<html><head><link rel='stylesheet' type='text/css' href='style.css'></head><body>{html}</body></html>"

    with open(file_path, "w") as fou:
        fou.write(html)
