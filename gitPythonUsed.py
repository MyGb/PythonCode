#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import getopt
from gitObjectModule import GitObject

def createDir(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        #print("文件目录已经存在.")
        pass

if __name__=="__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:],"p:",["--path="])
    except getopt.GetoptError as error:
        print(str(sys.argv[0])+" -p <path>")
        sys.exit()

    for opt,arg in opts:
        if opt in ("-p","--path"):
            #把windwos的路径分隔符换为Linux上的路径分隔符
            if "\\" in (arg):
                arg = arg.replace("\\","/")
            gitObject1 = GitObject(arg)#已经存在的Git仓库
            print(gitObject1.status())
            print(gitObject1.pull())
            print(gitObject1.checkout("Test"))
            #gitObject2 = GitObject.initRepo(arg)#初始化一个Git仓库
            #print(gitObject2.status())
            break

    