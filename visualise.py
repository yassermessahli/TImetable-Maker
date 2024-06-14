import pandas as pd

import df_to_html
import helper_functions as hf
import open_file

def visualise_timetable(variables):
    # convert variables to dictionary
    data = []

    for var in variables:
        data.append(
            {
                "group": hf.group_number_to_name(var.group),
                "day": hf.rename_day(var.slot.day),
                "time": hf.time_number_to_name(var.slot.time),
                "course": f"{var.session_type} {var.course}%newline%({var.teacher})",
            }
        )

    # Create a DataFrame from the data
    df = (
        pd.DataFrame(data)
        .set_index(["day", "group"])
        .pivot(columns="time", values="course")
    )


    file_path = "result/timetable.html"

    # Save the DataFrame to an HTML file
    change_dict = {"%newline%": "<br>"}
    df_to_html.df_to_html(df, file_path, change_dict)

    # Open the HTML file in the browser
    open_file.open_html_file_in_browser(file_path)

    # Save File as csv
    df.to_csv("result/timetable.csv")
