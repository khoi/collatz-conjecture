def calculate_step(n):
    assert n >= 1, "n must be >= 1"
    count = 0
    peak = 0
    while n != 1:
        count += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n > peak:
            peak = n
    return count, peak


numbers = list(range(1, 1000000))
results = [calculate_step(n) for n in numbers]

steps = [r[0] for r in results]
peaks = [r[1] for r in results]

max_step = max(steps)
max_step_idx = steps.index(max_step)

max_peak = max(peaks)
max_peak_idx = peaks.index(max_peak)

print(f"{numbers[max_step_idx]} has the most steps with {max_step}")
print(f"{numbers[max_peak_idx]} has the highest peak of {max_peak}")

numbers_with_the_same_step_count = [
    number for step, number in zip(steps, numbers) if step == number
]

print(
    f"numbers with the same amount of step as itself {numbers_with_the_same_step_count}"
)
