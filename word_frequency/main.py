def main():
    path = input('Укажите путь до файла: ')
    with open(path, 'r') as fp:
        for line in fp:
            print(line)

if __name__ == '__main__':
    main()
