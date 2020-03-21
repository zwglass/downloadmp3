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
        # print(type(requests))

        headers = {
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'DNT': '1',
            'Host': 'isure.stream.qqmusic.qq.com',
            'Range': 'bytes=0-',
            'Referer': 'https://y.qq.com/portal/player.html',
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'Cookie': '',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        }

        use_request_type = getattr(requests, request_type)
        res = use_request_type(mp3_url, headers=headers)
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
    url = 'https://isure.stream.qqmusic.qq.com/C400001R0QWN3gDgIN.m4a?guid=410688340&vkey=6986450083FF460662D950519E593459F9D80BD7E8B74C0619AF56385410A22C8B657D02FB0B648BF0C2015D2823FD990EFC56316F375778&uin=1906&fromtag=66'
    # MP3保存文件夹
    # save_url='D:/music/'
    save_url = '/Users/zhaoshenghua/development/downloadedFiles'
    # MP3文件名
    file_names = ['myMusic1.m4a', 'myMusic2.mp3', 'myMusic2.mp4', 'greyRoad.m4a']
    file_name = file_names[3]
    DownloadFile(url, save_url, file_name, 'get')