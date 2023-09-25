import time

DIM = 500

def readNumbers(file,matrix):
    with open("numbers.txt", "r") as file:
        for row in range(500):
            for col in range(500):
                line = file.readline().strip()
                try:
                    num = int(line)
                    matrix[row][col] = num
                except ValueError:
                    col-=1


        
def mnozenjeMatrik(A, C):
    for i in range(DIM):
        for j in range(DIM):
            for k in range(DIM):
                C[i][j] += A[i][k] * A[k][j]



A = [[0 for _ in range(DIM)] for _ in range(DIM)]
C = [[0 for _ in range(DIM)] for _ in range(DIM)]
readNumbers("numbers.txt",A) 
startTime = time.process_time()
mnozenjeMatrik(A, C)
endTime = time.process_time()
timeTaken = (endTime - startTime) * 1000.0
print(f"Execution time: {timeTaken:.3f} milliseconds")
print(f"Number: ",C[0][0])

