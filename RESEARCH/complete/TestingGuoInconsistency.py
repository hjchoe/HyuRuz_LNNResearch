from lnn import *
from helper import Executor

def TestingGuoInconsistency():
    # Initialize Model
    model = Model(name="TestingGuoInconsistency")

    # Initialize Propositions
    A,B,C = Propositions('A','B','C')

    # Define Premises
    premise1 = Implies(A, B)
    premise2 = Implies(B, C)

    # Add Premises to List
    premises = [premise1, premise2]

    # Define Query
    query = Not(Implies(A, C))

    # Run Proof Algorithm on Model
    Executor.prove(model=model, premises=premises, query=query)

if __name__ == "__main__":
    TestingGuoInconsistency()
