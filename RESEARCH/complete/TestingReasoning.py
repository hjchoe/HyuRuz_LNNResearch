from lnn import *
from helper import Executor

def TestingReasoning():
    # Initialize Model
    model = Model(name="TestingReasoning")

    # Initialize Propositions
    P,Q,R,S,T = Propositions('P','Q','R','S','T')

    # Define Premises
    premise1 = And(P, Q)
    premise2 = Implies(
        Or(P, S),
        Not(R)
    )
    premise3 = Or(R,T)

    # Add Premises to List
    premises = [premise1, premise2, premise3]

    # Define Query
    query = T

    # Run Proof Algorithm on Model
    Executor.prove(model=model, premises=premises, query=query) 

if __name__ == "__main__":
    TestingReasoning()
