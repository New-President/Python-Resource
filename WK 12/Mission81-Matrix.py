# Programming I

#######################
#     Mission 7.1     #
#   MatrixMultiply   #
#######################

# Background
# ==========
# Tom has studied about creating 3D games and wanted
# to write a function to multiply 2 matrices.
# Define a function MatrixMulti() function with 2 parameters.
# Both parameters are in a matrix format.


# Important Notes
# ===============
# 1) Comment out ALL input prompts before submitting.

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[2, 0, 0],
     [0, 2, 0],
     [0, 0, 2]]


# START CODING FROM HERE
# ======================

# Create your function here
def matrixmulti(X, Y):
     c = []
     for i in range(len(X)):
          d=[]
          for j in range(len(X[0])):
               e=0
               for k in range(len(Y)):
                    e+=X[i][k] * Y[k][j]
               d.append(e)
          c.append(d)
     return c


# Do not remove the next line
matrixmulti(A, B)
# 3) For testing, print out the output
#   - Comment out before submitting
