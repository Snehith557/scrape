import psutil

# Get the current process.
process = psutil.Process()

# Get the CPU and memory usage of the process.
cpu_usage = process.cpu_percent()
memory_usage = process.memory_info().rss / (1024 * 1024) # in MB.

print(f"CPU usage: {cpu_usage}%")
print(f"Memory usage: {memory_usage} MB")