# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# __author__ = 'Zhenyu Zhang'

import numpy as np
import random as ra
from .rngint import *
from .numstringparser import NumericStringParser


class Arith():
    def __init__(self):
        self.digit=2
        self.nDataColumn=2
        self.currentOperator='+'
        self.Operators=['+','-','*','/']
        self.nOperands=2
        self.nTest=100
        self.elapseTime=0.0
        self.texts=[]

        self.difficulties=['Primary','Intermediate','Advanced']
        self.diffiLevel=1

        self.modeTexts=[['+','-','*','/'],
                        ['+ -','+ - *','+ - * /'],
                        ['+ - ()','+ - * ()','+ - * / ()']]

        self.mode=0
        self.correctResults=np.zeros(self.nTest)
        self.nsp=NumericStringParser()
        self.minnumber=0
        self.maxnumber=0
        self.smallest=-10000000000
        self.biggest=-self.smallest
        self.timerOn=False
        self.empty=True
        return

    def getModeText(self):
        return self.modeTexts[self.diffiLevel][self.mode]

    def getMode(self):
        return  self.mode

    def getnTest(self):
        return self.nTest

    def setnTest(self,n):
        self.nTest=n
        return

    def new(self):
        self.reset()
        return

    def clear(self):
        self.texts=[]
        self.totalMarks=0
        self.marks=np.zeros(self.nTest,int)
        self.correctResults=np.zeros(self.nTest)
        return

    def getMarks(self):
        return self.marks

    def getTotalMark(self):
        return self.totalMarks

    def mark(self,results):
        self.totalMarks=0
        self.marks=np.zeros(self.nTest,int)
        # print(len(results))
        # print(len(self.correctResults))
        assert (len(results)==len(self.correctResults))
        for i in range(0,self.nTest):
            if(results[i]==self.correctResults[i]):
                self.totalMarks+=1
                self.marks[i]=1
        return

    def reset(self):
        self.clear()
        self.minnumber=MinNumber(self.digit)
        self.maxnumber=MaxNumber(self.digit)

        for i in range(0,self.nTest):
            text=self.generateTestText()
            self.texts.append(text)
            self.correctResults[i]=self.nsp.eval(text)
        # print(self.correctResults)
        self.empty=False
        return

    def calcResults(self):
        for i in range(0,self.nTest):
            self.correctResults[i]=self.nsp.eval(self.texts[i])
        return
    def getRandomOperator(self):
        op='+'
        if self.diffiLevel==1:
            if(self.mode==0):
                i=ra.randrange(0,2)
                op=self.Operators[i]
            elif self.mode==1:
                i=ra.randrange(0,3)
                op=self.Operators[i]
            elif self.mode==2:
                i=ra.randrange(0,4)
                op=self.Operators[i]
        elif self.diffiLevel==0:
            if(self.mode==0):
                i=0
                op=self.Operators[i]
            elif self.mode==1:
                i=1
                op=self.Operators[i]
            elif self.mode==2:
                i=2
                op=self.Operators[i]
            elif self.mode==3:
                i=3
                op=self.Operators[i]
        return op

    def saveToHandle(self,fh):
        # f.write()
        # for i in range(0,self.)
        # TODO
        return

    def saveToFile(self,fname):
        try:
            f = open(fname, 'w')
        except IOError:
            print("Error: There was an error when writing to \"%s\"" %(fname))
            return
        self.saveToHandle(f)
        f.close()
        return

    def generateTestText(self):
        """
        generate one test question
        """
        operands=[]
        texts=[]
        correctResult=0
        for i in range(0,self.nOperands):
            x=RandomInteger(self.digit)
            operands.append(x)
            texts.append(str(x))
        testText=texts[0]
        for i in range(1,self.nOperands):
            op=self.getRandomOperator()
            testText=testText+op+texts[i]
        return testText

    def parse(self,text):
        nsp=NumericStringParser()
        val=nsp.eval(text)
        return val