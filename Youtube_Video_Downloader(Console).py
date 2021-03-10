from pytube import YouTube


def main():

    url = input("Paste URL here: ")

    yt = YouTube(url)

    stream = yt.streams.first()

    stream.download()


if __name__ == '__main__':
    main()