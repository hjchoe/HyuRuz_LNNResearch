from lnn import Model, Proposition, And, Or, Not, Fact
from helper import printer

def test2():
    model = Model()

    G = Proposition("G")
    S = Proposition("S")
    E = Proposition("E")

    conjecture = And(
        G,
        Or(
            S,
            Not(
                E
            )
        )
    )

    model.add_knowledge(conjecture)

    model.add_data({
        G: Fact.FALSE,
        S: Fact.TRUE,
        E: Fact.FALSE
    })

    printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

if __name__ == "__main__":
    test2()