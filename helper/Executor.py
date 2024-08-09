from typing import List, Tuple
from lnn import Model, Formula, Fact, World
from . import Printer

contradictionFound: bool = False

def foundContradiction():
    global contradictionFound
    contradictionFound = True

def prove(model: Model, premises: List[Formula], query: Formula, printB: bool=True, detailed: bool=True, file: bool=True, filename: str="", graph: bool=True) -> None:
    # <----- INITIALIZATION ----->
    
    global contradictionFound
    contradictionFound = False

    Printer.initPrinter(name=filename)
    # Builds Knowledge Base of Premises
    for premise in premises:
        model.add_knowledge(premise, world=World.AXIOM)
    Printer.printModelInfoToProof(name=model.name, premises=premises, query=query)

    # <----- DIRECT PROOF ----->

    model.set_query(query)

    # Prints the model BEFORE inference to either file or IO output based on function parameters:
    #      * printB (bool): Whether to print or not
    #      * file (bool): Whether to print to File or IO output
    #      * detailed (bool): Whether to print detailed information (params and formula numbers)
    if printB:
        if file:
            Printer.printFile_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)
        else:
            Printer.print_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)

    # Runs upward and downward inference on Model until convergence or no new knowledge discovered
    #      * Receives number of steps and number of facts inferred during inference
    steps, facts_inferred = model.infer()

    Printer.print_solution_steps()

    queryState = query.state()
    if contradictionFound:
        query.add_data(Fact.TRUE)
        Printer.principleOfExplosion(query.name)
    
    # <----- PROOF BY CONTRADICTION ----->
    elif queryState == Fact.UNKNOWN:
        Printer.startContradiction(query)
        
        model.flush()
        model = Model(name=f"{model.name} With Contradiction")

        # Builds Knowledge Base of Premises
        for premise in premises:
            model.add_knowledge(premise, world=World.AXIOM)
        
        query.add_data(Fact.FALSE)
        model.add_knowledge(query)

        # Prints the model BEFORE inference to either file or IO output based on function parameters:
        #      * printB (bool): Whether to print or not
        #      * file (bool): Whether to print to File or IO output
        #      * detailed (bool): Whether to print detailed information (params and formula numbers)
        if printB:
            if file:
                Printer.printFile_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)
            else:
                Printer.print_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)

        # Runs upward and downward inference on Model until convergence or no new knowledge discovered
        #      * Receives number of steps and number of facts inferred during inference
        steps, facts_inferred = model.infer()

        Printer.print_solution_steps()

        # <----- PROOF BY ADONIS ----->
        if not contradictionFound:
            Printer.startAdonis(query)
        
            model.flush()
            model = Model(name=f"{model.name} With Adonis")

            # Builds Knowledge Base of Premises
            for premise in premises:
                model.add_knowledge(premise, world=World.AXIOM)
            
            query.add_data(Fact.TRUE)
            model.add_knowledge(query)

            # Prints the model BEFORE inference to either file or IO output based on function parameters:
            #      * printB (bool): Whether to print or not
            #      * file (bool): Whether to print to File or IO output
            #      * detailed (bool): Whether to print detailed information (params and formula numbers)
            if printB:
                if file:
                    Printer.printFile_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)
                else:
                    Printer.print_BeforeInfer(model=model, query=query, params=detailed, numbering=detailed)

            # Runs upward and downward inference on Model until convergence or no new knowledge discovered
            #      * Receives number of steps and number of facts inferred during inference
            steps, facts_inferred = model.infer()

            Printer.print_solution_steps()
            
            Printer.concludeAdonis(contradictionFound, query.name)
        else:
            Printer.concludeContradiction(query.name)

    else:
        queryState = True if queryState==Fact.TRUE else False if queryState==Fact.FALSE else None
        Printer.concludeProof(queryState, query.name)

    # <----- FINALIZATION ----->

    # Prints the model AFTER inference to either file or IO output based on function parameters: 
    #      * printB (bool): Whether to print or not
    #      * file (bool): Whether to print to File or IO output
    #      * detailed (bool): Whether to print detailed information (params and formula numbers)
    if printB:
        if file:
            Printer.printFile_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=detailed, numbering=detailed)
        else:
            Printer.print_AfterInfer(model=model, query=query, params=detailed, numbering=detailed, steps=steps, facts_inferred=facts_inferred)
    
    # Generates and shows a visual plot of the Directed Acyclic Graph
    #      * graph (bool): Whether to generate and show graph or not
    if graph:
        model.plot_graph()
    
    print(f"\nCompleted Inference on {model.name} Model!")

def inferModel(model: Model, premises: List[Formula], query: Tuple[Formula, Fact], printB: bool=True, detailed: bool=True, file: bool=True, filename: str="", graph: bool=True) -> None:
    """
    inferModel()
    ------------
    Runs inference on model until convergence.
    __________________________________________
    Has options to print model with detail to file and show graph with detail.

    Parameters:
    -----------
    model:      {Model}                 (REQUIRED)      ->  The model to run inference on.                                                  \n
    premises:   {List[Formula]}         (REQUIRED)      ->  List of premises in model.
    query:      {Tuple[Formula, Fact]}  (OPTIONAL)      ->  The query to add to the model (if exists, otherwise pass in None).              \n
    printB:     {bool}                  (DEFAULT: True) ->  Boolean to determine whether to print or not.                                   \n
    detailed:   {bool}                  (DEFAULT: True) ->  Boolean to determine whether to show details or not (in both print and graph).  \n
    file:       {bool}                  (DEFAULT: True) ->  Boolean to determine whether to print to file or to IO instead.                 \n
    filename:   {str}                   (DEFAULT: "")   ->  Filename if printing to file.                                                   \n
    graph:      {bool}                  (DEFAULT: True) ->  Boolean to determine whether to generate and show graph or not.                 \n
    """

    # Builds Knowledge Base of Premises
    for premise in premises:
        model.add_knowledge(premise, world=World.AXIOM)

    # Sets query in the Model
    if query[1] is Fact.UNKNOWN:
        model.set_query(query[0])          # Automatically sets query to UNKNOWN and becomes target of convergence during inference
    else:
        query[0].add_data(query[1])     # Sets a specific Truth Value to Query before adding it to Model
        model.add_knowledge(query[0])

    Printer.initPrinter(name=filename)

    # Prints the model BEFORE inference to either file or IO output based on function parameters:
    #      * printB (bool): Whether to print or not
    #      * file (bool): Whether to print to File or IO output
    #      * detailed (bool): Whether to print detailed information (params and formula numbers)
    if printB:
        if file:
            Printer.printFile_BeforeInfer(model=model, query=query[0], params=detailed, numbering=detailed)
        else:
            Printer.print_BeforeInfer(model=model, query=query[0], params=detailed, numbering=detailed)

    Printer.printModelInfoToProof(name=model.name, premises=premises, query=query[0])
    
    # Runs upward and downward inference on Model until convergence or no new knowledge discovered
    #      * Receives number of steps and number of facts inferred during inference
    steps, facts_inferred = model.infer()

    Printer.print_solution_steps()

    # Prints the model AFTER inference to either file or IO output based on function parameters: 
    #      * printB (bool): Whether to print or not
    #      * file (bool): Whether to print to File or IO output
    #      * detailed (bool): Whether to print detailed information (params and formula numbers)
    if printB:
        if file:
            Printer.printFile_AfterInfer(model=model, steps=steps, facts_inferred=facts_inferred, query=query[0], params=detailed, numbering=detailed)
        else:
            Printer.print_AfterInfer(model=model, query=query[0], params=detailed, numbering=detailed, steps=steps, facts_inferred=facts_inferred)
    
    # Generates and shows a visual plot of the Directed Acyclic Graph
    #      * graph (bool): Whether to generate and show graph or not
    if graph:
        model.plot_graph()
    
    print(f"\nCompleted Inference on {model.name} Model!")