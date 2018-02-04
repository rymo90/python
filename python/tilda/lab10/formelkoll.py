#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from linkedQFile import LinkedQ
from molgrafik import *
from hashfil import *
from hashtest import *
class Formelfel(Exception):
    pass
def readFormel(q):
    mol= readMol(q)
    if q.peek()==')':
        raise Formelfel("Felaktig gruppstart vid radslutet")
    return mol
def readMol(q):
    mol= readGroupp(q)
    if q.peek() == "." or q.peek()==')':
        return mol
    else:
        mol.next = readMol(q)
    return mol
def readGroupp(q):
    rutan = Ruta()
    stringNum=""
    if q.peek()=='(':
        q.dequeue()
        rutan.down = readMol(q)
        if q.peek()==')':
            q.dequeue()
            if q.peek().isdigit():
                rutan.num= int(readNum(q))
            else:
                raise Formelfel("Saknad siffra vid radslutet")
        else:
            raise Formelfel("Saknad högerparentes vid radslutet")
    elif q.peek().isalpha():
        rutan.atom = readAtom(q)
        if q.peek().isdigit():
            rutan.num= int(readNum(q))
    else:
        raise Formelfel("Felaktig gruppstart vid radslutet")
    return rutan
def readAtom(q):
    temp=""
    if q.peek().isupper():
        UpperLetter= q.dequeue()
        if q.peek().islower():
            lowerLetter = q.dequeue()
            temp = UpperLetter+lowerLetter
            checkAtom = listaAtomer(temp)
            if checkAtom==True:
                pass
            else:
                raise Formelfel("Okänd atom vid radslutet")
        else:
            checkAtom=listaAtomer(UpperLetter)
            if checkAtom== True:
                temp= UpperLetter
            else:
                raise Formelfel("Okänd atom vid radslutet")
    else:
        raise Formelfel("Saknad stor bokstav vid radslutet")
    return temp
def readNum(q):
    temp=""
    if int(q.peek())!=0:
        num = q.dequeue()
        if q.peek().isdigit():
            while q.peek().isdigit():
                temp+= q.dequeue()
        else:
            if (int(num) >= 2):
                temp= str(num)
            else:
                raise Formelfel("För litet tal vid radslutet")
    else:
        raise Formelfel("För litet tal vid radslutet")
    return temp
def listaAtomer(testatom):
    atoms = """
    H   He  Li  Be  B   C   N   O   F   Ne  Na  Mg  Al  Si  P   S   Cl  Ar  K   Ca  Sc  Ti  V   Cr
    Mn  Fe  Co  Ni  Cu  Zn  Ga  Ge  As  Se  Br  Kr  Rb  Sr  Y   Zr  Nb  Mo  Tc  Ru  Rh  Pd  Ag  Cd
    In  Sn  Sb  Te  I   Xe  Cs  Ba  La  Ce  Pr  Nd  Pm  Sm  Eu  Gd  Tb  Dy  Ho  Er  Tm  Yb  Lu  Hf
    Ta  W   Re  Os  Ir  Pt  Au  Hg  Tl  Pb  Bi  Po  At  Rn  Fr  Ra  Ac  Th  Pa  U   Np  Pu  Am  Cm
    Bk  Cf  Es  Fm  Md  No  Lr  Rf  Db  Sg  Bh  Hs  Mt  Ds  Rg  Cn  Fl  Lv
"""
    atomString= atoms.split()
    hitta= False
    for i in range(len(atomString)):
        if atomString[i]== testatom:
            hitta= True
    return hitta
def storFormel(formeln):
    q= LinkedQ()
    formeln= list(formeln)
    for i in formeln:
        q.enqueue(i)
    q.enqueue(".")
    return q
def viktDictionary(atom):
    atomlista = skapaAtomlista()
    hashtabell= lagraHashtabell(atomlista)
    molvikt = hashtabell.get(atom).vikt
    return molvikt
def weight(mol):
    if mol==None:
        return 0
    if  mol.atom=="()":
        return float(weight(mol.down))*mol.num+float(weight(mol.next))
    return float(viktDictionary(mol.atom)+float(weight(mol.down)))*mol.num+float(weight(mol.next))

def kollaFormeln(formeln):
    temp=""
    x= ""
    q= storFormel(formeln)
    try:
        mol = readFormel(q)
        mg= Molgrafik()
        mg.show(mol)
        print("Formeln är syntaktiskt korrekt")
        molvikt = weight(mol)
        print(molvikt)
    except Formelfel as e:
        while q.peek()!= ".":
            temp+= q.dequeue()
        if temp!="":
            temp=" "+temp
        print(e,end="")
        print(temp)
def main():
    q= LinkedQ()
    stopa = False
    while not stopa:
        formeln= input("")
        if formeln=="#":
            stopa= True
        else:
            kollaFormeln(formeln)
if __name__=="__main__":
    main()
