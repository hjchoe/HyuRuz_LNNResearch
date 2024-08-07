from typing import List, Tuple
from lnn import Model, Formula, Fact, World
from . import Printer

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

    Printer.setFilename(name=filename)

    # Prints the model BEFORE inference to either file or IO output based on function parameters:
    #      * printB (bool): Whether to print or not
    #      * file (bool): Whether to print to File or IO output
    #      * detailed (bool): Whether to print detailed information (params and formula numbers)
    if printB:
        if file:
            Printer.printFile_BeforeInfer(model=model, query=query[0], params=detailed, numbering=detailed)
        else:
            Printer.print_BeforeInfer(model=model, query=query[0], params=detailed, numbering=detailed)

    Printer.printModelInfoToProof(model=model, premises=premises, query=query[0])
    
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