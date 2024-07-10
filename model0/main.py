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
        self.root.configure(bg="gray")

        # Labels
        self.create_label(self.root, "Select RGC Type:", 0, 0)
        self.create_label(self.root, "Receptive Field Size (degrees):", 0, 1)
        self.create_label(self.root, "Center Light Intensity (cd/m²):", 0, 4)
        self.create_label(self.root, "Surround Light Intensity (cd/m²):", 0, 5)

        # Combobox
        cell_type_menu = ttk.Combobox(self.root, textvariable=self.cell_type_var)
        cell_type_menu["values"] = (
            "Parasol",
            "Midget",
            "Bistratified",
            "Small Bistratified",
        )
        cell_type_menu.grid(column=1, row=0, padx=10, pady=10)
        cell_type_menu.configure(background="white")

        # Entry Fields
        self.create_entry(self.root, self.receptive_field_size_var, 1, 1)
        self.create_entry(self.root, self.center_intensity_var, 1, 4)
        self.create_entry(self.root, self.surround_intensity_var, 1, 5)

        # Buttons
        self.create_button(self.root, "Create Cell", self.create_cell, 0, 2)
        self.create_button(self.root, "Get Response", self.get_response, 0, 6)

        # Info and Response Labels
        self.info_label = self.create_label(self.root, "", 0, 3, colspan=2)
        self.response_label = self.create_label(self.root, "", 0, 7, colspan=2)

    def create_label(self, parent, text, col, row, colspan=1):
        label = tk.Label(parent, text=text, bg="white", fg="black")
        label.grid(column=col, row=row, columnspan=colspan, padx=10, pady=10)
        return label

    def create_entry(self, parent, textvariable, col, row):
        entry = ttk.Entry(parent, textvariable=textvariable)
        entry.grid(column=col, row=row, padx=10, pady=10)
        return entry

    def create_button(self, parent, text, command, col, row):
        button = ttk.Button(parent, text=text, command=command)
        button.grid(column=col, row=row, columnspan=2, pady=10)
        return button

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
        if len(self.time_series) > 10:  # Keep the time series to fixed length
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
        if mode == "gui":
            root = tk.Tk()
            app = RGCApp(root)
            root.mainloop()
            break
        print("Invalid mode. Please enter 'text' or 'gui'.")
