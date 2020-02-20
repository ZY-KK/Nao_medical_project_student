#!/usr/bin/env python
# -*-coding:utf-8 -*-

class node:
    def __init__(self, data):

        self._data = data
        self._children = []
        self._father = []

    def getdata(self):
        return self._data

    def getchildren(self):
        return self._children

    def getFather(self):
        return self._father

    def addChildren(self, node):
        self._children.append(node)

    def addFather(self, node):
        self._father.append(node)

    def go(self, data):
        for child in self._children:
            if child.getdata() == data:
                return child
        return None


class tree:
    def __init__(self, header):
        self._head = node(header)

    def linktohead(self, node):
        self._head.addChildren(node)

    def getHeader(self):
        return self._head

    fatherNode=None

    def findFather(self, node, string):


        if len(node.getchildren())==0:
            if node.getdata()==string:
                self.fatherNode=(node.getFather()[0].getdata())
        else:
            for i in node.getchildren():
                self.findFather(i,string)
        return self.fatherNode

