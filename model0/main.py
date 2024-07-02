from interaction import create_cell, interact_with_cell


def main() -> None:
    print(
        """
        Retinal Ganglion Cell Simulator
        -------------------------------
        """
    )
    while True:
        cell = create_cell()
        if cell:
            result = interact_with_cell(cell)
            if result == 'exit':
                break


if __name__ == "__main__":
    main()
