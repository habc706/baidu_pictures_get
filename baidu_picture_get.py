import requests
import time
# 注意：这里pn=  后面的数字是30的倍数，也是页面打开的数量限制！！！  # 最后1&e是一个时间戳！！！
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 '
                  'Safari/537.36 SLBrowser/7.0.0.6241 SLBChan/25 '
}
word = input('请输入你想要搜索的文字：')
number = input('请输入你想要获取的照片数量:')
num = 1
while num * 30 <= int(number):
    num = num + 1
imglist = []

for i in range(0, int(num)):
    finalurl = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10746385342931146838&ipn=rj&ct' \
               '=201326592&is=&fp=result&queryWord=%E6%9D%8E%E5%85%8B%E5%8B%A4%E5%9B%BE%E7%89%87' \
               '&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word={}' \
               '&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&nojc=&cg' \
               '=star&pn={}&rn=30&gsm=b4&{}='.format(
        word, (i + 1) * 30, time.time())

    response = requests.get(url=finalurl, headers=head).json()
    for j in range(0, len(response['data']) - 1):
        imglist.append(response['data'][j]['thumbURL'])
#
print(len(imglist))
for ke in range(0, int(number)):
    content = requests.get(url=imglist[ke], headers=head).content
    path = 'video\\'+str(ke)+'.png'
    with open(path, 'wb') as e:
        e.write(content)
print('ok')

