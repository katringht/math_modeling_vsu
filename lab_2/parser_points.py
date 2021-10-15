def parser():
    f = open('points1.txt', "r")
    list_of_points = []
    for line in f:
        val = [map(float,(s.split(","))) for s in line.split(";")]
        list_of_points.append(val)
    return list_of_points


def choose_charts(currentLen):
    print("Number of charts - {}.\nAccessible commands:\n'0' - all charts\n couple of numbers'12' - first and second charts\n '3' - just third chart".format(currentLen) )
    request = str(input("Enter a value: "))
    if len(request) == 1:
        if int(request) == 0:
            return 0, currentLen
        else:
            return int(request) - 1, int(request)
    elif len(request) == 2:
        if int(request[0]) < int(request[1]):
            return int(request[0]) - 1, int(request[1])
        else: 
            return int(request[1]) - 1, int(request[0])
    else: 
        print("Incorrect input")