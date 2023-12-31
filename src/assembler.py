def first(in_file):
    with open("./input/" + in_file, "r") as file:
        lines = file.read().split('\n')
        location = 0
        for l in lines:
            sections = l.split()
