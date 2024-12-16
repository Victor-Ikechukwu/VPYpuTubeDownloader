from flask import Flask, render_template, request, send_from_directory, jsonify
import os
import yt_dlp
from datetime import datetime

app = Flask(__name__)

# Get the default download path (browser's download path)
def get_default_download_path():
    if os.name == 'nt':  # For Windows
        return os.path.join(os.environ['USERPROFILE'], 'Downloads')
    elif os.name == 'posix':  # For Linux/Mac
        return os.path.join(os.environ['HOME'], 'Downloads')
    else:
        return ''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form['url']
    selected_format = request.form['format']

    # Default download path (browser's download directory)
    download_path = get_default_download_path()

    if not video_url:
        return jsonify({"error": "Please enter a valid YouTube URL."})

    try:
        # Get the current date and time for unique naming
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{download_path}/%(title)s_{current_time}.%(ext)s',  # Include the date and time
        }

        # Adjust download options based on selected format
        if selected_format in ['mp3', 'wav']:
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': selected_format,
                'preferredquality': '192',
            }]

        # Download the video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])

        return jsonify({"message": "Download completed!"})

    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"})

@app.route('/uploads/<filename>')
def send_file(filename):
    # Serve file from the default download path
    return send_from_directory(get_default_download_path(), filename)

if __name__ == "__main__":
    app.run(debug=True)
