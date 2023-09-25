import time

def stooge_sort(arr, l, h):
  if arr[l] > arr[h]:
    temp = arr[l]
    arr[l] = arr[h]
    arr[h] = temp

  if h - l + 1 > 2:
    t = (h - l + 1) // 3

    stooge_sort(arr, l, h - t)
    stooge_sort(arr, l + t, h)
    stooge_sort(arr, l, h - t)
    
def read_integers_from_file(file_path):
	counter = 0

	seznam = []
	with open(file_path, 'r') as file:
		while True:
			number = file.readline()
			if not number:
				break
			if counter > 2000:
				break
			else:
				seznam += [int(number)]
				counter +=1
		return seznam



seznam = read_integers_from_file("numbers.txt")
startTime = time.process_time()
stooge_sort(seznam,0,len(seznam)-1)
endTime = time.process_time()

timeTaken = (endTime - startTime) * 1000.0
print(f"Execution time: {timeTaken:.3f} milliseconds")


