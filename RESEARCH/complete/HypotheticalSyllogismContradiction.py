from lnn import *
from helper import Executor

def HypotheticalSyllogismContradiction():
    """
    Proving Transitivity Using Proof by Contradiction
    """
    model = Model(name="Hypothetical Syllogism using Contradiction")

    P = Proposition("P")
    Q = Proposition("Q")
    R = Proposition("R")

    premises = list()

    premise1 = Implies(
        P,
        Q
    )
    premises.append(premise1)

    premise2 = Implies(
        Q,
        R
    )
    premises.append(premise2)

    query = Implies(P, R)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.FALSE), filename="HypotheticalSyllogismContradiction") 

if __name__ == "__main__":
    HypotheticalSyllogismContradiction()