import os
from typing import Tuple
from lnn import Model, Formula
from contextlib import redirect_stdout

def print_BeforeInfer(model: Model, query: Formula=None, params: bool=False, numbering: bool=False):
    print("\n<------------------------------ BEFORE INFERENCE ------------------------------>")
    model.print(params=params, numbering=numbering)
    
    if query:
        print("\n__QUERY__")
        query.print(params=params)
    
def print_AfterInfer(model: Model, query: Formula=None, params: bool=False, numbering: bool=False, steps: Tuple[int, int]=(-1, -1), facts_inferred="N/A"):
    print("\n<------------------------------ AFTER INFERENCE ------------------------------>")
    model.print(params=params, numbering=numbering)
    print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

    if query:
        print("\n__QUERY__")
        query.print(params=params)

def printFile_BeforeInfer(filename: str, model: Model, query: Formula=None, params: bool=False, numbering: bool=False):
    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "In.txt")
    with open(path, 'w') as f:
        with redirect_stdout(f):
            print("\n<------------------------------ BEFORE INFERENCE ------------------------------>")
            model.print(params=params, numbering=numbering)
            
            if query:
                print("\n__QUERY__")
                query.print(params=params)
    f.close()
    
def printFile_AfterInfer(filename: str, model: Model, steps: Tuple[int, int], facts_inferred, query: Formula=None, params: bool=False, numbering: bool=False):
    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Out.txt")
    with open(path, 'w') as f:
        with redirect_stdout(f): 
            print("\n<------------------------------ AFTER INFERENCE ------------------------------>")
            model.print(params=params, numbering=numbering)
            print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

            if query:
                print("\n__QUERY__")
                query.print(params=params)
    f.close()