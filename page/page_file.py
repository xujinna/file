# -*- coding:utf-8 -*-
import os, sys
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

from base.base_driver import init_driver

class PageFile(BaseAction):

    # 操作
    caozu = By.XPATH, "//*[contains(@content-desc,'操作')]"

    # 属性
    attr = By.XPATH, "//*[contains(@text,'属性')]"

    # 刷新
    new = By.XPATH, "//*[contains(@text,'刷新')]"

    # 新建文件夹
    create_mkdir = By.XPATH, "//*[contains(@text,'新建文件夹')]"

    # 新建文件夹-名称
    mkdir_name = By.ID, "com.cyanogenmod.filemanager:id/input_name_dialog_edit"

    # 新建文件夹-确定按钮
    confirm_button = By.XPATH, "//*[contains(@text,'确定')]"

    # 新建文件
    create_file = By.XPATH, "//*[contains(@text,'新建文件')]"

    # 全部选择
    all_choice = By.XPATH, "//*[contains(@text,'全部选择')]"

    # 取消全选
    cancel_choice = By.XPATH, "//*[contains(@text,'取消全选')]"

    # 添加到书签
    label = By.XPATH, "//*[contains(@text,'添加到书签')]"

    # 添加快捷方式
    shortcut = By.XPATH, "//*[contains(@text,'添加快捷方式')]"

    # Set as home
    set_as_home = By.XPATH, "//*[contains(@text,'Set as home')]"

    def setup(self):
        self.driver = init_driver()
        self.click(self.caozu, time=30, poll=5)

    # 属性
    def attribute(self):
        self.click(self.attr)

    # 刷新
    def refresh(self):
        self.click(self.new)

    # 新建文件夹
    def mkdir(self):
        self.click(self.create_mkdir)

    # 新建文件夹-名称
    def mkdir_text_name(self, text):
        self.input_text(self.mkdir_name, text)

    # 新建文件夹-确定按钮
    def mkdir_confirm_button(self):
        self.click(self.confirm_button)


    # 新建文件
    def file(self):
        self.click(self.create_file)

    # 全部选择
    def choice(self):
        self.click(self.all_choice)

    # 取消全选
    def no_choice(self):
        self.click(self.cancel_choice)

    # 添加到书签
    def add_label(self):
        self.click(self.label)

    # 添加快捷方式
    def add_shortcut(self):
        self.click(self.shortcut)

    # set as home
    def set_home(self):
        self.click(self.set_as_home)
