"""Interaction with the text comparer from the command line."""
import argparse
import sys

from semtextsim.semtextsim import Comparer


def main():
    """Console script for semtextsim."""
    parser = argparse.ArgumentParser()
    parser.add_argument("strings", nargs="*")
    args = parser.parse_args()

    print("Arguments: " + str(args._))
    print(Comparer())
    return 0


if __name__ == "__main__":
    sys.exit(main())
