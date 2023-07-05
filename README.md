# Matrix-to-RREF
This project was done as a part of the `MTH101 (Linear Algebra)` course offered in the first semester. The aim of the project was to solve the given [matrix](https://www.britannica.com/science/matrix-mathematics) and convert it into its `Reduced Row Echelon Form` or [RREF](http://linear.ups.edu/html/section-RREF.html#:~:text=Definition%20RREF%20Reduced%20Row%2DEchelon%20Form&text=If%20there%20is%20a%20row,row%20is%20equal%20to%201.) and present the solution in [parametric vector form](https://web.math.ucsb.edu/~mpedrick/teaching/LLM/LLM_1_5_key.pdf).

## Pre-Requisites

### Application
- VS Code or Python IDLE
  
### Knowledge
- Matrix
- RREF properties
- Steps to convert a matrix to its RREF
- Nullspace
- How to find nullspace
- Finding parametric solutions using nullspace and free variables.

## Intuition and Approach

### Converting to RREF
- The matrix is passed as a parameter through the `rref` function. The function searches for the first non-zero integer in the first column and swaps it with the first row. This process is iteratively repeated for all the columns, swapping the desired row with the second row, third row, and so on. This is done to simplify calculations by shifting the zeroes to the bottom of the matrix and shifting the non-zero rows to the top of the matrix.
- Each row is then simplified by dividing the entire row with an integer such that the [pivot](https://en.wikipedia.org/wiki/Pivot_element) of each row is 1. The pivots are simultaneously stored in a list `pivot`, which is used in the next function to evaluate the [nullspace](https://www.geeksforgeeks.org/null-space-and-nullity-of-a-matrix/).
- Further row operations are performed to set all the integers, below the pivot column of a row, to 0.

### Finding nullspace
- The list `pivot` created in `rref` function is used to classify all columns into `column space` and `nullspace`

### Finding solution
- The solutions are then calculated using the nullspace, free variables, and pivots calculated.
- It is then represented in parametric form `(x1v1+x2v2+x3v3+....)`.

## Input format
The matrix is given as input as a nested list by entering the rows and columns as given.

## Output format
The output consists of only the parametric vector form, which is in the form of a string.
