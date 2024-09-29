# YouTubeVideo_Downloader

## Important Note:
    FFmpeg Installation: Ensure that the ffmpeg binary is placed in the C:\ drive (C:\ffmpeg\bin) and that the directory is added to your system's PATH environment variable. This allows the application to access the ffmpeg commands. And the linkfor downloding the zip file is - https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-essentials.7z ,(Extract the file and place the bin folder in "C:\ffmpeg\" the full path should like "C:\ffmpeg\bin".)

    Pytube Cipher Patch: It may be necessary to apply a patch to the cipher.py file in the pytube library to ensure proper functionality(Since youtube updated thier regex pattern). The changes should be made in "cipher.py" and the file location can be found by using "pip show pytube" using cmd which shows the file path, from the path select pytube folder and make the follwing changes in "cipher.py". Change the line 272 & 273 to :

     line 272- r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
     line 273- r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])\([a-z]\)',

     and remove the ";" from Line 287.

## Important Note While running the file:
    After running of "test_project.py" close all the poped-up Tk windows to make sure the test has passed.
    Both "project.py" and "test_project.py" files works perfectly in VS Code locally but may not function as expected in Codespaces due to environment differences.

## Description
    This project is a YouTube video downloader application developed using Python. It uses the `pytube` library to download videos from YouTube and `ffmpeg` for merging video and audio files. The application features a simple graphical user interface (GUI) built with Tkinter, allowing users to easily input a video URL and initiate downloads. This project was interesting while i created it, and some video which are restricted by youtube can't be downloaded as you try to download it a message pops-up showing try another link and in near future downloading restricted video could be also possible after implemanting it.

### Key Features
- **Check Internet Connectivity**: Verifies whether the user is connected to the internet before attempting to download videos.
- **Download Videos**: Utilizes the `pytube` library to download videos from YouTube by providing the video URL.
- **Merge Audio and Video**: Uses `ffmpeg` to merge separate audio and video streams into a single output file.
- **User-Friendly GUI**: A Tkinter-based interface that makes it easy for users to interact with the application.

### Installation
To set up this project locally, make sure you have Python installed, and then install the required libraries listed in "requirements.txt".

