from typing import Optional
from rgc import MidgetRGC, ParasolRGC, BistratifiedRGC, RetinalGanglionCell

def create_cell() -> Optional[RetinalGanglionCell]:
    cell_type: str = input("Enter the type of RGC (Midget, Parasol, Bistratified):\n").strip()
    receptive_field_size: float = float(input("Enter the receptive field size:\n").strip())

    if cell_type.lower() == 'midget':
        return MidgetRGC(receptive_field_size)
    elif cell_type.lower() == 'parasol':
        return ParasolRGC(receptive_field_size)
    elif cell_type.lower() == 'bistratified':
        return BistratifiedRGC(receptive_field_size)
    else:
        print("Invalid cell type. Check spelling and try again.")
        return None

def interact_with_cell(cell: RetinalGanglionCell) -> None:
    print("\nCell Information:")
    print(cell.display_info())

    while True:
        light_intensity: str = input("\nEnter light intensity (or 'exit' to quit): ").strip()
        if light_intensity.lower() == 'exit':
            break
        try:
            light_intensity_value: float = float(light_intensity)
            print(cell.respond_to_light(light_intensity_value))
        except ValueError:
            print("Please enter a valid number for light intensity.")
