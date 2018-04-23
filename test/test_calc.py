from unittest import TestCase
'单元测试'
__author__ = 'yangzteL'

import first


class TestCalc(TestCase):
    # 方法名固定
    def setUp(self):
        print('单元测试前执行...')

    # 方法名固定
    def tearDown(self):
        print('单元测试后执行...')
    def test_calc(self):
        assert first.calc(5, 1) == 5
