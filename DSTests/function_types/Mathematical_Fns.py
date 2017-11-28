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
import numpy as np


class Mathematical:
    # Variables
    __file = ''
    __delimiter = ''
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

    def compareDataFrame(self, actual, expected, fnc='',index_col=1):
        actual.to_csv("Test.csv")
        actual_tmp = pd.read_csv("Test.csv",index_col=index_col)
        expected.to_csv("Test1.csv")
        expected_tmp = pd.read_csv("Test1.csv",index_col=index_col)

        if self.utils.verifyDFMatch(actual=actual_tmp, expected=expected_tmp) is None:
            self.log.info("Verified the DF Matches for {}() function".format(fnc).upper())
        else:
            self.log.error("DF match failed for {}() function".format(fnc).upper())


    def validate_sqrt(self, file_path, col_name, delimiter=',',new_col_name=''):
        data_frames = self.__initiate_vars(file_path,delimiter)
        if new_col_name is None:
            sqrt_rzt = data_frames[1].sqrt(col_name)
            sqrt_pd = data_frames[0][col_name] ** 0.5

        else:
            sqrt_rzt = data_frames[1].sqrt(col_name, new_col_name)
            sqrt_pd = data_frames[0]
            sqrt_pd[new_col_name] = sqrt_pd[col_name] ** 0.5

        self.compareDataFrame(actual=sqrt_rzt, expected=sqrt_pd, fnc="sqrt")

    def validate_inverse(self, file_path, col_name, delimiter=',',new_col_name=''):
        data_frames = self.__initiate_vars(file_path, delimiter)
        if new_col_name is None:
            inverse_rzt = data_frames[1].inverse(col_name)
            inverse_pd = data_frames[0]
            inverse_pd[col_name] = 1/inverse_pd[col_name]
        else:
            inverse_rzt = data_frames[1].inverse(col_name, new_col_name)
            inverse_pd = data_frames[0]
            inverse_pd[new_col_name] = 1/inverse_pd[col_name]
        self.compareDataFrame(actual=inverse_rzt, expected=inverse_pd, fnc="inverse")

    def validate_power(self, file_path, col_name, exponent, delimiter=',',new_col_name=''):
        data_frames = self.__initiate_vars(file_path, delimiter)
        if new_col_name is None:
            power_rzt = data_frames[1].pow(col_name,exponent=exponent)
            power_pd = data_frames[0]
            power_pd[col_name] = power_pd[col_name] ** exponent
        else:
            power_rzt = data_frames[1].pow(col_name, new_col_name, exponent=exponent)
            power_pd = data_frames[0]
            power_pd[new_col_name] = power_pd[col_name] ** exponent
        self.compareDataFrame(actual=power_rzt, expected=power_pd, fnc="power")

    def validate_log2(self, file_path, col_name, delimiter=',',new_col_name=''):
        data_frames = self.__initiate_vars(file_path, delimiter)
        if new_col_name is None:
            log_rzt = data_frames[1].log2(col_name)
            log_pd = data_frames[0]
            log_pd[col_name] = np.log2(log_pd[col_name])
        else:
            log_rzt = data_frames[1].log2(col_name, new_col_name)
            log_pd = data_frames[0]
            log_pd[new_col_name] = np.log2(log_pd[col_name])
        self.compareDataFrame(actual=log_rzt, expected=log_pd, fnc="log2")

    def validate_log10(self, file_path, col_name, delimiter=',', new_col_name=''):
        data_frames = self.__initiate_vars(file_path, delimiter)
        if new_col_name is None:
            log_rzt = data_frames[1].log10(col_name)
            log_pd = data_frames[0]
            log_pd[col_name] = np.log10(log_pd[col_name])
        else:
            log_rzt = data_frames[1].log10(col_name, new_col_name)
            log_pd = data_frames[0]
            log_pd[new_col_name] = np.log10(log_pd[col_name])
        self.compareDataFrame(actual=log_rzt, expected=log_pd, fnc="log10")

    def validate_log(self, file_path, col_name, base=10, delimiter=',', new_col_name=''):
        data_frames = self.__initiate_vars(file_path, delimiter)
        if new_col_name is None:
            log_rzt = data_frames[1].log(col_name, base=base)
            log_pd = data_frames[0]
            log_pd[col_name] = np.log(log_pd[col_name])/np.log(base)
        else:
            log_rzt = data_frames[1].log(col_name, new_col_name, base=base)
            log_pd = data_frames[0]
            log_pd[new_col_name] = np.log(log_pd[col_name])/np.log(base)
        self.compareDataFrame(actual=log_rzt, expected=log_pd, fnc="log")
