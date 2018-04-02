# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.getcwd())

from base.base_driver import init_driver
from page.page_file import PageFile

class TestFile:

    def setup(self):
        self.driver = init_driver()
        self.file = PageFile(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_file(self):
        self.file.mkdir_text_name("zzz")
        self.file.mkdir_confirm_button()
        # self.file.mkdir_text_name("aaa")
        # self.file.mkdir_confirm_button()



