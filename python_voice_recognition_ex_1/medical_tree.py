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

    childrenArray = []

    def findLastChildren(self, node, string):


        if len(node.getchildren())==0:
            if node.getdata()==string:
                self.childrenArray.append(node.getFather()[0].getdata())
        else:
            for i in node.getchildren():
                self.findLastChildren(i,string)
        return self.childrenArray


if __name__ == "__main__":
    """create nodes"""
    hospital = node('Hospital')
    internalDepartment = node('Internal Department')
    surgicalDepartment = node('Surgical Department')
    fever = node('fever')
    headache = node('headache')
    blood = node('blood')
    fall = node('fall')

    """add the value"""
    hospital.addChildren(internalDepartment)
    hospital.addChildren(surgicalDepartment)
    internalDepartment.addChildren(fever)
    internalDepartment.addChildren(headache)
    surgicalDepartment.addChildren(blood)
    surgicalDepartment.addChildren(fall)

    internalDepartment.addFather(hospital)
    surgicalDepartment.addFather(hospital)

    fever.addFather(internalDepartment)
    headache.addFather(internalDepartment)

    blood.addFather(surgicalDepartment)
    fall.addFather(surgicalDepartment)

    tree = tree(hospital)
    #    tree.linktohead(hospital)

    # testcase

    print tree.findLastChildren(hospital, "blood")
