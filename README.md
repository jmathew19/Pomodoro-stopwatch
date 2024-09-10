# Multi-Timer Stopwatch

This is a Python-based multi-timer stopwatch application built using `Tkinter` for the GUI. It allows users to create multiple stopwatches, 
track time, visualize time spent using a bar graph, and manage each timer individually. The app is dynamic and can accommodate an unlimited 
number of timers with features such as start, stop, reset, and delete.

I created this to help me see how I am spending my time and visualize the poroportion of time I am spending on it

## Features

- **Add Multiple Timers**: Create as many timers as you need, each with its own display.
- **Start, Stop, Reset**: Each timer can be individually controlled with start, stop, and reset buttons.
- **Customizable Timer Labels**: Edit the timer names for better identification.
- **Delete Timers**: Remove any timer that you no longer need.
- **Total Time Display**: Shows the sum of elapsed times from all running timers.
- **Bar Graph**: Visual representation of elapsed times for all active timers in proportion to the total time.

## Prerequisites

- Python 3.x
- Tkinter (should be included with standard Python installations)

## Installation

1. Clone or download this repository.
2. Ensure you have Python 3 installed on your system.
3. Install any necessary dependencies. Tkinter is typically bundled with Python, but if not, you can install it as follows:
   ```bash
   sudo apt-get install python3-tk
   ```

## Running the Application

1. Navigate to the directory containing the script.
2. Run the script with Python:
   ```bash
   python stopwatch.py
   ```
3. The application window will open, where you can start adding and managing timers.

## How to Use

1. **Add Timer**: Click the "Add Timer" button to create a new timer. You can assign a custom name to each timer.
2. **Start Timer**: Click the "Start" button to start the timer.
3. **Stop Timer**: Click the "Stop" button to pause the timer.
4. **Reset Timer**: Click the "Reset" button to reset the timer to `00:00:00`.
5. **Delete Timer**: Click the "Delete" button to remove a timer from the list.
6. **Track Total Time**: The total time for all active timers is displayed at the top.
7. **Visualize Time**: A bar graph dynamically updates to show the proportion of time each timer contributes to the total time.

## Customization

- **Colors**: You can customize the predefined colors for the timers by editing the `self.colors` list in the script.
- **Timer Label Width**: Adjust the width of the editable timer labels by modifying the `width` parameter in the `Entry` widget.
