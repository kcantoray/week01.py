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

    i = 0
    j = 0

    for k in range(len(s3)):
        if i < len(s1) and s3[k] == s1[i]:
            i += 1
        elif j < len(s2) and s3[k] == s2[j]:
            j += 1
        else:
            return False

    return True

print(is_interleaved("aabcc", "dbbca", "aadbbcbcac"))
print(is_interleaved("aabcc", "dbbca", "aadbbbaccc"))
print(is_interleaved("", "", ""))
