def are_isomorphic(s: str, t: str) -> bool:
    """Determine whether two strings are isomorphic."""
    
    if len(s) != len(t):
        return False

    if len(s) < 1 or len(s) > 500:
        return False

    for character in s:
        if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False

    for character in t:
        if character not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            return False

    pairs = []
    used = []

    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]

        found = False

        for pair in pairs:
            if pair[0] == s_char:
                found = True
                if pair[1] != t_char:
                    return False

        if not found:
            for character in used:
                if character == t_char:
                    return False

            pairs.append([s_char, t_char])
            used.append(t_char)

    return True

def is_interleaved(s1: str, s2: str, s3: str) -> bool:
    """Determine whether s3 is an interleaving of s1 and s2."""

    if len(s1) + len(s2) != len(s3):
        return False

    for character in s1:
        if character not in "abcdefghijklmnopqrstuvwxyz":
            return False

    for character in s2:
        if character not in "abcdefghijklmnopqrstuvwxyz":
            return False

    for character in s3:
        if character not in "abcdefghijklmnopqrstuvwxyz":
            return False

    possible = []

    for i in range(len(s1) + 1):
        row = []
        for j in range(len(s2) + 1):
            row.append(False)
        possible.append(row)

    possible[0][0] = True

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if possible[i][j]:
                if i < len(s1) and s3[i + j] == s1[i]:
                    possible[i + 1][j] = True

                if j < len(s2) and s3[i + j] == s2[j]:
                    possible[i][j + 1] = True

    return possible[len(s1)][len(s2)]

def contiguous_length(nums: list[int]) -> int:
    """Find the longest contiguous subarray with equal 0s and 1s."""

    balance = 0
    max_length = 0
    first = []

    for i in range(2 * len(nums) + 1):
        first.append(-1)

    offset = len(nums)
    first[offset] = 0

    for i in range(len(nums)):        
        if nums[i] == 0:
            balance -= 1
        else:
            balance += 1

        position = balance + offset

        if first[position] == -1:
            first[position] = i + 1
        else:
            length = i + 1 - first[position]

            if length > max_length:
                max_length = length

    return max_length

print(contiguous_length([0, 1]))
print(contiguous_length([0, 1, 0]))
print(contiguous_length([0, 0, 1, 0, 0, 0, 1, 1]))
