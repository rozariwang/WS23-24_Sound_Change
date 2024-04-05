from pytube import YouTube #importing module pytube, install first if not installed yet
import os.path

def extract(line):
    """
    Extract audio and video data from the gathered source links in the text file.
        Parameters:
            line: A line containing year and link, seperated by column ;
    """

    # Seperate the line into year and link tokens
    tokens = line.split(';')
    year, link = (tokens[0][1:], tokens[1])
        
    print("Processing", year)

    # Instantiate YouTube object
    yt = YouTube(link)

    #Download audio active path
    yt.streams.filter(only_audio=True).first().download(output_path='./data/audio',filename=(year+'_audio.mp4'))

    print(year, "is successfully downloaded!")

    return 0

def extract_from_links(file):
    """
        Reads a file containing links and extracts audio video source.
            Parameters:
                file: Text file containing youtube links.
    """
    if os.path.isfile(file):
    # Read the links text file and download the video source
        with open(file) as links:
            for line in links:
                if extract(line):
                    continue

#extract_from_links('links_to_audio.txt')