from lnn import *
from helper import Executor

def ConstructiveDilemma():
    model = Model(name="Constructive Dilemma")

    P = Proposition("P")
    Q = Proposition("Q")
    R = Proposition("R")
    S = Proposition("S")

    premises = list()

    premise1 = And(
        Implies(
            P,
            Q
        ),
        Implies(
            R,
            S
        )
    )
    premises.append(premise1)

    premise2 = Or(
        P,
        R
    )
    premises.append(premise2)

    query = Or(Q, S)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.FALSE), filename="ConstructiveDilemma") 

if __name__ == "__main__":
    ConstructiveDilemma()