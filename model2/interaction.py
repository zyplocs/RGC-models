from rgc import MidgetCell, ParasolCell, BistratifiedCell


def get_user_input():
    cell_type = input(
        "Enter cell type (midget/parasol/bistratified): ").strip().lower()
    location_x = float(input("Enter x location ").strip())
    location_y = float(input("Enter y location ").strip())
    stimulus_intensity = float(input("Enter stimulus intensity :").strip())
    return cell_type, (location_x, location_y), stimulus_intensity


def main():
    cell_type, location, stimulus_intensity = get_user_input()

    if cell_type == 'midget':
        cell = MidgetCell(location)
    elif cell_type == 'parasol':
        cell = ParasolCell(location)
    elif cell_type == 'bistratified':
        cell = BistratifiedCell(location)
    else:
        print("Invalid cell type")
        return

    response = cell.respond_to_stimulus(stimulus_intensity)
    print(f"The cell response is: {response}")

    cell.visualize_receptive_field()


if __name__ == "__main__":
    main()
