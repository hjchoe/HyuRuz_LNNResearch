from lnn import Model, Variables, Predicate, Forall, Implies, And, World, Exists, Fact
from helper import printer

def American():
    model = Model()

    x, y, z = Variables("x", "y", "z")

    F = Predicate("F")
    G = Predicate("G")

    Forall(
        x,
        Implies(
            And(
                F(x),
                Implies(
                    F(x),
                    G(x)
                )
            ),
            G(x)
        )
    )

    Forall(
        x,
        Implies(
            And(
                F(x),
                Implies(
                    F(x),
                    G(x)
                )
            ),
            G(x)
        )
    )




    American = Predicate("American")
    Weapon = Predicate("Weapon")
    Sells = Predicate("Sells", arity=3)
    Hostile = Predicate("Hostile")
    Criminal = Predicate("Criminal")
    Missile = Predicate("Missile")
    Owns = Predicate("Owns", arity=2)
    Enemy = Predicate("Enemy", arity=2)

    model.add_knowledge(
        Forall(
            x, y, z,
            Implies(
                And(
                    American(x),
                    Weapon(y),
                    Sells(x, y, z),
                    Hostile(z)
                ),
                Criminal(x)
            )
        ),
        Forall(
            x,
            Implies(
                And(
                    Missile(x),
                    Owns("nono", x)
                ),
                Sells(
                    "west",
                    x,
                    "nono"
                )
            )
        ),
        Forall(
            x,
            Implies(
                Missile(x),
                Weapon(x)
            )
        ),
        Forall(
            Implies(
                Enemy(x, "america"),
                Hostile(x)
            )
        ),
        world=World.AXIOM
    )

    query = Exists(
        x,
        Criminal(x)
    )

    # model.set_query(query)

    model.add_data({
        Owns: {
            ("nono", "m1"): Fact.TRUE
        },
        Missile: {
            "m1": Fact.TRUE,
            "m2": Fact.TRUE,
            "m3": Fact.TRUE
        },
        American: {
            "west": Fact.TRUE
        },
        Enemy: {
            ("nono", "america"): Fact.TRUE,
            ("wakanda", "america"): Fact.TRUE,
            ("gotham", "america"): Fact.TRUE
        }
    })

    printer.print_BeforeInfer(model=model, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    model.plot_graph(formula_number=False, edge_variables=True, with_labels=False, arrows=True, node_size=500, font_size=9)

if __name__ == "__main__":
    American()