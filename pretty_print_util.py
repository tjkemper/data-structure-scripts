
def get_spaces_array(height):
    """Return list for number of spaces per tree height (for pretty printing)."""
    memo = [0] * (height + 1)  # Fill with '0's. '+ 1' because if height = 4 then spaces = memo[4].
    if height > 0:
        memo[0] = 2  # Arbitrary base case
    _get_spaces_array_helper(len(memo), memo)
    return memo


def _get_spaces_array_helper(n, memo):
    """Recursively determine number of spaces at each height.

    :param n: The height to find num spaces for.
    :param memo: Memoization table. But that dynamic programming tho!
    """
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


def print_slashes(h, spaces, num_keys):
    """Print slashes (under tree at height h).

    :param h: Height of tree to print slashes under.
    :param spaces: Spaces array (get by calling get_spaces_array())
    :param num_keys: The number of keys at height h of the tree.
    """
    if h >= 2:
        num_rows = spaces[h - 2]
        num_spaces = spaces[h - 1]
        before = num_spaces - 1
        after = 0
        for row in range(num_rows):
            for e in range(num_keys):
                left = " " * before + "/" + " " * after
                right = " " * after + "\\" + " " * before
                print(left + " " + right + " ", end="")
            print()
            before -= 1
            after += 1
