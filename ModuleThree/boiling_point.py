def max_and_min(point):
    margin = abs(point * 0.05)
    max = point + margin
    min = point - margin
    return (max, min)


def boiling_material(boiling_map, boiling_point):
    for key in boiling_map:
        max, min = max_and_min(boiling_map[key])
        if (min <= boiling_point <= max):
            return key
    return 'Unknown'


def seed():
    return {
        'Butane': -0.5,
        'Cooper': 1187,
        'Gold': 2660,
        'Mercury': 357,
        'Methane': -161.7,
        'Nonane': 150.8,
        'Silver': 2197,
        'Walter': 100
    }
  
print(boiling_material(seed(), -0.475))
