# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    hash_table = {}
    result = []

    for path in files:
        file_item = path.split('/')[-1]

        if file_item not in hash_table:
            hash_table[file_item] = [path]
        else:
            hash_table[file_item].append(path)

    for query in queries:
        if query in hash_table:
            results = hash_table[query]
            for path in results:
                result.append(path)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
