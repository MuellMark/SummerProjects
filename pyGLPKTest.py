import glpk                         # Import the GLPK module

lp = glpk.LPX()                     # Create empty problem instance
lp.name = 'sample'                  # Assign symbolic name to problem
lp.obj.maximize = True              # Set this as a maximization problem
lp.rows.add(2)                      # Append three rows to this instance
for r in lp.rows:                   # Iterate over all rows
    r.name = chr(ord('p')+r.index)  # Name them p, q, and r
lp.rows[0].bounds = None, 1     # Set bound -inf < p <= 100
lp.rows[1].bounds = None, 1     # Set bound -inf < q <= 600
# lp.rows[2].bounds = None, 300.0     # Set bound -inf < r <= 300
lp.cols.add(2)                      # Append three columns to this instance

for c in lp.cols:                   # Iterate over all columns
    c.name = 'x%d' % c.index        # Name them x0, x1, and x2
    c.bounds = 0, None            # Set bound 0 <= xi < inf
    c.kind=int
lp.obj[:] = [6, 6]        # Set objective coefficients
lp.matrix = [
    2, 1,                  # Set nonzero entries of the
    1, 2,                 # constraint matrix. (In this
    # 2.0, 2.0, 6.0                   # case, all are non-zero.)
]
lp.simplex()
#lp.integer()                     # Solve this LP with the simplex method
print(lp.obj.value)
#print(lp.rows[0] )
# print 'Z = %g;' % lp.obj.value,     # Retrieve and print obj func value
# print '; '.join(                    # Print struct variable names and
#                                     # primal values
#     '%s = %g' % (c.name, c.primal) for c in lp.cols
# )