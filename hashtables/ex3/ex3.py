def intersection(arrays):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    results = []

    for array in arrays:
        for num in array:
            if num not in hash_table:
                hash_table[num] = 1
            else:
                hash_table[num] += 1

    pairs = hash_table.items()
    
    for key, value in pairs:
       if value == len(arrays):
           results.append(key)

    # print([key for key, value in hash_table.items() if value == len(arrays)])
    # return only the items that have an occurence equal to the length of the arrays
    return results

print(intersection([[1,2,4,5,6,7], [1,4,7,6],[1,9,0,7]]))


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
