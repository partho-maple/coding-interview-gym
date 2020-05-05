def airportConnections(airports, routes, startingAirport):
    airportGraph = createAirportGraph(airports, routes)
    unreachableAirportNodes = getUnreachableAirportNodes(airportGraph, airports, startingAirport)
    markUnreachableConnections(airportGraph, unreachableAirportNodes)
    return getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes)


def createAirportGraph(airports, routes):
    graph = {}
    for airport in airports:
        graph[airport] = AirportNode(airport)
    for route in routes:
        airport, connection = route
        graph[airport].connections.append(connection)
    return graph


def getUnreachableAirportNodes(airportGraph, airports, startingAirport):
    visitedAirports = {}
    dfsFromStartingAirport(airportGraph, startingAirport, visitedAirports)

    unreachableAirportNodes = []
    for airport in airports:
        if airport in visitedAirports:
            continue
        airportNode = airportGraph[airport]
        airportNode.isRechable = False
        unreachableAirportNodes.append(airportNode)
    return unreachableAirportNodes


def dfsFromStartingAirport(airportGraph, startingAirport, visitedAirports):
    if startingAirport in visitedAirports:
        return
    visitedAirports[startingAirport] = True
    connections = airportGraph[startingAirport].connections
    for connection in connections:
        dfsFromStartingAirport(airportGraph, connection, visitedAirports)


def markUnreachableConnections(airportGraph, unreachableAirportNodes):
    for airportNode in unreachableAirportNodes:
        airport = airportNode.airport
        unreachableCOnnections = []
        dfsAddUnreachableConnections(airportGraph, airport, unreachableCOnnections, {})
        airportNode.unreachableConnections = unreachableCOnnections


def dfsAddUnreachableConnections(airportGraph, airport, unreachableCOnnections, visitedAirports):
    if airportGraph[airport].isRechable:
        return
    if airport in visitedAirports:
        return
    visitedAirports[airport] = True
    unreachableCOnnections.append(airport)
    connections = airportGraph[airport].connections
    for connection in connections:
        dfsAddUnreachableConnections(airportGraph, connection, unreachableCOnnections, visitedAirports)


def getMinNumberOfNewConnections(airportGraph, unreachableAirportNodes):
    unreachableAirportNodes.sort(key=lambda airport: len(airport.unreachableConnections), reverse=True)

    numberOfNewConnections = 0
    for airportNode in unreachableAirportNodes:
        if airportNode.isRechable:
            continue
        numberOfNewConnections += 1
        for connection in airportNode.unreachableConnections:
            airportGraph[connection].isRechable = True
    return numberOfNewConnections


class AirportNode:
    def __init__(self, airport):
        self.airport = airport
        self.connections = []
        self.isRechable = True
        self.unreachableConnections = []
