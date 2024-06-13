class RetinalGanglionCell:
    def __init__(self, cell_type: str, cell_size: str, dendritic_field_size: str) -> None:
        self.cell_type = cell_type
        self.cell_size = cell_size
        self.dendritic_field_size = dendritic_field_size

    def respond_to_light(self, light_intensity: int) -> str:
        response_intensity = 'medium' if light_intensity > 50 else 'low'
        return f"{self.cell_type} RGC response to {light_intensity} intensity: {response_intensity} response"


class MidgetRGC(RetinalGanglionCell):
    def __init__(self, cell_size: str, dendritic_field_size: str) -> None:
        super().__init__("Midget", cell_size, dendritic_field_size)


class ParasolRGC(RetinalGanglionCell):
    def __init__(self, cell_size: str, dendritic_field_size: str) -> None:
        super().__init__("Parasol", cell_size, dendritic_field_size)


class BistratifiedRGC(RetinalGanglionCell):
    def __init__(self, cell_size: str, dendritic_field_size: str) -> None:
        super().__init__("Bistratified", cell_size, dendritic_field_size)
