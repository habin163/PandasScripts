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


class Aggregate:
    # Variables
    __file = ''
    __delimiter= ''
    __col_name = ''
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

    def validate_count(self, file_path, delimiter=','):
        data_frames = self.__initiate_vars(file_path, delimiter)
        count_pd = len(data_frames[0])
        count_rzt = data_frames[1].count()
        if self.utils.verifyArrayMatch(actual=count_rzt,expected=count_pd):
            self.log.info("Verified the row count matches in both Data Frames")
        else:
            self.log.error("Row count match failed")

    def validate_minima(self, file_path, delimiter=',', col_name=''):
        data_frames = self.__initiate_vars(file_path, delimiter)
        min_pd = data_frames[0][col_name].min()
        min_rzt = data_frames[1][col_name].min()
        if self.utils.verifyArrayMatch(actual=min_rzt,expected=min_pd):
            self.log.info("Verified the Minima matches in both Data Frames on column name : {}".format(col_name).upper())
        else:
            self.log.error("Minima does not match")

    def validate_maxima(self, file_path, delimiter=',', col_name=''):
        data_frames = self.__initiate_vars(file_path, delimiter)
        max_pd = data_frames[0][col_name].max()
        max_rzt = data_frames[1][col_name].max()
        if self.utils.verifyArrayMatch(actual=max_rzt, expected=max_pd):
            self.log.info(
                "Verified the Maxima matches in both Data Frames on column name : {}".format(col_name).upper())
        else:
            self.log.error("Maxima does not match")