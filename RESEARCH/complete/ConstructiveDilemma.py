from lnn import *
from helper import Executor

def ConstructiveDilemma():
    model = Model(name="Constructive Dilemma")

    P,Q,R,S = Propositions('P','Q','R','S')

    premise1 = And(
        Implies(P, Q),
        Implies(R, S)
    )

    premise2 = Or(P, R)

    premises = [premise1, premise2]

    query = Or(Q, S)

    Executor.prove(model=model, premises=premises, query=query, filename="ConstructiveDilemma") 

if __name__ == "__main__":
    ConstructiveDilemma()