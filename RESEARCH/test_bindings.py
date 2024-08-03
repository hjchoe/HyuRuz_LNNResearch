from lnn import *
from ..helper import printer

def test_bindings1():
    """
    P Arity:        1
    Q Arity:        1
    Ground Terms:   1
    Variables:      1

    P(ground)
    Q(free)
    """

    model = Model()

    x = Variable('x')

    P = Predicate("P")
    Q = Predicate("Q")

    # Forallx (P('a') --> Q(x))
    axiom = Forall(
        x,
        Implies(
            P('a'),
            Q(x)
        )
    )

    query = Exists(x, Q(x))

    model.add_knowledge(axiom, world=World.AXIOM)

    model.add_data({
        P: {
            'a': Fact.TRUE
        }
    })

    model.set_query(query)

    printer.print_BeforeInfer(model=model, query=query, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

def test_bindings2():
    """
    P Arity:        2
    Q Arity:        1
    Ground Terms:   1
    Variables:      1
    
    P(ground, free)
    Q(free)
    """

    model = Model()

    x = Variable('x')

    P = Predicate("P", arity=2)
    Q = Predicate("Q")

    # Forallx (P('a', x) --> Q(x))
    axiom = Forall(
        x,
        Implies(
            P('a', x),
            Q(x)
        )
    )

    query = Exists(x, Q(x))

    model.add_knowledge(axiom, world=World.AXIOM)

    model.add_data({
        P: {
            ('a', 'b'): Fact.TRUE
        }
    })

    model.set_query(query)

    printer.print_BeforeInfer(model=model, query=query, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

def test_bindings3():
    """
    P Arity:        2
    Q Arity:        1
    Ground Terms:   1
    Variables:      1
    
    P(free, ground)
    Q(free)
    """

    model = Model()

    x = Variable('x')

    P = Predicate("P", arity=2)
    Q = Predicate("Q")

    axiom = Forall(
        x,
        Implies(
            P(x, 'a'),
            Q(x)
        )
    )

    query = Exists(x, Q(x))

    model.add_knowledge(axiom, world=World.AXIOM)

    model.add_data({
        P: {
            ('a', 'b'): Fact.TRUE
        }
    })

    model.set_query(query)

    printer.print_BeforeInfer(model=model, query=query, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

def test_bindings4():
    """Testing double binding with single variable."""

    model = Model()

    x = Variable('x')

    M = Predicate("M")
    O = Predicate("O", arity=2)
    S = Predicate("S", arity=3)

    axiom = Forall(
        x,
        Implies(
            And(
                M(x),
                O('a', x)
            ),
            S('a', x, 'b')
        )
    )

    query = Exists(x, S('a', x, 'b'))

    model.add_knowledge(axiom, world=World.AXIOM)

    model.add_data({
        M: {
            'b': Fact.TRUE
        },
        O: {
            ('a', 'b'): Fact.TRUE
        }
    })

    model.set_query(query)

    printer.printFile_BeforeInfer(model=model, query=query, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.printFile_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

if __name__ == "__main__":
    test_bindings1()