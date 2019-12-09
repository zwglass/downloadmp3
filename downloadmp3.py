import os
import requests

def DownloadFile(mp3_url, save_url,file_name, request_type='get'):
    try:
        if mp3_url is None or save_url is None or file_name is None:
            print('参数错误')
            return None
        # 文件夹不存在，则创建文件夹
        folder = os.path.exists(save_url)
        if not folder:
            os.makedirs(save_url)
        # 读取MP3资源
        print(type(requests))
        use_request_type = getattr(requests, request_type)
        res = use_request_type(mp3_url)
        # res = requests.get(mp3_url)
        # 获取文件地址
        file_path = os.path.join(save_url, file_name)
        print('开始写入文件：', file_path)
        # 打开本地文件夹路径file_path，以二进制流方式写入，保存到本地
        with open(file_path, 'wb') as fd:
            for chunk in res.iter_content():
                fd.write(chunk)
        print(file_name+' 成功下载！')
    except Exception as e:
        print("程序错误:", e)

if __name__ == "__main__":
    # MP3源地址url
    # url = 'https://res.wx.qq.com/voice/getvoice?mediaid=MzU1Njc2MzY3M18yMjQ3NDg0MTkx'
    url = 'http://antiserver.kuwo.cn/anti.s?rid=MUSIC_79885733&response=res&format=mp3|aac&type=convert_url&br=128kmp3&agent=iPhone&callback=getlink&jpcallback=getlink.mp3'
    # MP3保存文件夹
    # save_url='D:/music/'
    save_url = '/Users/zhanwangyanjing/downloaded-music'
    # MP3文件名
    file_name = 'mymusic1.mp3'
    DownloadFile(url,save_url, file_name, 'get')