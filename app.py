# ---------------------------------------------------------
# Hyderabad Traffic Navigation - Streamlit UI
# ---------------------------------------------------------

import streamlit as st
import matplotlib.pyplot as plt

from src.road_network import ROAD_NETWORK
from src.dijkstra import dijkstra
from src.traffic_mapper import TRAFFIC_CONDITIONS


# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Hyderabad Traffic Navigator",
    page_icon="🚗",
    layout="wide"
)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.title("🚗 Hyderabad Traffic Navigator")

st.write(
    "Traffic-aware route optimization using "
    "vehicle detection, traffic classification "
    "and Dijkstra's algorithm."
)


# ---------------------------------------------------------
# Available locations
# ---------------------------------------------------------

locations = list(ROAD_NETWORK.keys())


# ---------------------------------------------------------
# Source and Destination
# ---------------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    source = st.selectbox(
        "📍 Source",
        locations
    )

with col2:

    destination = st.selectbox(
        "🏁 Destination",
        locations,
        index=min(1, len(locations) - 1)
    )


# ---------------------------------------------------------
# Find Route
# ---------------------------------------------------------

find_route = st.button(
    "🔎 Find Best Route",
    use_container_width=True
)


# ---------------------------------------------------------
# Route Calculation
# ---------------------------------------------------------

if find_route:

    if source == destination:

        st.warning(
            "Source and destination must be different."
        )

    else:

        cost, route = dijkstra(
            ROAD_NETWORK,
            source,
            destination,
            TRAFFIC_CONDITIONS
        )

        if route:

            # -------------------------------------------------
            # Calculate physical distance
            # -------------------------------------------------

            distance = 0

            for i in range(len(route) - 1):

                current = route[i]
                next_location = route[i + 1]

                for neighbour, road_distance in ROAD_NETWORK[current]:

                    if neighbour == next_location:

                        distance += road_distance
                        break

            # -------------------------------------------------
            # Route Result
            # -------------------------------------------------

            st.success("Best route found!")

            st.subheader("🛣️ Recommended Route")

            st.write(
                " → ".join(route)
            )

            # -------------------------------------------------
            # Metrics
            # -------------------------------------------------

            metric1, metric2 = st.columns(2)

            with metric1:

                st.metric(
                    "Distance",
                    f"{distance} km"
                )

            with metric2:

                st.metric(
                    "Traffic-Adjusted Cost",
                    cost
                )

        else:

            st.error(
                "No route could be found."
            )


# ---------------------------------------------------------
# Traffic Legend
# ---------------------------------------------------------

st.subheader("🚦 Traffic Conditions")

legend1, legend2, legend3 = st.columns(3)

with legend1:

    st.success(
        "🟢 Low Traffic"
    )

with legend2:

    st.warning(
        "🟡 Medium Traffic"
    )

with legend3:

    st.error(
        "🔴 High Traffic"
    )


# ---------------------------------------------------------
# Road Network Visualization
# ---------------------------------------------------------

st.subheader("🗺️ Hyderabad Prototype Road Network")


# ---------------------------------------------------------
# Approximate positions of locations
# ---------------------------------------------------------
# These positions are only for visualization.
# They do NOT represent exact GPS coordinates.
# ---------------------------------------------------------

POSITIONS = {
    "Secunderabad": (1, 8),
    "Begumpet": (3, 7),
    "Ameerpet": (4, 6),

    "Punjagutta": (5, 5.5),
    "Madhura Nagar": (3.5, 5),

    "Banjara Hills": (6, 4.5),
    "Yousufguda": (4.5, 4.5),

    "Jubilee Hills": (6, 3.5),
    "Mehdipatnam": (5, 2.5),

    "Madhapur": (8, 3),

    # Moved below the Mehdipatnam-Gachibowli road
    "Durgam Cheruvu": (9, 1.8),

    "HITEC City": (10, 3),

    # Moved below the Mehdipatnam-Gachibowli road
    "Kondapur": (11, 1.8),

    "Shilpa Layout": (11, 3.5),
    "Gachibowli": (12.5, 2.5)
}

# ---------------------------------------------------------
# Determine selected route
# ---------------------------------------------------------

selected_route = []

if find_route and source != destination:

    cost, selected_route = dijkstra(
        ROAD_NETWORK,
        source,
        destination,
        TRAFFIC_CONDITIONS
    )


# ---------------------------------------------------------
# Draw network
# ---------------------------------------------------------

fig, ax = plt.subplots(figsize=(14, 9))


# ---------------------------------------------------------
# Draw road segments
# ---------------------------------------------------------

drawn_edges = set()


for location, roads in ROAD_NETWORK.items():

    for neighbour, distance in roads:

        edge = tuple(
            sorted(
                [location, neighbour]
            )
        )

        if edge in drawn_edges:
            continue

        drawn_edges.add(edge)

        x1, y1 = POSITIONS[location]
        x2, y2 = POSITIONS[neighbour]

        traffic_level = TRAFFIC_CONDITIONS.get(
            (location, neighbour),
            "Medium"
        )

        # Traffic colors
        if traffic_level == "Low":

            road_color = "green"

        elif traffic_level == "High":

            road_color = "red"

        else:

            road_color = "orange"

        # -------------------------------------------------
        # Highlight selected route
        # -------------------------------------------------

        is_route = False

        for i in range(len(selected_route) - 1):

            if (
                selected_route[i] == location
                and
                selected_route[i + 1] == neighbour
            ) or (
                selected_route[i] == neighbour
                and
                selected_route[i + 1] == location
            ):

                is_route = True
                break

        if is_route:

            ax.plot(
                [x1, x2],
                [y1, y2],
                color="blue",
                linewidth=5,
                zorder=2
            )

        else:

            ax.plot(
                [x1, x2],
                [y1, y2],
                color=road_color,
                linewidth=2,
                alpha=0.7,
                zorder=1
            )


# ---------------------------------------------------------
# Draw locations
# ---------------------------------------------------------

for location, (x, y) in POSITIONS.items():

    if location == source:

        ax.scatter(
            x,
            y,
            s=180,
            color="blue",
            edgecolors="black",
            zorder=5
        )

    elif location == destination:

        ax.scatter(
            x,
            y,
            s=180,
            color="purple",
            edgecolors="black",
            zorder=5
        )

    else:

        ax.scatter(
            x,
            y,
            s=80,
            color="white",
            edgecolors="black",
            zorder=4
        )

    ax.text(
        x,
        y + 0.18,
        location,
        fontsize=9,
        ha="center"
    )


# ---------------------------------------------------------
# Chart formatting
# ---------------------------------------------------------

ax.set_title(
    "Hyderabad Prototype Road Network",
    fontsize=15
)

ax.set_xlim(0, 14)
ax.set_ylim(1, 9)

ax.axis("off")

st.pyplot(
    fig,
    use_container_width=True
)


# ---------------------------------------------------------
# Explanation
# ---------------------------------------------------------

st.info(
    "Traffic conditions are derived from vehicle-count "
    "observations. Since the dataset does not contain "
    "GPS-based road labels, the road traffic values are "
    "used as prototype conditions for demonstrating "
    "traffic-aware route optimization."
)