import time

def ackermann(m, n):
    if m == 0:
      return n + 1
    elif n == 0:
      return ackermann(m - 1, 1)
    else:
      return ackermann(m - 1, ackermann(m, n - 1))
 
start_time = time.process_time()
out = ackermann(4, 1)
end_time = time.process_time()
time_taken = (end_time - start_time) * 1000.0

print(f"Time taken: {time_taken:.2f} milliseconds")
print(f"Result: {out}\n")
