"""
  @Author habin,
  Created on 27/11/17,
  Project: DSTests
"""
class Basics:

    def __init__(self,df):
        self.df = df

    def column_headers(self):
        return self.df.columns.values.tolist()

    def column_values(self,column):
        return self.df[column].tolist()

    def column_uniques(self,column):
        return self.df[column].unique().tolist()

    def row_count(self):
        return len(self.df)

    def dataframe_shape(self):
        return self.df.shape

    def column_min(self,column):
        return self.df[column].min()

    def column_max(self,column):
        return self.df[column].max()

    def column_mean(self,column):
        return self.df[column].mean()

    def column_median(self,column):
        return self.df[column].median()

    def column_mode(self,column):
        return self.df[column].mode()[0]

    def column_variance(self,column):
        return self.df[column].var()

    def column_standard_deviation(self,column):
        return self.df[column].std()

    def column_sort_asc(self,column):
        return self.df.sort_values(by=column, ascending=True)

    def column_sort_desc(self,column):
        return self.df.sort_values(by=column, ascending=False)

    def dataframe_sample(self,count=100):
        return self.df.head(n=count)

    def dataframe_filter_values(self,column,array):
        idx = self.df.index[self.df[column].isin(array)]
        return self.df.loc[idx]

    def dataframe_to_csv(self,file,delimiter=","):
        self.df.to_csv(file, sep=delimiter)

    def dataframe_corr(self,method):
        return self.df.corr(method=method)