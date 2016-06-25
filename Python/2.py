def even_fibonacci(n):
    prev, curr = 1, 1
    sum_even = 0
    while curr <= n:
        prev, curr = curr, prev + curr
        if not (curr % 2):
            sum_even += curr
    return sum_even

def main():
    print even_fibonacci(4000000)

if __name__ == "__main__":
    main()
