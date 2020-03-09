#!/usr/bin/python3
#-*- coding: utf8 -*-


import pickle
from io import *


class Pregunton():
    def __init__(self):
        self.preguntas = ""
        self.salvado = False
        self.data_list = []

    def __str__(self):
        return "BIENVENIDO A PREGUNTON"

    def preguntas(self):
        pass

    def save(self):
        f = open("data_question.txt", "wb+")
        f.close()

#Falta terminar.



