# reusable_python_functions
 A group of Python functions that can be used to format data from the platform or from Microsoft Lists.

## delete_report_top_rows
This function uses openpyxl to remove the first 3 lines from an Excel file downloaded from the platform.

This then makes the data readable using Pandas.


## save_csv_as_xlsx
Removes the headache of opening CSV files in Excel on macOS. It does this by saving a CSV file as an Excel file. This displays UTF-8 characters correctly on macOS as Excel displays UTF-8 characters in CSV files incorrectly.