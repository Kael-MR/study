from pytubefix import YouTube
from pytubefix.cli import on_progress

print('''
youtube downloader
witch download do you want?
[1] video
[2] audio
''')

while True:
    vetor1 = int(input('decision?'))
    if vetor1 == 1:
        link = str(input('contents link: '))
        url = f"{link}"

        #this is where you put your path that you want to save the result
        destine = "YTdownloads/videos"


        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)

        ys = yt.streams.get_highest_resolution()
        ys.download(output_path=destine)
        break


    elif vetor1 == 2:
        link = str(input('digite o link do conteudo: '))
        url = f"{link}"


        #this is where you put your path that you want to save the result
        destine = "YTdownloads/audios"

        yt = YouTube(url, on_progress_callback=on_progress)
        print(yt.title)

        ys = yt.streams.get_audio_only()
        ys.download(output_path=destine)
        break


    else:
        print('option not recognized, try again')


print('mission acomplished, search if the archive is where you think it is')

