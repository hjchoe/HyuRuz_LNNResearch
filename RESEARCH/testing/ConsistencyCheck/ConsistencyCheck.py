from lnn import *
from helper import Executor

def check0():
    model = Model(name="Check0")

    A,B = Propositions('A','B')

    premise1 = A
    premise2 = Not(A)

    premises = [premise1, premise2]

    query = B

    Executor.prove(model=model, premises=premises, query=query, filename="Check0")

def check2():
    model = Model(name="Check2")

    A,B = Propositions('A','B')

    premise = And(A, B)

    premises = [premise]

    query = Not(A)

    Executor.prove(model=model, premises=premises, query=query, filename="Check2")

def check3():
    model = Model(name="Check3")

    A,B,C = Propositions('A','B','C')

    premise1 = Implies(A, B)
    premise2 = Implies(B, C)

    premises = [premise1, premise2]

    query = Implies(A, C)

    Executor.prove(model=model, premises=premises, query=query, filename="Check3")

def check4():
    model = Model(name="Check4")

    A,B,C = Propositions('A','B','C')

    premise1 = Implies(A, B)
    premise2 = Implies(B, C)

    premises = [premise1, premise2]

    query = Not(Implies(A, C))

    Executor.prove(model=model, premises=premises, query=query, filename="Check4")

def check5():
    model = Model(name="Check5")

    P,Q = Propositions('P','Q')

    premise1 = Or(P, Q)
    premise2 = Implies(P, Q)

    premises = [premise1, premise2]

    query = P

    Executor.prove(model=model, premises=premises, query=query, filename="Check5")

if __name__ == "__main__":
    check0()
    check2()
    check3()
    check4()
    check5()