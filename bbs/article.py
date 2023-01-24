import re
def youtubeurl(a):
    url = a
    ur = re.split('[/=&]',url)
    if 'youtube' in ur[2]:
        if 'embed' in ur[3]:
            return url
        elif 'watch?v' in ur[3]:
            ur[3] = 'embed'
            a = ('https://www.youtube.com/embed/'+ur[4])
            t = a.replace(' ', '')
            return t
    elif 'youtu.be' in ur[2]:
        a = ('https://www.youtube.com/embed/'+ur[3])
        t = a.replace(' ', '')
        return t
    else:
        return 'Youtubeリンクではありません'