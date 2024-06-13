def print_pattern(n):
    for i in range(n):
        # Print leading spaces
        for j in range(i):
            print("   ", end="")
        # Print descending numbers with four spaces in between
        for k in range(n - i, 0, -1):
            print(f"{k}   ", end=" ")
        # Move to the next line
        print()

# Example usage
n = 5
print_pattern(n)
