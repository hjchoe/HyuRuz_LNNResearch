from typing import Tuple
from lnn import Model, Formula
from . import Printer

def inferModel(model: Model, query: Formula, print: bool=True, print_detailed: bool=True, print_file: bool=True, filename: str="", graph: bool=True):
    """
    Runs inference on model with a query until convergence.
    Can print model with detail to file.
    Can show graph with detail.
    """
    model.set_query(query)

    if print:
        if print_file:
            Printer.printFile_BeforeInfer(filename=filename, model=model, query=query, params=print_detailed, numbering=print_detailed)
        else:
            Printer.print_BeforeInfer(model=model, query=query, params=print_detailed, numbering=print_detailed)
    
    steps, facts_inferred = model.infer()

    if print:
        if print_file:
            Printer.printFile_AfterInfer(filename=filename, model=model, steps=steps, facts_inferred=facts_inferred, query=query, params=print_detailed, numbering=print_detailed)
        else:
            Printer.print_AfterInfer(model=model, query=query, params=print_detailed, numbering=print_detailed, steps=steps, facts_inferred=facts_inferred)
        
    if graph:
        model.plot_graph()