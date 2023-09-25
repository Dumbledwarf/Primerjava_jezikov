import time

def lcs(X, Y):
  m = len(X)
  n = len(Y)

  L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if X[i - 1] == Y[j - 1]:
        L[i][j] = L[i - 1][j - 1] + 1
      else:
        L[i][j] = max(L[i - 1][j], L[i][j - 1])

  lcs = []
  i = m
  j = n
  while i > 0 and j > 0:
    if X[i - 1] == Y[j - 1]:
      lcs.append(X[i - 1])
      i -= 1
      j -= 1
    else:
      if L[i - 1][j] > L[i][j - 1]:
        i -= 1
      else:
        j -= 1

  lcs.reverse()
  return ''.join(lcs)

X = "string1.txt"
Y = "string2.txt"
with open(X, 'r') as file:
    X = file.read()
with open(Y, 'r') as file:
    Y = file.read()
	
startTime = time.process_time()
lcsSeq = lcs(X, Y)
endTime = time.process_time()
timeTaken = (endTime - startTime) * 1000.0
print(f"Execution time: {timeTaken:.3f} milliseconds")
print(lcsSeq)

