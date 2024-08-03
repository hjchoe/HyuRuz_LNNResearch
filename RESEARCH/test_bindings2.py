from lnn import Model, Variable, Predicate, Forall, Implies, And, Exists, World, Fact
from helper import printer

def test_bindings2():
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
    test_bindings2()