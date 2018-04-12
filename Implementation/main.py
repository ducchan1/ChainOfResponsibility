from Client import Client


def main():
    sgtin_str = raw_input("Please enter a sgtin value to be converted to human readable:")
    client = Client()
    client.print_sgtin_to_human_readable(sgtin_str)


if __name__ == "__main__":
    main()
