#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import getopt,sys

def runTask(argv):
    branchVersion = 0
    try:
        #opts：格式信息;args对应的参数.
        opts, args = getopt.getopt(argv[1:],"hv:c:",["version=","client="])
    except getopt.GetoptError:
        print(str(argv[0])+" -v <version> -c <client>")
        sys.exit()

    for opt,arg in opts:
        if opt == '-h':
            print(str(argv[0])+" -v <version> -c <client>")
            sys.exit()
        elif opt in ("-v","--version"):
            pass
        elif opt in ("-c","--client"):
            pass
            
    print("done.")

if __name__ == '__main__':
    #print(str(sys.argv))#获取输入的完整的参数
    runTask(sys.argv)#获取除运行命令的其他参数