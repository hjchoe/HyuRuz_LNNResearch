from lnn import *
from helper import Executor

def HypotheticalSyllogismContradiction():
    """
    Proving Transitivity Using Proof by Contradiction Example
    """
    model = Model(name="Hypothetical Syllogism")

    P,Q,R = Propositions('P','Q','R')

    premise1 = Implies(P, Q)

    premise2 = Implies(Q, R)

    premises = [premise1, premise2]

    query = Implies(P, R)

    Executor.prove(model=model, premises=premises, query=query, filename="HypotheticalSyllogism") 

if __name__ == "__main__":
    HypotheticalSyllogismContradiction()