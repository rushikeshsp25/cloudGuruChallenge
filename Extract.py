import pandas

def extract_csv(csv_url, date_columns=[]):
    """
        Parameters:
        csv_url (string): url of the csv file
        date_columns (list): list of the column names containing date type values

        Returns:
        pandas dataframe of the csv file
    """
    try:
        if not isinstance(csv_url, str) or not isinstance(date_columns, list):
            raise Exception("Invalid Arguments")
        return pandas.read_csv(csv_url,parse_dates=date_columns)
    except:
        raise Exception("Something went wrong while fetching CSV data")

if __name__=="__main__":
    nyt_csv = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
    jhu_csv = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
    nyt_dfs = extract_csv(nyt_csv, ['date'])
    jhu_dfs = extract_csv(jhu_csv, ['Date'])
    print(nyt_dfs)
    print(jhu_dfs)