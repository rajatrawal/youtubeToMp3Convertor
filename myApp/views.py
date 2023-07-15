from django.http import HttpResponse
from django.shortcuts import render
import youtube_dl
import time
import os


def index(request):
    delete_files()
    return render(request,'myApp/index.html')

def convert(link):
        try :
            video_info = youtube_dl.YoutubeDL().extract_info( url = link,download=False)
            filename = f"./static/music/{round(time.time())+6000}.mp3"
            options={
            'format':'bestaudio/best',
            'keepvideo':False,
            'outtmpl':filename,
            }
            with youtube_dl.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])
            return filename
        except:
            return False
def download(request):
        if request.method == "POST":
            try :
                link = request.POST.get('link')
                # filename = convert(link)
                filename  = True
                if filename != False:
                    filename=filename.split('/')[-1]
                    return HttpResponse(filename)
                else:
                    return HttpResponse('error')
            except :
                return HttpResponse('error')
        else:
            return HttpResponse('Not Allowed')
            

def delete_files():
    for i in os.listdir('./static/music'):
        file_time = i.split('.')[0]
        if (time.time() > int(file_time)):
            os.remove('./static/music/'+i)


    
    