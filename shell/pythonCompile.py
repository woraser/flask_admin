#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:Charles.chen
# createDate:2017/8/16
# Title:编译文件 为.pyc格式
# Tip:
import os
import compileall
import py_compile
from datetime import datetime

ignoreFile = [".gitignore", ".pyc"]
ignoreDir = [".git", ".idea"]
source_suffix = ".py"
target_suffix = ".pyc"


# compile and copy the source code
def compileFiles(sourceDir=None,  targetDir=None):
    if targetDir is None:
        timeStr = str(datetime.now().strftime("%Y%m%d%H%M%S"))
        targetDir = "".join([sourceDir, "_compile_", timeStr])
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
            pass
        pass
    for ignore in ignoreDir:
        if sourceDir.find(ignore) > 0:
            return
        pass
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(sourceFile):
            suffix = getFileSuffix(sourceFile)
            if suffix in ignoreFile:
                pass
            else:
                # create target dir
                if not os.path.exists(targetDir):
                    os.makedirs(targetDir)
                    pass
                if suffix == source_suffix:
                    compilePath = buildCompileFile(targetFile)
                    py_compile.compile(file=sourceFile, cfile=compilePath, dfile=None, doraise=False)
                    pass
                else:
                    if not os.path.exists(targetFile) or (os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                        open(targetFile, "wb").write(open(sourceFile, "rb").read())
                    pass
                pass
        if os.path.isdir(sourceFile):
            First_Directory = False
            if not os.listdir(sourceFile):
                # 空目录
                os.makedirs(targetFile)
                pass
            else:
                compileFiles(sourceFile, targetFile)

# build a .pyc file path
def buildCompileFile(fileName=None):
    fileSplit = os.path.splitext(fileName)
    newPath ="".join([fileSplit[0], target_suffix])
    return newPath
    pass

# get suffix from file
def getFileSuffix(fileName=None):
    return os.path.splitext(fileName)[1]

    pass




if __name__ == '__main__':
    compileFiles("E://Python27//flask_admin")
    pass