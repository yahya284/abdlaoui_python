import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import requests

# Function to open the file dialog and select a file
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Audio/Video Files", "*.mp3;*.mp4;*.wav")])
    if filename:
        file_path.set(filename)  # Set the selected file path to the label
        status_label.config(text="Selected file: " + filename)

# Function to handle the file upload
def upload_file():
    file_path_value = file_path.get()
    if not file_path_value:
        messagebox.showerror("Error", "No file selected.")
        return

    url = 'http://127.0.0.1:5000/upload'  # Server URL

    try:
        with open(file_path_value, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, files=files)

        # Check server response
        if response.status_code == 200:
            messagebox.showinfo("Success", "File uploaded successfully!")
        else:
            messagebox.showerror("Error", f"Failed to upload file: {response.json().get('error')}")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main Tkinter window
root = tk.Tk()
root.title("File Upload Client")

# Set the window size
root.geometry("400x300")

# Create a StringVar to store the file path
file_path = tk.StringVar()

# Create the widgets
browse_button = tk.Button(root, text="Browse File", command=browse_file)
upload_button = tk.Button(root, text="Upload File", command=upload_file)
status_label = tk.Label(root, text="No file selected.")
exit_button = tk.Button(root, text="Exit", command=root.quit)

# Arrange the widgets on the window
browse_button.pack(pady=20)
status_label.pack(pady=10)
upload_button.pack(pady=20)
exit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
