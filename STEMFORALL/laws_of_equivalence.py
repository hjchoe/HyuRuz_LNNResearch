from lnn import Model, Variables, Predicate, Forall, And, Implies, Iff, Not, Or, Exists, World, Fact, Loss

def lawsOfEquiv():
    """
    Variable:
        x
    
    Predicate:
        F(_)
        G(_)

    Axioms:
        E& = Forall x [ { ( F(x) ^ G(x) ) --> F(x) } ^ { ( F(x) ^ G(x) ) --> G(x) } ]
                                                       ^ ROOT
                                             ^ NODE                         ^ NODE
                                   ^ NODE                         ^ NODE          
        DeMorgans1 = Forall x [ ~{ F(x) ^ G(x) } <---> { ~F(x) v ~G(x) } ]
                                                     ^ ROOT
                                          ^ NODE                 ^ NODE
        DeMorgans2 = Forall x [ ~{ F(x) v G(x) } <---> { ~F(x) ^ ~G(x) } ]
                                                     ^ ROOT
                                          ^ NODE                 ^ NODE
        ModusPollens = Forall x [ { ( F(x) --> G(x) ) ^ ~G(x) } --> ~F(x) ]
                                                                   ^ ROOT
                                                        ^ NODE
                                              ^ NODE
        DoubleNegation = Forall x [ F(x) --> ~~F(x) ]
                                              
    Query:
        ( ~( F("H") v F("I") ) ^ ( F("J") --> F("H") ) ) ^ ~( F("K") v ~F("J") )
    
    Objects:
        H = F("H")
        I = F("I")
        J = F("J")
        K = F("K")
    """

    model = Model()

    x, y, s, t = Variables("x", "y", "s", "t")

    F = Predicate("F")

    # E& = Forall x,y [ { ( F(x) ^ F(y) ) --> F(x) } ^ { ( F(x) ^ F(y) ) --> F(y) } ]
    E_and = Forall(
        x,
        y,
        And(
            Implies(
                And(
                    F(x),
                    F(y)
                ),
                F(x)
            ),
            Implies(
                And(
                    F(x),
                    F(y)
                ),
                F(y)
            )
        )
    )

    # DeMorgans1 = Forall x,y [ ~{ F(x) ^ F(y) } <---> { ~F(x) v ~F(y) } ]
    DeMorgans1 = Forall(
        x,y,
        Iff(
            Not(
                And(
                    F(x),
                    F(y)
                )
            ),
            Or(
                Not(
                    F(x)
                ),
                Not(
                    F(y)
                )
            )
        )
    )

    # DeMorgans2 = Forall x,y [ ~{ F(x) v F(y) } <---> { ~F(x) ^ ~F(y) } ]
    DeMorgans2 = Forall(
        x,y,
        Iff(
            Not(
                Or(
                    F(x),
                    F(y)
                )
            ),
            And(
                Not(
                    F(x)
                ),
                Not(
                    F(y)
                )
            )
        )
    )
    
    # ModusPollens = Forall x,y [ { ( F(x) --> F(y) ) ^ ~F(y) } --> ~F(x) ]
    ModusPollens = Forall(
        x,y,
        Implies(
            And(
                Implies(
                    F(x),
                    F(y)
                ),
                Not(
                    F(y)
                )
            ),
            Not(
                F(x)
            )
        )
    )

    # DoubleNegation = Forall x [ F(x) --> ~~F(x) ]
    DoubleNegation = Forall(
        x,
        Implies(
            F(x),
            Not(
                Not(
                    F(x)
                )
            )
        )
    )

    # query = ( ~( F("G") v F("Q") ) ^ ( F("K") --> F("G") ) ) ^ ~( F("P") v ~F("K") )
    query = Exists(
        x, y, s, t,
        And(
            And(
                Not(
                    Or(
                        F(x),
                        F(y)
                    )
                ),
                Implies(
                    F(s),
                    F(x)
                )
            ),
            Not(
                Or(
                    F(t),
                    Not(
                        F(s)
                    )
                )
            )
        )
    )
    """
    query = Exists(
        x, y, s, t,
        And(
            And(
                Not(
                    Or(
                        (x, F('G')),
                        (y, F('Q'))
                    )
                ),
                Implies(
                    (s, F('K')),
                    (x, F('G'))
                )
            ),
            Not(
                Or(
                    (t, F('P')),
                    Not(
                        (s, F('K'))
                    )
                )
            )
        )
    )
    """

    model.add_knowledge(
        E_and,
        #DeMorgans1,
        #DeMorgans2,
        #ModusPollens,
        #DoubleNegation,
        world=World.AXIOM
    )

    model.add_data({
        F: {
            'G': Fact.UNKNOWN,
            'Q': Fact.UNKNOWN,
            'K': Fact.UNKNOWN,
            'P': Fact.UNKNOWN
        }
    })

    model.print(params=True)

    model.plot_graph(formula_number=False, edge_variables=True, with_labels=False, arrows=True, node_size=500, font_size=9)


    model.infer()

    model.print(params=True)

    # model.infer()



    # epochs, total_loss = model.train(losses=Loss.CONTRADICTION, pbar=True)

    # model.print(params=True)

    # print(f"epochs: {epochs}\ntotal_loss: {total_loss}")

    query.print(params=True)
    query.upward()
    query.print(params=True)


if __name__ == "__main__":
    lawsOfEquiv()