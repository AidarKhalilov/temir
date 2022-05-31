import tabulate


def delete_double_column(x):
    for i in range(len(x[0])):
        current = [x[element][i] for element in range(len(x))]
        for j in range(i + 1, len(x[0])):
            buffer = [x[element][j] for element in range(len(x))]
            if buffer == current:
                return delete_double_column(delete_column(x, j))
    return x


def delete_column(x, j):
    for i in range(len(x)):
        x[i].pop(j)
    return x

def delete_empty_columns(x):
    for i in range(len(x[0])):
        if x[0][i] is None:
            return delete_column(x, i)
    return x


def delete_empty_rows(x):
    for i in range(len(x)):
        if x[i][0] is None:
            x.pop(i)
            return delete_empty_rows(x)
    return x


def transform(x):
    for i in range(len(x)):
        for j in range(len(x[i])):
            match j:
                case 0:
                    x[i][j] = '.'.join(x[i][j].split('.')[::-1])
                case 1:
                    x[i][j] = ' '.join(x[i][j].split(' ')[::-1])
                case 2:
                    if x[i][j] == 'false':
                        x[i][j] = 'Не выполнено'
                    else:
                        x[i][j] = 'Выполнено'
                case 3:
                    x[i][j] = x[i][j].split('@')[1]
    return x


def main(x):
    x = delete_double_column(x)
    x = delete_empty_columns(x)
    x = delete_empty_rows(x)
    x = transform(x)
    return x

    
print(tabulate.tabulate(main(
    [
        [None, None, None, None, None, None, None],
        [None, '00.09.17', 'Силберг Кирилл', 'true', None, 'silberg93@yahoo.com', 'silberg93@yahoo.com'],
        [None, '02.03.20', 'Новелак Валерий', 'true', None, 'novelak14@mail.ru', 'novelak14@mail.ru'],
        [None, '02.04.19', 'Мумалин Сергей', 'false', None, 'mumalin92@mail.ru', 'mumalin92@mail.ru']
    ]
)))