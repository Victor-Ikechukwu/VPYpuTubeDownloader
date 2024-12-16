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
    

@app.route('/fetch_video_info', methods=['POST'])
def fetch_video_info():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'URL is required.'})
    
    try:
        ydl_opts = {'quiet': True, 'extract_flat': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', 'Unknown Title')
            thumbnail = info_dict.get('thumbnail', '')
        
        return jsonify({'title': title, 'thumbnail': thumbnail})
    
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form['url']
    selected_format = request.form['format']  # Could be 'best', 'mp3', 'wav', etc.
    quality = request.form.get('quality')

    # Default download path (browser's download directory)
    download_path = get_default_download_path()

    if not video_url:
        return jsonify({"error": "Please enter a valid YouTube URL."})

    try:
        # Get the current date and time for unique naming
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Set default download options
        ydl_opts = {
            'outtmpl': f'./downloads/{current_time}_%(title)s.%(ext)s',  # Set download directory
            'quiet': False,  # Enable verbosity for progress
        }

        # Check if the user wants the best format
        if selected_format == 'best':
            # Set options to get the best video and audio format
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
        elif selected_format in ['mp3', 'wav']:
            # If the user wants audio-only formats
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': selected_format,
                'preferredquality': '192',
            }]
        else:
            # Default to best available format if no specific format is given
            ydl_opts['format'] = 'bestvideo+bestaudio/best'

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
















