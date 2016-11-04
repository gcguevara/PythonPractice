'''
    GARRETT GUEVARA
    PRACTICING ALGORITHMS
    
    Find the peak of a one-dimensional array
    under the assumption that the array is
    linear, a peak exists, and there is one peak.
    
'''

# the inefficient way
def peak_of_1d(A):
    for i in range(0, 7):
        if A[i-1] <= A[i] and A[i] >= A[i+1]:
            return i

# like the phone book trick, cut it in half until you find the peak
def second_peak_of_1d(A,i,j):
    k = A[j/2]
    if A[k-1] <= A[k] >= A[k+1]:
        return k
    elif A[k-1] > A[k]:
        return peak_of_1d(A,i,k-1)
    elif A[k] < A[k+1]:
        return peak_of_1d(A,k+1,j)

# mathematically works, but python finds an error with a list indice
# being a float after finding the middle index (7/2 = 3.5)

# may need to import numpy library for proper function

A = [1, 5, 9, 8, 6, 4, 3]

print(peak_of_1d(A))


