from pytube import YouTube

#link = input("Enter the link: ")
yt = YouTube('https://www.youtube.com/watch?v=PwmsQITuNYQ')

#Title of video
print("Title: ",yt.title)
#Number of views of video
print("Number of views: ",yt.views)
#Length of the video
print("Length of video: ",yt.length,"seconds")
#Description of video
print("Description: ",yt.description)
#Rating
print("Ratings: ",yt.rating)

#printing all the available streams
#print(yt.streams)

#print(yt.streams.filter(only_audio=True))
#print(yt.streams.filter(only_video=True))
#print(yt.streams.filter(progressive=True))

ys = yt.streams.get_highest_resolution()
#ys = yt.streams.get_by_itag('22')
ys.download()
print('Download completed')