from lnn import *
from helper import Executor

def TestingInconclusive():
    # Initialize Model
    model = Model(name="TestingInconclusive")

    # Initialize Propositions
    P,Q = Propositions('P','Q')

    # Define Premises
    premise1 = Or(P, Q)
    premise2 = Implies(P, Q)

    # Add Premises to List
    premises = [premise1, premise2]

    # Define Query
    query = P

    # Run Proof Algorithm on Model
    Executor.prove(model=model, premises=premises, query=query)

if __name__ == "__main__":
    TestingInconclusive()
