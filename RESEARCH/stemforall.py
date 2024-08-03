from lnn import *
from helper import printer

def stemforall():
    model = Model()

    x,y,z = Variables('x','y','z')

    P = Predicate("Professor")
    T = Predicate("Teaches at", arity=2)
    G = Predicate("does Great things for", arity=2)
    S = Predicate("Student")
    W = Predicate("Works with", arity=2)
    S4A = Predicate("lectures at StemforAll")
    B = Predicate("Best")
    Great = Predicate("has a Great", arity=2)

    model.add_knowledge(P, T, G, S, W, S4A, B, Great)

    query = Exists(x, W('Iosevich', x))

    axiom1 = Forall(
        x,y,z,
        Implies(
            And(
                P(x),
                T(x, y),
                S(z),
                G(z, y)
            ),
            W(x, z)
        )
    )

    axiom2 = Forall(
        x,
        Implies(
            S4A(x),
            G(x, 'University of Rochester')
        )
    )

    axiom3 = Forall(
        x,
        Implies(
            And(
                P(x),
                B(x)
            ),
            T(x, 'University of Rochester')
        )
    )

    model.add_knowledge(
        axiom1,
        axiom2,
        axiom3,
        world=World.AXIOM
    )

    model.add_data({
        B: {
            'Iosevich': Fact.TRUE
        },
        P: {
            'Iosevich': Fact.TRUE
        },
        S: {
            'Stephanie': Fact.TRUE
        },
        Great: {
            ('Stephanie', 'Researchers'): Fact.TRUE
        },
        S4A: {
            'Stephanie': Fact.TRUE
        }
    })

    model.set_query(query)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)

    printer.printFile_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.printFile_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)




if __name__ == "__main__":
    stemforall()