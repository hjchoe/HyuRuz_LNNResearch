from lnn import *
from helper import Executor

def Q25():

    model = Model(name="Q25")

    W,X,Y,Z = Propositions('W','X','Y','Z')

    premise1 = And(
        Or(W, X),
        Or(Y, Z)
    )
    premise2 = Not(X)
    premise3 = Not(Y)

    premises = [premise1, premise2, premise3]

    query = And(W, Z)

    Executor.prove(model=model, premises=premises, query=query, filename="Q25")


def Q24():
    model = Model(name="Q24")

    P,Q,R,S = Propositions('P','Q','R','S')

    premise1 = And(
        P,
        Implies(Q, R)
    )
    premise2 = And(
        P,
        Implies(R, S)
    )
    premise3 = Not(S)

    premises = [premise1, premise2, premise3]

    query = Not(Q)
    query = (query, Fact.UNKNOWN)

    Executor.inferModel(model=model, premises=premises, query=query, filename="Q24")

def Q23():
    model = Model(name="Q23")

    A,B,C,D,E = Propositions('A','B','C','D','E')

    premise1 = And(Or(A, B), Implies(Not(A), Not(B)))
    premise2 = Implies(A, C)
    premise3 = Implies(B, D)

    premises = [premise1, premise2, premise3]

    query = Or(Or(C, D), E)

    Executor.prove(model=model, premises=premises, query=query, filename="Q23")

def Q22():
    model = Model(name="Q22")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')
    S = Proposition('S')

    premise1 = And(Q, R, S)
    premise2 = Implies(Q, P)

    premises = [premise1, premise2]

    query = Or(Or(P, R), S)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q22")

def Q21():
    model = Model(name="Q21")

    A = Proposition('A')
    B = Proposition('B')
    C = Proposition('C')

    premise1 = And(
        Implies(A, B),
        Implies(B, C)
    )
    premise2 = Not(C)

    premises = [premise1, premise2]
    query = Not(A)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q21")

def Q20():
    model = Model(name="Q20")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')

    premise1 = Implies(Or(P, Q), R)
    premise2 = P

    premises = [premise1, premise2]
    query = R

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q20")

def Q19():
    model = Model(name="Q19")

    A = Proposition('A')
    B = Proposition('B')
    C = Proposition('C')
    D = Proposition('D')

    premise1 = And(Or(A, B), Implies(C, D))
    premise2 = Not(B)
    premise3 = Not(D)

    premises = [premise1, premise2, premise3]
    query = And(A, Not(C))

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q19")

def Q18():
    model = Model(name="Q18")

    W = Proposition('W')
    X = Proposition('X')
    Y = Proposition('Y')
    Z = Proposition('Z')

    premise1 = And(W, X)
    premise2 = And(Y, Z)

    premises = [premise1, premise2]
    query = And(X, Y)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q18")

def Q17():
    model = Model(name="Q17")

    A = Proposition('A')
    B = Proposition('B')
    C = Proposition('C')

    premise1 = And(Not(A), Not(C))
    premise2 = Implies(B, C)

    premises = [premise1, premise2]
    query = Not(B)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q17")

def Q16():
    model = Model(name="Q16")

    W = Proposition('W')
    X = Proposition('X')
    Y = Proposition('Y')
    Z = Proposition('Z')

    premise1 = X
    premise2 = Implies(X, Y)
    premise3 = Implies(W, Z)

    premises = [premise1, premise2, premise3]
    query = Or(Y, Z)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q16")

# Example where model is able to correctly detect a logically inconsistent system and does not reason (expected)
#      query should result in UNKNOWN
def Q15():
    model = Model(name="Q15")

    A,B,C,D = Propositions('A','B','C','D')

    premise1 = Or(Implies(A, B), Implies(C, D))
    premise2 = Not(Implies(A, B))
    premise3 = Implies(D, B)
    premise4 = C

    premises = [premise1, premise2, premise3, premise4]
    query = B

    Executor.prove(model=model, premises=premises, query=query, filename="Q15")

def Q14():
    model = Model(name="Q14")

    A = Proposition('A')
    B = Proposition('B')
    C = Proposition('C')

    premise1 = Implies(A, B)
    premise2 = And(Not(B), C)

    premises = [premise1, premise2]
    query = Not(A)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q14")

def Q13():
    model = Model(name="Q13")

    X = Proposition('X')
    Y = Proposition('Y')
    Z = Proposition('Z')

    premise1 = And(X, Y)
    premise2 = Implies(Or(X, Y), Z)

    premises = [premise1, premise2]
    query = Z

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q13")

def Q12():
    model = Model(name="Q12")

    A = Proposition('A')
    B = Proposition('B')
    C = Proposition('C')
    D = Proposition('D')
    E = Proposition('E')

    premise1 = And(And(A, B), C)
    premise2 = Implies(A, D)

    premises = [premise1, premise2]
    query = Or(D, E)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q12")

def Q11():
    model = Model(name="Q11")

    W = Proposition('W')
    X = Proposition('X')
    Y = Proposition('Y')
    Z = Proposition('Z')

    premise1 = Implies(Or(W, X), Or(Y, Z))
    premise2 = W
    premise3 = Not(Z)

    premises = [premise1, premise2, premise3]
    query = Y

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q11")

def Q10():
    model = Model(name="Q10")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')
    S = Proposition('S')

    premise1 = And(Implies(P, Q), Implies(R, S))
    premise2 = P
    premise3 = R

    premises = [premise1, premise2, premise3]
    query = And(Q, S)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q10")

def Q9():
    model = Model(name="Q9")

    X = Proposition('X')
    Y = Proposition('Y')
    Z = Proposition('Z')

    premise1 = Implies(X, Y)
    premise2 = Implies(Y, Z)
    premise3 = Not(Z)

    premises = [premise1, premise2, premise3]
    query = Not(X)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q9")

def Q8():
    model = Model(name="Q8")

    X = Proposition('X')
    Y = Proposition('Y')
    Z = Proposition('Z')

    premise1 = X
    premise2 = Y

    premises = [premise1, premise2]
    query = Or(And(X, Y), Z)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q8")

def Q7():
    model = Model(name="Q7")

    A = Proposition('A')
    B = Proposition('B')
    C = Proposition('C')
    D = Proposition('D')

    premise1 = Implies(C, Or(A, B))
    premise2 = Or(C, D)
    premise3 = Not(D)
    premise4 = Not(B)

    premises = [premise1, premise2, premise3, premise4]
    query = A

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q7")

def Q6():
    model = Model(name="Q6")

    A = Proposition('A')
    B = Proposition('B')
    C = Proposition('C')
    D = Proposition('D')

    premise1 = A
    premise2 = Implies(Or(Or(A, B), C), D)

    premises = [premise1, premise2]
    query = D

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q6")

def Q5():
    model = Model(name="Q5")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')
    S = Proposition('S')

    premise1 = P
    premise2 = Implies(Or(P, Q), R)
    premise3 = Implies(R, S)

    premises = [premise1, premise2, premise3]
    query = S

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q5")

def Q4():
    model = Model(name="Q4")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')
    S = Proposition('S')

    premise1 = Or(P, Q)
    premise2 = Implies(Q, R)
    premise3 = Implies(R, S)
    premise4 = Not(P)

    premises = [premise1, premise2, premise3, premise4]
    query = S

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q4")

def Q3():
    model = Model(name="Q3")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')
    S = Proposition('S')

    premise1 = Or(P, Or(Q, Or(R, S)))
    premise2 = Not(P)
    premise3 = Not(Q)
    premise4 = Not(S)

    premises = [premise1, premise2, premise3, premise4]
    query = R

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q3")

def Q2():
    model = Model(name="Q2")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')

    premise1 = P
    premise2 = Q
    premise3 = Implies(And(P, Q), R)

    premises = [premise1, premise2, premise3]
    query = R

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q2")

def Q1():
    model = Model(name="Q1")

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')

    premise1 = Implies(P, Q)
    premise2 = P

    premises = [premise1, premise2]
    query = Or(Q, R)

    Executor.inferModel(model=model, premises=premises, query=(query, Fact.UNKNOWN), filename="Q1")

# Example where model is able to correctly detect a logically inconsistent system and does not reason (expected)
#      query should result in UNKNOWN
def leder():
    model = Model(name="leder")

    P, Q, R, S = Propositions('P', 'Q', 'R', 'S')

    premise = And(
        Implies(P, Q),
        Implies(R, Q),
        Implies(R, S),
        P
    )
    premises = [premise]

    query = And(
        Implies(P, Q),
        S
    )

    Executor.prove(model=model, premises=premises, query=query, filename="leder")

def adonis():
    model = Model(name="adonis")

    A,B,C = Propositions('A','B','C')

    premise1 = Or(A, B)
    
    premise2 = Implies(A, C)

    premise3 = Implies(B, C)

    premises = [premise1, premise2, premise3]

    query = C

    Executor.prove(model=model, premises=premises, query=query, filename="adonis")

def adonis2():
    model = Model(name="adonis2")

    B,C,D = Propositions('B','C','D')

    premise1 = Not(B)

    premise2 = Implies(D, B)

    premise3 = C

    premises = [premise1, premise2, premise3]

    query = Implies(C, D)

    Executor.prove(model=model, premises=premises, query=query, filename="adonis2")

if __name__ == "__main__":
    """
    Q1()
    Q2()
    Q3()
    Q4()
    Q5()
    Q6()
    Q7()
    Q8()
    Q9()
    Q10()
    Q11()
    Q12()
    Q13()
    Q14()
    Q15()
    Q16()
    Q17()
    Q18()
    Q19()
    Q20()
    Q21()
    Q22()
    Q23()
    Q24()
    Q25()
    leder()
    """

    Q15()
    adonis2()
