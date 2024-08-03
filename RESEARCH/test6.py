from lnn import Model, Proposition, Or, Not, World
from ..helper import printer

def test6():
    model = Model()

    A = Proposition("A")

    # A v ~A
    axiom1 = Or(
        A,
        Not(A)
    )

    model.add_knowledge(axiom1, world=World.AXIOM)

    printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)


if __name__ == "__main__":
    test6()