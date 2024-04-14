from pytube import YouTube

#https://www.youtube.com/watch?v=fhqv2RBHIGQ&pp=ygULa29udHJhdm9sdGE%3D

#Youtube nesnesi oluşturun.

def dowload_video(url):
    try:
        yt = YouTube(url)

        #En Yüksek çözünürlük için belirtmeliyiz.

        stream = yt.streams.get_highest_resolution()

        # indirme işlemi.

        stream.download()
        print("Video İndirildi.", stream.default_filename)
    
    except Exception as e:
        print("Bir Hata Oluştu.", e)

if __name__ == "__main__":
    video_url = input("Youtube Video URL'sini Giriniz...")
    dowload_video(video_url)