from lnn import *
from helper import Executor
from helper import Printer

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

    Executor.inferModel(model=model, query=query, filename="test_bindings1")

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

    Executor.inferModel(model=model, query=query, filename="test_bindings2")

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

    Executor.inferModel(model=model, query=query, filename="test_bindings3")

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

    Executor.inferModel(model=model, query=query, filename="test_bindings4")


def test_bindings5():
    """
    P Arity:        3
    Q Arity:        1
    Ground Terms:   1
    Variables:      1
    
    P(free, free, ground)
    Q(free)
    """

    model = Model()

    x,y = Variables('x', 'y')

    P = Predicate("P", arity=3)
    Q = Predicate("Q")

    axiom = Forall(
        x,y,
        Implies(
            P(x, y, 'a'),
            Q(x)
        )
    )

    model.add_knowledge(axiom, world=World.AXIOM)

    Printer.print_BeforeInfer(model=model, params=False, numbering=True)

    """
    query = Exists(x, Q(x))

    

    model.add_data({
        P: {
            ('a', 'b'): Fact.TRUE
        }
    })

    Executor.inferModel(model=model, query=query, filename="test_bindings3")
    """




if __name__ == "__main__":
    """
    print("\n@@@@@ 1")
    test_bindings1()
    
    print("\n@@@@@ 2")
    
    print("\n@@@@@ 3")
    test_bindings3()
    """

    test_bindings2()
    test_bindings5()