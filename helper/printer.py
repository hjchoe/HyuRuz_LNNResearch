from typing import Tuple
from lnn import Model, Formula

def print_BeforeInfer(model: Model, query: Formula = False, params: bool = False, numbering: bool = False):
    print("\n<------------------------------ BEFORE INFERENCE ------------------------------>")
    model.print(params=params, numbering=numbering)
    
    if query:
        print("\n__QUERY__")
        query.print(params=params)
    
def print_AfterInfer(model: Model, steps: Tuple[int, int], facts_inferred, query: Formula = False, params: bool = False, numbering: bool = False):
    print("\n<------------------------------ AFTER INFERENCE ------------------------------>")
    model.print(params=params, numbering=numbering)
    print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

    if query:
        print("\n__QUERY__")
        query.print(params=params)