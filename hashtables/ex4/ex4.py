def has_negatives(a):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    result = []

    for num in a:
        hash_table[num] = 1
        if num != 0 and num * -1 in hash_table:
            result.append(abs(num))

    return result

   
print(has_negatives([1, 2, 3]))

# if __name__ == "__main__":
#     print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
