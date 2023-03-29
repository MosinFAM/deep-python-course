def gen(file_name, lst):
    with open(file_name, 'r', encoding='utf-8') as infile:
        for line in infile:
            for word in lst:
                if word.lower() in line.lower().split(' '):
                    yield line
