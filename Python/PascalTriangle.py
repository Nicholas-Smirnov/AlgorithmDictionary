# A pascal triangle is a list of rows of numbers.
# The first row is [1]. The second row is [1, 1].
# The third row is [1, 2, 1]. 
# The fourth row is [1, 3, 3, 1].

# The actual algorithm is O(n^2)

def PascalTriangle(Size):
    
    Triangle = [[1]]
    
    for i in range(Size-1):
        Triangle.append([1])
        for j in range(i):
            Triangle[i].append(Triangle[i-1][j] + Triangle[i-1][j+1])
        Triangle[i].append(1)
    
    Triangle.remove([1])
    Triangle.insert(0, [1])

    for Row in Triangle:
        print(Row)

    return Triangle

PascalTriangle(10)

# Created by Nicholas Smirnov
