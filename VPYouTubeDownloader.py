# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 14:56:29 2024

@author: Victor-PhD
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yt_dlp
import time  # Added to simulate slower downloads for testing

def download_video():
    video_url = url_entry.get()
    download_path = path_entry.get()
    selected_format = format_var.get()

    if not video_url:
        messagebox.showerror("Error", "Please enter a valid YouTube video URL.")
        return

    if selected_format not in ['mp4', 'mp3', 'wav']:
        messagebox.showerror("Error", "Please select a valid format.")
        return

    try:
        # Set download options
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{download_path}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
        }

        # Adjust download options based on selected format
        if selected_format in ['mp3', 'wav']:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': selected_format,
                'preferredquality': '192',
            }]

        # Start download
        status_label.config(text="Downloading...")
        progress_var.set(0)
        app.update_idletasks()  # Update the GUI before starting the download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        
        status_label.config(text="Download completed!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        status_label.config(text="")

def progress_hook(d):
    if d['status'] == 'downloading':
        # Calculate the percentage
        if d.get('total_bytes') is not None:
            downloaded = d.get('downloaded_bytes', 0)
            total = d.get('total_bytes', 1)  # Avoid division by zero
            percentage = (downloaded / total) * 100
            progress_var.set(percentage)
            progress_bar.update_idletasks()  # Update the progress bar
            status_label.config(text=f"Downloading: {percentage:.2f}%")
            
            # Simulate a slower download for testing
            time.sleep(0.05)  # Remove this line in a real application
    elif d['status'] == 'finished':
        status_label.config(text="Download Completed!")
        progress_var.set(100)

def browse_folder():
    folder_selected = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, folder_selected)

# Create the main window
app = tk.Tk()
app.title("Victor's Portal YouTube Downloader")
app.geometry("550x350")
app.configure(bg="#f0f0f0")

# Create style for ttk widgets
style = ttk.Style()
style.theme_use('clam')
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TButton", font=("Helvetica", 12), padding=6)
style.configure("TCombobox", font=("Helvetica", 12))

# Style the progress bar to make it green
style.configure("green.Horizontal.TProgressbar", troughcolor="white", background="green")

# Create widgets
ttk.Label(app, text="Enter a Valid YouTube URL:").pack(pady=10)
url_entry = ttk.Entry(app, width=50)
url_entry.pack(pady=5)

ttk.Label(app, text="Select the Download Path:").pack(pady=10)
path_entry = ttk.Entry(app, width=50)
path_entry.pack(pady=5)

browse_button = ttk.Button(app, text="Browse", command=browse_folder)
browse_button.pack(pady=5)

ttk.Label(app, text="Select your desired format:").pack(pady=10)
format_var = tk.StringVar(value='mp4')
format_combobox = ttk.Combobox(app, textvariable=format_var, values=["mp4", "mp3", "wav"], state="readonly")
format_combobox.pack(pady=5)

# Add the "Download Now" button
download_button = ttk.Button(app, text="Download Now :)", command=download_video)
download_button.pack(pady=20)

# Add a progress bar to show download progress
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(app, orient="horizontal", length=400, mode="determinate", variable=progress_var, style="green.Horizontal.TProgressbar")
progress_bar.pack(pady=10)

# Status label for displaying current status
status_label = ttk.Label(app, text="")
status_label.pack(pady=10)

# Run the application
app.mainloop()


