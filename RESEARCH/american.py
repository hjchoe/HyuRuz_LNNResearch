from lnn import Model, Predicate, Variables, And, Forall, Implies, World, Fact, Exists
from ..helper import printer

def american():
    model = Model()

    x, y, z = Variables('x', 'y', 'z')

    American = Predicate("American")
    Weapon = Predicate("Weapon")
    Sells = Predicate("Sells", arity=3)
    Hostile = Predicate("Hostile")
    Criminal = Predicate("Criminal")
    Missile = Predicate("Missile")
    Owns = Predicate("Owns", arity=2)
    Enemy = Predicate("Enemy", arity=2)

    axiom1 = Forall(
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
    )

    axiom2 = Forall(
        x,
        Implies(
            And(
                Missile(x),
                Owns('nono', x)
            ),
            Sells('west', x, 'nono')
        )
    )

    axiom3 = Forall(
        Implies(
            Missile(x),
            Weapon(x)
        )
    )
    
    axiom4 = Forall(
        x,
        Implies(
            Enemy(x, 'america'),
            Hostile(x)
        )
    )

    model.add_knowledge(
        axiom1,
        axiom2,
        axiom3,
        axiom4,
        world=World.AXIOM
    )

    model.add_data({
        Owns: {
            ('nono', 'm1'): Fact.TRUE
        },
        Missile: {
            'm1': Fact.TRUE,
            'm2': Fact.TRUE,
            'm3': Fact.TRUE
        },
        American: {
            'west': Fact.TRUE
        },
        Enemy: {
            ('nono', 'america'): Fact.TRUE,
            ('wakanda', 'america'): Fact.TRUE,
            ('gotham', 'america'): Fact.TRUE
        }
    })

    query = Exists(x, Criminal(x))

    model.set_query(query)

    model.print()

    printer.print_BeforeInfer(model=model, query=query, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True, node_size=500, font_size=9)
    

if __name__ == "__main__":
    american()