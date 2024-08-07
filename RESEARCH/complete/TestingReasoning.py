from lnn import *
from helper import Executor

def TestingReasoning():
    model = Model(name="Testing Reasoning")

    P = Proposition("P")
    Q = Proposition("Q")
    R = Proposition("R")
    S = Proposition("S")
    T = Proposition("T")

    premises = list()

    premise1 = And(
        P,
        Q
    )
    premises.append(premise1)

    premise2 = Implies(
        Or(
            P,
            S
        ),
        Not(R)
    )
    premises.append(premise2)

    premise3 = Or(
        R,
        T
    )
    premises.append(premise3)

    query = T

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="TestingReasoning") 

if __name__ == "__main__":
    TestingReasoning()
