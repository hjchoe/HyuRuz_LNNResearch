from lnn import *
from helper import Executor

def TestingReasoning():
    model = Model(name="Testing Reasoning")

    P,Q,R,S,T = Propositions('P','Q','R','S','T')

    premise1 = And(P, Q)

    premise2 = Implies(
        Or(P, S),
        Not(R)
    )

    premise3 = Or(R,T)

    premises = [premise1, premise2, premise3]

    query = T

    Executor.prove(model=model, premises=premises, query=query, filename="TestingReasoning") 

if __name__ == "__main__":
    TestingReasoning()
