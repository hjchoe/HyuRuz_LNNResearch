import os
from typing import List, Tuple
from lnn import Model, Formula
from contextlib import redirect_stdout

# Initializing Global Variables
filename: str = ""
dirPath: str            
solution_steps = []     # Temporary list for model to store solution steps before printing them out to Proof File

def initPrinter(name: str):
    global filename
    global dirPath
    global solution_steps
    filename = name
    dirPath = f"INFO/{filename}_INFO"
    os.makedirs(dirPath, exist_ok=True)
    solution_steps = []

def print_BeforeInfer(file: bool, model: Model, query: Formula=None, detailed: bool=True):
    if file:
        printFile_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)
    else:
        print_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)

def printIO_BeforeInfer(model: Model, query: Formula=None, params: bool=False, numbering: bool=False):
    print('<' + '-'*30 + " BEFORE INFERENCE " + '-'*30 + '>')
    model.print(params=params, numbering=numbering)
    
    if query:
        print("\n__QUERY__")
        query.print(params=params)

def printFile_BeforeInfer(model: Model, query: Formula=None, params: bool=False, numbering: bool=False):
    path = os.path.join(dirPath, "In.txt")
    with open(path, 'w') as f:
        with redirect_stdout(f):
            print('<' + '-'*30 + " BEFORE INFERENCE " + '-'*30 + '>')
            model.print(params=params, numbering=numbering)
            
            if query:
                print("\n__QUERY__")
                query.print(params=params)
    f.close()

def print_AfterInfer(file: bool, model: Model, query: Formula=None, detailed: bool=True, steps: Tuple[int, int]=(-1, -1), facts_inferred="N/A"):
    if file:
        printFile_AfterInfer(model=model, query=query, params=detailed, numbering=detailed, steps=steps, facts_inferred=facts_inferred)
    else:
        printIO_AfterInfer(model=model, query=query, params=detailed, numbering=detailed, steps=steps, facts_inferred=facts_inferred)
    
def printIO_AfterInfer(model: Model, query: Formula=None, params: bool=False, numbering: bool=False, steps: Tuple[int, int]=(-1, -1), facts_inferred="N/A"):
    print('<' + '-'*30 + " AFTER INFERENCE " + '-'*30 + '>')
    model.print(params=params, numbering=numbering)
    print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

    if query:
        print("\n__QUERY__")
        query.print(params=params)
    
def printFile_AfterInfer(model: Model, steps: Tuple[int, int], facts_inferred, query: Formula=None, params: bool=False, numbering: bool=False):
    path = os.path.join(dirPath, "Out.txt")
    with open(path, 'w') as f:
        with redirect_stdout(f): 
            print('<' + '-'*30 + " AFTER INFERENCE " + '-'*30 + '>')
            model.print(params=params, numbering=numbering)
            print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

            if query:
                print("\n__QUERY__")
                query.print(params=params)
    f.close()

def print_ModelInfo(name: str, premises: List[Formula], query: Formula):
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

    solution_steps.append((col1, col2, col3))       # Add the step to the solution steps list

def addSolStep_UpwardPass(operator: Tuple[str, bool]):
    global solution_steps                               # Call global list to store solution steps
    col1 = f"     [ {operator[0]} : {operator[1]} ]"    # Collect the strings for each column
    solution_steps.append((col1, "Upward Pass", ""))    # Add the step to the solution steps list

def print_solution_steps():
    global solution_steps  # Use the global list to store solution steps
    if len(solution_steps) == 0: return
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
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print("\n     * The model was unable to converge on a solution during direct proof. Attempting PROOF BY CONTRADICTION...\n")

            col1 = f"     [ {query} : FALSE ]"

    # Add the step to the solution steps list
    solution_steps.append((col1, "Proof By Contradiction", ""))

def startAdonis(query: Formula):
    global solution_steps  # Use the global list to store solution steps
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print("\n     * The model was unable to converge on a solution during proof by contradiction. Attempting PROOF BY ADONIS...\n")

            col1 = f"     [ {query} : TRUE ]"

    # Add the step to the solution steps list
    solution_steps.append((col1, "Proof By Adonis", ""))  

def principleOfExplosion(queryName: str):
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print(f"\n     * The model has determined the PREMISES are INCONSISTENT.\n\n     QUERY [ {queryName} ] is TRUE due to the Principle of Explosion\n\n     QED.")

def concludeProof(state: bool, queryName: str):
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            if state:
                print(f"\n     {queryName} is TRUE\n     QED.")
            else:
                print(f"\n     * The model has determined the QUERY is INCONSISTENT with the premises.\n\n     QED.")

def concludeAdonis(state: bool, queryName: str):
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            if state:
                print(f"\n     * The model has determined the QUERY is INCONSISTENT with the premises.\n\n     QED.")
            else:
                print(f"\n     * The model has determined the QUERY is INCONCLUSIVE.")

def concludeContradiction(queryName: str):
    path = os.path.join(dirPath, "Proof.txt")

    with open(path, 'a') as f:
        with redirect_stdout(f):
            print(f"\n     * The model has found a CONTRADICTION.\n\n     QUERY [ {queryName} ] is TRUE due to Proof by Contradiction\n\n     QED.")