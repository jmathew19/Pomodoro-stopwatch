import tkinter as tk
from datetime import datetime, timedelta
import random


class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Multi-Timer Stopwatch")
        self.timers = []  # List to hold individual timers

        # Predefined colors for timers
        self.colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta", "yellow"]
        self.i = 0

        # Create a canvas for the bar graph
        self.canvas = tk.Canvas(root, height=50, bg="white")
        self.canvas.pack(fill=tk.X, padx=20, pady=10)

        # Label for total elapsed time
        self.total_time_label = tk.Label(root, text="Total Time: 00:00:00", font=("Helvetica", 20), bg="lightgray",
                                         fg="black")
        self.total_time_label.pack(fill=tk.X, padx=20, pady=10)

        # Button to add a new timer
        self.add_timer_button = tk.Button(root, text="Add Timer", command=self.add_timer, font=("Helvetica", 20),
                                          bg="orange", fg="black")
        self.add_timer_button.pack(pady=20)

        # Update the bar graph and total time label regularly
        self.update_bar_graph()
        self.update_total_time_label()

    def add_timer(self):
        # Create a frame for each timer
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Assign a color to the timer
        color = self.colors[self.i]
        self.i = (self.i + 1) % len(self.colors)

        # Create an editable label (Entry) first with a limited width
        editable_label = tk.Entry(frame, font=("Helvetica", 24), width=10)  # Adjust width as needed
        editable_label.grid(row=0, column=0, padx=10, pady=10)

        # Create the display for the stopwatch with the color background
        time_label = tk.Label(frame, text="00:00:00", font=("Helvetica", 24), bg=color, fg="white")
        time_label.grid(row=0, column=1, padx=10, pady=10)

        # Timer data
        timer_data = {
            "running": False,
            "start_time": None,
            "elapsed_time": timedelta(),
            "time_label": time_label,
            "frame": frame,
            "color": color,
            "editable_label": editable_label
        }

        # Start button
        start_button = tk.Button(frame, text="Start", command=lambda: self.start(timer_data), font=("Helvetica", 12),
                                 bg="blue", fg="green")
        start_button.grid(row=1, column=0, padx=5, pady=5)

        # Stop button
        stop_button = tk.Button(frame, text="Stop", command=lambda: self.stop(timer_data), font=("Helvetica", 12),
                                bg="red", fg="red")
        stop_button.grid(row=1, column=1, padx=5, pady=5)

        # Reset button
        reset_button = tk.Button(frame, text="Reset", command=lambda: self.reset(timer_data), font=("Helvetica", 12),
                                 bg="blue", fg="blue")
        reset_button.grid(row=1, column=2, padx=5, pady=5)

        # Delete button
        delete_button = tk.Button(frame, text="Delete", command=lambda: self.delete_timer(timer_data),
                                  font=("Helvetica", 12), bg="gray", fg="orange")
        delete_button.grid(row=1, column=3, padx=5, pady=5)

        self.timers.append(timer_data)

    def update_time(self, timer_data):
        if timer_data["running"]:
            current_time = datetime.now()
            timer_data["elapsed_time"] = current_time - timer_data["start_time"]
            time_str = str(timer_data["elapsed_time"]).split(".")[0]  # Remove microseconds
            timer_data["time_label"].config(text=time_str)
            self.root.after(50, lambda: self.update_time(timer_data))
            self.update_bar_graph()
            self.update_total_time_label()

    def start(self, timer_data):
        if not timer_data["running"]:
            timer_data["running"] = True
            timer_data["start_time"] = datetime.now() - timer_data["elapsed_time"]
            self.update_time(timer_data)

    def stop(self, timer_data):
        if timer_data["running"]:
            timer_data["running"] = False
            self.update_bar_graph()
            self.update_total_time_label()

    def reset(self, timer_data):
        timer_data["running"] = False
        timer_data["elapsed_time"] = timedelta()
        timer_data["time_label"].config(text="00:00:00")
        self.update_bar_graph()
        self.update_total_time_label()

    def delete_timer(self, timer_data):
        # Stop the timer if it's running
        timer_data["running"] = False
        # Destroy the frame, which removes all widgets inside it
        timer_data["frame"].destroy()
        # Remove the timer data from the list
        self.timers.remove(timer_data)
        self.update_bar_graph()
        self.update_total_time_label()

    def update_bar_graph(self):
        # Clear the canvas
        self.canvas.delete("all")

        # Calculate the total elapsed time across all timers
        total_time = sum((timer["elapsed_time"] for timer in self.timers), timedelta())
        if total_time.total_seconds() == 0:
            return  # No time to display

        # Draw the bars on the canvas
        current_x = 0
        canvas_width = self.canvas.winfo_width()

        for timer in self.timers:
            timer_fraction = timer["elapsed_time"] / total_time
            bar_width = int(timer_fraction * canvas_width)
            self.canvas.create_rectangle(current_x, 0, current_x + bar_width, 50, fill=timer["color"])
            current_x += bar_width

    def update_total_time_label(self):
        total_time = sum((timer["elapsed_time"] for timer in self.timers), timedelta())
        time_str = str(total_time).split(".")[0]  # Remove microseconds
        self.total_time_label.config(text=f"Total Time: {time_str}")


# Create the main window and run the application
root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()
