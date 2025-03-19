
import scipy as sp

matriceAdjacence = [[0,530,120,0,0,0],
                    [0,0,180,260,130,0],
                    [0,0,0,170,110,80],
                    [0,0,0,0,0,300],
                    [0,0,0,0,0,260],
                    [0,0,0,0,0,0]]

MatriceCsArray = sp.sparse.csr_array(matriceAdjacence)

result = sp.sparse.csgraph.maximum_flow(MatriceCsArray,0,5)

print(result)
print(result.flow[0])
