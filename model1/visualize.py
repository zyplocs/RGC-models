import matplotlib.pyplot as plt


def plot_response(light_intensity: int, response: str) -> None:
    plt.figure()
    plt.bar(['Reponse'], [light_intensity], color='yellow')
    plt.title(f'Response Level: {response}')
    plt.ylabel('Intensity')
    plt.show
