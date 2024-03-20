from itertools import permutations
import sys

def main():
    # Reading input from standard input
    input_str = sys.stdin.readline().strip()
    S, K = input_str.split()  # Splitting input string and integer K
    K = int(K)  # Converting K to an integer
    
    # Generating permutations of size K and sorting them lexicographically
    perm = sorted(permutations(S, K))
    
    # Printing permutations
    for p in perm:
        print(''.join(p))  # Joining elements of permutation tuple and printing
    
    return 0

if __name__ == '__main__':
    main()
