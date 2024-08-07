from lnn import *
from helper import Executor

# Modus Ponens
def ModusPonens():
    model = Model(name="Modus Ponens")

    P = Proposition("P")
    Q = Proposition("Q")

    P.add_data(Fact.TRUE)

    premises = list()

    premise1 = Implies(
        P,
        Q
    )
    premises.append(premise1)

    query = Q

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="ModusPonens")

# Modus Tollens
def ModusTollens():
    model = Model(name="Modus Tollens")

    P = Proposition("P")
    Q = Proposition("Q")

    premises = list()

    premise1 = Not(Q)
    premises.append(premise1)

    premise2 = Implies(
       P,
       Q
    )
    premises.append(premise2)

    query = Not(P)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="ModusTollens")

def Absorption1():
    model = Model(name="Absorption 1")

    P = Proposition("P")
    Q = Proposition("Q")

    premises = list()

    premise1 = Not(
        Implies(
            P,
            Q
        )
    )
    premises.append(premise1)

    query = P

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Absorption1")

def Absorption2():
    model = Model(name="Absorption 2")

    P = Proposition("P")
    Q = Proposition("Q")

    premises = list()

    premise1 = Not(
        Implies(
            P,
            Q
        )
    )
    premises.append(premise1)

    query = Not(Q)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Absorption2")

# Conjunctive Elimination
def ConjunctiveElimination():
    model = Model(name="Conjunctive Elimination")

    P = Proposition("P")
    Q = Proposition("Q")

    premises = list()

    premise1 = And(
        P,
        Q
    )
    premises.append(premise1)

    query = P

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="ConjunctiveElimination")

# Modus Ponendo Tollens
def ModusPonendoTollens():
    # Initialize Model
    model = Model(name="Modus Ponendo Tollens")

    # Initialize Propositions: P, Q as UNKNOWN
    P = Proposition("P")
    Q = Proposition("Q")

    # Initialize Premises
    premises = list()
    premise1 = P                    # P
    premise2 = Not(And(P,Q))        # ~(P ^ Q)
    premises.append(premise1)
    premises.append(premise2)

    # Initialize Query
    query = Not(Q)                  # ~Q

    # Set Query in Model and Execute Inference
    #      * Prints Results to In.txt and Out.txt
    #      * Generates Graph
    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="ModusPonendoTollens")

# Disjunctive Syllogism
def DisjunctiveSyllogism():
    model = Model(name="Disjunctive Syllogism")

    P = Proposition("P")
    Q = Proposition("Q")

    premises = list()

    premise1 = Not(P)
    premises.append(premise1)

    premise2 = Or(P, Q)
    premises.append(premise2)

    query = Q

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="DisjunctiveSyllogism")

# DeMorgan's Law
def DeMorgansLaw():
    model = Model(name="DeMorgan's Law")

    P = Proposition("P")
    Q = Proposition("Q")

    premises = list()

    premise1 = Not(
        Or(
            P,
            Q
        )
    )
    premises.append(premise1)

    query = Not(P)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="DeMorgan's")

if __name__ == "__main__":
    ModusPonens()
    ModusTollens()
    Absorption1()
    Absorption2()
    ConjunctiveElimination()
    ModusPonendoTollens()
    DisjunctiveSyllogism()
    DeMorgansLaw()
