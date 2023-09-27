def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet a given total amount.

    Args:
        coins (list of int): A list of coin denominations available.
        total (int): The target total amount to make change for.

    Returns:
        int: The fewest number of coins needed to meet the total.
             If the total cannot be reached using the
             sprovided coin denominations, returns -1.
    """
    if total <= 0:
        return 0

    fewest_number = [float('inf')] * (total + 1)

    fewest_number[0] = 0

    for coin in coins:
        for current_total in range(coin, total + 1):
            fewest_number[current_total] = min(
                fewest_number[current_total],
                fewest_number[current_total - coin] + 1
            )

    if fewest_number[total] == float('inf'):
        return -1
    else:
        return fewest_number[total]
