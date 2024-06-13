from rgc_types import MidgetRGC, ParasolRGC, BistratifiedRGC
from visualize import plot_response


def main() -> None:
    cell_type = input("Enter the type of RGC (Midget, Parasol, Bistratified): ")
    cell_size = input("Enter cell size (small, medium, large): ")
    dendritic_field_size = input("Enter dendritic field size (small, medium, large): ")
    light_intensity = int(input("Enter light intensity (0-100): "))

    cell = None
    if cell_type.lower() == "midget":
        cell = MidgetRGC(cell_size, dendritic_field_size)
    elif cell_type.lower() == "parasol":
        cell = ParasolRGC(cell_size, dendritic_field_size)
    elif cell_type.lower() == "bistratified":
        cell = BistratifiedRGC(cell_size, dendritic_field_size)
    else:
        print("Invalid RGC type entered.")
        return

    response = cell.respond_to_light(light_intensity)
    print(response)
    plot_response(light_intensity, response.split(': ')[-1])


if __name__ == "__main__":
    main()
