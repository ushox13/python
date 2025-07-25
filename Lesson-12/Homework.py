import threading
import math
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def check_range(start, end, primes):
    """Check a range of numbers for primes and add them to the shared list."""
    for num in range(start, end):
        if is_prime(num):
            primes.append(num)
def main():
    """Main function to create threads and check for primes."""
    start = 1
    end = 100
    num_threads = 4
    step = (end - start) // num_threads
    threads = []
    primes = []
    # Create threads
    for i in range(num_threads):
        thread_start = start + i * step
        thread_end = start + (i + 1) * step if i < num_threads - 1 else end
        thread = threading.Thread(target=check_range, args=(thread_start, thread_end, primes))
        threads.append(thread)
        thread.start()
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    print("Prime numbers found:", primes)



import threading
from collections import defaultdict
def process_file_chunk(file_chunk, word_count):
    """Process a chunk of the file and count word occurrences."""
    for line in file_chunk:
        words = line.strip().split()
        for word in words:
            word_count[word] += 1
def main():
    """Main function to read file and create threads for word counting."""
    file_path = 'large_text_file.txt'  # Replace with your file path
    num_threads = 4
    word_count = defaultdict(int)
    with open(file_path, 'r') as file:
        lines = file.readlines()
        chunk_size = len(lines) // num_threads
        threads = []
        # Create threads to process chunks of the file
        for i in range(num_threads):
            start_index = i * chunk_size
            end_index = (i + 1) * chunk_size if i < num_threads - 1 else len(lines)
            thread = threading.Thread(target=process_file_chunk, args=(lines[start_index:end_index], word_count))
            threads.append(thread)
            thread.start()
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
    print("Word occurrences:", dict(word_count))
if __name__ == "__main__":
    main()
