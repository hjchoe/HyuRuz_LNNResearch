from lnn import *
from helper import Executor

# Modus Ponens
def ModusPonens():
    model = Model(name="Modus Ponens")

    P,Q = Propositions('P', 'Q')

    premise1 = P

    premise2 = Implies(P, Q)

    premises = [premise1, premise2]

    query = Q

    Executor.prove(model=model, premises=premises, query=query)

# Modus Tollens
def ModusTollens():
    model = Model(name="Modus Tollens")

    P,Q = Propositions('P','Q')

    premise1 = Not(Q)

    premise2 = Implies(P, Q)

    premises = [premise1, premise2]

    query = Not(P)

    Executor.prove(model=model, premises=premises, query=query)

def Absorption1():
    model = Model(name="Absorption 1")

    P,Q = Propositions('P','Q')

    premise1 = Not(
        Implies(P, Q)
    )
    
    premises = [premise1]

    query = P

    Executor.prove(model=model, premises=premises, query=query)

def Absorption2():
    model = Model(name="Absorption 2")

    P,Q = Propositions('P','Q')

    premise1 = Not(
        Implies(P, Q)
    )

    premises = [premise1]

    query = Not(Q)

    Executor.prove(model=model, premises=premises, query=query)
    
# Conjunctive Elimination
def ConjunctiveElimination():
    model = Model(name="Conjunctive Elimination")

    P,Q = Propositions('P','Q')

    premise1 = And(
        P,
        Q
    )
    
    premises = [premise1]

    query = P

    Executor.prove(model=model, premises=premises, query=query)
    
# Modus Ponendo Tollens
def ModusPonendoTollens():
    # Initialize Model
    model = Model(name="Modus Ponendo Tollens")

    # Initialize Propositions: P, Q as UNKNOWN
    P,Q = Propositions('P','Q')

    # Initialize Premises
    premise1 = P                    # P
    premise2 = Not(And(P,Q))        # ~(P ^ Q)

    premises = [premise1, premise2]

    # Initialize Query
    query = Not(Q)                  # ~Q

    Executor.prove(model=model, premises=premises, query=query)
    
# Disjunctive Syllogism
def DisjunctiveSyllogism():
    model = Model(name="Disjunctive Syllogism")

    P,Q = Propositions('P','Q')

    premise1 = Not(P)

    premise2 = Or(P, Q)

    premises = [premise1, premise2]

    query = Q

    Executor.prove(model=model, premises=premises, query=query)
    
# DeMorgan's Law
def DeMorgansLaw():
    model = Model(name="DeMorgan's Law")

    P,Q = Propositions('P','Q')

    premise1 = Not(
        Or(
            P,
            Q
        )
    )

    premises = [premise1]

    query = Not(P)

    Executor.prove(model=model, premises=premises, query=query)
    
if __name__ == "__main__":
    Absorption1()
    Absorption2()
    ModusPonens()
    ModusTollens()
    Absorption1()
    Absorption2()
    ConjunctiveElimination()
    ModusPonendoTollens()
    DisjunctiveSyllogism()
    DeMorgansLaw()
