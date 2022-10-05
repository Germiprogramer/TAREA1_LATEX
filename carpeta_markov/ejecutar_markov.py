from markov1 import *
from markov2 import *

print("Cadenas de Markov para ver la probabilidad de que crezca o decrezca el GDP de un pais")
print("\n")
markov1('China')
markov1('Germany')
markov1('Italy')
markov1('Kyrgyz Republic')
markov1('Nigeria')
markov1('Spain')
print("\n")
print("Cadenas de Markov para comparar el GDP de distintos paises")
print("\n")
markov2('Germany', 'China', 'Spain')