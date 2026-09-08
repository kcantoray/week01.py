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

print(are_isomorphic("a", "a"))
print(are_isomorphic("ab", "aa"))
