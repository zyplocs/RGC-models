#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Function to convert a string to lowercase
void to_lowercase(char* str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower((unsigned char)str[i]);
    }
}

// Base struct for Retinal Ganglion Cell
typedef struct {
    char cell_type[20];
    float receptive_field_size;
    char response_characteristic[100];
    char* (*respond_to_light)(float light_intensity);
} RetinalGanglionCell;

// Specific struct for MidgetRGC
typedef struct {
    RetinalGanglionCell base;
} MidgetRGC;

// Specific struct for ParasolRGC
typedef struct {
    RetinalGanglionCell base;
} ParasolRGC;

// Specific struct for BistratifiedRGC
typedef struct {
    RetinalGanglionCell base;
} BistratifiedRGC;

// Response functions
char* midget_respond_to_light(float light_intensity) {
    static char response[100];
    float firing_rate = 10 + 0.5 * light_intensity; // Example response function
    sprintf(response, "Midget RGC response to light intensity %.2f cd/m²: Firing rate %.2f Hz", light_intensity, firing_rate);
    return response;
}

char* parasol_respond_to_light(float light_intensity) {
    static char response[100];
    float firing_rate = 5 + 0.8 * light_intensity; // Example response function
    sprintf(response, "Parasol RGC response to light intensity %.2f cd/m²: Firing rate %.2f Hz", light_intensity, firing_rate);
    return response;
}

char* bistratified_respond_to_light(float light_intensity) {
    static char response[100];
    float firing_rate = 8 + 0.6 * light_intensity; // Example response function
    sprintf(response, "Bistratified RGC response to light intensity %.2f cd/m²: Firing rate %.2f Hz", light_intensity, firing_rate);
    return response;
}

// Cell creation functions
MidgetRGC* create_midget_rgc(float receptive_field_size) {
    MidgetRGC* cell = (MidgetRGC*)malloc(sizeof(MidgetRGC));
    strcpy(cell->base.cell_type, "Midget");
    cell->base.receptive_field_size = receptive_field_size;
    strcpy(cell->base.response_characteristic, "High spatial resolution, color sensitive");
    cell->base.respond_to_light = midget_respond_to_light;
    return cell;
}

ParasolRGC* create_parasol_rgc(float receptive_field_size) {
    ParasolRGC* cell = (ParasolRGC*)malloc(sizeof(ParasolRGC));
    strcpy(cell->base.cell_type, "Parasol");
    cell->base.receptive_field_size = receptive_field_size;
    strcpy(cell->base.response_characteristic, "High temporal resolution, luminance sensitive");
    cell->base.respond_to_light = parasol_respond_to_light;
    return cell;
}

BistratifiedRGC* create_bistratified_rgc(float receptive_field_size) {
    BistratifiedRGC* cell = (BistratifiedRGC*)malloc(sizeof(BistratifiedRGC));
    strcpy(cell->base.cell_type, "Bistratified");
    cell->base.receptive_field_size = receptive_field_size;
    strcpy(cell->base.response_characteristic, "Moderate spatial resolution, blue-yellow color contrast");
    cell->base.respond_to_light = bistratified_respond_to_light;
    return cell;
}

// Function to create a cell based on user input
RetinalGanglionCell* create_cell() {
    char cell_type[20];
    float receptive_field_size;

    printf("Enter the type of RGC (Midget, Parasol, Bistratified): ");
    scanf("%19s", cell_type);
    to_lowercase(cell_type); // Convert user input to lowercase

    printf("Enter the receptive field size in degrees of visual angle: ");
    scanf("%f", &receptive_field_size);

    if (strcmp(cell_type, "midget") == 0) {
        return (RetinalGanglionCell*)create_midget_rgc(receptive_field_size);
    } else if (strcmp(cell_type, "parasol") == 0) {
        return (RetinalGanglionCell*)create_parasol_rgc(receptive_field_size);
    } else if (strcmp(cell_type, "bistratified") == 0) {
        return (RetinalGanglionCell*)create_bistratified_rgc(receptive_field_size);
    } else {
        printf("Invalid cell type.\n");
        return NULL;
    }
}

// Function to interact with a cell
void interact_with_cell(RetinalGanglionCell* cell) {
    printf("\nCell Information:\n");
    printf("Type: %s, Receptive Field Size: %.2f degrees, Response Characteristic: %s\n", cell->cell_type, cell->receptive_field_size, cell->response_characteristic);

    while (1) {
        char light_intensity_str[10];
        float light_intensity;

        printf("\nEnter light intensity in cd/m² (or 'back' to select another cell, 'exit' to quit): ");
        scanf("%9s", light_intensity_str);

        if (strcmp(light_intensity_str, "exit") == 0) {
            exit(0);  // Exit the program
        } else if (strcmp(light_intensity_str, "back") == 0) {
            break;  // Go back to cell selection
        }

        light_intensity = atof(light_intensity_str);
        printf("%s\n", cell->respond_to_light(light_intensity));
    }
}

// Main function
int main() {
    printf("Retinal Ganglion Cell Simulator\n");

    while (1) {
        RetinalGanglionCell* cell = create_cell();
        if (cell) {
            interact_with_cell(cell);
            free(cell);
        }
    }

    return 0;
}
