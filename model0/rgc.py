import numpy as np
from typing import List


class RetinalGanglionCell:
    def __init__(self,
                 cell_type: str,
                 receptive_field_size: float,
                 response_characteristic: str
                 ) -> None:
        self.cell_type: str = cell_type
        self.receptive_field_size: float = receptive_field_size
        self.response_characteristic: str = response_characteristic
        self.spontaneous_firing_rate: float = 5.0

    def respond_to_light(self,
                         light_intensity: float,
                         surround_intensity: float,
                         time_series: List[float]
                         ) -> str:
        raise NotImplementedError(
            "This method should be overridden by subclasses"
        )

    def display_info(self) -> str:
        return (f"Type: {self.cell_type}, "
                f"Receptive Field Size: {self.receptive_field_size}, "
                f"Response Characteristic: {self.response_characteristic}"
                )


class MidgetRGC(RetinalGanglionCell):
    def __init__(self,
                 receptive_field_size: float
                 ) -> None:
        super().__init__('Midget',
                         receptive_field_size,
                         'High spatial resolution, color sensitive'
                         )

    def respond_to_light(self,
                         light_intensity: float,
                         surround_intensity: float,
                         time_series: List[float]
                         ) -> str:
        center_weight: float = 0.6
        surround_weight: float = -0.4
        center_response: float = center_weight * light_intensity
        surround_response: float = surround_weight * surround_intensity
        net_response: float = self.spontaneous_firing_rate + center_response + surround_response
        return f"Midget RGC net reponse: {net_response}, Temporal response: {self.temporal_response(time_series)}"

    def temporal_response(self,
                          time_series: List[float]
                          ) -> float:
        response: np.ndarray = np.convolve(time_series,
                                           np.ones(10)/10,
                                           mode='valid'
                                           )
        return float(response[-1]) if response.size > 0 else 0.0


class ParasolRGC(RetinalGanglionCell):
    def __init__(self,
                 receptive_field_size: float
                 ) -> None:
        super().__init__('Parasol', receptive_field_size, 'High temporal resolution, luminance sensitive')

    def respond_to_light(self,
                         light_intensity: float
                         ) -> str:
        return f"Parasol RGC response to light intensity {light_intensity}: Rapid, transient firing rate"


class BistratifiedRGC(RetinalGanglionCell):
    def __init__(self,
                 receptive_field_size: float
                 ) -> None:
        super().__init__('Bistratified',
                         receptive_field_size,
                         'Moderate spatial resolution, blue-yellow color contrast'
                         )

    def respond_to_light(self,
                         light_intensity: float
                         ) -> str:
        return f"Bistratified RGC response to light intensity {light_intensity}: Specific response to blue-yellow contrast"
