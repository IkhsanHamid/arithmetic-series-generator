def generate_arithmetic_series(n):
    start = 2
    difference = 3
    result = []

    for i in range(n):
        result.append(start + i * difference)

    return result

if __name__ == "__main__":
    n = 7  # Ganti dengan input 4 atau 7
    series = generate_arithmetic_series(n)
    print(", ".join(map(str, series)))
