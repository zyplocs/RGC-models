import numpy as np
from typing import List


class RetinalGanglionCell:
    def __init__(self, cell_type, receptive_field_size, response_characteristic):
        self.cell_type: str = cell_type
        self.receptive_field_size: float = receptive_field_size
        self.response_characteristic: str = response_characteristic
        self.spontaneous_firing_rate: float = 5.0  # Ex. baseline firing rate

    def respond_to_light(
        self,
        light_intensity,
        surround_intensity,
        time_series,
    ):
        raise NotImplementedError("This method should be overridden by subclasses")

    def display_info(self):
        return (
            f" - Type: {self.cell_type}"
            f"\n - Receptive Field Size: {self.receptive_field_size}"
            f"\n - Response Characteristic: {self.response_characteristic}"
        )


class MidgetRGC(RetinalGanglionCell):
    def __init__(self, receptive_field_size):
        super().__init__(
            "Midget", receptive_field_size, "High spatial resolution, color sensitive"
        )

    def respond_to_light(
        self,
        light_intensity,
        surround_intensity,
        time_series,
    ):
        center_weight = 0.6
        surround_weight = -0.4
        center_response = center_weight * light_intensity
        surround_response = surround_weight * surround_intensity
        net_response = (
            self.spontaneous_firing_rate + center_response + surround_response
        )
        return f"Midget RGC net reponse: {net_response:.2f} (spikes/s), Temporal response: {self.temporal_response(time_series):.2f} (spikes/s)"

    def temporal_response(self, time_series):
        if not time_series:
            return 0.0
        kernel = np.ones(10) / 10  # Simple moving average
        response = np.convolve(time_series, kernel, mode="valid")
        return float(response[-1]) if response.size > 0 else 0.0


class ParasolRGC(RetinalGanglionCell):
    def __init__(self, receptive_field_size):
        super().__init__(
            "Parasol",
            receptive_field_size,
            "High temporal resolution, luminance sensitive",
        )

    def respond_to_light(
        self,
        light_intensity,
        surround_intensity,
        time_series,
    ):
        center_weight = 0.8
        surround_weight = -0.2
        center_response = center_weight * light_intensity
        surround_response = surround_weight * surround_intensity
        net_response = (
            self.spontaneous_firing_rate + center_response + surround_response
        )
        return f"Parasol RGC net response: {net_response:.2f} (spikes/s), Temporal response: {self.temporal_response(time_series):.2f} (spikes/s)"

    def temporal_response(self, time_series):
        if not time_series:
            return 0.0
        kernel = np.exp(-np.arange(10) / 10)  # Exponential decay
        response = np.convolve(time_series, kernel, mode="valid")
        return float(response[-1]) if response.size > 0 else 0.0


class BistratifiedRGC(RetinalGanglionCell):
    def __init__(self, receptive_field_size):
        super().__init__(
            "Bistratified",
            receptive_field_size,
            "Moderate spatial resolution, blue-yellow color contrast",
        )

    def respond_to_light(
        self,
        light_intensity,
        surround_intensity,
        time_series,
    ):
        center_weight = 0.5
        surround_weight = -0.5
        center_response = center_weight * light_intensity
        surround_response = surround_weight * surround_intensity
        net_response = (
            self.spontaneous_firing_rate + center_response + surround_response
        )
        return f"Bistratified RGC net response: {net_response:.2f} (spikes/s), Temporal response: {self.temporal_response(time_series):.2f} (spikes/s)"

    def temporal_response(self, time_series):
        if not time_series:
            return 0.0
        kernel = np.cos(np.linspace(0, np.pi, 10))
        kernel = np.abs(kernel)
        response = np.convolve(time_series, kernel, mode="valid")
        return float(response[-1]) if response.size > 0 else 0.0
