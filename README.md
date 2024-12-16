
# Victor's Portal YouTube Downloader

Victor's Portal YouTube Downloader is a simple and user-friendly desktop application for downloading YouTube videos and audio in various formats. The application is built using Python's `tkinter` for the GUI and `yt-dlp` for downloading videos and converting audio formats.

## Features
- **Download YouTube videos in the best available quality.**
- **Extract and download audio in `mp3` or `wav` formats.**
- **User-friendly interface with progress tracking.**
- **Customizable download path selection.**
- **Error handling for invalid inputs and download issues.**

## Prerequisites
Before running the application, make sure you have the following:
- **Python 3.x** installed. [Download Python](https://www.python.org/downloads/)
- **`yt-dlp`** library installed. You can install it via:
  ```bash
  pip install yt-dlp

- **ffmpeg installed and added to your system's PATH (required for audio conversion to mp3 or wav).**
- You can download ffmpeg from https://ffmpeg.org/download.html.

## Installation
- **1. Clone the Repository:**
  ```bash
  git clone https://github.com/thilak-r/VPYouTubeDownloader.git

- Replace yourusername with your GitHub username.

- **2. Navigate to the Project Directory:**
  ```bash
  cd VPYouTubeDownloader

- **3. Install the Required Libraries:** Make sure you have the required Python libraries installed:
  ```bash
  pip install yt-dlp

- **4. Running the Application:**  You can run the application with:
  ```bash
  python VPYouTubeDownloader.py


# Usage

- **1. Enter a Valid YouTube URL:** Paste the URL of the YouTube video you want to download.
- **2. Select the Download Path:** Choose a folder where the downloaded file will be saved.
- **3. Choose the Format:** Select the desired format (mp4, mp3, or wav) from the dropdown.
Click "Download Now :)" The application will start downloading the video, and the progress bar will indicate the download status.

## How to Install ffmpeg
To download audio formats *(mp3 or wav)*, you need ffmpeg installed on your system.
- **1. Download ffmpeg from** https://ffmpeg.org/download.html.
- **2. Extract the downloaded file and add the** *bin* **folder to your system's PATH**.
      *On Windows, search for "Environment Variables" in the Start Menu, and add the path to ffmpeg's bin directory to the PATH variable.

## Customization
- **Themes and Styling:** You can change the appearance of the application by modifying the ttk.Style() configurations.
- **Additional Formats:** To add more formats or resolutions, modify the format_combobox options and adjust the ydl_opts settings in the download_video() function.
- **Download Queue and History:** You can implement features like a download queue or history log by adding a list to track multiple downloads and recording each download in a file.

## Known Issues
- **Missing ffmpeg Error:**  If ffmpeg is not installed or not added to the system's PATH, the application will not be able to convert audio formats.
- **Invalid URL:** Make sure to provide a valid YouTube URL. The application does not currently validate the URL format before attempting to download.

## Contributing
If you would like to contribute, feel free to submit a pull request or open an issue.

- **i.Fork the repository**
- **ii. Create a new branch (git checkout -b feature-branch)**
- **iii. Commit your changes (git commit -am 'Add a new feature')**
- **iv. Push to the branch (git push origin feature-branch)**
- **v. Create a new Pull Request**
  
## License
This project is licensed under the MIT License. See the **LICENSE** file for more information.

## Acknowledgments
**yt-dlp** for providing a robust tool to download videos from YouTube.

**Python's tkinter** library for making GUI programming in Python accessible.

# MIT License

Copyright (c) 2024 Victor Ikechukwu Agughasi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
