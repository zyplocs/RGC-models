from typing import Optional
from rgc import MidgetRGC, ParasolRGC, BistratifiedRGC, RetinalGanglionCell


def create_cell() -> Optional[RetinalGanglionCell]:
    print("Welcome to RGC model0")
    print("You will be prompted to create a Retinal Ganglion Cell (RGC) by selecting its type and receptive field size.")
    print("Types of RGCs:")
    print("  - Midget: High spatial resolution, color sensitive")
    print("  - Parasol: High temporal resolution, luminance sensitive")
    print("  - Bistratified: Moderate spatial resolution, blue-yellow color contrast")

    cell_type: str = input(
        "Enter the type of RGC (Midget, Parasol, Bistratified):\n").strip()
    receptive_field_size: float = float(input(
        "Enter the receptive field size (in degrees of visual angle:\n").strip())

    if cell_type.lower() == 'midget':
        return MidgetRGC(receptive_field_size)
    elif cell_type.lower() == 'parasol':
        return ParasolRGC(receptive_field_size)
    elif cell_type.lower() == 'bistratified':
        return BistratifiedRGC(receptive_field_size)
    else:
        print("Invalid cell type. Check spelling and try again.")
        return create_cell


def interact_with_cell(cell: RetinalGanglionCell) -> None:
    print("\nCell Information:")
    print(cell.display_info())

    print("\nYou can now input light intensities to see how the cell responds.")
    print("Please enter the light intensity at the center and the surrounding area of the receptive field.")
    print("You will see the net response of the cell in spikes per second, as well as the temporal response which reflects how the response changes over time.")
    print("You can type 'back' to select another cell or 'exit' to quit the simulation.")

    time_series: list = []

    while True:
        light_intensity: str = input(
            "\nEnter center light intensity (in cd/m²) (or 'back' to select another cell, 'exit' to quit): ").strip()
        if light_intensity.lower() == 'exit':
            return 'exit'
        elif light_intensity.lower() == 'back':
            return 'back'
        surround_intensity: str = input(
            "Enter surround light intensity (in cd/m²): ").strip()

        try:
            light_intensity_value: float = float(light_intensity)
            surround_intensity_value: float = float(surround_intensity)
            time_series.append(light_intensity_value)
            if len(time_series) > 10:  # Keep the time series to a fixed length
                time_series.pop(0)
            response = cell.respond_to_light(light_intensity_value,
                                             surround_intensity_value,
                                             time_series)
            print(response)
            print("\nExplanation:")
            print("Net Response: This value indicates the overall firing rate of the cell in response to the given light intensities.")
            print("Temporal Response: This value shows how the firing rate has changed over the recent history of light intensities.")
        except ValueError:
            print("Please enter valid numbers for light intensities.")
