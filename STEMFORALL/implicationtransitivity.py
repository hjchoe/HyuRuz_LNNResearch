# ----------------------------------------------------------------------------------------------------------------
# Project Title:    Proving Transitivity of Implication Using A Logical Neural Network (LNN) Model
# File Name:        implicationtransitivity.py
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
#   This code trains a Logical Neural Network (LNN) model for inference to prove the transitivity of implication.
# 
# Reference:
#   IBM Logical Neural Networks (LNN): https://ibm.github.io/LNN/index.html
# ----------------------------------------------------------------------------------------------------------------

from lnn import Propositions, Implies, And, Model, Fact, Loss, Direction

def implicationtransitivity():

    ### Proving The Transitivity of Implication
    # (A --> B) ^ (B --> C) --> (A --> C)
    #                        ^ ROOT

    ### Knowledge
    A, B, C = Propositions("A", "B", "C")
    A_IMPLIES_B = Implies(A, B)
    B_IMPLIES_C = Implies(B, C)
    A_IMPLIES_B__AND__B_IMPLIES_C = And(A_IMPLIES_B, B_IMPLIES_C)
    A_IMPLIES_C = Implies(A, C)
    ROOT = Implies(A_IMPLIES_B__AND__B_IMPLIES_C, A_IMPLIES_C)
    model = Model()
    model.add_knowledge(ROOT)

    ### Data
    A_IMPLIES_B.add_data(Fact.TRUE)
    B_IMPLIES_C.add_data(Fact.TRUE)
    ROOT.add_data(Fact.TRUE)

    ### Reasoning
    print("\n<------------------------------ BEFORE INFERENCE ------------------------------>")
    model.print(params=True)
    model.infer()
    print("\n<------------------------------ AFTER INFERENCE ------------------------------>")
    model.print(params=True)

    # User Input for Detailed
    detailed = False
    answer = input("Detailed Info? (default= N) [Y/N]: ")
    if answer == "Y": detailed = True

    print("\n{============================== TRUTH TABLE ==============================}\n")
    print(f"| {str(A):{len(str(A))}} | {str(B):{len(str(B))}} | {str(C):{len(str(C))}} | {str(A_IMPLIES_B):{10}} | {str(B_IMPLIES_C):{10}} | {str(A_IMPLIES_C):{10}} | {str(A_IMPLIES_B__AND__B_IMPLIES_C):{len(str(A_IMPLIES_B__AND__B_IMPLIES_C))}} | {str(ROOT):{len(str(ROOT))}}  |")
    print("-------------------------------------------------------------------------------------------------------------")

    for A_Bool in [True, False]:
        for B_Bool in [True, False]:
            for C_Bool in [True, False]:
                A.add_data(Fact.TRUE if A_Bool else Fact.FALSE)
                B.add_data(Fact.TRUE if B_Bool else Fact.FALSE)
                C.add_data(Fact.TRUE if C_Bool else Fact.FALSE)

                ROOT.add_data(Fact.UNKNOWN)
                A_IMPLIES_B.add_data(Fact.UNKNOWN)
                B_IMPLIES_C.add_data(Fact.UNKNOWN)
                A_IMPLIES_B__AND__B_IMPLIES_C.add_data(Fact.UNKNOWN)
                A_IMPLIES_C.add_data(Fact.UNKNOWN)

                model.infer()

                ### Training
                model.train(direciton=Direction.UPWARD, losses=[Loss.CONTRADICTION])
                
                print(f"""| {"T" if A_Bool else "F"} | {"T" if B_Bool else "F"} | {"T" if C_Bool else "F"} | {A_IMPLIES_B.state():<{10}} | {B_IMPLIES_C.state():<{10}} | {A_IMPLIES_C.state():<{10}} | {A_IMPLIES_B__AND__B_IMPLIES_C.state():<{len(str(A_IMPLIES_B__AND__B_IMPLIES_C))}} |  {ROOT.state():<{len(str(ROOT))}} |""")

                if detailed: model.print()

if __name__ == "__main__":
    implicationtransitivity()
