#-------------------------------------------------------------------------------

                            #Task 14

#-------------------------------------------------------------------------------
import numpy as np

# Q1. (Array Properties)

#2D array of shape (5, 6) filled with random integers between 10 and 100.
arr = np.random.randint(10, 100, size=(5,6))

print(f"The array is - \n{arr}")
print(f"The shape of the array is - {arr.shape}")
print(f"The size of the array is - {arr.size}")
print(f"The datatype of the array is - {arr.dtype}")


#-------------------------------------------------------------------------------

# Q2. (Statistical Methods - Basic)

arr = np.random.randint(1, 50 , size = 20)

print(f"The array in question is - {arr}")
print(f"The minimum value in the array is - {arr.min()} and it's located at index - {arr.argmin()}")
print(f"The maximum value in the array is - {arr.max()} and it's located at index - {arr.argmax()}")
print(f"The sum of all the element is - {arr.sum()}")
print(f"It's mean is - {arr.mean()} and standard deviation is - {arr.std()}")


#-------------------------------------------------------------------------------

# Q3. (Statistical Methods on 2D Array)

arr = np.random.randint(20, 80, size =(4,5))

print(f"The matrix is -\n {arr}")
print(f"It's minimum and maximum values are - {arr.min()} and {arr.max()} respectively!")
print(f"The sum of all the elements in this array is - {arr.sum()}")
print(f"It's mean and std is - {arr.mean()} and {arr.std()} respectively!")

print(f"The sum of each row is - {arr.sum(axis=0)}")
print(f"The sum of each column is - {arr.sum(axis=1)} ")


#-------------------------------------------------------------------------------

#Q4. (Reshape)

arr = np.arange(1,25)

print(f"The array is - {arr}")

reshape_arr1 = arr.reshape(4,6)
print(f"After first reshape - \n{reshape_arr1}")
print(f"Shape of first reshape - {reshape_arr1.shape}")
print("-"*30)


reshape_arr2 = arr.reshape(3,8)
print(f"After second reshape -\n {reshape_arr2}")
print(f"Shape of second reshape - {reshape_arr2.shape}")
print("-"*30)


reshape_arr3 = arr.reshape(2,3,4)
print(f"After third reshape - \n{reshape_arr3}")
print(f"Shape of third reshape - {reshape_arr3.shape}")
print("-"*30)


#-------------------------------------------------------------------------------

#Q5. (NumPy Indexing - 1D & 2D)


arr = np.array([
[10, 20, 30, 40],
[50, 60, 70, 80],
[90, 100, 110, 120]
])


print(f"The matrix is - \n{arr}")

print(f"The first row of the matrix is - {arr[0]} ")
print(f"The last column of the mateix is - {arr[:,3]}")
print(f"The center 2x2 matrix is - \n {arr[1:3,1:3]}")
print(f"All the even numbers in here are - {arr[arr % 2 == 0]}")


#-------------------------------------------------------------------------------

# Q6. (Advanced Indexing)


arr = np.random.randint(1,100 , size = (5,5))

print(f"The matrix is - \n{arr}")

print(f"The diagonal elements are - {arr.diagonal()}")
print(f"The elements greater then 50 are - {arr[arr > 50]}")
arr[arr < 30] = 0        
print(f"Modified array:\n{arr}") 


#-------------------------------------------------------------------------------

#Q7. (Arithmetic Operations) 


a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])


print(f"Array 1 - {a}")
print(f"Array 2 - {b}")

print(f"Addition - {a + b }")
print(f"Subtractiob - {a-b}")
print(f"Multiplication - {a * b}")
print(f"Division - {a / b}")

print(f"The element wise power for array 1 is - {a ** 2}")

print(f"The element wise power for array 2 is - {b ** 2}")

print(f"The modulo operation on array 1 divided by 2 gives - {a % 2}")
print(f"The modulo operation on array 2 divided by 2 gives - {b % 2}")


#-------------------------------------------------------------------------------

# Q8. (Matrix Multiplication)


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

print(f"Matrix 1 - \n {A}")
print(f"Matrix 2 - \n{B}")

print(f"Element wise multiplication of both matrix returns - \n{A*B}")
print(f"Matrix multiplication of both returns - \n{A@B}")

'''In element wise multiplication, we do multiplication of elements placed at same index
in both matrixes.But, in matrix multiplication we do what we did in M2 , divide the element at one index 
with all the row element and add them and so we did.'''



#-------------------------------------------------------------------------------

# Q9. (Combined - Properties + Operations + Indexing)

arr = np.random.randn(6,6)

print(f"The matrix is - {arr}")
print(f"It's Shape - {arr.shape}")
print(f"It's Size - {arr.size}")
print(f"It's dtype is - {arr.dtype}")

print(f"The maximum value index is - {arr.argmax()}")
print(f"The minimum value index is - {arr.argmin()} ")

print(f"The top left 3x3 submatrix is - \n {arr[0:3,0:3]}")

arr = np.abs(arr)

print(f"Replacing all negative number with their absolute value gives -\n {arr}")

print(f"The mean of the modified array is - {arr.mean()}")


#-------------------------------------------------------------------------------

# Q10. (Mini Project - Student Performance Analysis)


# Student Marks Analyzer:

marks = np.random.randint(30, 101, size=(10, 5))
print("Student Marks (10 x 5):\n", marks)

totals = marks.sum(axis=1)
averages = marks.mean(axis=1)

print("\n Total Marks per Student:\n", totals)
print("\n Average Marks per Student:\n", averages)

highest_idx = np.argmax(totals)
lowest_idx = np.argmin(totals)

print(f"\n Student {highest_idx+1} has the HIGHEST total marks: {totals[highest_idx]}")
print(f"Student {lowest_idx+1} has the LOWEST total marks: {totals[lowest_idx]}")

class_mean = marks.mean()
class_std = marks.std()

print(f"\n Overall Class Mean: {class_mean}")
print(f"Overall Class Standard Deviation: {class_std}")

reshaped = marks.reshape(5, 10)
print("\n Reshaped Array (5 x 10):\n", reshaped)

top3_indices = np.argsort(totals)[-3:][::-1] 
print("\n Top 3 Students (indices):", top3_indices + 1)
print("Marks of Top 3 Students:\n", marks[top3_indices])
