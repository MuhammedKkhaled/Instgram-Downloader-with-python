import requests
import json
from tkinter import filedialog

url = "https://instagram-media-downloader.p.rapidapi.com/rapid/post.php"

posturl = input("Enter Your post Url >>>>> ")

filename = input("Enter File name>>>>>>>")

filelocate = filedialog.askdirectory()

querystring = {"url": posturl}

headers = {
    'x-rapidapi-host': "instagram-media-downloader.p.rapidapi.com",
    'x-rapidapi-key': "5a40937917mshe59e02f31b0b1efp16d112jsn400f6fe46610"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# Text to json to neglecate the string and transform it to Json

textojso = json.loads(response.text)


#  how to know if the input is video or image

postfileurl = ''

if 'video' in textojso:
    postfileurl = textojso['video']

else: postfileurl = textojso['image']

# get the info or extention for the file (png / mp4 / jbg )

reqpostfileurl = requests.get(postfileurl)

fileEx = reqpostfileurl.headers['Content-Type'].split('/')[-1].split('.')[0]

ffname = filelocate + '/' + filename + '.' + fileEx

# save file in device
# Wb is Write byte  ->  open the file and write all the bytes

with reqpostfileurl as rq:
    with open(ffname, 'wb') as file:
        file.write(rq.content)
print(ffname)