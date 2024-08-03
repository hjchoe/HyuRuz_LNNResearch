from lnn import Model, Variable, Proposition, Predicate, Forall, And, Or, Implies, Not, World, Fact
from ..helper import printer

def test():
    model = Model()

    x = Variable("x")

    A = Predicate("A")
    B = Predicate("B")
    C = Predicate("C")
    D = Predicate("D")

    model.add_knowledge(
        Forall(
            x,
            And(
                And(
                    A(x),
                    Not(B(x))
                ),
                Implies(
                    C(x),
                    Not(D(x))
                )
            )
        ),
        world=World.AXIOM
    )

    model.add_data({
        A: {"z": Fact.UNKNOWN},
        B: {"z": Fact.UNKNOWN},
        C: {"z": Fact.UNKNOWN},
        D: {"z": Fact.UNKNOWN},
    })

    model.print()

    model.infer()

    model.print()


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