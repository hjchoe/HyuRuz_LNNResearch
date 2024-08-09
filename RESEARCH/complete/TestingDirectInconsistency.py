from lnn import *
from helper import Executor

def TestingDirectInconsistency():
    # Initialize Model
    model = Model(name="TestingDirectInconsistency")

    # Initialize Propositions
    A,B = Propositions('A','B')

    # Define Premise
    premise = And(A, B)

    # Add Premise to List
    premises = [premise]

    # Define Query
    query = Not(A)

    # Run Proof Algorithm on Model
    Executor.prove(model=model, premises=premises, query=query)

if __name__ == "__main__":
    TestingDirectInconsistency()
