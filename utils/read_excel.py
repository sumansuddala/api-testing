from pandas import read_excel

def read_file(filepath, sheetname):
    df = read_excel(filepath, sheet_name = sheetname)
    return df