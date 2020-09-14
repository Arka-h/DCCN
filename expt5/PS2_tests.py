import numpy as np
from PS2_rect import even_parity
a=np.array([[0,1,1,0,0,],
            [1,1,0,1,1,],
            [1,0,1,1,0,]
            ], ndmin=2)

b=np.array([[1,0,0,1,1,],
            [0,0,1,0,1,],
            [1,0,1,0,0,]
            ], ndmin=2)

c=np.array([[0,1,1,1,1,],
            [1,1,1,0,1,],
            [1,0,0,0,0,]
            ], ndmin=2)

array_of_codewords = [a,b,c]

def rect_parity(codeword:np.ndarray,nrows:int,ncols:int):
    compressed_row = np.apply_along_axis(even_parity,1,codeword)[:-1] # row wise compression ,False
    compressed_col = np.apply_along_axis(even_parity,0,codeword)[:-1] # column wise compression [:-1]
    # finding index with 1
    i,j = -1,-1
    for t in range(nrows):
        if compressed_row[t]==1:
            i = t
    for t in range(ncols):
        if compressed_col[t]==1:
            j = t
    # print(compressed_row) 
    # print(compressed_col)
    if np.sum(compressed_row) and np.sum(compressed_col) :
        print("failed...")
        codeword[i,j] = codeword[i,j]^1
        print(f"detected error at {(i,j)}..")
    else:
        print("passed...")
    return codeword[:-1,:-1]

# utility functions

def test_correct_errors(array_of_codewords):
    print('Testing all codewords...')
    for codeword in array_of_codewords:
        print('\nTesting codeword:')
        print(codeword)
        message_sequence = rect_parity( codeword , nrows=2, ncols=4)
        print("message_sequence : \n",message_sequence,"\n")
    pass
    
if __name__ == "__main__" :
    # keep the pivot zero, as it doesn't affect the result of either 
    test_correct_errors(array_of_codewords)