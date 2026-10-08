# AI-Based Traffic-Aware GPS Navigation System

## Project Overview

This project presents a prototype AI-based GPS navigation system that considers
traffic conditions while selecting the best route.

Instead of selecting a route only based on physical distance, the system
assigns traffic weights to roads and uses the Dijkstra algorithm to find the
route with the minimum traffic-adjusted cost.

## Problem Statement

Traditional shortest-path navigation may select a shorter route even when
that route has heavy traffic.

The objective of this project is to develop a traffic-aware route optimization
system that:

- Detects vehicles from traffic images.
- Counts vehicles on each image.
- Classifies traffic as Low, Medium, or High.
- Assigns traffic weights to roads.
- Uses Dijkstra's algorithm for route optimization.
- Displays the selected route through a Streamlit dashboard.

## System Workflow

Traffic Images / CCTV Data
        ↓
YOLO Vehicle Detection
        ↓
Vehicle Counting
        ↓
Traffic Classification
        ↓
Traffic Mapping
        ↓
Hyderabad Prototype Road Network
        ↓
Traffic-Weighted Graph
        ↓
Dijkstra Algorithm
        ↓
Optimal Route
        ↓
Streamlit Dashboard

## Technologies Used

- Python
- YOLO11
- OpenCV
- Pandas
- NumPy
- Matplotlib
- Streamlit
- Dijkstra's Algorithm
- Git & GitHub

## Vehicle Detection

The system uses YOLO11n for vehicle detection.

The vehicle classes considered are:

- Car
- Bus
- Truck

From the processed traffic dataset:

- Images processed: 1,844
- Total vehicles detected: 19,762
- Cars: 18,272
- Buses: 1,346
- Trucks: 144

## Traffic Classification

Traffic level is determined using the total number of detected vehicles.

| Vehicle Count | Traffic Level |
|---------------|---------------|
| 0–7           | Low           |
| 8–13          | Medium        |
| 14–22         | High          |

The traffic classification is rule-based using vehicle-count thresholds.

## Traffic Weight

Each traffic level is converted into a numerical weight:

| Traffic Level | Weight |
|---------------|--------|
| Low           | 1      |
| Medium        | 2      |
| High          | 4      |

## Traffic-Aware Cost Calculation

The cost of each road is calculated as:

**Road Cost = Distance × Traffic Weight**

For example:

A 5 km road with High traffic:

**5 × 4 = 20**

The total route cost is:

**Total Route Cost = Sum of all road costs**

Dijkstra's algorithm selects the route with the minimum total
traffic-adjusted cost.

## Prototype Road Network

The system uses a simplified Hyderabad road network containing locations such
as:

- Secunderabad
- Begumpet
- Ameerpet
- Punjagutta
- Banjara Hills
- Jubilee Hills
- Madhapur
- Durgam Cheruvu
- HITEC City
- Kondapur
- Shilpa Layout
- Gachibowli
- Mehdipatnam
- Yousufguda
- Madhura Nagar

The road distances are approximate prototype values used for demonstrating
route optimization.

## Example Route

For the route:

**Ameerpet → Gachibowli**

The system produced:

- Distance: 21 km
- Traffic-adjusted cost: 36

Route:

**Ameerpet → Punjagutta → Banjara Hills → Mehdipatnam → Gachibowli**

## Streamlit Dashboard

The project includes a Streamlit dashboard where the user can:

1. Select a source location.
2. Select a destination.
3. Calculate the best route.
4. View the route distance.
5. View the traffic-adjusted cost.
6. Visualize the prototype road network and traffic conditions.

## Important Note

The traffic dataset provides vehicle-density observations but does not contain
GPS coordinates.

Therefore, traffic observations are mapped to the prototype Hyderabad road
network for demonstrating traffic-aware route optimization.

The system is a prototype and does not represent real-time Google Maps traffic
conditions.

## How to Run

Clone the repository:

```bash
git clone https://github.com/Hrishika08122006/GPS-Traffic-Navigation.git