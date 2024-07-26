from lnn import Model, Variables, Predicate, Forall, Implies, And, Not, World, Fact, Loss

def t4():
    """
    Variables:
        x, y
    
    Predicate:
    formula [ F() ]
    truth [ T() ]
    
    Axioms:
        Modus Ponens = Forall x,y [ (F(x) ^ F(y)) --> ( ( T(x --> y) ^ T(x) ) --> T(y) ) ]
                                                   ^ ROOT
                                          ^ CHILD                              ^ CHILD
                                                                     ^ CHILD
                                                               ^ CHILD
        T4 = Forall x [ F(x) --> ( T( x  --> ~~x ) ]

    
    true ~~(F(x) --> ~~(F(x)))

    Query:
        (~~x --> ~~x)
    """

    model = Model()

    x, y = Variables("X", "Y")

    formula = Predicate("F")
    truth = Predicate("T")

    modus_ponens = Forall(
        x,
        y,
        Implies(
            And(
                formula(x),
                formula(y)
            ),
            Implies(
                And(
                    truth(
                        Implies(
                            x,
                            y
                        )
                    ),
                    truth(x)
                ),
                truth(y)
            )
        )
    )

    t4 = Forall(
        x,
        Implies(
            formula(x),
            Not(
                Not(
                    formula(x)
                )
            )
        )
    )

    # T4 = Forall x [ F(x) --> ( T( x  --> ~~x ) ]

    conjecture = Forall(
        x,
        Not(
            Not(
                Implies(
                    formula(x),
                    Not(
                        Not(
                            formula(x)
                        )
                    )
                )
            )
        )
    )

    model.add_knowledge(
        modus_ponens,
        t4,
        world=World.AXIOM
    )

    """
    model.add_data(
        {
            formula: {
                "F": Fact.UNKNOWN
            }
        }
    )
    """

    model.set_query(conjecture)
    
    model.print(params=True)

    steps, facts_inferred = model.infer()

    model.print(params=True)

    print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

    epochs, total_loss = model.train(losses=Loss.CONTRADICTION, pbar=True)

    model.print(params=True)

    print(f"epochs: {epochs}\ntotal_loss: {total_loss}")

if __name__ == "__main__":
    t4()