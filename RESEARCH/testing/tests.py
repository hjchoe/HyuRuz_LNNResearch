from lnn import Model, Variable, Proposition, Predicate, Forall, And, Or, Implies, Not, World, Fact
from helper import Printer

def test1():
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

    Printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    Printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

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

    Printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    Printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

def test4():
    model = Model()

    A = Proposition("A")
    B = Proposition("B")
    C = Proposition("C")

    model.add_knowledge(A, B)

    A_and_B = And(A, B)
    A_and_C = And(A, C)

    model.add_knowledge(
        A_and_B,
        A_and_C,
        world=World.AXIOM
    )

    conjecture = Or(
        And(
            A,
            B
        ),
        And(
            A,
            C
        )
    )

    model.set_query(conjecture)

    Printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    Printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

def test5():
    model = Model()

    A = Proposition("A")

    # A v ~A
    axiom1 = Or(
        A,
        Not(A)
    )

    model.add_knowledge(axiom1, world=World.AXIOM)

    Printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    Printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
