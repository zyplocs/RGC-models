import numpy as np

class RetinalGanglionCell:
    def __init__(self, cell_type, receptive_field_size, location):
        self.cell_type = cell_type
        self.receptive_field_size = receptive_field_size
        self.location = location
        self.spontaneous_firing_rate = np.random.poisson(5)  # spikes/second

    def respond_to_stimulus(self, stimulus_intensity):
        # Simple linear response model
        response = self.spontaneous_firing_rate + stimulus_intensity * self.receptive_field_size
        return response

    def visualize_receptive_field(self):
        import matplotlib.pyplot as plt
        # Create a simple visualization of the receptive field
        fig, ax = plt.subplots()
        circle = plt.Circle(self.location, self.receptive_field_size, color='b', fill=False)
        ax.add_artist(circle)
        ax.set_xlim(self.location[0] - 10, self.location[0] + 10)
        ax.set_ylim(self.location[1] - 10, self.location[1] + 10)
        ax.set_aspect('equal', 'box')
        plt.title(f'{self.cell_type.capitalize()} Cell Receptive Field')
        plt.show()


class MidgetCell(RetinalGanglionCell):
    def __init__(self, location):
        super().__init__('midget', 1.0, location)


class ParasolCell(RetinalGanglionCell):
    def __init__(self, location):
        super().__init__('parasol', 2.0, location)


class BistratifiedCell(RetinalGanglionCell):
    def __init__(self, location):
        super()__init__('bistratified', 1.5, location)
