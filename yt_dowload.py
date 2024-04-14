import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube

def download_video():
    """
    Initiates the download process for the requested YouTube video.
    This function retrieves the user input from the GUI, sets up the YouTube object, selects the appropriate stream,
    and initiates the download process. It also handles exceptions and updates the user interface with success or error messages.
    """
    # Collect the necessary inputs from the user interface
    url = url_entry.get()
    resolution = resolution_combobox.get()
    audio_only = audio_var.get()
    path = path_label.cget("text")

    try:
        # Create a YouTube object with the URL
        yt = YouTube(url)
        # Register the callback for updating the download progress
        yt.register_on_progress_callback(show_progress)

        # Determine the stream to download based on user selection
        if audio_only:
            stream = yt.streams.filter(only_audio=True).first()
        elif resolution:
            stream = yt.streams.filter(res=resolution).first()
        else:
            stream = yt.streams.get_highest_resolution()

        # Perform the download to the specified path or default path
        if path:
            stream.download(output_path=path)
        else:
            stream.download()

        # Display a success message to the user
        messagebox.showinfo("Success", f"Video downloaded as {stream.default_filename}")
    except Exception as e:
        # Handle exceptions and display an error message to the user
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def show_progress(stream, chunk, bytes_remaining):
    """
    Updates the progress bar as the video downloads.
    This callback function is triggered during the download process to update the progress bar
    based on the bytes downloaded so far and the total file size.
    """
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_var.set(percentage_of_completion)
    app.update_idletasks()

def browse_folder():
    """
    Opens a dialog for the user to select a download directory.
    This function allows the user to choose a directory where the downloaded file will be saved.
    """
    folder = filedialog.askdirectory()
    if folder:
        path_label.config(text=folder)

def setup_gui():
    """
    Sets up the GUI components of the YouTube Video Downloader.
    This function creates and arranges all the widgets (buttons, labels, entries) on the GUI.
    """
    global url_entry, resolution_combobox, audio_var, path_label, progress_var, app

    app = tk.Tk()
    app.title("YouTube Video Downloader")
    app.geometry("400x300")
    app.config(bg="#f0f0f0")

    # Define and pack all GUI components using grid or pack layout managers
    tk.Label(app, text="YouTube URL:", bg="#f0f0f0", font=("Arial", 10)).pack(pady=(10, 0))
    url_entry = tk.Entry(app, width=40, font=("Arial", 10), bd=1, relief="solid")
    url_entry.pack(pady=(0, 10))

    tk.Label(app, text="Save to:", bg="#f0f0f0", font=("Arial", 10)).pack()
    path_label = tk.Label(app, text="", bg="#e0e0e0", width=40, font=("Arial", 10), bd=1, relief="solid")
    path_label.pack()
    browse_button = tk.Button(app, text="Browse", command=browse_folder, bg="#a6dcef", activebackground="#82c4d8", relief="groove", font=("Arial", 9))
    browse_button.pack(pady=(0, 10))

    tk.Label(app, text="Resolution:", bg="#f0f0f0", font=("Arial", 10)).pack()
    resolution_combobox = ttk.Combobox(app, values=["360p", "720p", "1080p"], state="readonly", font=("Arial", 10))
    resolution_combobox.pack(pady=(0, 10))

    audio_var = tk.BooleanVar()
    audio_check = tk.Checkbutton(app, text="Download Audio Only", variable=audio_var, onvalue=True, offvalue=False, bg="#f0f0f0", font=("Arial", 10))
    audio_check.pack(pady=(0, 10))

    download_button = tk.Button(app, text="Download", command=download_video, bg="#a6dcef", activebackground="#82c4d8", relief="groove", font=("Arial", 10))
    download_button.pack(pady=(0, 10))

    progress_var = tk.DoubleVar()
    progress = ttk.Progressbar(app, orient="horizontal", length=200, mode="determinate", var=progress_var)
    progress.pack()

    app.mainloop()

if __name__ == "__main__":
    setup_gui()
