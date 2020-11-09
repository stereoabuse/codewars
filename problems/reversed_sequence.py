# Reversed sequence
# 8 kyu


def reverse_seq(n):
    return sorted([n for n in range(1,n+1)], reverse=True)