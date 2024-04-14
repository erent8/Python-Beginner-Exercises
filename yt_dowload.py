import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    resolution = resolution_combobox.get()
    audio_only = audio_var.get()
    path = path_label.cget("text")

    try:
        yt = YouTube(url)
        yt.register_on_progress_callback(show_progress)

        if audio_only:
            stream = yt.streams.filter(only_audio=True).first()
        elif resolution:
            stream = yt.streams.filter(res=resolution).first()
        else:
            stream = yt.streams.get_highest_resolution()

        if path:
            stream.download(output_path=path)
        else:
            stream.download()

        messagebox.showinfo("Success", f"Video downloaded as {stream.default_filename}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def show_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    progress_var.set(percentage_of_completion)
    app.update_idletasks()

def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        path_label.config(text=folder)

def setup_gui():
    global url_entry, resolution_combobox, audio_var, path_label, progress_var, app

    app = tk.Tk()
    app.title("YouTube Video Downloader")
    app.geometry("400x250")  # Adjusted for better layout
    app.config(bg="#f3f4ed")

    tk.Label(app, text="YouTube URL:", bg="#f3f4ed").pack(pady=(10, 0))
    url_entry = tk.Entry(app, width=40)
    url_entry.pack(pady=(0, 10))

    tk.Label(app, text="Save to:", bg="#f3f4ed").pack()
    path_label = tk.Label(app, text="", bg="#d1d2c0", width=40)
    path_label.pack()
    browse_button = tk.Button(app, text="Browse", command=browse_folder)
    browse_button.pack(pady=(0, 10))

    tk.Label(app, text="Resolution:", bg="#f3f4ed").pack()
    resolution_combobox = ttk.Combobox(app, values=["360p", "720p", "1080p"], state="readonly")
    resolution_combobox.pack(pady=(0, 10))

    audio_var = tk.BooleanVar()
    audio_check = tk.Checkbutton(app, text="Download Audio Only", variable=audio_var, onvalue=True, offvalue=False, bg="#f3f4ed")
    audio_check.pack(pady=(0, 10))

    download_button = tk.Button(app, text="Download", command=download_video, bg="#a6dcef", activebackground="#82c4d8")
    download_button.pack(pady=(0, 10))

    progress_var = tk.DoubleVar()
    progress = ttk.Progressbar(app, orient="horizontal", length=200, mode="determinate", var=progress_var)
    progress.pack()

    app.mainloop()

if __name__ == "__main__":
    setup_gui()
