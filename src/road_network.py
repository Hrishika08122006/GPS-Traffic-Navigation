# ---------------------------------------------------------
# Hyderabad Prototype Road Network
# ---------------------------------------------------------
# This is a simplified representation of major connected
# locations used in our GPS traffic navigation prototype.
#
# Distances are approximate prototype values, not exact
# Google Maps distances.
# ---------------------------------------------------------

ROAD_NETWORK = {

    # North Hyderabad
    "Secunderabad": [
        ("Begumpet", 6)
    ],

    "Begumpet": [
        ("Secunderabad", 6),
        ("Ameerpet", 4)
    ],

    # Central Hyderabad
    "Ameerpet": [
        ("Begumpet", 4),
        ("Punjagutta", 2),
        ("Madhura Nagar", 3)
    ],

    "Punjagutta": [
        ("Ameerpet", 2),
        ("Banjara Hills", 3)
    ],

    "Madhura Nagar": [
        ("Ameerpet", 3),
        ("Yousufguda", 2)
    ],

    # Western / Central Hyderabad
    "Banjara Hills": [
        ("Punjagutta", 3),
        ("Jubilee Hills", 4),
        ("Mehdipatnam", 6)
    ],

    "Yousufguda": [
        ("Madhura Nagar", 2),
        ("Jubilee Hills", 3)
    ],

    "Jubilee Hills": [
        ("Banjara Hills", 4),
        ("Yousufguda", 3),
        ("Madhapur", 5)
    ],

    # HITEC City corridor
    "Madhapur": [
        ("Jubilee Hills", 5),
        ("Durgam Cheruvu", 2),
        ("HITEC City", 2)
    ],

    "Durgam Cheruvu": [
        ("Madhapur", 2),
        ("HITEC City", 2)
    ],

    "HITEC City": [
        ("Madhapur", 2),
        ("Durgam Cheruvu", 2),
        ("Kondapur", 3),
        ("Shilpa Layout", 2)
    ],

    # Western side
    "Kondapur": [
        ("HITEC City", 3),
        ("Gachibowli", 4)
    ],

    "Shilpa Layout": [
        ("HITEC City", 2),
        ("Gachibowli", 3)
    ],

    "Gachibowli": [
        ("Kondapur", 4),
        ("Shilpa Layout", 3),
        ("Mehdipatnam", 10)
    ],

    # Southern route
    "Mehdipatnam": [
        ("Banjara Hills", 6),
        ("Gachibowli", 10)
    ]
}


def display_road_network():

    print("\nHyderabad Prototype Road Network")
    print("-" * 50)

    for location, roads in ROAD_NETWORK.items():

        for destination, distance in roads:

            print(
                f"{location} -> {destination} : "
                f"{distance} km"
            )


if __name__ == "__main__":
    display_road_network()