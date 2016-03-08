#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'hiroki8080'

from unittest import TestCase
from nose.tools import ok_, eq_, raises
from engine import BASE_DIR, load_ini, get_target_dir, load_handlers

class EngineTest(TestCase):
    '''
    エンジンのテスト
    '''
    def setUp(self):
        print 'Engine test start.'
    def tearDown(self):
        print 'Engine test end.'


    def test_load_ini(self):
        # 設定ファイルが読み込めるかどうか
        eq_(load_ini('config.ini'), not None)


    @raises(IOError)
    def test_load_ini_ioe(self):
        # 設定ファイルが存在しない場合、例外がスローされるかどうか
        load_ini("hoge.ini")


    def test_get_target_dir(self):
        # target_dirに「.」が指定されている場合、カレントディレクトリが取得できるかどうか
        parser = load_ini('config.ini')
        eq_(get_target_dir(parser), BASE_DIR)
        # target_dirにパスが指定されている場合、取得できるかどうか
        parser = load_ini('config2.ini')
        eq_(get_target_dir(parser), 'D:\\hoge')


    def test_load_handlers(self):
        # ハンドラが読み込めるかどうか
        result = load_handlers('config.ini')
        eq_(len(result), 1)
        eq_(result[0].filesize, '100')
        eq_(result[0].type, 'delete')
