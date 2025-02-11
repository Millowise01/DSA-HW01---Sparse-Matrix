# DSA-HW01---Sparse-Matrix

# Sparse Matrix Operations
This program performs addition, subtraction, and multiplication on large sparse matrices efficiently Sparse matrices are matrices with mostly zero values, and this program stores only the non-zero elements to save memory.

# How to Use
1. Organize your files:

# Place your Python script (sparse_matrix.py) in /dsa/sparse_matrix/code/src/.

# Place your input files (matrix1.txt, matrix2.txt) in /dsa/sparse_matrix/sample_inputs/.

2. Run the program:
Navigate to the src directory:

# bash
cd /dsa/sparse_matrix/code/src/

# bash
python sparse_matrix.py

3. Follow the prompts:
Enter the file paths for the matrices (e.g., ../sample_inputs/matrix1.txt).
Choose the operation (add, subtract, or multiply).

4. View the result:
The program will display the resulting matrix.

# Input File Format
Input files should look like this:

rows=<number of rows>
cols=<number of columns>
(row, col, value)
(row, col, value)


# Example
matrix1.txt
rows=3
cols=3
(0, 0, 1)
(1, 1, 2)
(2, 2, 3)

# Example Output
If you add matrix1.txt and matrix2.txt, the output will be:
Resulting Matrix:
(0, 0, 5)
(1, 1, 7)
(2, 2, 9)

# Errors
The program will notify you if:
1. The input files are missing or have the wrong format.
2. The matrices have incompatible dimensions for the chosen operation.
