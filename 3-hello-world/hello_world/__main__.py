from .hello_world import greet_me  # type: ignore


def main() -> None:
    print(greet_me())


if __name__ == "__main__":
    main()
