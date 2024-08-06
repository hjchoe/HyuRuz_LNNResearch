from lnn import *
from helper import Printer

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

    model.add_knowledge(P, T, G, S, W, S4A, B)

    query = Exists(z, W('Iosevich', z))

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
        z,
        Implies(
            S4A(z),
            G(z, 'University of Rochester')
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
        S4A: {
            'Stephanie': Fact.TRUE
        }
    })

    model.set_query(query)
    
    filename = "stemforall"

    Printer.printFile_BeforeInfer(filename=filename, model=model, query=query, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    Printer.printFile_AfterInfer(filename=filename, model=model, query=query, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    model.plot_graph()




if __name__ == "__main__":
    stemforall()