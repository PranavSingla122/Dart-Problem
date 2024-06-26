import numpy as np

def simulate_min_distance(k, trials):
    min_distances = []
    
    for _ in range(trials):
        # Generate k points (x, y) uniformly distributed within the unit circle
        x = np.random.uniform(-1, 1, k)
        y = np.random.uniform(-1, 1, k)
        mask = x**2 + y**2 <= 1  # Only keep points within the unit circle
        distances = np.sqrt(x[mask]**2 + y[mask]**2)
        
        # Ensure we have exactly k points by regenerating if we don't
        while len(distances) < k:
            additional_x = np.random.uniform(-1, 1, k - len(distances))
            additional_y = np.random.uniform(-1, 1, k - len(distances))
            mask = additional_x**2 + additional_y**2 <= 1
            additional_distances = np.sqrt(additional_x[mask]**2 + additional_y[mask]**2)
            distances = np.concatenate((distances, additional_distances))
        
        # Find the minimum distance
        min_distance = np.min(distances)
        min_distances.append(min_distance)
    
    # Calculate the average minimum distance
    average_min_distance = np.mean(min_distances)
    return average_min_distance

# Parameters
k = 100
trials = 10000

# Simulate and print the average minimum distance
average_min_distance = simulate_min_distance(k, trials)
print(f"Average minimum distance achieved after {trials} trials with {k} darts: {average_min_distance:.4f}")
