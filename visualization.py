#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from openpyxl.workbook import Workbook

EXCEL_FILE_BASIC = "fpl_basic_stats.xlsx"


def data_to_excel(data_dict):
    """ using pandas DataFrame to write data to Excel
        sheet_name: str, default ‘Sheet1’ - Name of sheet which will contain DataFrame.
        columns: sequence or list of str, optional - Columns to write.
        header: bool or list of str, default True - Write out the column names.
        If a list of string is given it is assumed to be aliases for the column names.
      """
    columns = []
    for i in data_dict:
        columns.append(i)
    df = pd.DataFrame(data_dict, columns=columns)
    df.to_excel(EXCEL_FILE_BASIC)
    print("Done! check excel file ")
