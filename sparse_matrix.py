# Sparse Matrix Class to efficiently store and manipulate large sparse matrices
class SparseMatrix:
    def __init__(self, num_rows, num_cols):
        """
        Initialize a sparse matrix with a given number of rows and columns.
        Non-zero elements are stored in a dictionary of dictionaries for efficient access.
        """
        self.num_rows = num_rows  # Total number of rows in the matrix
        self.num_cols = num_cols  # Total number of columns in the matrix
        self.matrix = {}  # Dictionary to store non-zero elements: {row: {col: value}}

    def get_element(self, row, col):
        """
        Retrieve the value at a specific (row, col) position in the matrix.
        Returns 0 if the element is not stored (i.e., it's a zero).
        """
        return self.matrix.get(row, {}).get(col, 0)

    def set_element(self, row, col, value):
        """
        Set the value at a specific (row, col) position in the matrix.
        If the value is 0, remove the element from storage to save space.
        """
        if value != 0:  # Only store non-zero values
            if row not in self.matrix:
                self.matrix[row] = {}  # Create a new row if it doesn't exist
            self.matrix[row][col] = value  # Store the value at (row, col)
        elif row in self.matrix and col in self.matrix[row]:  # Remove zero values
            del self.matrix[row][col]
            if not self.matrix[row]:  # If the row is empty, remove it
                del self.matrix[row]

    @staticmethod
    def from_file(file_path):
        """
        Load a sparse matrix from a file.
        The file format is:
        - First line: rows=<number of rows>
        - Second line: cols=<number of columns>
        - Subsequent lines: (row, col, value) for non-zero elements
        """
        with open(file_path, 'r') as file:
            lines = file.readlines()

            # Read the number of rows and columns
            num_rows = int(lines[0].split('=')[1].strip())
            num_cols = int(lines[1].split('=')[1].strip())

            # Create a new sparse matrix
            matrix = SparseMatrix(num_rows, num_cols)

            # Read and store non-zero elements
            for line in lines[2:]:
                line = line.strip()
                if line:  # Skip empty lines
                    # Remove parentheses and split by commas
                    parts = line.strip('()').split(',')
                    row = int(parts[0].strip())
                    col = int(parts[1].strip())
                    value = int(parts[2].strip())
                    matrix.set_element(row, col, value)

            return matrix

    def __str__(self):
        """
        Convert the sparse matrix to a string for easy visualization.
        Useful for debugging and testing.
        """
        result = []
        for row in sorted(self.matrix.keys()):
            for col in sorted(self.matrix[row].keys()):
                result.append(f"({row}, {col}, {self.matrix[row][col]})")
        return "\n".join(result)


# Matrix Operations
def add_matrices(matrix1, matrix2):
    """
    Add two sparse matrices.
    Raises an error if the matrices have different dimensions.
    """
    if matrix1.num_rows != matrix2.num_rows or matrix1.num_cols != matrix2.num_cols:
        raise ValueError("Matrices must have the same dimensions for addition")

    result = SparseMatrix(matrix1.num_rows, matrix1.num_cols)

    # Add elements from matrix1
    for row in matrix1.matrix:
        for col in matrix1.matrix[row]:
            result.set_element(row, col, matrix1.get_element(row, col))

    # Add elements from matrix2
    for row in matrix2.matrix:
        for col in matrix2.matrix[row]:
            result.set_element(row, col, result.get_element(row, col) + matrix2.get_element(row, col))

    return result


def subtract_matrices(matrix1, matrix2):
    """
    Subtract matrix2 from matrix1.
    Raises an error if the matrices have different dimensions.
    """
    if matrix1.num_rows != matrix2.num_rows or matrix1.num_cols != matrix2.num_cols:
        raise ValueError("Matrices must have the same dimensions for subtraction")

    result = SparseMatrix(matrix1.num_rows, matrix1.num_cols)

    # Add elements from matrix1
    for row in matrix1.matrix:
        for col in matrix1.matrix[row]:
            result.set_element(row, col, matrix1.get_element(row, col))

    # Subtract elements from matrix2
    for row in matrix2.matrix:
        for col in matrix2.matrix[row]:
            result.set_element(row, col, result.get_element(row, col) - matrix2.get_element(row, col))

    return result


def multiply_matrices(matrix1, matrix2):
    """
    Multiply two sparse matrices.
    Raises an error if the number of columns in matrix1 does not match the number of rows in matrix2.
    """
    if matrix1.num_cols != matrix2.num_rows:
        raise ValueError("Number of columns in matrix1 must match number of rows in matrix2 for multiplication")

    result = SparseMatrix(matrix1.num_rows, matrix2.num_cols)

    # Perform multiplication
    for row in matrix1.matrix:
        for col1 in matrix1.matrix[row]:
            if col1 in matrix2.matrix:
                for col2 in matrix2.matrix[col1]:
                    value = matrix1.get_element(row, col1) * matrix2.get_element(col1, col2)
                    result.set_element(row, col2, result.get_element(row, col2) + value)

    return result


# Main Program
def main():
    """
    Main function to load matrices, perform operations, and display results.
    """
    # Ask the user for the file paths
    file1 = input("Enter the file path for the first matrix: ").strip()
    file2 = input("Enter the file path for the second matrix: ").strip()

    # Load matrices from files
    try:
        matrix1 = SparseMatrix.from_file(file1)
        matrix2 = SparseMatrix.from_file(file2)
    except FileNotFoundError:
        print("Error: One or both files could not be found. Please check the file paths.")
        return
    except Exception as e:
        print(f"Error loading matrices: {e}")
        return

    # Ask the user for the operation
    operation = input("Enter operation (add, subtract, multiply): ").strip().lower()

    # Perform the selected operation
    try:
        if operation == 'add':
            result = add_matrices(matrix1, matrix2)
        elif operation == 'subtract':
            result = subtract_matrices(matrix1, matrix2)
        elif operation == 'multiply':
            result = multiply_matrices(matrix1, matrix2)
        else:
            print("Invalid operation")
            return
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Print the result
    print("Resulting Matrix:")
    print(result)


# Run the program
if __name__ == "__main__":
    main()
