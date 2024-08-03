from lnn import Model, Proposition, Implies, Not, And, World, Fact
from ..helper import printer

def test3():
    model = Model()

    A = Proposition("A")
    B = Proposition("B")
    C = Proposition("C")
    C.add_data(Fact.TRUE)

    model.add_knowledge(A, B, C)

    axiom = Implies(
        A,
        And(
            B,
            Not(C)
        )
    )

    model.add_knowledge(
        axiom,
        world=World.AXIOM
    )

    printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

if __name__ == "__main__":
    test3()