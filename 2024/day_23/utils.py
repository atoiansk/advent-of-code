def parse_input(file_name):
    file = open(file_name, "r")
    lines = file.readlines()

    routes = {}

    for line in lines:
        connections = line.strip('\n').split('-')
        connections.sort()
        connection1, connection2 = connections

        if connection1 not in routes:
            routes[connection1] = set()
        routes[connection1].add(connection2)

        if connection2 not in routes:
            routes[connection2] = set()
        routes[connection2].add(connection1)

    return routes
