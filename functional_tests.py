# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张小胖听说有个在线待办事项应用很不错
        # 他搜索去登录了这个应用的首页
        self.browser.get('http://localhost:8000')

        #他看到网页标题和头部都包含"TO-DO"关键词
        self.assertIn('To-Do' , self.browser.title)
        self.fail('Finisfh the test!')

        #应用邀请她输入一个待办事项
        #她在文本框中输入了"Buy Box"
        #因为她的爱好是收藏盒子
        #输入后按回车,页面更新了
        #待办事项表格中显示了"1:Buy Box"
        #同时页面又出现一个文本框可以输入其他待办事项
        #他有输入了"Use Box"
        #页面再次更新,她的清单中显示两个待办事项
        #他想知道下次登录还有没有,应用是否保存
        #他看到网站为他生成了一个唯一的URL
        #而且网页中有一些文字解说这个功能
        #他访问了这个唯一的URL发现待办事项都在
        #他很满意之后去睡觉了

if __name__ == '__main__':
    unittest.main()