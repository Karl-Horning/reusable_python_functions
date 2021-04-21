import openpyxl

def delete_report_top_rows(workbookName):
    """
    This function uses openpyxl to remove 
    the first 3 lines from an Excel file 
    downloaded from the platform.
    """
    book = openpyxl.load_workbook(workbookName)
    # book.worksheets[0] is used when the name is variable.
    # book['Name of Sheet'] can be used for specific names.
    sheet = book.worksheets[0]

    # If cell A2 says that the report was automatically generated, 
    # delete the first 3 rows (the header).
    if 'Report automatically generated by' in sheet['A2'].value:
        sheet.delete_rows(1, 3)

    book.save(workbookName)

    return 0

delete_report_top_rows('Teacher Payment Report - Learnlight Holland.xlsx')