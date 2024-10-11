import pandas as pd

def notebook_settings():
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.max_rows', None) 
    from IPython.core.interactiveshell import InteractiveShell
    InteractiveShell.ast_node_interactivity = "all"