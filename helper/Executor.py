# Imports
from typing import Any, List, Tuple
from lnn import Model, Formula, Fact, World
from . import Printer

# Initializing Global Variables
contradictionFound: bool = False        # Global variable to track if a contradiction is found during inference

def foundContradiction() -> None:
    """
    Sets global variable 'contradictionFound' to True if it is False
    ________________________________________________________________
    * Used to mark whether the model encountered a contradiction during inference
    """

    global contradictionFound       # Call global variable 'contradictionFound'
    contradictionFound = True       # Set g.v. 'contradictionFound' to True

def resetAndRunModel(model: Model, premises: List[Formula], query: Formula, queryTV, printB: bool, detailed: bool, file: bool) -> Tuple[Tuple[int, int], Any]:
    """
    Resets Model, sets query to a certain truth value, and runs inference on it
    ___________________________________________________________________________
    Parameters
    __________
    model:      {Model}             (REQUIRED)      ->  The model to reset and run inference on                                 \n
    premises:   {List[Formula]}     (REQUIRED)      ->  List of premises in model                                               \n
    query:      {Formula}           (REQUIRED)      ->  The query to add to the model                                           \n
    queryTV:    {enum: Fact}        (REQUIRED)      ->  The truth value to set query to                                         \n
    printB:     {bool}              (DEFAULT: True) ->  Boolean to determine whether to print or not                            \n
    detailed:   {bool}              (DEFAULT: True) ->  Boolean to determine whether to show details or not                     \n
    file:       {bool}              (DEFAULT: True) ->  Boolean to determine whether to print to file or to Terminal instead    \n
    Returns
    _______
    (steps, facts_inferred)     {Tuple[Tuple[int, int], Any]}   -> Returns # of steps and facts inferred
    """

    model.flush()                                                       # Flush Model rests all neurons to Fact.UNKNOWN
    method = "Contradiction" if queryTV==Fact.FALSE else "Adonis"       # Adjust method name to reflect proof method
    model = Model(name=f"{model.name} With {method}")                   # Reinitialize Model

    for premise in premises:                                # Iterate through list of premises
        model.add_knowledge(premise, world=World.AXIOM)     # Add each premise to the Model's knowledge base as an axiom
    
    query.add_data(queryTV)         # Set query to Fact.FALSE
    model.add_knowledge(query)      # Add query to Model's knowledge base

    # Print the Model BEFORE inference if 'printB' argument is True
    if printB: Printer.print_BeforeInfer(file=file, model=model, query=query, detailed=detailed)

    # Run upward and downward inference passes on Model until it converges on solution or no new knowledge is discovered
    steps, facts_inferred = model.infer()

    Printer.print_solution_steps()      # Print all solution steps to 'Proof.txt' file

    return steps, facts_inferred

def prove(model: Model, premises: List[Formula], query: Formula, printB: bool=True, detailed: bool=True, file: bool=True, graph: bool=True) -> None:
    """
    Runs proof algorithm on Model
    _____________________________
    * Starts with Direct Proof, checks Principle of Explosion, tries Proof by Contradiction, tries Proof by Adonis, concludes inconclusive if all fails
    * Can print results to File or Terminal
    * Can generate visualization of Model

    Parameters
    __________
    model:      {Model}             (REQUIRED)      ->  The model to run inference on                                           \n
    premises:   {List[Formula]}     (REQUIRED)      ->  List of premises in model                                               \n
    query:      {Formula}           (REQUIRED)      ->  The query to add to the model                                           \n
    printB:     {bool}              (DEFAULT: True) ->  Boolean to determine whether to print or not                            \n
    detailed:   {bool}              (DEFAULT: True) ->  Boolean to determine whether to show details or not                     \n
    file:       {bool}              (DEFAULT: True) ->  Boolean to determine whether to print to file or to Terminal instead    \n
    graph:      {bool}              (DEFAULT: True) ->  Boolean to determine whether to generate and show graph or not          \n
    """
    
    # <-------------------- INITIALIZATION ------------------->
    
    global contradictionFound       # Call global variable 'contradictionFound'
    contradictionFound = False      # Set g.v. 'contradictionFound' to False

    for premise in premises:                                # Iterate through list of premises
        model.add_knowledge(premise, world=World.AXIOM)     # Add each premise to the Model's knowledge base as an axiom

    Printer.initPrinter(name=model.name)                                            # Initialize Printer with Model's name
    Printer.print_ModelInfo(name=model.name, premises=premises, query=query)        # Print Model's information to 'Proof.txt' file

    # <-------------------- DIRECT PROOF ------------------->

    model.set_query(query)      # Set query in model as Fact.UNKNOWN

    # Print the Model BEFORE inference if 'printB' argument is True
    #      * Prints to file if 'file' arg. is True, otherwise prints to Terminal
    #      * Prints detailed information if 'detailed' arg. is True
    if printB: Printer.print_BeforeInfer(file=file, model=model, query=query, detailed=detailed)

    # Run upward and downward inference passes on Model until it converges on solution or no new knowledge is discovered
    #      * Receives number of steps and number of facts inferred
    #      * Saves inference steps to Printer
    #      * Updates g.v. 'contradictionFound' if contradiction encountered
    steps, facts_inferred = model.infer()

    Printer.print_solution_steps()      # Print all solution steps to 'Proof.txt' file

    queryTV = query.state()     # Save query's truth value after inference to 'queryTV'

    # <-------------------- PRINCIPLE OF EXPLOSION CHECK ------------------->

    # Conclude Principle of Explosion if contradiction found during Direct Proof
    #      * Determines the premises are inconsistent and therefore query must be True
    if contradictionFound:
        query.add_data(Fact.TRUE)                   # Set query to True
        Printer.principleOfExplosion(query.name)    # Print Principle of Explosion conclusion to 'Proof.txt'

    # Conclude Direct Proof if Model converges on solution for query and no contradictions found
    elif queryTV != Fact.UNKNOWN:
        Printer.concludeProof(True if queryTV==Fact.TRUE else False, query.name)

    # <-------------------- PROOF BY CONTRADICTION ------------------->

    # Try Proof by Contradiction if Model does not prove query using Direct Proof or Principle of Explosion Check
    elif queryTV == Fact.UNKNOWN:
        Printer.startContradiction(query)       # Setup Proof by Contradiction in 'Proof.txt'
        
        steps, facts_inferred = resetAndRunModel(model=model, premises=premises, query=query, queryTV=Fact.FALSE, printB=printB, detailed=detailed, file=file)    # Reset Model, set query to a False, and run inference

        # Conclude Proof by Contradiction if Model converges on solution for query
        if contradictionFound:
            Printer.concludeContradiction(query.name)

        # <-------------------- PROOF BY ADONIS ------------------->

        # Try Proof by Adonis if Model does not prove query using Direct Proof, Principle of Explosion Check, or Proof by Contradiction
        else:
            Printer.startAdonis(query)      # Setup Proof by Adonis in 'Proof.txt'
        
            steps, facts_inferred = resetAndRunModel(model=model, premises=premises, query=query, queryTV=Fact.TRUE, printB=printB, detailed=detailed, file=file)    # Reset Model, set query to a True, and run inference
            
            # Conclude Proof by Adonis
            #      * Determines the premises are inconsistent if contradiction found during Proof by Adonis
            #      * Determines inconclusive otherwise
            Printer.concludeAdonis(contradictionFound, query.name)

    # <-------------------- FINALIZATION ------------------->

    # Print the Model AFTER inference if 'printB' argument is True
    #      * Prints to file if 'file' arg. is True, otherwise prints to Terminal
    #      * Prints detailed information if 'detailed' arg. is True
    if printB:
        Printer.print_AfterInfer(file=file, model=model, query=query, detailed=detailed, steps=steps, facts_inferred=facts_inferred)
    
    # Generate and show a visual plot of the Model (Directed Acyclic Graph) if 'graph' is True
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