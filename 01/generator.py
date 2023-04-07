def gen(file, lst):
    if type(file) == str:
        with open(file, 'r', encoding='utf-8') as infile:
            for line in infile:
                used_lines = []
                for word in lst:
                    if word.lower() in line.lower().split(' '):
                        if line not in used_lines:
                            used_lines.append(line)
                            yield line
                        else:
                            pass
    else:
        for line in file:
            used_lines = []
            for word in lst:
                if word.lower() in line.lower().split(' '):
                    if line not in used_lines:
                        used_lines.append(line)
                        yield line
                    else:
                        pass
