# ---------------------------------------------------------
# Traffic Mapper
# ---------------------------------------------------------
# Uses classified traffic observations to create prototype
# traffic conditions for our Hyderabad road network.
#
# IMPORTANT:
# The dataset does not contain GPS/road-location labels.
# Therefore, the traffic levels are used as prototype
# traffic conditions for demonstrating route optimization.
# ---------------------------------------------------------

import pandas as pd
from pathlib import Path
from collections import Counter


# ---------------------------------------------------------
# Files
# ---------------------------------------------------------

INPUT_FILE = Path("outputs/traffic_classification.csv")


# ---------------------------------------------------------
# Read classified traffic data
# ---------------------------------------------------------

df = pd.read_csv(INPUT_FILE)


print("\nTraffic Data Summary")
print("-" * 40)

print(
    "Low traffic observations:",
    (df["traffic_level"] == "Low").sum()
)

print(
    "Medium traffic observations:",
    (df["traffic_level"] == "Medium").sum()
)

print(
    "High traffic observations:",
    (df["traffic_level"] == "High").sum()
)


# ---------------------------------------------------------
# Road segments in our prototype network
# ---------------------------------------------------------

ROAD_SEGMENTS = [

    ("Secunderabad", "Begumpet"),
    ("Begumpet", "Ameerpet"),

    ("Ameerpet", "Punjagutta"),
    ("Ameerpet", "Madhura Nagar"),

    ("Punjagutta", "Banjara Hills"),

    ("Madhura Nagar", "Yousufguda"),
    ("Yousufguda", "Jubilee Hills"),

    ("Banjara Hills", "Jubilee Hills"),
    ("Banjara Hills", "Mehdipatnam"),

    ("Jubilee Hills", "Madhapur"),

    ("Madhapur", "Durgam Cheruvu"),
    ("Durgam Cheruvu", "HITEC City"),
    ("Madhapur", "HITEC City"),

    ("HITEC City", "Kondapur"),
    ("Kondapur", "Gachibowli"),

    ("HITEC City", "Shilpa Layout"),
    ("Shilpa Layout", "Gachibowli"),

    ("Mehdipatnam", "Gachibowli")
]


# ---------------------------------------------------------
# Number of observations for each road
# ---------------------------------------------------------

OBSERVATIONS_PER_ROAD = 30


# ---------------------------------------------------------
# Traffic scores
# ---------------------------------------------------------

TRAFFIC_SCORES = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}


# ---------------------------------------------------------
# Calculate traffic score for every road
# ---------------------------------------------------------

road_results = []


print("\nRoad Traffic Analysis")
print("-" * 60)


for index, road in enumerate(ROAD_SEGMENTS):

    source, destination = road

    # -----------------------------------------------------
    # Randomly select observations from the complete dataset
    # -----------------------------------------------------

    road_samples = df.sample(
        n=OBSERVATIONS_PER_ROAD,
        random_state=42 + index
    )

    # -----------------------------------------------------
    # Count traffic levels
    # -----------------------------------------------------

    counts = Counter(
        road_samples["traffic_level"]
    )

    # -----------------------------------------------------
    # Calculate average traffic score
    # -----------------------------------------------------

    average_score = sum(
        TRAFFIC_SCORES[level]
        for level in road_samples["traffic_level"]
    ) / len(road_samples)

    # -----------------------------------------------------
    # Store result
    # -----------------------------------------------------

    road_results.append({
        "road": road,
        "source": source,
        "destination": destination,
        "low": counts.get("Low", 0),
        "medium": counts.get("Medium", 0),
        "high": counts.get("High", 0),
        "average_score": average_score
    })


# ---------------------------------------------------------
# Rank roads according to traffic score
# ---------------------------------------------------------

road_results.sort(
    key=lambda x: x["average_score"]
)


# ---------------------------------------------------------
# Assign relative traffic levels
# ---------------------------------------------------------

total_roads = len(road_results)

low_cutoff = int(total_roads * 0.20)
high_cutoff = int(total_roads * 0.80)


for index, result in enumerate(road_results):

    if index < low_cutoff:

        result["traffic_level"] = "Low"

    elif index >= high_cutoff:

        result["traffic_level"] = "High"

    else:

        result["traffic_level"] = "Medium"


# ---------------------------------------------------------
# Create final traffic conditions
# ---------------------------------------------------------

TRAFFIC_CONDITIONS = {}


print("\nRanked Road Traffic Conditions")
print("-" * 70)


for result in road_results:

    source = result["source"]
    destination = result["destination"]
    traffic_level = result["traffic_level"]

    # Store both directions
    TRAFFIC_CONDITIONS[
        (source, destination)
    ] = traffic_level

    TRAFFIC_CONDITIONS[
        (destination, source)
    ] = traffic_level

    print(
        f"\n{source} -> {destination}"
    )

    print(
        f"  Low: {result['low']} | "
        f"Medium: {result['medium']} | "
        f"High: {result['high']}"
    )

    print(
        f"  Average score: "
        f"{result['average_score']:.2f}"
    )

    print(
        f"  Traffic level: "
        f"{traffic_level}"
    )


# ---------------------------------------------------------
# Final traffic conditions
# ---------------------------------------------------------

print("\nFinal Prototype Traffic Conditions")
print("-" * 60)


for road, traffic in TRAFFIC_CONDITIONS.items():

    source, destination = road

    print(
        f"{source} -> {destination} : {traffic}"
    )


# ---------------------------------------------------------
# Traffic distribution across roads
# ---------------------------------------------------------

print("\nRoad Traffic Distribution")
print("-" * 40)

traffic_distribution = Counter(
    result["traffic_level"]
    for result in road_results
)

print(
    "Low roads:",
    traffic_distribution["Low"]
)

print(
    "Medium roads:",
    traffic_distribution["Medium"]
)

print(
    "High roads:",
    traffic_distribution["High"]
)