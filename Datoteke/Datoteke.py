import time

def write_to_file(text, filename):
  for i in range(100000):
    with open(filename, "a") as temp:
        temp.write(text)

startTime = time.process_time()
write_to_file("To je besedilo, ki ga bomo zapisali v datoteko.\n", "izhod.txt")
endTime = time.process_time()

timeTaken = (endTime - startTime) * 1000.0
print(f"Execution time: {timeTaken:.3f} milliseconds")