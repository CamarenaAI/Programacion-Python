# import module_name
import module.printing_functions

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

module.printing_functions.print_models(unprinted_designs, completed_models)
module.printing_functions.show_completed_models(completed_models)

# from module_name import function_name
from module.printing_functions import print_models, show_completed_models

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# from module_name import function_name as fn
from module.printing_functions import print_models as pm, show_completed_models as scm

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)

# import module_name as mn
import module.printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

# from module_name import *
from module.printing_functions import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)