import json
from datetime import datetime
import time

f = open(r'C:\Users\Sena\Downloads\messages.json', 'r',encoding="utf-8-sig")
data = json.load(f)
f.close()
 

#cData = json.dumps(data, indent=2)

#print (cData)

allKeys = ['sender', 'created_at', 'story_share', 'text', 'media_owner', 'media_share_caption', 
        'media_share_url', 'media', 'likes', 'live_video_invite', 'animated_media_images', 'is_random', 
        'user', 'link', 'media_url', 'voice_media', 'video_call_action']

#for block in data[1]['conversation']:
#    d_keys =block.keys()
#    for key in d_keys:
#        if key not in keys:
#            keys.append(key)
#    
#print(keys)

keys = set(['created_at', 'sender', 'text'])

def convTime(s):
    d = datetime.strptime(s[:-13], '%Y-%m-%dT%H:%M:%S')
    date = d.strftime('%d-%m-%Y')
    time = d.strftime('%H:%M:%S')
    return date , time

d = ''
c = 1 
end = convo['conversation'][-1]['created_at']
convo = data[1]
#for convo in data:#
#if convo['participants'] == ['le.vagalam', 'sena__ba']:
#    for com in convo['conversation']:
#     comKeys = set(com.keys())
#     if keys.issubset(comKeys):
#         date, time = convTime(com['created_at'])
#         if date != d:
#             c = c*-1
#             #print(com['created_at'])
#             if c == 1:
#                 print('close')
#             elif com['created_at'] == end:
#                 print('close')
#             print('\n'+'date: ' + date) 
#             d = date
#         print('\n' + com['sender'] +': ' +com['text'] +'  '+time )
#             
#print(data[1]['conversation'][-1]['created_at'])
             
#current_time = time.localtime()
#t = time.strftime('%Y-%m-%dT%H:%M:%S', current_time)

#day_string = current_time.strftime('%d-%m-%Y')
#print(day_string)
             
#print(data[1]['conversation'][8]['created_at'][:-13])


d = datetime.strptime('2019-02-17T22:22:11', '%Y-%m-%dT%H:%M:%S')
day_string = d.strftime('%b-%Y')

print(day_string)