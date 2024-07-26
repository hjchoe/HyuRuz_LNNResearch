# ----------------------------------------------------------------------------------------------------------------
# Project Title:    "First Official Piece Of Code"
# File Name:        FirstOfficialPieceOfCode.py
# Program:          STEMforALL
# University:       University of Rochester
# Department:       Goergen Institute for Data Science
# Research Group:   Automated Theorem Proving
# Research Topic:   Neura-Symbolic AI: FOL and LNNs
# 
# Authors:
#   Hyunho Choe (James)
#       hchoe4@u.rochester.edu
#   Ruzica Vuckovic
#       rvuckovi@u.rochester.edu
# 
# Date: 7/25/2024
# 
# Reference:
#   Research Github: https://github.com/hjchoe/LNN
#   IBM Logical Neural Networks (LNN): https://ibm.github.io/LNN/index.html
# ----------------------------------------------------------------------------------------------------------------

from lnn import Model, Variable, Predicate, Forall, Implies, And, Or, Not, World, Fact, Exists
from ..helper import advPrint as printer

def test():
    """
    Variable:
        x
    
    Predicates:
        G(_)
        H(_)
        I(_)
        J(_)
        K(_)
        L(_)
        M(_)

    Premises:
        ∀x ( G(x) --> { H(x) ^ I(x) } )
        ∀x ( H(x) --> { J(x) v K(x) } )
        ∀x ( I(x) --> { ~K(x) ^ L(x) } )
        ∀x ( J(x) --> M(x) )
    
    Object:
        G(a) = True
    
    Conjecture:
        ∃x ( M(x) ^ L(x) )      // Result should be True
    """

    # Create Model
    model = Model()

    # Initialize Variables
    x = Variable("x")

    # Initialize Predicates
    G = Predicate("G")
    H = Predicate("H")
    I = Predicate("I")
    J = Predicate("J")
    K = Predicate("K")
    L = Predicate("L")
    M = Predicate("M")

    # Build Knowledge/Axioms
    Premise_1 = Forall(
        x,
        Implies(
            G(x),
            And(
                H(x),
                I(x)
            )
        )
    )

    Premise_2 = Forall(
        x,
        Implies(
            H(x),
            Or(
                J(x),
                K(x)
            )
        )
    )

    Premise_3 = Forall(
        x,
        Implies(
            I(x),
            And(
                Not(
                    K(x)
                ),
                L(x)
            )
        )
    )

    Premise_4 = Forall(
        x,
        Implies(
            J(x),
            M(x)
        )
    )

    # Add Knowledge/Axioms to Model
    model.add_knowledge(
        Premise_1,
        Premise_2,
        Premise_3,
        Premise_4,
        world=World.AXIOM
    )

    # Add Data/Objects to Model
    model.add_data({
        G: {
            "a": Fact.TRUE
        }
    })

    # Build Query/Conjecture
    query = Exists(
        x,
        And(
            M(x),
            L(x)
        )
    )

    # Set Query/Conjecture
    model.set_query(query)

    # Print Model Before
    printer.print_BeforeInfer(model=model, query=query, params=False, numbering=True)

    # Run Inference on Model
    steps, facts_inferred = model.infer()

    # Print Model After
    printer.print_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=False, numbering=True)

    # User input for Show Plot
    graph = False
    answer = input("View Graph? (default= N) [Y/N]: ")
    if answer == "Y": model.plot_graph(formula_number=False, edge_variables=True, with_labels=False, arrows=True, node_size=500, font_size=9)

if __name__ == "__main__":
    test()
