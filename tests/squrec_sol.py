from lnn import Model, Variable, Predicate, Forall, Or, Not, Implies, Exists, World, Fact
from ..helper import printer

def squrec_sol():
    model = Model()

    x = Variable("x")

    square = Predicate("square")
    rectangle = Predicate("rectangle")
    foursides = Predicate("foursides")

    clause1 = Forall(
        x,
        Or(
            Not(square(x)),
            rectangle(x))
    )
    clause2 = Forall(
        x,
        Or(
            Not(rectangle(x)),
            foursides(x))
    )

    conjecture = Exists(x, foursides(x))

    model.add_knowledge(
        clause1,
        clause2,
        world=World.AXIOM
    )

    model.add_data(
        {
            square: {
                "c": Fact.TRUE,
                "k": Fact.TRUE
            }
        }
    )

    model.set_query(conjecture)

    model.plot_graph()

    printer.print_BeforeInfer(model=model, query=conjecture, params=False, numbering=True)

    steps, facts_inferred = model.infer()

    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=conjecture, params=False, numbering=True)

    model.plot_graph()

if __name__ == "__main__":
    squrec_sol()
