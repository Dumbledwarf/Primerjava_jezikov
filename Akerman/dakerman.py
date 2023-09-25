import time
import sys 

MAX = 10000
mem = [[0] * (MAX+1) for _ in range(MAX+1)]

def ackermann(m, n):
    if m<=MAX and n <=MAX and mem[m][n] !=0:
        return mem[m][n]
    result = 0
    if m == 0:
      result = n + 1
    elif n == 0:
      result = ackermann(m - 1, 1)
    else:
      result = ackermann(m - 1, ackermann(m, n - 1))
      
    if m<=MAX and n <=MAX :
        mem[m][n] = result
    
    return result


start_time = time.process_time()
out = ackermann(4, 1)
end_time = time.process_time()
time_taken = (end_time - start_time) * 1000.0

print(f"Time taken: {time_taken:.2f} milliseconds")
print(f"Result: {out}\n")
