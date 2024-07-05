import tkinter as tk
from tkinter import ttk
from interaction import create_cell, interact_with_cell
from rgc import (
    MidgetRGC,
    ParasolRGC,
    BistratifiedRGC,
    SmallBistratifiedRGC,
    RetinalGanglionCell,
)


class RGCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RGC Simulator")

        self.cell_type_var = tk.StringVar(value="Parasol")
        self.receptive_field_size_var = tk.DoubleVar(value=2.0)
        self.center_intensity_var = tk.DoubleVar()
        self.surround_intensity_var = tk.DoubleVar()
        self.time_series = []

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Select RGC Type:").grid(
            column=0, row=0, padx=10, pady=10
        )
        cell_type_menu = ttk.Combobox(self.root, textvariable=self.cell_type_var)
        cell_type_menu["values"] = (
            "Parasol",
            "Midget",
            "Bistratified",
            "Small Bistratified",
        )
        cell_type_menu.grid(column=1, row=0, padx=10, pady=10)

        ttk.Label(self.root, text="Receptive Field Size (degrees):").grid(
            column=0, row=1, padx=10, pady=10
        )
        ttk.Entry(self.root, textvariable=self.receptive_field_size_var).grid(
            column=1, row=1, padx=10, pady=10
        )

        ttk.Button(self.root, text="Create Cell", command=self.create_cell).grid(
            column=0, row=2, columnspan=2, pady=10
        )

        self.info_label = ttk.Label(self.root, text="")
        self.info_label.grid(column=0, row=3, columnspan=2, pady=10)

        ttk.Label(self.root, text="Center Light Intensity (cd/m²):").grid(
            column=0, row=4, padx=10, pady=10
        )
        ttk.Entry(self.root, textvariable=self.center_intensity_var).grid(
            column=1, row=4, padx=10, pady=10
        )

        ttk.Label(self.root, text="Surround Light Intensity (cd/m²):").grid(
            column=0, row=5, padx=10, pady=10
        )
        ttk.Entry(self.root, textvariable=self.surround_intensity_var).grid(
            column=1, row=5, padx=10, pady=10
        )

        ttk.Button(self.root, text="Get Response", command=self.get_response).grid(
            column=0, row=6, columnspan=2, pady=10
        )

        self.response_label = ttk.Label(self.root, text="")
        self.response_label.grid(column=0, row=7, columnspan=2, pady=10)

    def create_cell(self):
        cell_type = self.cell_type_var.get()
        receptive_field_size = self.receptive_field_size_var.get()

        if cell_type == "Parasol":
            self.cell = ParasolRGC(receptive_field_size)
        elif cell_type == "Midget":
            self.cell = MidgetRGC(receptive_field_size)
        elif cell_type == "Bistratified":
            self.cell = BistratifiedRGC(receptive_field_size)
        else:
            self.cell = SmallBistratifiedRGC(receptive_field_size)

        self.info_label.config(text=self.cell.display_info())

    def get_response(self):
        center_intensity = self.center_intensity_var.get()
        surround_intensity = self.surround_intensity_var.get()
        self.time_series.append(center_intensity)
        if len(self.time_series) > 10:  # Keep the time series to a fixed length
            self.time_series.pop(0)
        response = self.cell.respond_to_light(
            center_intensity, surround_intensity, self.time_series
        )
        self.response_label.config(text=response)


if __name__ == "__main__":
    while True:
        mode = (
            input(
                "Select mode: 'text' for text interaction, 'gui' for graphical user interface: "
            )
            .strip()
            .lower()
        )
        if mode == "text":
            cell = create_cell()
            if cell:
                interact_with_cell(cell)
            else:
                print("Failed to create cell. Exiting.")
            break
        elif mode == "gui":
            root = tk.Tk()
            app = RGCApp(root)
            root.mainloop()
            break
        else:
            print("Invalid mode. Please enter 'text' or 'gui'.")
