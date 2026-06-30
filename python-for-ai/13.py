#------------------------------------------------------------------------
            # Task 13
#------------------------------------------------------------------------
import numpy as np

#Q1. (Basic Array Creation)

arr1d = np.array([10,20,30,40,50])
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(f"First array is - {arr1d}")
print(f"The shape and dtype of first array is - {arr1d.shape} and {arr1d.dtype} respectively!")
print("-"*10)
print(f"Second array is - {arr2d}")
print(f"The shape and dtype of first array is - {arr2d.shape} and {arr2d.dtype} respectively!")


#------------------------------------------------------------------------

#Q2. (np.zeros() and np.ones())

arr1 = np.zeros(8) #A 1D array of 8 zeros.

arr2 = np.ones((4,4)) # A 2D array of shape (4, 4) filled with ones.

arr3 = np.zeros((3,3))  # A 3x3 matrix of zeros.


print(f"A 1D array of 8 zeros is - {arr1}")
print(f"A 2D array of shape (4, 4) filled with ones is - {arr2}")
print(f"A 3x3 matrix of zeros is - {arr3}")


#------------------------------------------------------------------------


# Q3. (np.arange())


ar1 = np.arange(0,21) # Numbers from 0 to 20 (step 1).

ar2 = np.arange(10,51,2) # Even numbers from 10 to 50.

ar3 = np.arange(5,101,5) # Numbers from 5 to 100 with step of 5.

print(f"Numbers from 0 to 20 (step 1). - {ar1}")
print(f"Even numbers from 10 to 50. - {ar2}")
print(f"Numbers from 5 to 100 with step of 5. - {ar3}")


#------------------------------------------------------------------------

# Q4. (np.linspace())


ar1 = np.linspace(0,5,10)

ar2 = np.linspace(-10,10,15)

print(f"10 equally spaced numbers between 0 and 5. - {ar1}")
print(f"Its length is - {len(ar1)}")
print("-"*20)
print(f"15 equally spaced numbers between -10 and 10. - {ar2}")
print(f"Its length is - {len(ar2)}")


#------------------------------------------------------------------------

# Q5. (Random Arrays)


ar1 = np.random.rand(10)
print(f"1D array of 10 random numbers is - {ar1}")

ar2 = np.random.randn(3,3)
print(f"A 3x3 matrix of random numbers is - {ar2}")

ar3 = np.random.randint(10, 50, size=(4,5))
print(f"A 2D array of random integers between 10 & 50 are - {ar3}")

#------------------------------------------------------------------------

# Q6. (Vectors and Basic Operations)

v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])

print(f"Vector 1 - {v1}")
print(f"Vector 2 - {v2}")


add = v1 + v2
sub = v1 - v2
mul = v1 * v2
dot = np.dot(v1,v2)

print(f"The addition of the two vectors is - {add}")
print(f"The subtraction of the two vectors is - {sub}")
print(f"The multiplication of the two vectors is - {mul}")
print(f"The dot product of the two vectors is - {dot}")



#------------------------------------------------------------------------

# Q7. (Matrices and Operations)

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

print(f"Array 1 = {A}")
print(f"Array 2 = {B}")

add = A + B
dot = np.dot(A,B)
mul = A * B

print(f"The addition of the two arrays is - {add}")
print(f"The matrix multiplication of the two arrays is - {dot}")
print(f"The element-wise multiplication of the two arrays is - {mul}")


#------------------------------------------------------------------------

# Q8. (Properties of Arrays)

ar = np.random.randint(1,100,size = (4,4))

print(f"The Matrix is - {ar}")
print(f"It's shape is - {ar.shape}")
print(f"It's dimension is - {ar.ndim}")
print(f"It's datatype is - {ar.dtype}")
print(f"It's Minimum and Maximum value is - {ar.min} and {ar.max} respectively!")


#------------------------------------------------------------------------

#  Q9. (Combined - Random + Reshape + Statistics)


ar = np.random.randint(1,50,size = 20)

print(f"The original matrix - {ar}")

ar_reshape = ar.reshape(4,5)

print(f"After Reshaping it to 4x5, matrix becomes - {ar_reshape}")

print(f"The sum of the matrix is - {ar_reshape.sum()}")
print(f"The mean of it is - {ar_reshape.mean()}")
print(f"It's standard deviation of the matrix is - {ar_reshape.std()}")
print(f"The maximum value in each row is - {ar_reshape.max(axis=1)}")


#------------------------------------------------------------------------

# Q10. (Mini Project - NumPy Application)

# Simple Statistics Calculator


try :
    num = int(input("How many numbers do you want to generate? - "))
    ar = np.random.randint(10,100,size=num)
    print(f"The original matrix is - {ar}")

    print(f"It's Mean: {ar.mean():.2f}")
    print(f"Its's Median: {np.median(ar):.2f}")
    print(f"It's Standard Deviation: {ar.std():.2f}")
    print(f"It's Minimum: {ar.min()}")
    print(f"It's Maximum: {ar.max()}")

    if num % 2 == 0: 
        row = 2
        col = num // 2
        ar_reshape = ar.reshape(row, col)
        print("Reshaped Array:")
        print(ar_reshape)

        # Row-wise sum
        row_sum = ar_reshape.sum(axis=1)
        print("Row-wise Sum:")
        print(row_sum)
    else:
        print("Cannot reshape due to the number of elements!")

except ValueError :
    print("Pls eneter a valid number!")