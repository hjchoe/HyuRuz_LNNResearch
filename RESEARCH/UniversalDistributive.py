from contextlib import redirect_stdout
from typing import Set
from lnn import Formula, Model, Proposition, Or, And, Not, Iff, World, Fact, Loss
from ..helper import printer

def iterate_subformulas(formula: Formula):
    yield formula
    for subformula in formula.operands:
        yield from iterate_subformulas(subformula)

def decomposeFormula(formula: Formula) -> Set[Formula]:
    formulae = [Formula]
    for subformula in iterate_subformulas(formula):
        #print(type(subformula))
        formulae.append(subformula)

    formulae.pop(0)
    return set(formulae)

# ((p ^ q) v (p ^ r)) <-> (p ^ (q v r))
def Distributive_Or(p: Formula, q: Formula, r: Formula) -> Iff:
    return Iff(
        Or(
            And(
                p,
                q
            ),
            And(
                p,
                r
            )
        ),
        And(
            p,
            Or(
                q,
                r
            )
        )
    )

def UniversalDistributive_Or(model: Model, formulae: {Formula}) -> dict:
    truths = dict()
    with open('UniversalDistributiveFormulae.txt', 'w') as f:
        with redirect_stdout(f):
            print("\n<------------------------------ Universal Distributive Formula Knowledge Database ------------------------------>")
            for p in formulae:
                for q in formulae:
                        for r in formulae:
                            formula = Distributive_Or(p, q, r)
                            formula.print()
                            truths.update({formula: 0})
                            model.add_knowledge(formula, world=World.AXIOM)
        f.close()
    return truths

def Negation_Or(p: Formula) -> Or:
    return Or(
        p,
        Not(p)
    )

def UniversalNegation_Or(model: Model, formulae: {Formula}):
    for p in formulae:
        print(f"{p}")
        model.add_knowledge(Negation_Or(p), world=World.AXIOM)

def TruthTable(model: Model, A: Proposition, B: Proposition, query: Formula):
    with open('UniversalDistributiveTruthTable.txt', 'w') as f:
        with redirect_stdout(f):
            i = 0
            for A_Bool in [Fact.TRUE, Fact.FALSE]:
                for B_Bool in [Fact.TRUE, Fact.FALSE]:
                    i+=1
                    print(f"\n~~~ ATTEMPT {i} ~~~")
                    model.flush()
                    A.add_data(A_Bool)
                    B.add_data(B_Bool)
                    model.infer()
                    A.print()
                    B.print()
                    query.print()
                    model.print()

def UniversalDistributive():
    model = Model()

    A = Proposition("A")
    B = Proposition("B")
    A.add_data(Fact.TRUE)

    model.add_knowledge(A, B)

    # ((A v -A) & B) v ((A v -A) & -B)
    query = Or(
        And(
            Or(
                A,
                Not(A)
            ),
            B
        ),
        And(
            Or(
                A,
                Not(A)
            ),
            Not(B)
        )
    )

    #dictionary = decomposeFormula(query)
    #truths = UniversalDistributive_Or(model, dictionary)

    #UniversalNegation_Or(model, dictionary)

    model.add_knowledge(query)

    #printer.print_BeforeInfer(model=model, params=False, numbering=True)
    printer.printFile_BeforeInfer(model=model, params=False, numbering=True)

    #epochs, total_loss = model.train(losses=Loss.CONTRADICTION, pbar=True)

    #steps, facts_inferred = model.infer()
    #model.infer_query()

    #printer.print_AfterInfer(model=model, steps=epochs, facts_inferred=total_loss, params=False, numbering=True)
    #printer.printFile_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, params=False, numbering=True)

    print("__QUERY__")
    query.print()

    TruthTable(model, A, B, query)

    model.plot_graph(formula_number=False, with_labels=False, arrows=True)

if __name__ == "__main__":
    UniversalDistributive()

# ((((A ∧ ¬B) ∨ (A ∧ B)) → (A ∧ (¬B ∨ B))) ∧ ((A ∧ (¬B ∨ B)) → ((A ∧ ¬B) ∨ (A ∧ B))))