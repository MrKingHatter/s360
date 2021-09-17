import gspread
from gspread_dataframe import set_with_dataframe
import pandas as pd
from typing import Union, List


class Sheet:
    def __init__(self, name: str, columns: List[str]):
        self.name = name
        self.sheet = pd.DataFrame(columns=columns)

    def import_dataframe(self, dataframe: pd.DataFrame):
        self.sheet = dataframe

    def __getitem__(self, key):
        return self.sheet[key]

    def shape(self):
        return self.sheet.shape


class SpreadSheetHandler:
    """
    Object for handling interactions with Google sheets
    Arguments:
        sheet_link: the link to the google sheets document
        auth: google authorization key
    Attributes:
        sheets: gspread object for holding the google sheets document
    Methods:
        grab_sheet: method for grabbing a specific sheet from the sheets in a pandas DataFrame
        overwrite: method for writing a pandas DataFrame to a sheet
    """

    def __init__(self, sheet_link: str, auth: gspread.client.Client):
        self.sheets = auth.open_by_url(sheet_link)  # Grab the sheets from the link

    def grab_sheet(self, sheet_name: str) -> Union[Sheet, None]:
        """
        Method for grabbing the data from a given sheet as a pandas DataFrame
        """
        new_sheet = Sheet(sheet_name, [])
        try:
            sheet = self.sheets.worksheet(sheet_name)  # Grab the specified sheet
            sheet_df = pd.DataFrame(sheet.get_all_records())  # Format to pandas DataFrame
            new_sheet.import_dataframe(sheet_df)
            return new_sheet
        except gspread.WorksheetNotFound:
            return None

    def overwrite(self, sheet_name: str, data: Sheet):
        """
        Method for overwriting all the data in a given sheet with a new dataframe
        """
        try:
            sheet = self.sheets.worksheet(sheet_name)  # Grab the sheet
            sheet.clear()  # Clear the worksheet if it exists
            set_with_dataframe(sheet, data, include_index=False, include_column_header=True)  # Save the dataframe
        except gspread.WorksheetNotFound:
            self.sheets.add_worksheet(title=sheet_name, rows=data.shape()[0], cols=data.shape()[1])  # Otherwise reate the new sheet of a fitting size
            sheet = self.sheets.worksheet(sheet_name)  # Grab the fresh sheet
            set_with_dataframe(sheet, data, include_index=False, include_column_header=True)  # Save the dataframe

