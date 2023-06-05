# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 14:43:34 2022

@author: mikey
"""
from random import randint

def calculateAnswer(lhs, operator, rhs):
    print("answerfound")
    if(operator=="+"):
        return lhs+rhs
    if(operator=="-"):
        return lhs-rhs
    if(operator=="*"):
        return lhs*rhs
    if(operator=="/"):
        if(rhs==0):
            raise Exception("Cannot divide by zero")
        return lhs/rhs
    if(operator=="^"):
        return lhs**rhs
    raise Exception("Unknown Operator")

def generateQuestion(lowerBound,upperBound):
    ops="/*-+"
    opIndex=randint(0,len(ops)-1)
    operator=ops[opIndex]
    lhs=randint(lowerBound,upperBound)
    rhs=randint(lowerBound,upperBound)
    while(rhs==0 and operator =="/"):
        rhs=randint(lowerBound,upperBound)
    return lhs,operator,rhs

def isAccuateEnough(answer1,answer2,tolerance=0.01):
    difference=abs(float(answer1)-float(answer2))
    return difference <= tolerance

def quiz():
    totalQuestions=5
    numCorrect=0
    for i in range(totalQuestions):
        print("QuestionStart")
        question = generateQuestion(-10,10)
        correctAnswer = calculateAnswer(question[0],question[1],question[2])
        playerAnswer = input("{0} {1} {2} = ".format(question[0],question[1],question[2]))
        if(isAccuateEnough(playerAnswer,correctAnswer)):
            print("Correct!")
            numCorrect+=1
        else:
            print("Incorrect. The correct answer is "+str(correctAnswer))
    print("You got {0} out of {1} answers correct, or {2}%".format(numCorrect, totalQuestions,100*numCorrect/totalQuestions))

quiz()

