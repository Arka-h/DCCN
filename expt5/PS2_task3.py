'''
Exp 5 Task1 
Group 3 
Prathamesh Bagekari 4
Akshat Bhat 5
Arka Haldi 15
'''
import numpy as np
def test_single_bit_error(n, k, datawords, codewords, syndrome_decode, Generator_matrix):
    print(f'Testing all n*2**k = {n*2**k} valid codewords')
    print()

    for i, codeword in enumerate(codewords):
        for err in range(n):
            # create single bit error
            codeword[err] ^= 1
            print(f'\ntesting {codeword}')

            s,pred_dataword = syndrome_decode(codeword, n, k, Generator_matrix)

            if np.array_equal(pred_dataword, datawords[i]):
                print(f'single bit error found!\nsyndrome : {s} \n...passed , \ndeciphered dataword : {pred_dataword}')
            else:
                print(
                    f'OOPS: Error decoding {codeword} ...expected {datawords[i]} got {pred_dataword}')
    print()

def test_codewords(n, k, datawords, codewords, syndrome_decode, Generator_matrix):
    print(f'Testing all 2**k = {2**k} valid codewords')
    print()
    for i, codeword in enumerate(codewords):
        print(f'testing {list(datawords[i])}')
        s,pred_dataword = syndrome_decode(codeword, n, k, Generator_matrix)
        if np.array_equal(pred_dataword, datawords[i]):
            print(f'...passed,\nno error found!,\nSyndrome: {s}')
        else:
            print(
                f'OOPS: Error decoding {codeword} ...expected {datawords[i]} got {pred_dataword}')
    print()
