MAX_ISOMORPHIC_LENGTH = 500
MAX_INTERLEAVED_LENGTH = 100
MAX_INTERLEAVED_RESULT_LENGTH = 200

UPPERCASE_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE_LETTERS = "abcdefghijklmnopqrstuvwxyz"


def are_isomorphic(s: str, t: str) -> bool:
    """Determine whether two strings are isomorphic.

    Parameters:
        s: The first string.
        t: The second string.

    Returns:
        True if the strings are isomorphic, otherwise False.
    """
    result = True

    # The strings must have the same length.
    if len(s) != len(t):
        result = False

    # The strings must have between 1 and 500 characters.
    if len(s) < 1 or len(s) > MAX_ISOMORPHIC_LENGTH:
        result = False

    # Check that s contains only letters.
    for character in s:
        if character not in UPPERCASE_LETTERS + LOWERCASE_LETTERS:
            result = False

    # Check that t contains only letters.
    for character in t:
        if character not in UPPERCASE_LETTERS + LOWERCASE_LETTERS:
            result = False

    if result:
        pairs = []
        used = []

        # Check that each character has one consistent mapping.
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            found = False

            for pair in pairs:
                if pair[0] == s_char:
                    found = True
                    if pair[1] != t_char:
                        result = False

            # A new character cannot map to a used character.
            if not found:
                for character in used:
                    if character == t_char:
                        result = False

                pairs.append([s_char, t_char])
                used.append(t_char)

    return result


def is_interleaved(s1: str, s2: str, s3: str) -> bool:
    """Determine whether s3 is an interleaving of s1 and s2.

    Parameters:
        s1: The first string.
        s2: The second string.
        s3: The string being checked.

    Returns:
        True if s3 is an interleaving, otherwise False.
    """
    result = True

    # The length of s3 must equal the combined lengths.
    if len(s1) + len(s2) != len(s3):
        result = False

    # Check that all three strings contain lowercase letters.
    for character in s1:
        if character not in LOWERCASE_LETTERS:
            result = False

    for character in s2:
        if character not in LOWERCASE_LETTERS:
            result = False

    for character in s3:
        if character not in LOWERCASE_LETTERS:
            result = False

    # Check the maximum allowed lengths.
    if len(s1) > MAX_INTERLEAVED_LENGTH:
        result = False

    if len(s2) > MAX_INTERLEAVED_LENGTH:
        result = False

    if len(s3) > MAX_INTERLEAVED_RESULT_LENGTH:
        result = False

    if result:
        # possible stores possible positions in s1 and s2.
        possible = []

        for i in range(len(s1) + 1):
            row = []
            for j in range(len(s2) + 1):
                row.append(False)
            possible.append(row)

        possible[0][0] = True

        # Check every possible position in s1 and s2.
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if possible[i][j]:
                    if i < len(s1) and s3[i + j] == s1[i]:
                        possible[i + 1][j] = True

                    if j < len(s2) and s3[i + j] == s2[j]:
                        possible[i][j + 1] = True

        # The final position tells us whether s3 can be formed.
        if not possible[len(s1)][len(s2)]:
            result = False

    return result


def contiguous_length(nums: list[int]) -> int:
    """Find the longest contiguous subarray with equal 0s and 1s.

    Parameters:
        nums: A list containing 0s and 1s.

    Returns:
        The length of the longest balanced subarray.
    """
    balance = 0
    max_length = 0
    first = []

    # Create space for every possible balance.
    for i in range(2 * len(nums) + 1):
        first.append(-1)

    # Offset allows negative balances to be list positions.
    offset = len(nums)
    first[offset] = 0

    # Check each number and update the balance.
    for i in range(len(nums)):
        if nums[i] == 0:
            balance -= 1
        else:
            balance += 1

        position = balance + offset

        # Save the first position where this balance appears.
        if first[position] == -1:
            first[position] = i + 1
        else:
            # A repeated balance gives a balanced subarray.
            length = i + 1 - first[position]

            if length > max_length:
                max_length = length

    return max_length
