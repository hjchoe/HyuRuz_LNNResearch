import os
from typing import List, Tuple
from lnn import Model, Formula
from contextlib import redirect_stdout

filename: str = ""
solution_steps = []

def initPrinter(name: str):
    global filename
    global solution_steps
    filename = name
    solution_steps = []

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

def printFile_BeforeInfer(model: Model, query: Formula=None, params: bool=False, numbering: bool=False):
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
    
def printFile_AfterInfer(model: Model, steps: Tuple[int, int], facts_inferred, query: Formula=None, params: bool=False, numbering: bool=False):
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

def printModelInfoToProof(name: str, premises: List[Formula], query: Formula):
    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'w') as f:
        with redirect_stdout(f):
            print(f"Model:\n     {name}")
            print(f"\nPremise{'s' if len(premises) > 1 else ''}:")
            for premise in premises:
                print(f"     {premise.structure} : {premise.state(to_bool=True)}")
            print(f"\nQuery:\n     {query.structure} : {query.state(to_bool=True)}")
            print(f"\nDerivation Solution:")

def addSolStep_Derivation(operand: Tuple[str, bool], rule: str, operator: Tuple[str, bool]):
    global solution_steps  # Use the global list to store solution steps

    # Collect the strings for each column
    col1 = f"     [ {operand[0]} : {operand[1]} ]"
    col2 = rule
    col3 = f"from [ {operator[0]} : {operator[1]} ]"

    # Add the step to the solution steps list
    solution_steps.append((col1, col2, col3))

def addSolStep_UpwardPass(operator: Tuple[str, bool]):
    global solution_steps  # Use the global list to store solution steps

    # Collect the strings for each column
    col1 = f"     [ {operator[0]} : {operator[1]} ]"

    # Add the step to the solution steps list
    solution_steps.append((col1, "Upward Pass", ""))

def print_solution_steps():
    global solution_steps  # Use the global list to store solution steps

    if len(solution_steps) == 0:
        return

    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    # Calculate the maximum lengths for each column
    col1_max_len = max(len(step[0]) for step in solution_steps)
    col2_max_len = max(len(step[1]) for step in solution_steps)
    col3_max_len = max(len(step[2]) for step in solution_steps)

    # Format the columns
    col1_width = col1_max_len + 5
    col2_width = col2_max_len + 5
    col3_width = col3_max_len + 5

    with open(path, 'a') as f:
        with redirect_stdout(f):
            for step in solution_steps:
                col1, col2, col3 = step
                print(f"{col1:<{col1_width}}{col2:<{col2_width}}{col3:<{col3_width}}")
    solution_steps = []

def startContradiction(query: Formula):
    global solution_steps  # Use the global list to store solution steps

    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print("\n     * The model was unable to converge on a solution during direct proof. Attempting PROOF BY CONTRADICTION...\n")

            col1 = f"     [ {query} : FALSE ]"

    # Add the step to the solution steps list
    solution_steps.append((col1, "Proof By Contradiction", ""))

def startAdonis(query: Formula):
    global solution_steps  # Use the global list to store solution steps

    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print("\n     * The model was unable to converge on a solution during proof by contradiction. Attempting PROOF BY ADONIS...\n")

            col1 = f"     [ {query} : TRUE ]"

    # Add the step to the solution steps list
    solution_steps.append((col1, "Proof By Adonis", ""))  

def principleOfExplosion(queryName: str):
    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print(f"\n     * The model has determined the PREMISES are INCONSISTENT.\n\n     QUERY [ {queryName} ] is TRUE due to the Principle of Explosion\n\n     QED.")

def concludeProof(state: bool, queryName: str):
    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            if state:
                print(f"\n     {queryName} is TRUE\n     QED.")
            else:
                print(f"\n     * The model has determined the QUERY is INCONSISTENT with the premises.\n\n     QED.")

def concludeAdonis(state: bool, queryName: str):
    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            if state:
                print(f"\n     * The model has determined the QUERY is INCONSISTENT with the premises.\n\n     QED.")
            else:
                print(f"\n     * The model has determined the QUERY is INCONCLUSIVE.")

def concludeContradiction(queryName: str):
    dirPath = f"{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print(f"\n     * The model has found a CONTRADICTION.\n\n     QUERY [ {queryName} ] is TRUE due to Proof by Contradiction\n\n     QED.")