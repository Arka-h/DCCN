'''
Exp 5 Task2
Group 3
Prathamesh Bagekari 4
Akshat Bhat 5
Arka Haldi 15
'''

import numpy as np
import itertools as it
from PS2_task3 import *

def syndrome_decode(codeword, n, k, G):
    q = n - k  # Redundant Bits

    # G(k x n) = [I(k x k) : P(k x q)]
    P = G[:, k:]  # Parity Sub Matrix

    # Parity Check Matrix = H(q x n) = [trans(P(q x n) : I(q x q))]
    P_transpose = np.transpose(P)

    H = np.concatenate((P_transpose, np.identity(q)), axis=1)
    H_transpose = np.transpose(H)

    S = np.mod(np.dot(codeword, H_transpose), 2)  # Syndrome
    # print('H_transpose:\n',H_transpose)
    if np.array_equal(S, np.zeros(q)):
        return (S,codeword[:-q])
    else:
        for i, row in enumerate(H_transpose):
            if np.array_equal(S, row):
                codeword[i] ^= 1
                return (S,codeword[:-q])

def validate_and_print_result(n, k, Generator_matrix):
    # generate 2**k = 16 datawords
    datawords = list(it.product(range(2), repeat=k))
    # convert datawords into codewords
    codewords = [np.mod(np.dot(dataword, Generator_matrix), 2)
                 for dataword in datawords]
    test_codewords(n, k, datawords, codewords, syndrome_decode, Generator_matrix)
    test_single_bit_error(n, k, datawords, codewords, syndrome_decode, Generator_matrix)


if __name__ == "__main__":
    # (7,4) Hamming Code , for the purpose of this experiment
    # ==> n = 7, k = 4, q = n - k = 3
    n = 7
    k = 4
    Generator_matrix = np.array([
        [1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 1, 0, 1, 1]],
        ndmin=2)

    validate_and_print_result(n, k, Generator_matrix)
