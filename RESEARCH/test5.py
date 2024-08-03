from lnn import *
x = Variable('x')
A = Predicate('A')
B = Predicate('B')

rule1 = Forall(
    x,
    Or(
        A,
        Not(A)
    )
)
rule2 = Forall(
    x,
    Or(
        B,
        Not(B)
    )
)

model = Model()
model.add_knowledge(rule, world=World.AXIOM)

model.print()
model.infer()
model.print()