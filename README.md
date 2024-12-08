# NBA Player Performance and Aggressiveness Analysis

This project analyzes NBA player statistics from the 2023-2024 season to uncover insights into the relationships between player age, position, aggressiveness, and performance. It utilizes Python libraries for data manipulation, statistical analysis, and visualization.

## Project Overview

The analysis focuses on exploring how factors like age and position influence a player's aggressiveness and overall performance. It involves data cleaning, preprocessing, descriptive statistics, hypothesis testing, and inferential analysis to draw meaningful conclusions. Key findings include correlations between aggressiveness and points scored, as well as insights into the playing habits of older vs. younger players and different positions.

## Data Sources

The project utilizes the following datasets containing NBA player statistics:

-   `dataset.csv`
-   `nba_data.csv`
-   `NBA_dataset.csv`

**Note:** If these datasets are publicly available, it would be helpful to add links to their original sources. If not, it is important to mention the origin, i.e., "These datasets were provided by \[Source] and are used for educational purposes."

## Project Structure
content_copy

Markdown

nba-analysis/
├── dataset.csv
├── nba_data.csv
├── NBA_dataset.csv
├── project.py
├── project_2.py
├── README.md
└── LICENSE (optional)

*   **`project.py`:** Main script for data loading, preprocessing, and visualization.
*   **`project_2.py`:** Script for performing statistical analysis (hypothesis testing, confidence intervals).

## Requirements

*   Python 3.x
*   Pandas
*   NumPy
*   Matplotlib
*   Seaborn
*   SciPy

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Raef-Hany/Statistical-Analysis-of-NBA-Player-Performance-and-Aggressiveness
    ```

2. **Install the required libraries:**

    ```bash
    pip install pandas numpy matplotlib seaborn scipy
    ```

## Usage

1. **Data Analysis and Visualization:**

    ```bash
    python project.py
    ```
    This script will perform data analysis and generate visualizations, including:

    *   Distribution of Player Ages
    *   Distribution of Points per Game
    *   Distribution of Positions
    *   Distribution of Fouls Committed
    *   Distribution of Players Starting the Game

2. **Statistical Analysis:**

    ```bash
    python project_2.py
    ```
    This script will perform statistical analyses, such as:

    *   Calculating the proportion of aggressive players.
    *   Calculating the proportion of players who start games.
    *   Generating confidence intervals for mean points, age variance, and other proportions.
    *   Conducting hypothesis tests to explore relationships between variables (e.g., age and aggressiveness).

## Key Findings (Optional - Add if you want to highlight the main results)

*   **Aggressive players tend to score more points.**
*   **Older players generally start more games and are more aggressive than younger players.**
*   **Center players are more aggressive compared to players in other positions.**
*   **(Add more findings as needed)**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. (If you don't have a LICENSE file yet, you can easily create one on GitHub).
