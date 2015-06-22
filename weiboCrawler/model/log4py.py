#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import model.syscontext

# 创建logger
logName = model.syscontext.config.get('logName', 'WeiboCrawler')
logger = logging.getLogger(logName)
logger.setLevel(logging.INFO)

# 创建handler，写控制台
streamHandler = logging.StreamHandler()
# 创建handler，写文件
logPath = model.syscontext.config.get('logPath', './log')
logFileName = os.path.join(logPath, ("%s.log" % logName))
fileHandler = logging.FileHandler(logFileName)

# 定义输出格式
formatter = logging.Formatter("%(asctime)s|%(name)s|%(levelname)s|%(message)s")
streamHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(streamHandler)
# logger.addHandler(fileHandler)

def logInfo(msg):
    logger.info(msg)

def logWarn(msg):
    logger.warn(msg)

def logError(msg):
    logger.error(msg)

if __name__ == '__main__':
    logInfo("test")
    logWarn("test")
    logError("test")
