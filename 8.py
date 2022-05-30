import re


def parse_keys(x):
    keys = r'(?<=`)\w+(?=\s*::=)'
    return re.findall(keys, x)


def parse(x):
    result = {}
    keys = parse_keys(x)
    values = re.findall(r'\w+(?=\s*\\end)', x)
    for i in range(len(keys)):
        result[keys[i]] = values[i]
    return result


print(parse('\begin new `enma_140::= maxedi_22 \end, \begin new `veis ::= zaer\end, \begin new `usra ::= aresxe \end, \begin new `rage ::= rimaus \end,'))
