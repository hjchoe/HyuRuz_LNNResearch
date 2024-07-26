from lnn import Model, Variable, Predicate, Forall, Implies, Exists, World, Fact

def squarerectangle():
    model = Model()

    x = Variable("x")

    square = Predicate("square")
    rectangle = Predicate("rectangle")
    foursides = Predicate("foursides")

    all_squares_are_rectangles = Forall(x, Implies(square(x), rectangle(x)))
    all_rectangles_have_foursides = Forall(x, Implies(rectangle(x), foursides(x)))

    conjecture = Exists(x, foursides(x))

    model.add_knowledge(
        all_squares_are_rectangles,
        all_rectangles_have_foursides,
        world=World.AXIOM
    )

    model.add_data(
        {
            square: {
                "c": Fact.UNKNOWN,
                "k": Fact.UNKNOWN
            }
        }
    )

    model.set_query(conjecture)

    model.print(params=True)

    steps, facts_inferred = model.infer()

    model.print(params=True)
    print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

    steps = facts_inferred = model.infer_query()
    model.print(params=True)
    print(f"steps: {steps}\nfacts_inferred: {facts_inferred}")

    model.plot_graph()

if __name__ == "__main__":
    squarerectangle()
