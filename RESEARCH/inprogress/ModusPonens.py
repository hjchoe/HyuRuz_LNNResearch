from lnn import Formula, Model, Forall, Variable, Predicate, Implies, And, Not, Fact
from helper import Printer

def ModusPonens(lhs: Formula, rhs: Formula):
    return Implies(
        And(
            lhs,
            Implies(
                lhs,
                rhs
            )
        ),
        rhs
    )

def ModusPonensTest():
    model = Model()

    x = Variable("x")

    F = Predicate("F")
    G = Predicate("G")

    query = Forall(
        x,
        And(
            Not(F(x)),
            F(x)
        )
    )

    modusponens = Implies(
        And(
            F(x)
        )
    )

    model.add_knowledge(
        query
    )

    model.add_data({
        F: {
            "a": Fact.UNKNOWN
        }
    })

    # Print Model Before
    Printer.print_BeforeInfer(model=model, query=query, params=False, numbering=True)

    # Run Inference on Model
    steps, facts_inferred = model.infer()

    # Print Model After
    Printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    # User input for Show Plotgi
    answer = input("View Graph? (default= Y) [Y/N]: ")
    if answer != "N":
        model.plot_graph(formula_number=False, edge_variables=True, with_labels=False, arrows=True, node_size=500, font_size=9)
    
    
if __name__ == "__main__":
    ModusPonensTest()
