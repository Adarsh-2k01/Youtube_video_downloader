import os
import subprocess
import ffmpeg
from pytube import YouTube
from pytube.exceptions import *
from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import threading
import requests

def update_progress(value, progress):
    progress['value'] = value
    a.update_idletasks()

def check_internet():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def go_button(link):
    if not check_internet():
        messagebox.showerror("No Internet", "No internet connection detected. Please check your connectivity and try again!")
        return "No Internet"  # Return status for testing

    d = link.get()
    try:
        if d == "":
            raise ValueError("No URL provided")
        else:
            # Create a new Tk instance for the download window
            c = Tk()
            c.geometry('800x500+350+100')
            c.title("YOUTUBE VIDEO DOWNLOADER")
            c.iconbitmap(r"C:/Users/adars/Desktop/downloader icon.ico")
            c.config(bg="#ADD8E6")
            F2 = Frame(c, width=1000, height=800)
            F2.place(x=500, y=10)
            L2 = Label(c, text="*Choose a serial number!!", font=('Helvetica 12 bold'), bg="#ADD8E6", fg="#FF0000")
            L2.place(x=660, y=280)

            col = ("Serial. no.", "Resolution", "Size (MB)")
            tree = ttk.Treeview(F2, columns=col, show="headings")
            for i in col:
                tree.heading(i, text=i)
                tree.column(i, width=150)
            tree.pack(fill=X)

            yt = YouTube(d)
            video_streams = yt.streams.filter(file_extension='mp4', only_video=True)
            for i in video_streams:
                aaa = video_streams.index(i) + 1
                size_in_mb = round(i.filesize / (1024 * 1024), 2)
                tree.insert("", "end", values=(aaa, i.resolution, size_in_mb))

            E2 = Entry(c, border=3, font=("signal", 20, "bold"), borderwidth=5, relief="solid", fg="#964C1D", bg="#ADD8E6")
            E2.place(x=600, y=350)

            progress = ttk.Progressbar(c, orient=HORIZONTAL, length=400, mode='determinate')
            progress.place(x=555, y=420)

            def download():
                g = int(E2.get()) - 1
                selected_video_stream = video_streams[g]
                print(f"Downloading video {selected_video_stream.resolution}...")
                video_file = selected_video_stream.download(filename='video.mp4')
                update_progress(33, progress)

                audio_stream = yt.streams.filter(only_audio=True).first()
                print("Downloading audio...")
                audio_file = audio_stream.download(filename='audio.mp4')
                update_progress(66, progress)

                def run_ffmpeg():
                    print("Merging video and audio...")
                    ffmpeg_command = [
                        'ffmpeg', '-y',
                        '-i', 'video.mp4',
                        '-i', 'audio.mp4',
                        '-c:v', 'libx264',
                        '-c:a', 'aac',
                        'output.mp4'
                    ]

                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    process = subprocess.Popen(ffmpeg_command, startupinfo=startupinfo)
                    process.wait()

                    os.remove('video.mp4')
                    os.remove('audio.mp4')

                    update_progress(100, progress)
                    print("Download and merge completed!")
                    messagebox.showinfo("Download Complete", "The video has been downloaded and merged successfully!")

                threading.Thread(target=run_ffmpeg).start()

            B3 = Button(c, text="DOWNLOAD", width=10, height=2, bg="#ADD8E6", activebackground="#d5c1aa", relief=RAISED, cursor="hand2", command=download)
            B3.place(x=720, y=490)
            c.bind('<Return>', lambda event: download())
            c.mainloop()
    except RegexMatchError:
        messagebox.showerror("ERROR", "Invalid YouTube URL. Please enter a valid URL.")
        return "Invalid URL"
    except ValueError as e:
        messagebox.showerror("ERROR", str(e))
        return str(e)
    except Exception as e:
        messagebox.showerror("ERROR", f"Oops! Something went wrong. Try another URL.\nDetails: {str(e)}")
        return "General Error"


def main():
    global a
    a = Tk()
    a.geometry('800x600+350+100')
    a.minsize(800, 600)
    a.title("YOUTUBE VIDEO DOWNLOADER")
    a.iconbitmap(r"C:/Users/adars/Desktop/downloader icon.ico")

    F1 = Frame(a, width=1900, height=1800)
    F1.pack()
    img = ImageTk.PhotoImage(Image.open(r"C:/Users/adars/Desktop/canvas bg.jpg"))
    label = Label(F1, image=img)
    label.pack()

    L1 = Label(a, text="ENTER THE VIDEO URL:", font=("Roboto", 30, "bold"), borderwidth=5, relief="solid", bg="#ADD8E6", fg="#191C27")
    L1.place(x=550, y=150)

    link = StringVar()
    E1 = Entry(a, textvariable=link, border=3, font=("signal", 20, "bold"), borderwidth=5, relief="solid", fg="#964C1D", bg="#ADD8E6")
    E1.place(x=620, y=300)

    m = Menu(a)
    a.config(menu=m)
    FileMenu = Menu(m)
    m.add_cascade(label="File", menu=FileMenu)
    EditMenu = Menu(m)
    m.add_cascade(label="Edit", menu=EditMenu)
    OptionMenu = Menu(m)
    m.add_cascade(label="Option", menu=OptionMenu)

    def cmdExit():
        m = messagebox.askquestion('Exit Application', 'Are you sure want to exit this application!')
        if m == 'yes':
            a.destroy()

    FileMenu.add_command(label="Exit", command=cmdExit)

    def cmdClear():
        E1.delete(0, "end")

    EditMenu.add_command(label="Clear", command=cmdClear)

    def cmdSelectAll():
        E1.select_range(0, "end")

    EditMenu.add_command(label="Select All", command=cmdSelectAll)

    def cmdAbout():
        b = Tk()
        b.geometry('300x400+350+100')
        b.minsize(300, 400)
        b.maxsize(300, 400)
        b.title("About")
        b.iconbitmap(r"C:\Users\adars\Desktop\downloader icon.ico")
        C1 = Canvas(b, width=800, height=750, bg="lightblue", border=5)
        C1.create_text(550, 400, text="This is free YouTube Downloader", fill="black", font=('Helvetica 10 bold'))
        C1.create_text(550, 470, text="You can download required videos of your", fill="black", font=('Helvetica 10 bold'))
        C1.create_text(550, 485, text="need", fill="black", font=('Helvetica 10 bold'))
        C1.create_text(550, 555, text="Email:adarshjs2001@gmail.com", fill="black", font=('Helvetica 10 bold'))
        C1.create_text(550, 625, text="Thanks for downloading this program", fill="black", font=('Helvetica 10 bold'))
        C1.create_text(550, 645, text="(｡◕‿◕｡)", fill="black", font=('Helvetica 10 bold'))
        C1.place(anchor='center')
        def close_button():
            b.destroy()
        B1 = Button(b, text="Close", width=42, bg="#ADD8E6", activebackground="#DCAE96", relief=RIDGE, cursor="hand2", command=close_button)
        B1.place(x=0, y=375)
        b.mainloop()
    OptionMenu.add_command(label="About", command=cmdAbout)

    B2 = Button(a, text="GO", width=10, height=2, bg="#ADD8E6", highlightbackground="black", highlightthickness=4, bd=4, activebackground="#964C1D", relief=RAISED, cursor="hand2", command=lambda: go_button(link))
    B2.place(x=732, y=420)
    a.bind('<Return>', lambda event: go_button(link))
    a.focus()
    a.mainloop()

if __name__ == "__main__":
    main()
