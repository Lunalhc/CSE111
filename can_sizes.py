
import math



def main():
    radius = 6.83
    height = 10.16
    volumn = compute_volume(radius, height)
    surface =compute_surface(radius, height)
    efficiency = storage_efficiency(volumn, surface)



    print(f"#1 picnic {efficiency}")
    
    radius = 7.78
    height = 11.91
    volumn = compute_volume(radius, height)
    surface =compute_surface(radius, height)
    efficiency = storage_efficiency(volumn, surface)
    print(f"#1 tall {efficiency}")
    radius = 8.73
    height = 11.59
    volumn = compute_volume(radius, height)
    surface =compute_surface(radius, height)
    efficiency = storage_efficiency(volumn, surface)
    print(f"#2 tall {efficiency}")
    print(f"#2 {efficiency}")


def compute_surface(radius, height):

    surface = 2*math.pi*radius*(radius + height)
    return surface

def storage_efficiency(volumn, surface):

    efficiency = volumn/surface
    return efficiency

def compute_volume(radius, height):
    volumn = math.pi * radius**2*height
    return volumn

main()