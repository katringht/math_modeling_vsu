import matplotlib.pyplot as plt

def parser():
    x, y = [],[]
    f = open("points.txt", "r")

    for line in f:
        val = [map(int,(s.split(","))) for s in line.split(";")]
        x.append(val[0])
        y.append(val[1])
    return x, y

def show_chart(i, i1):
    x, y = parser()
    plt.scatter(x[i:i1], y[i:i1])
    plt.ylabel("y")
    plt.xlabel("x")
    plt.show()

def get_charts(currentLen):
    print("Number of charts - {}.\nAccessible commands:\n'0' - all charts\n couple of numbers'12' - first and second charts\n '3' - just third chart".format(currentLen) )
    request = str(input("Enter a value: "))
    if len(request) == 1:
        if int(request) == 0:
            show_chart(0, len(lenX))
        else:
            show_chart(int(request) - 1, int(request))
    elif len(request) == 2:
        show_chart(int(request[0]) - 1, int(request[1]))
    else: 
        print("Incorrect input")


lenX, _ = parser()
get_charts(len(lenX))
