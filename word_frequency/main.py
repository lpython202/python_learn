from collections import Counter


def main():
    path = input('Укажите путь до файла: ')
    counter = Counter()
    symbols = ',.!@-—:;()?/'
    translation_table = dict.fromkeys(map(ord, symbols), None)

    with open(path, 'r') as fp:
        for line in fp:
            line = line.lower()
            line = line.translate(translation_table)
            line_list = line.split()
            counter.update(line_list)
    print(counter.most_common(10))

if __name__ == '__main__':
    main()

