import tkinter as tk
import time

# Function to update time
def update_time():
    current_time = time.strftime('%H:%M:%S %p')  # Get current time
    clock_label.config(text=current_time)        # Update label
    clock_label.after(1000, update_time)         # Schedule next update

# Window creation
window = tk.Tk()
window.title("Bhavana's Digital Clock")
window.geometry('400x200')  # Use lowercase x

# Time display label
clock_label = tk.Label(window,
                       font=('Calibri', 50, 'bold'),
                       bg='black',
                       fg='white')
clock_label.pack(anchor='center', expand=True)

# Start time update
update_time()

# Start the program loop
window.mainloop()
