from lnn import *
from helper import Executor, Printer

def Distributive():
    model = Model()

    P = Proposition('P')
    Q = Proposition('Q')
    R = Proposition('R')

    premises = list()

    premise1 = Implies(
        Or(
            And(
                P,
                Q
            ),
            And(
                P,
                R
            )
        ),
        And(
            P,
            Q
        )
    )


    model.add_knowledge(premise1)

    Printer.print_BeforeInfer(model=model, params=False, numbering=True)

    model.infer()

    Printer.print_BeforeInfer(model=model, params=False, numbering=True)

    # Executor.inferModel(model=model, premises=premises, query=(query, Fact.FALSE), filename="Distributive") 

if __name__ == "__main__":
    Distributive()