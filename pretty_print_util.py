
def get_spaces_array(height):
    """Return list for number of spaces per tree height (for pretty printing)."""
    memo = [0] * (height + 1)  # Fill with '0's.
    if height > 0:
        memo[0] = 2
    _get_spaces_array_helper(len(memo), memo)
    return memo


def _get_spaces_array_helper(n, memo):
    """Recursively determine number of spaces at each height."""
    # Base case.
    if n == 1:
        return memo[n-1]
    else:
        # Check if memo already has value.
        if memo[n-1] != 0:
            return memo[n-1]
        else:
            # Damn, gotta do some work.
            prev = _get_spaces_array_helper(n-1, memo)
            next_val = 2 * prev + 1
            memo[n-1] = next_val
            return next_val
