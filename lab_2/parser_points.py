def parser(file):
    f = open(file, "r")
    list_of_points = []
    for line in f:
        val = [map(float,(s.split(","))) for s in line.split(";")]
        list_of_points.append(val)
    return list_of_points