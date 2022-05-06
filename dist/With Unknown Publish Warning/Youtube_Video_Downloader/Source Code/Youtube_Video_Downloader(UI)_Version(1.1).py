from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
from tkinter.messagebox import showinfo

Location_Name = ""


def main():

    def openLocation():

        global Location_Name

        Location_Name = filedialog.askdirectory()

        if (len(Location_Name) > 1):
            locationError.config(text=Location_Name, fg="green")
        else:
            #locationError.config(text="Please Select Folder!!!", fg="red")
            showinfo("Warning", "Please Select Folder!!!")

    def DownloadVideo():

        choice = ydChoice.get()
        url = ydEntry.get()

        if len(url) > 1:
            ydError.config(text="")
            try:
                yt = YouTube(url)

                if (choice == cboChoice[0]):
                    select = yt.streams.filter(progressive=True, file_extension='mp4').last()

                elif (choice == cboChoice[1]):
                    select = yt.streams.filter(progressive=True).first()

                elif (choice == cboChoice[2]):
                    select = yt.streams.filter(only_audio=True).first()

                else:
                    #ydError.config(text="Please Select Quality!!!", fg="red")
                    showinfo("Warning", "Please Select Quality!!!")
            except Exception:

                showinfo("Warning", "Somethings Wrong Please Check Step by Step Carefully !!")

        try:

            select.download(Location_Name)
            showinfo("Done", "Successfully Downloaded!!")

        except UnboundLocalError:

            showinfo("Warning", "Somethings Wrong Please Check Step by Step Carefully !!")




    tk = Tk()

    tk.title("Youtube Video Downloader (Version 1.1)")
    tk.geometry("500x400")
    tk.columnconfigure(0, weight=1)
    tk.resizable(False, False)

    # Link Label
    ydLabel = Label(tk, text="Please Paste URL of the video here", font=("jost", 13))
    ydLabel.grid()

    # Text Box
    ydEntryVar = StringVar()
    ydEntry = Entry(tk, width=50, textvariable=ydEntryVar)
    ydEntry.grid()

    # Error Message
    ydError = Label(tk, text=" ", fg="red", font=("jost", 10))
    ydError.grid()

    blank = Label()
    blank.grid()

    # Location Label
    locationLabel = Label(tk, text="Choose location that you want to save", font=("jost", 12))
    locationLabel.grid()

    # Save Button
    savebtn = Button(tk, width=20, bg="red", fg="white", text="Choose Location", command=openLocation)
    savebtn.grid()

    # Error Message For Location Path
    locationError = Label(tk, text=" ", fg="red", font=("jost", 10))
    locationError.grid()

    blank = Label()
    blank.grid()

    # Select Quality
    ydQuality = Label(tk, text="Select Quality", font=("jost", 13))
    ydQuality.grid()

    # ComboBox
    cboChoice = ["720p", "144p", "Only Audio"]
    ydChoice = ttk.Combobox(tk, values=cboChoice)
    ydChoice.grid()

    blank = Label()
    blank.grid()

    # Download Button
    downloadbtn = Button(tk, width=10, bg="red", fg="white", text="Download", command=DownloadVideo)
    downloadbtn.grid()

    blank = Label()
    blank.grid()

    # Developer
    DeveloperLabel = Label(tk, text="Created by", font=("jost", 12))
    DeveloperLabel.grid()

    DeveloperNameLabel = Label(tk, text="Min Khant Soe (Hak Hak)", font=("jost", 12))
    DeveloperNameLabel.grid()

    DeveloperNameLabel = Label(tk, text="https://github.com/1MinKhantSoe1", font=("jost", 12))
    DeveloperNameLabel.grid()

    tk.mainloop()


if __name__ == '__main__':
    main()
