class RetinalGanglionCell:
    def __init__(self, cell_type: str,
                 receptive_field_size: float,
                 response_characteristic: str) -> None:
        self.cell_type: str = cell_type
        self.receptive_field_size: float = receptive_field_size
        self.response_characteristic: str = response_characteristic

    def respond_to_light(self,
                         light_intensity: float) -> str:
        raise NotImplementedError(
            "This method should be overridden by subclasses")

    def display_info(self) -> str:
        return f"Type: {self.cell_type}, Receptive Field Size: {self.receptive_field_size}, Response Characteristic: {self.response_characteristic}"


class MidgetRGC(RetinalGanglionCell):
    def __init__(self,
                 receptive_field_size: float) -> None:
        super().__init__('Midget', receptive_field_size, 'High spatial resolution, color sensitive')

    def respond_to_light(self,
                         light_intensity: float) -> str:
        return f"Midget RGC response to light intensity {light_intensity}: Moderate to high firing rate"


class ParasolRGC(RetinalGanglionCell):
    def __init__(self,
                 receptive_field_size: float) -> None:
        super().__init__('Parasol', receptive_field_size, 'High temporal resolution, luminance sensitive')

    def respond_to_light(self,
                         light_intensity: float) -> str:
        return f"Parasol RGC response to light intensity {light_intensity}: Rapid, transient firing rate"


class BistratifiedRGC(RetinalGanglionCell):
    def __init__(self,
                 receptive_field_size: float) -> None:
        super().__init__('Bistratified', receptive_field_size, 'Moderate spatial resolution, blue-yellow color contrast')

    def respond_to_light(self,
                         light_intensity: float) -> str:
        return f"Bistratified RGC response to light intensity {light_intensity}: Specific response to blue-yellow contrast"