from elastic_funcs import post_to_index


def main():
    post_to_index('../test.json', 'tindex')


if __name__ == "__main__":
    main()
