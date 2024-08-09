from lnn import *
from helper import Executor

def TestingPrincipleOfExplosion():
    # Initialize Model
    model = Model(name="TestingPrincipleOfExplosion")

    # Initialize Propositions
    A,B = Propositions('A','B')

    # Define Premises
    premise1 = A
    premise2 = Not(A)

    # Add Premises to List
    premises = [premise1, premise2]

    # Define Query
    query = B

    # Run Proof Algorithm on Model
    Executor.prove(model=model, premises=premises, query=query)

if __name__ == "__main__":
    TestingPrincipleOfExplosion()
