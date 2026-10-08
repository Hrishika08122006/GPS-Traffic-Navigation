# ---------------------------------------------------------
# Traffic-Aware Dijkstra Algorithm
# ---------------------------------------------------------

import heapq

from src.road_network import ROAD_NETWORK
from src.traffic_mapper import TRAFFIC_CONDITIONS


# ---------------------------------------------------------
# Traffic weights
# ---------------------------------------------------------

TRAFFIC_WEIGHTS = {
    "Low": 1,
    "Medium": 2,
    "High": 4
}


# ---------------------------------------------------------
# Calculate traffic-adjusted road cost
# ---------------------------------------------------------

def calculate_road_cost(distance, traffic_level):

    traffic_weight = TRAFFIC_WEIGHTS[traffic_level]

    return distance * traffic_weight


# ---------------------------------------------------------
# Dijkstra Algorithm
# ---------------------------------------------------------

def dijkstra(
    graph,
    source,
    destination,
    traffic_conditions
):

    priority_queue = [
        (0, source, [source])
    ]

    visited_cost = {}

    while priority_queue:

        current_cost, current_location, path = heapq.heappop(
            priority_queue
        )

        # Skip if this location was already reached
        # with a lower cost.
        if current_location in visited_cost:
            continue

        visited_cost[current_location] = current_cost

        # Destination reached
        if current_location == destination:

            return current_cost, path

        # Explore neighbouring roads
        for neighbour, distance in graph[current_location]:

            road_key = (
                current_location,
                neighbour
            )

            traffic_level = traffic_conditions.get(
                road_key,
                "Medium"
            )

            road_cost = calculate_road_cost(
                distance,
                traffic_level
            )

            new_cost = current_cost + road_cost

            new_path = path + [neighbour]

            heapq.heappush(
                priority_queue,
                (
                    new_cost,
                    neighbour,
                    new_path
                )
            )

    return None, []


# ---------------------------------------------------------
# Test Dijkstra
# ---------------------------------------------------------

if __name__ == "__main__":

    # -----------------------------------------------------
    # Get available locations
    # -----------------------------------------------------

    locations = list(ROAD_NETWORK.keys())

    print("\nTraffic-Aware GPS Navigation")
    print("-" * 60)

    print("\nAvailable Locations:")

    for index, location in enumerate(locations, start=1):

        print(
            f"{index}. {location}"
        )

    # -----------------------------------------------------
    # Select source
    # -----------------------------------------------------

    source_number = int(
        input("\nEnter source number: ")
    )

    source = locations[source_number - 1]

    # -----------------------------------------------------
    # Select destination
    # -----------------------------------------------------

    destination_number = int(
        input("Enter destination number: ")
    )

    destination = locations[destination_number - 1]

    # -----------------------------------------------------
    # Run Dijkstra
    # -----------------------------------------------------

    cost, route = dijkstra(
        ROAD_NETWORK,
        source,
        destination,
        TRAFFIC_CONDITIONS
    )

    # -----------------------------------------------------
    # Display result
    # -----------------------------------------------------

    print("\n" + "-" * 60)

    print("Source:", source)

    print("Destination:", destination)

    if route:

        print("\nRecommended Route:")

        print(
            " -> ".join(route)
        )

        # Calculate physical distance
        distance = 0

        for i in range(len(route) - 1):

            current = route[i]
            next_location = route[i + 1]

            for neighbour, road_distance in ROAD_NETWORK[current]:

                if neighbour == next_location:

                    distance += road_distance
                    break

        print(
            "\nDistance:",
            distance,
            "km"
        )

        print(
            "Traffic-Adjusted Cost:",
            cost
        )

    else:

        print("\nNo route found.")