from __future__ import unicode_literals
import youtube_dl
import requests

ydl_opts = {}
url = 'https://api.gfycat.com/v1/me/gfycats'
params = {
    'count': 400,
    'cursor': ''
}
headers = {
	'Authorization': '<YOUR_AUTH_HERE>'
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	while True:
		response = requests.get(url, params=params, headers=headers)
		
		if response.status_code != 200:
			print('Error:', response.status_code, response.text)
			break
			
		for gfy in response.json()['gfycats']:
			ydl.download(["https://www.gfycat.com/{}".format(gfy['gfyId'])])
		
		if 'cursor' in response.json():
			params['cursor'] = response.json()['cursor']
		else:
			break
