import argparse  # pragma: no cover
import time

from . import BaseClass, base_function  # pragma: no cover


def main() -> None:  # pragma: no cover
    """
    The main function executes on commands:
    `python -m notmuch` and `$ notmuch `.

    This is your program's entry point.

    You can change this function to do whatever you want.
    Examples:
        * Run a test suite
        * Run a server
        * Do some other stuff
        * Run a command line application (Click, Typer, ArgParse)
        * List all available tasks
        * Run an application (Flask, FastAPI, Django, etc.)
    """
    parser = argparse.ArgumentParser(
        description="notmuch.",
        epilog="Enjoy the notmuch functionality!",
    )
    # This is required positional argument
    parser.add_argument(
        "max_range",
        type=int,
        help="range to count to",
        default=10,
    )
    # This is optional named argument
    parser.add_argument(
        "-d",
        "--delay",
        type=float,
        help="time to sleep between ticks",
        default=1.0,
        required=False,
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Optionally adds verbosity",
    )
    args = parser.parse_args()

    for i in range(args.max_range):
        if args.verbose:
            print("The current digit is {i}.")
        else:
            print(i)
        time.sleep(args.delay)

    if args.verbose:
        print("Executing main function")
    base = BaseClass()
    if args.verbose:
        print(base.base_method())
        print(base_function())
        print("End of main function")


if __name__ == "__main__":  # pragma: no cover
    main()
