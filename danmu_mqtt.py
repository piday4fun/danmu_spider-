import requests
import json
import time
import paho.mqtt.client as mqtt
 
HOST = "solasolo.oicp.net"
PORT = 1883

def test(count,value):
    '''
    加量,加油'''
    data = {
            "count": count,
            "time": value
        }
    pl1 = json.dumps(data)
    client = mqtt.Client()
    client.connect(HOST, PORT, 60)
    client.publish("piday4fun/action", payload=pl1) # 发布一个主题为'chat',内容为‘hello liefyuan’的信息
    # client.loop_forever()

def getdm(roomid):
    global count
    cookies = {
        '$CURRENT_FNVAL': '16',
        '_uuid': '8F5A3A04-3516-688F-DFD9-1753EA4066F447985infoc',
        'LIVE_BUVID': 'AUTO6515732103534301',
        'stardustvideo': '1',
        'laboratory': '1-1',
        'rpdid': '|(J|JuukRu|Y0J\'ul~Jku|R|k',
        'buvid3': 'A194E945-535A-42A3-8750-6FE3F276CE8D155809infoc',
        'im_notify_type_393348954': '0',
        'CURRENT_QUALITY': '80',
        'DedeUserID': '393348954',
        'DedeUserID__ckMd5': '93fe03331b2665fe',
        'SESSDATA': '65dd27bc%2C1599566176%2C3f1cc*31',
        'bili_jct': 'abf20064ef38b1446eca56cca1b00fe5',
        'Hm_lvt_8a6d461cf92ec46bd14513876885e489': '1581755955,1584171299,1584171568,1584171588',
        'Hm_lpvt_8a6d461cf92ec46bd14513876885e489': '1584171588',
        '_dfcaptcha': '369355ebdd21c3cc50827acbfa7b5e75',
        'PVID': '21',
        'Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02': '1584011095,1584098246,1584098316,1584171697',
        'Hm_lpvt_8a6e55dbd2870f0f5bc9194cddf32a02': '1584171697',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'Sec-Fetch-Dest': 'empty',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://live.bilibili.com',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://live.bilibili.com/'+roomid,
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    }

    data = {
    'roomid': roomid,
    'csrf_token': 'abf20064ef38b1446eca56cca1b00fe5',
    'csrf': 'abf20064ef38b1446eca56cca1b00fe5',
    'visit_id': ''
    }
    response = requests.post('https://api.live.bilibili.com/ajax/msg', headers=headers, cookies=cookies, data=data)
    # print(response.text)
    result=response.json()
    danmus=result['data']['room']
    list1=[]
    f = open("piday.txt", "r",encoding="utf-8")
    for line in f.readlines():
        list1.append(line.replace("\n",""))
    # print(list1)
    
    for danmu in danmus:
        print("%s 网友:%s  评论了:%s"%(danmu['timeline'],danmu['nickname'],danmu['text']))
        if ("%s 网友:%s  评论了:%s"%(danmu['timeline'],danmu['nickname'],danmu['text'])) in list1:
            print("已经有了")
        else:
            print("新弹幕:")

            print("%s 网友:%s  评论了:%s"%(danmu['timeline'],danmu['nickname'],danmu['text']),file=open("piday.txt","a",encoding="utf-8"))
            if danmu['text']=="#加油":
                count+=1
                test(count,"1")
            if danmu['text']=="#加量":
                count+=1
                test(count,"10")
if __name__ == "__main__":
    count=0
    while 1:
        rid="598887"
        getdm(rid)
        print("运行")
        # test()
        time.sleep(5)
