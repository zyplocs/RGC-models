from interaction import create_cell, interact_with_cell


def main() -> None:
    print(
        """
        Retinal Ganglion Cell Simulator
        -------------------------------
        """)
    cell = create_cell()
    if cell:
        interact_with_cell(cell)


if __name__ == "__main__":
    main()
