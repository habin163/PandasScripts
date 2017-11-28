"""
  @Author habin,
  Created on 27/11/17,
  Project: DSTests
"""

import pandas as pd
from utilities import custom_logger as cl
from bbcliutils.rztdata import ExecContexts as cntx
from bbcliutils.rztdata.RZTData import RZTData
from utilities.utils import Utils

class StringFunctions:
    log = cl.customLogs()

    def __init__(self):
        self.utils = Utils()
        pass

    def __initiate_vars(self,file_path, delimiter):
        """
        Creates the Data Frame objects and returns back in array
        :param file_path:
        :param delimiter:
        :return:
        """
        df_pandas = pd.read_csv(file_path,delimiter=delimiter)
        rzt_data = RZTData(cntx.experiment)
        df_rzt = rzt_data.read({
            'path':file_path,
            'delimiter':delimiter,
            'encoding':'utf-8'
        })

        return [df_pandas,df_rzt]

    def compareDataFrame(self, actual, expected, fnc='',index_col=1):
        actual.to_csv("Test.csv")
        actual_tmp = pd.read_csv("Test.csv",index_col=index_col)
        expected.to_csv("Test1.csv")
        expected_tmp = pd.read_csv("Test1.csv",index_col=index_col)

        if self.utils.verifyDFMatch(actual=actual_tmp, expected=expected_tmp) is None:
            self.log.info("Verified the DF Matches for {}() function".format(fnc).upper())
        else:
            self.log.error("DF match failed for {}() function".format(fnc).upper())

    def validate_asc_sort(self, file_path, col_name, delimiter=','):
        data_frames = self.__initiate_vars(file_path,delimiter)
        asc_pd = data_frames[0].sort_values(by=col_name,ascending=True)
        asc_rzt = data_frames[1].asc_sort(col_name)

        self.compareDataFrame(actual=asc_rzt, expected=asc_pd, fnc="ascending")

    def validate_desc_sort(self, file_path, col_name, delimiter=','):
        data_frames = self.__initiate_vars(file_path,delimiter)
        dsc_pd = data_frames[0].sort_values(by=col_name,ascending=False)
        dsc_rzt = data_frames[1].desc_sort(col_name)

        self.compareDataFrame(actual=dsc_rzt, expected=dsc_pd, fnc="descending")

    def validate_to_upper(self, file_path, col_name, delimiter=','):
        data_frames = self.__initiate_vars(file_path, delimiter)
        to_upper_rzt = data_frames[1].to_upper(col_name)
        to_upper_pd = data_frames[0]
        to_upper_pd[col_name] = to_upper_pd[col_name].str.upper()

        self.compareDataFrame(actual=to_upper_rzt, expected=to_upper_pd, fnc="to_upper")

    def validate_to_lower(self, file_path, col_name, delimiter=','):
        data_frames = self.__initiate_vars(file_path, delimiter)
        to_lower_rzt = data_frames[1].to_lower(col_name)
        to_lower_pd = data_frames[0]
        to_lower_pd[col_name] = to_lower_pd[col_name].str.lower()

        self.compareDataFrame(actual=to_lower_rzt, expected=to_lower_pd, fnc="to_lower")

    def validate_to_title(self, file_path, col_name, delimiter=','):
        data_frames = self.__initiate_vars(file_path, delimiter)
        to_title_rzt = data_frames[1].to_titlecase(col_name)
        to_title_pd = data_frames[0]
        to_title_pd[col_name] = to_title_pd[col_name].str.title()

        self.compareDataFrame(actual=to_title_rzt, expected=to_title_pd, fnc="to_title")

    def validate_trim(self, file_path, col_name, delimiter=','):
        data_frames = self.__initiate_vars(file_path, delimiter)
        trim_rzt = data_frames[1].trim(col_name)
        trim_pd = data_frames[0]
        trim_pd[col_name] = trim_pd[col_name].str.strip()

        self.compareDataFrame(actual=trim_rzt, expected=trim_pd, fnc="trim")

    def validate_format_date(self, file_path, col_name, new_format='%d/%m/%Y', delimiter=','):
        data_frames = self.__initiate_vars(file_path, delimiter)
        format_rzt = data_frames[1].format_date(key=col_name,destinationformat=new_format)
        format_pd = data_frames[0]
        format_pd[col_name] = pd.to_datetime(format_pd[col_name], format=new_format)

        self.compareDataFrame(actual=format_rzt, expected=format_pd, fnc="format_date")