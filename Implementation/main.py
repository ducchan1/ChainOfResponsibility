from Client import Client
from ChainBuilder import build_chain_of_responsibility_for_SGTIN

def main():
    # prepare the chain of responsibility (could be in a different class builder)
    root_handler = build_chain_of_responsibility_for_SGTIN()

    sgtin_str = raw_input("Please enter a sgtin value to be converted to human readable:")
    client = Client(root_handler)
    client.print_sgtin_to_human_readable(sgtin_str)


if __name__ == "__main__":
    main()
