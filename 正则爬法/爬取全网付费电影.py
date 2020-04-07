# 流媒体 伪流媒体 实施流媒体
# 协议不同 HLS(APPLE) RTMP(ADOBE) RTSP(ColumbiaUniversty) MSS(MICROSOFT) FFMPEG(VLC)
import requests
movie_url = "https://jx.618g.com/?url=https://v.qq.com/x/cover/mzc00200sqw6k6u/i0031p1bg8z.html"

text = requests.get(movie_url).text

print(text)

# ffmpeg -i "里面放网址m3u8结尾" -vcodec copy -acodec copy"自定义名字"