"""
  @Author habin,
  Created on 27/11/17,
  Project: DSTests
"""

import unittest
from function_types.Aggregate_Fns import Aggregate
import pytest
from utilities import custom_logger as cl
from function_types.Mathematical_Fns import Mathematical
from function_types.String_Fns import StringFunctions

class PocTests(unittest.TestCase):
    log = cl.customLogs()

    __file = "/Users/habin/Desktop/corr_test.csv"

    @pytest.fixture(scope='session')
    def setUp(self):
        self.agg = Aggregate()
        self.mat = Mathematical()
        self.stt = StringFunctions()


    def test_aggregate(self):
        self.log.info("Validating count function")
        self.agg.validate_count(file_path=self.__file)


    def test_mathematical(self):
        self.log.info("Validating square root function")
        self.mat.validate_sqrt(self.__file, "float",new_col_name='Habin')
        self.log.info("Validating Inverse/Reciprocal of a column")
        self.mat.validate_inverse(self.__file, "float",new_col_name='Habin')
        self.log.info("Validating Power function")
        self.mat.validate_power(self.__file,"float",2,new_col_name="Habin")
        self.log.info("Validating Log2 function")
        self.mat.validate_log2(self.__file, "float",new_col_name="Habin")
        self.log.info("Validating Log10 function")
        self.mat.validate_log10(self.__file, "float",new_col_name="Habin")
        self.log.info("Validating Log function")
        self.mat.validate_log(self.__file, "float",new_col_name="Habin")


    def test_string(self):
        self.log.info("Validating to_upper function")
        self.stt.validate_to_upper(self.__file, "gender")
        self.log.info("Validating to_lower function")
        self.stt.validate_to_lower(self.__file, "gender")
        self.log.info("Validating to_title function")
        self.stt.validate_to_title(self.__file, "gender")
        self.log.info("Validating trim function")
        self.stt.validate_trim(self.__file, "gender")
        self.log.info("Validating format_date function")
        self.stt.validate_format_date(self.__file, "last-updated-datetime")
