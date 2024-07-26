# ------------------------------------------------------------------------------------------------------------
# Project Title:    Proving Four Color Theorem Example Using A Logical Neural Network (LNN) Model
# File Name:        fourcolortheorem.py
# Program:          STEMforALL
# University:       University of Rochester
# Department:       Goergen Institute for Data Science
# Research Group:   Automated Theorem Proving
# 
# Authors:
#   Hyunho Choe (James)
#       hchoe4@u.rochester.edu
#   Ruzica Vuckovic
#       rvuckovi@u.rochester.edu
# 
# Date: 7/17/2024
# 
# Description:
#   This code trains a Logical Neural Network (LNN) model for inference to solve a four color theorem problem.
# 
# Reference:
#   IBM Logical Neural Networks (LNN): https://ibm.github.io/LNN/index.html
# -------------------------------------------------------------------------------------------------------------
from lnn import Predicate, Variables, And, Exists, Implies, Forall, Model, Fact, World, Not, Congruent, Loss, XOr

def fourcolortheorem_simple():
    """Four color theorem problem example

    Imagine a square with two crossed diagonals from the corners and a circle drawn in the middle.
    Label regions going clockwise starting from the top. Start with the outside layer of regions.

    ___Knowledge___

    Regions: A, B, C, D, E, F, G, H

    Adjacent(A, B)
    Adjacent(A, D)
    Adjacent(A, E)
    Adjacent(B, C)
    Adjacent(B, F)
    Adjacent(C, D)
    Adjacent(C, G)
    Adjacent(D, H)
    Adjacent(E, F)
    Adjacent(E, H)
    Adjacent(F, G)
    Adjacent(G, H)

    ___Axioms___

    ( forall x, y ( Colored(x, y) ^ Unique(x) ) ) --> FourColorComplete(x)
    forall x ( ( Region(x) ^ Red(x) ^ Not(Green(x)) ^ Not(Blue(x)) ^ Not(Yellow(x)) ) --> Colored(x, "red") )
    forall x ( ( Region(x) ^ Green(x) ^ Not(Red(x)) ^ Not(Blue(x)) ^ Not(Yellow(x)) ) --> Colored(x, "green") )
    forall x ( ( Region(x) ^ Blue(x) ^ Not(Red(x)) ^ Not(Green(x)) ^ Not(Yellow(x)) ) --> Colored(x, "blue") )
    forall x ( ( Region(x) ^ Yellow(x) ^ Not(Red(x)) ^ Not(Green(x)) ^ Not(Blue(x)) ) --> Colored(x, "yellow") )
    forall x,y ( Adjacent(x, y) ^ Not(Colored(x, "red") ^ Colored(y, "red")) ^ Not(Colored(x, "green") ^ Colored(y, "green")) ^ Not(Colored(x, "blue") ^ Colored(y, "blue")) ^ Not(Colored(x, "yellow") ^ Colored(y, "yellow")) ) ) --> Unique(x)
    """

    # Define variables
    x, y = Variables("x", "y")

    # Define model
    model = Model()

    # Define predicates
    region = Predicate("region")
    red = Predicate("red")
    green = Predicate("green")
    blue = Predicate("blue")
    yellow = Predicate("yellow")
    colored = Predicate("colored", arity=2)
    adjacent = Predicate("adjacent", arity=2)
    unique = Predicate("unique", arity=2)
    fourColorComplete = Predicate("fourColorComplete")

    # Define and add the background knowledge to the model
    query = Forall(
        x,
        fourColorComplete(x)
    )

    model.add_knowledge(
        Implies(
            Forall(
                x,
                y,
                And(
                    colored(x, y),
                    unique(x, y)
                )
            ),
            fourColorComplete(x)
        ),
        Forall(
            x,
            Implies(
                And(
                    region(x),
                    red(x),
                    Not(green(x)),
                    Not(blue(x)),
                    Not(yellow(x))
                ),
                colored(x, "red")
            )
        ),
        Forall(
            x,
            Implies(
                And(
                    region(x),
                    green(x),
                    Not(red(x)),
                    Not(blue(x)),
                    Not(yellow(x))
                ),
                colored(x, "green")
            )
        ),
        Forall(
            x,
            Implies(
                And(
                    region(x),
                    blue(x),
                    Not(red(x)),
                    Not(green(x)),
                    Not(yellow(x))
                ),
                colored(x, "blue")
            )
        ),
        Forall(
            x,
            Implies(
                And(
                    region(x),
                    yellow(x),
                    Not(red(x)),
                    Not(green(x)),
                    Not(blue(x)),
                ),
                colored(x, "yellow")
            )
        ),
        Forall(
            x,
            y,
            Implies(
                And(
                    adjacent(x, y),
                    Not(And(
                        colored(x, "red"), colored(y, "red")
                    ))
                ),
                unique(x, "red")
            )
        ),

        world=World.AXIOM
    )

    # Set query
    # model.set_query(query)

    # Add fact data to model
    model.add_data(
        {
            region: {
                "A": Fact.TRUE,
                "B": Fact.TRUE
            },
            adjacent: {
                ("A", "B"): Fact.TRUE,
                ("B", "A"): Fact.TRUE
            }
        }
    )

    # Perform inference
    model.print()

    model.upward()

    model.print()

    model.downward()

    model.print()

def fourcolortheorem_complex():

    # Define variables
    x, y, z = Variables("x", "y", "z")

    # Define model
    model = Model()

    # Define predicates
    region = Predicate("region")
    color = Predicate("color")
    adjacent = Predicate("adjacent", arity=2)
    colored = Predicate("colored", arity=2)
    fourColorComplete = Predicate("fourColorComplete")

    # Define Query

    query = Forall(x, Implies(region(x), fourColorComplete(x)))

    # Define axioms
    axiomOne = Forall(
        x,
        Implies(
            region(x),
            Forall(
                y,
                z,
                Implies(
                    And(
                        colored(x, y),
                        colored(x, z)
                    ),
                    Congruent(color(y), color(z))
                )
            )
        )
    )
    axiomTwo = Forall(
        x,
        y,
        Implies(
            adjacent(x, y),
            Forall(
                z,
                Implies(
                    colored(x, z),
                    Not(
                        colored(y, z)
                    )
                )
            )
        )
    )
    axiomThree = Forall(
        x,
        Exists(
            y,
            Implies(
                Implies(
                    region(x),
                    colored(x, y)
                ),
                fourColorComplete(x)
            )
        )
    )


    # Add background knowledge to model
    model.add_knowledge(
        axiomOne,
        axiomTwo,
        axiomThree,
        world=World.AXIOM, # Formulae follow assumptions of universally being TRUE
    )

    # Set query
    model.set_query(query)

    # Add fact data to model
    model.add_data(
        {
            region: {
                "A": Fact.TRUE,
                "B": Fact.TRUE,
                "C": Fact.TRUE,
                "D": Fact.TRUE,
                "E": Fact.TRUE,
                "F": Fact.TRUE,
                "G": Fact.TRUE,
                "H": Fact.TRUE
            },
            color: {
                "red": Fact.TRUE,
                "green": Fact.TRUE,
                "blue": Fact.TRUE,
                "yellow": Fact.TRUE
            },
            colored: {
                ("A", "red"): Fact.UNKNOWN,
                ("A", "green"): Fact.UNKNOWN,
                ("A", "blue"): Fact.UNKNOWN,
                ("A", "yellow"): Fact.UNKNOWN,
                ("B", "red"): Fact.UNKNOWN,
                ("B", "green"): Fact.UNKNOWN,
                ("B", "blue"): Fact.UNKNOWN,
                ("B", "yellow"): Fact.UNKNOWN,
                ("C", "red"): Fact.UNKNOWN,
                ("C", "green"): Fact.UNKNOWN,
                ("C", "blue"): Fact.UNKNOWN,
                ("C", "yellow"): Fact.UNKNOWN,
                ("D", "red"): Fact.UNKNOWN,
                ("D", "green"): Fact.UNKNOWN,
                ("D", "blue"): Fact.UNKNOWN,
                ("D", "yellow"): Fact.UNKNOWN
            },
            adjacent: {
                ("A", "B"): Fact.TRUE,
                ("A", "D"): Fact.TRUE,
                ("A", "E"): Fact.TRUE,
                ("B", "C"): Fact.TRUE,
                ("B", "F"): Fact.TRUE,
                ("C", "D"): Fact.TRUE,
                ("C", "G"): Fact.TRUE,
                ("D", "H"): Fact.TRUE,
                ("E", "F"): Fact.TRUE,
                ("E", "H"): Fact.TRUE,
                ("F", "G"): Fact.TRUE,
                ("G", "H"): Fact.TRUE
            },
        }
    )

    # Perform inference
    model.train(losses=Loss.CONTRADICTION)
    model.print(params=True)

if __name__ == "__main__":
    fourcolortheorem_simple()
