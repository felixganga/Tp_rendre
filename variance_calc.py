def calculate_variance(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    variance = sum((x - mean) ** 2 for x in numbers) / n
    return variance

# Exemple d'utilisation
data = [1, 2, 3, 4, 5]
variance = calculate_variance(data)
print("Variance :", variance)