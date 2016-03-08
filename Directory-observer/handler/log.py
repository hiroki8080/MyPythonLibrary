#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

__author__ = 'hiroki8080'

class LogWatchHandler(FileSystemEventHandler):
    '''
    ログをウォッチするハンドラ
    '''

    def on_created(self, event):
        if event.is_directory:
            return
        print('%s has been created.' % event.src_path)

    def on_modified(self, event):
        if event.is_directory:
            return
        print('%s has been modified.' % event.src_path)

    def on_deleted(self, event):
        if event.is_directory:
            return
        print('%s has been deleted' % event.src_path)

class LogRotationHandler(FileSystemEventHandler):
    '''
    ログをローテーションするハンドラ
    '''

    filesize = '0'
    type = 'delete'

    def on_modified(self, event):
        if event.is_directory:
            return
        # ログファイルが更新された際に、ファイルが指定された値より大きくなった場合に削除します。
        if os.path.splitext(event.src_path)[-1].lower() in ('.log'):
            size = os.path.getsize(event.src_path)
            print('file size %s byte.' % size)
            if int(self.filesize) < size:
                if self.type == 'delete':
                    print('rotate target [%s.]' % event.src_path)
                    os.remove(event.src_path)
