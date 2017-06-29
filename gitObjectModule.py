#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from git import Repo

class GitObject(object):
    def __init__(self,repoPath):
        self.repo = Repo(repoPath)
        self.git = self.repo.git

    @classmethod
    def initRepo(self,initRepoPath=None):
        if initRepoPath:
            Repo.init(initRepoPath)
            return GitObject(initRepoPath)

    def status(self):
        return self.git.status()

    def add(self,addInfo=None):
        if not addInfo:
            addInfo = "."
        return self.git.add(addInfo)

    def commit(self,commitInfo=None):
        if not commitInfo:
            commitInfo = "through python script auto commit."
        return self.git.commit("-m \""+commitInfo+"\"")

    def push(self):
        self.git.pull()
        return self.git.push()

    def pull(self):
        return self.git.pull()
    
    def checkout(self,branchName=None):
        if branchName:
            resultInfo = self.git.checkout(branchName)
            print(self.git.for_each_ref())
            return resultInfo
        else:
            print("...branchName input error...")
    
    def deleteBranch(self,branchName):
        resultInfo = self.git.branch("-D",branchName)
        print(self.git.for_each_ref())
        return resultInfo
