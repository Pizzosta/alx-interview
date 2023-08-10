#!/usr/bin/python3
'''Minimum Operations'''


def minOperations(n):
    '''Calculates the fewest number of operations
    needed to result in exactly n H
    characters in this file.

    Args:
        n (int): The desired number of characters.

    Returns:
        int: The minimum number of operations needed.
             Returns 0 if n is impossible to achieve.
    '''
    copied_chars = 1  # Number of characters currently in the file
    clipboard = 0     # Number of H's copied to clipboard
    operations = 0    # Operations counter

    # Continue until the desired number of characters is achieved
    while copied_chars < n:
        # If clipboard is empty, perform Copy All operation
        if clipboard == 0:
            clipboard = copied_chars  # Copy all characters to clipboard
            operations += 1  # Increment operations counter

        # If no characters have been pasted yet
        if copied_chars == 1:
            copied_chars += clipboard  # Paste the copied characters
            operations += 1  # Increment operations counter
            continue

        remaining = n - copied_chars  # Cal the remaining chars to be pasted

        # Check if it's impossible to achieve 'n' chars with the curr clipboard
        if remaining < clipboard:
            return 0

        # If remaining chars can't be div by copied_chars, paste the clipboard
        if remaining % copied_chars != 0:
            copied_chars += clipboard  # Paste the clipboard
            operations += 1  # Increment operations counter
        else:
            clipboard = copied_chars  # Copy all characters to clipboard
            copied_chars += clipboard  # Paste the copied characters
            operations += 2  # Incre operas counter for both Copy All & Paste

    # Check if the desired number of characters is achieved
    if copied_chars == n:
        return operations
    else:
        return 0  # Return 0 if achieving 'n' characters is not possible
