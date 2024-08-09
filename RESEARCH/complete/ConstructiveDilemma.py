from lnn import *
from helper import Executor

def ConstructiveDilemma():
    # Initialize Model
    model = Model(name="ConstructiveDilemma")

    # Initialize Propositions
    P,Q,R,S = Propositions('P','Q','R','S')

    # Define Premises
    premise1 = And(
        Implies(P, Q),
        Implies(R, S)
    )
    premise2 = Or(P, R)

    # Add Premises to List
    premises = [premise1, premise2]

    # Define Query
    query = Or(Q, S)

    # Run Proof Algorithm on Model
    Executor.prove(model=model, premises=premises, query=query) 

if __name__ == "__main__":
    ConstructiveDilemma()
