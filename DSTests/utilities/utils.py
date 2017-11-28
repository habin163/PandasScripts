"""
  @Author habin,
  Created on 27/11/17,
  Project: DSTests
"""

import utilities.custom_logger as cl


from pandas.util.testing import assert_frame_equal
class Utils(object):

    log = cl.customLogs()

    def verifyArrayMatch(self,actual,expected):
        self.log.info("Actual array from RZTDL : {} \n Expected from Pandas/Python : {}".format(actual,expected))
        return  actual == expected

    def verifyDFMatch(self,actual,expected):
        # self.log.info("Verifying data frames")
        # actual.to_csv("Test1.csv")

        try:
            return assert_frame_equal(actual,expected)
        except Exception as e:
            self.log.error(e)
            return False

