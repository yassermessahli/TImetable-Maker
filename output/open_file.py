import webbrowser
import os


def open_html_file_in_browser(file_path):
    """
    Opens an HTML file in the default web browser.

    :param file_path: Path to the HTML file
    """
    try:
        abs_path = os.path.abspath(file_path)
        webbrowser.open("file://" + abs_path)
    except Exception as e:
        print(f"An error occurred: {e}")


# Usage example:
# open_html_file_in_browser("index.html")
