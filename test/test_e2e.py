import pytest

from Utilities.BaseClass import BaseClass

class TestOne(BaseClass):
    def test_e2e(self, setup):
        self.driver.find