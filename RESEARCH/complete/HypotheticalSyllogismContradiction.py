from lnn import *
from helper import Executor

def HypotheticalSyllogismContradiction():
    """
    Proving Transitivity Using Proof by Contradiction Example
    """

    # Initialize Model
    model = Model(name="HypotheticalSyllogism")

    # Initialize Propositions
    P,Q,R = Propositions('P','Q','R')

    # Define Premises
    premise1 = Implies(P, Q)
    premise2 = Implies(Q, R)

    # Add Premises to List
    premises = [premise1, premise2]

    # Define Query
    query = Implies(P, R)

    # Run Proof Algorithm on Model
    Executor.prove(model=model, premises=premises, query=query) 

if __name__ == "__main__":
    HypotheticalSyllogismContradiction()
