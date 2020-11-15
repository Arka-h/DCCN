'''
Exp 5 Task1 
Group 3 
Prathamesh Bagekari 4
Akshat Bhat 5
Arka Haldi 15
'''
def test_single_bit_error(n, k, datawords, codewords, Generator_matrix):
    print(f'Testing all n*2**k = {n*2**k} valid codewords')
    print()

    for i, codeword in enumerate(codewords):
        for err in range(n):
            # create single bit error
            codeword[err] ^= 1
            print(f'testing {codeword}', end=' ')

            pred_dataword = syndrome_decode(codeword, n, k, Generator_matrix)

            if np.array_equal(pred_dataword, datawords[i]):
                print(f'...passed  deciphered dataword {pred_dataword}')
            else:
                print(
                    f'OOPS: Error decoding {codeword} ...expected {datawords[i]} got {pred_dataword}')
    print()

def test_codewords(n, k, datawords, codewords, Generator_matrix):
    print(f'Testing all 2**k = {2**k} valid codewords')
    print()
    for i, codeword in enumerate(codewords):
        print(f'testing {list(datawords[i])}', end=' ')
        pred_dataword = syndrome_decode(codeword, n, k, Generator_matrix)
        if np.array_equal(pred_dataword, datawords[i]):
            print('...passed')
        else:
            print(
                f'OOPS: Error decoding {codeword} ...expected {datawords[i]} got {pred_dataword}')
    print()
