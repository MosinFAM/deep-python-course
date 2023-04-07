def gen(file, lst):
    with open(file, 'r', encoding='utf-8') if type(file) == str else file as infile:
        for line in infile:
            for word in lst:
                if word.lower() in line.lower().split(' '):
                    yield line
                    break
