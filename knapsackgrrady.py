def knapsack_greedy(values, weights, capacity, n):
  """
  Solves the knapsack problem using a greedy approach based on value-to-weight ratio.

  Args:
      values: List of item values.
      weights: List of item weights.
      capacity: Maximum knapsack capacity.
      n: Number of items.

  Returns:
      The total value of the selected items and the list of selected items.
  """
  # Calculate value-to-weight ratios
  ratios = [value / weight for value, weight in zip(values, weights)]

  # Sort items (values, weights, and ratios) by ratio in descending order
  sorted_items = sorted(zip(values, weights, ratios), key=lambda x: x[2], reverse=True)

  selected_values = []
  selected_weights = []
  total_value = 0
  remaining_capacity = capacity

  # Fill the knapsack greedily
  for value, weight, _ in sorted_items:
    if weight <= remaining_capacity:
      selected_values.append(value)
      selected_weights.append(weight)
      total_value += value
      remaining_capacity -= weight
    else:
      break  # No more items can fit

  return total_value, selected_values, selected_weights

# Example usage (same as before)
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

total_value, selected_values, selected_weights = knapsack_greedy(values, weights, capacity, len(values))

print("Total value:", total_value)
print("Selected items (values, weights):", list(zip(selected_values, selected_weights)))
