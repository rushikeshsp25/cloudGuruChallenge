import pandas as pd
from Extract import extract_csv


def tranform_data(nyt_dfs,jhu_dfs):
	 """
        Parameters:
        nyt_dfs = extracted NewYork dataset
        jhu_dfs = extractted John Hopkins dataset

        Returns:
        merged dataframe of NYT and JHS datasets
    """
	jhu_dfs = jhu_dfs[jhu_dfs['Country/Region'] == 'US']           						#Step : Remove non-us data (reverse coding)
	jhu_dfs = jhu_dfs.loc[:,['Date','Recovered']]                 						#Step : Remove unnecessary columns 
	jhu_dfs = jhu_dfs.rename(columns = {'Date': 'date', 'Recovered': 'recovered'}) 		#Step : Renaming columns for JHS to have consistency and to avoid key issues while merging datasets
	final_dfs = pd.merge(nyt_dfs,jhu_dfs, on="date")                                    #Step : Join datasets.
	return final_dfs

	

if __name__=="__main__":
    nyt_csv = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv"
    jhu_csv = "https://raw.githubusercontent.com/datasets/covid-19/master/data/time-series-19-covid-combined.csv"
    nyt_dfs = extract_csv(nyt_csv, ['date'])
    jhu_dfs = extract_csv(jhu_csv, ['Date'])
    final_dfs= tranform_data(nyt_dfs,jhu_dfs)
    print(final_dfs)
    
