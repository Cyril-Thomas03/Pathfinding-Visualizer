# Pathfinding Visualization with A* Search

This project visualizes the A* search algorithm, a popular pathfinding algorithm, using Pygame.  It allows users to interactively create a grid-based environment, define a start and end point, and observe the A* algorithm finding the shortest path between them.  Obstacles can be added to the grid to further challenge the algorithm.

## Table of Contents

*   [Introduction](#introduction)
*   [Features](#features)
*   [Technologies Used](#technologies-used)
*   [Installation](#installation)
*   [How to Use](#how-to-use)
*   [Code Structure](#code-structure)
*   [Algorithm Explanation](#algorithm-explanation)
*   [Future Improvements](#future-improvements)

## Introduction

Pathfinding is a fundamental problem in computer science with applications in robotics, game development, and many other fields. The A* search algorithm is a widely used and efficient algorithm for finding the shortest path between two points in a graph or grid. This project provides a visual demonstration of how the A* algorithm works, making it easier to understand its steps and logic.

## Features

*   **Interactive Grid Creation:** Users can click to create start and end points, as well as obstacles (walls) on the grid.
*   **A\* Pathfinding:** The A\* algorithm is implemented to find the shortest path between the defined start and end points.
*   **Real-time Visualization:** The algorithm's progress is visualized in real-time, showing the nodes it explores and the path it eventually finds.
*   **Obstacle Placement:** Users can add obstacles to the grid to create more complex pathfinding scenarios.
*   **Grid Reset:** The grid can be easily reset to clear the environment and start a new pathfinding problem.

## Technologies Used

*   **Python:** The primary programming language used.
*   **Pygame:** A Python library for creating games and multimedia applications, used for the visualization.
*   **PriorityQueue (from the `queue` module):** Used for efficient management of open nodes in the A\* algorithm.

## Installation

1.  **Install Python:** If you don't have Python installed, download and install it from [https://www.python.org/](https://www.python.org/).

2.  **Install Pygame:** Open a terminal or command prompt and run:

    ```bash
    pip install pygame
    ```

## How to Use

1.  **Run the script:** Save the code as a `.py` file (e.g., `pathfinding.py`) and run it from your terminal:

    ```bash
    python pathfinding.py
    ```

2.  **Create the environment:**
    *   **Left-click:** To place the start point (orange), the end point (turquoise), or obstacles (black).
    *   **Right-click:** To remove a placed element (start, end, or obstacle).

3.  **Start the pathfinding:** Press the **spacebar** to initiate the A\* search algorithm.

4.  **Reset the grid:** Press the **'c' key** to clear the grid and start a new scenario.

## Code Structure

The code is organized as follows:

*   **`Spot` Class:** Represents a single cell in the grid, storing its position, color (state), neighbors, and drawing functionality.
*   **`distance` Function:** Calculates the Manhattan distance between two points, used as a heuristic in A\*.
*   **`build_grid` Function:** Creates the grid of `Spot` objects.
*   **`draw_grid` Function:** Draws the grid lines.
*   **`draw` Function:** Draws all the spots on the grid.
*   **`get_clicked_pos` Function:** Converts mouse click coordinates to grid cell indices.
*   **`reconstruct_path` Function:** Backtracks from the end point to reconstruct the shortest path.
*   **`algorithm` Function:** Implements the A\* search algorithm.
*   **`main` Function:** Handles user interaction, grid setup, and algorithm execution.

## Algorithm Explanation

The A\* algorithm uses a combination of heuristics and actual path costs to find the shortest path. It maintains two sets of nodes: an "open set" (nodes to be explored) and a "closed set" (nodes already explored).  The algorithm repeatedly selects the node from the open set with the lowest "f score," where f score = g score + h score.

*   **g score:** The cost of the path from the start node to the current node.
*   **h score:** The estimated cost from the current node to the end node (heuristic).

The algorithm explores the neighbors of the selected node, calculates their g and f scores, and adds them to the open set if they haven't been visited or if a shorter path to them has been found. This process continues until the end node is reached or the open set is empty (no path found).

## Future Improvements

*   **Different Heuristics:** Experiment with different heuristic functions (e.g., Euclidean distance).
*   **Path Smoothing:** Implement path smoothing techniques to create more natural-looking paths.
*   **Cost Weights:** Allow users to assign different costs to different types of terrain (e.g., higher cost for difficult terrain).
*   **More Advanced Obstacles:** Implement more complex obstacle shapes or moving obstacles.
*   **Performance Optimization:** Explore ways to optimize the algorithm's performance for larger grids.


This README provides a good overview of your project.  Remember to include the license information if you are making your project public.  Good luck!

Credits:
This program was made with help from the tutorial by Tech with Tim and thus the main purpose in creating this was learning. 

