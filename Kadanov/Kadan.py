import time

def kadane(arr):
  max_ending_here = 0
  max_so_far = -float("inf")

  for i in range(len(arr)):
    max_ending_here += arr[i]
    if max_ending_here < 0:
      max_ending_here = 0
    if max_so_far < max_ending_here:
      max_so_far = max_ending_here

  return max_so_far

def read_integers_from_file(file_path):
    try:
        seznam = []
        with open(file_path, 'r') as file:
            while True:
                number = file.readline()
                if not number:
                    break
                seznam += [int(number)]
            return seznam
    except FileNotFoundError:
        return []
        
seznam = read_integers_from_file("numbers.txt")
startTime = time.process_time()
maks = kadane(seznam)
endTime = time.process_time()
print(maks)
timeTaken = (endTime - startTime) * 1000.0
print(f"Execution time: {timeTaken:.3f} milliseconds")
    