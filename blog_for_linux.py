# -*- coding: utf-8 -*
import webbrowser  
import time    
import os    
import random
import requests
#s = requests.seesion()  
#count = random.randint(1,2)   
urllist=[ 
        'https://blog.csdn.net/fuqiuai/article/details/79495865',
        'https://blog.csdn.net/fuqiuai/article/details/80425532',
        'https://blog.csdn.net/fuqiuai/article/details/79495865',
        'https://blog.csdn.net/fuqiuai/article/details/80347126',
        'https://blog.csdn.net/fuqiuai/article/details/80106374',
        'https://blog.csdn.net/fuqiuai/article/details/79989934',
        'https://blog.csdn.net/fuqiuai/article/details/79898175',
        'https://blog.csdn.net/fuqiuai/article/details/79888863',
        'https://blog.csdn.net/fuqiuai/article/details/79871686',
        'https://blog.csdn.net/fuqiuai/article/details/79732564',
        'https://blog.csdn.net/fuqiuai/article/details/79528064',
        'https://blog.csdn.net/fuqiuai/article/details/79507206',
        'https://blog.csdn.net/fuqiuai/article/details/79507189',
        'https://blog.csdn.net/fuqiuai/article/details/79507164',
        'https://blog.csdn.net/fuqiuai/article/details/79507143',
        'https://blog.csdn.net/fuqiuai/article/details/79507117',
        'https://blog.csdn.net/fuqiuai/article/details/79507078',
        'https://blog.csdn.net/fuqiuai/article/details/79507053',
        'https://blog.csdn.net/fuqiuai/article/details/79507017',
        'https://blog.csdn.net/fuqiuai/article/details/79496005',
        'https://blog.csdn.net/fuqiuai/article/details/80003755',
        'https://blog.csdn.net/fuqiuai/article/details/79495910',
        'https://blog.csdn.net/fuqiuai/article/details/79495834',
        'https://blog.csdn.net/fuqiuai/article/details/79495807',
        'https://blog.csdn.net/fuqiuai/article/details/79484998',
        'https://blog.csdn.net/fuqiuai/article/details/79484929',
        'https://blog.csdn.net/fuqiuai/article/details/79484421',
        'https://blog.csdn.net/fuqiuai/article/details/79483057',
        'https://blog.csdn.net/fuqiuai/article/details/79482487',
        'https://blog.csdn.net/fuqiuai/article/details/79469412',
        'https://blog.csdn.net/fuqiuai/article/details/79458943',
        'https://blog.csdn.net/fuqiuai/article/details/79458648',
        'https://blog.csdn.net/fuqiuai/article/details/79458331',
        'https://blog.csdn.net/fuqiuai/article/details/79456971'
]

# 设置打开网页的浏览器
firefoxPath = r'/usr/share/app-install/desktop/Firefox Web Browser'            #  例如我的：C:\***\***\***\***\Google\Chrome\Application\chrome.exe 
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser(firefoxPath))  #这里的'firefox'可以用其它任意名字，这里将想打开的浏览器保存到'firefox'

for j in range(0,1000):#设置循环的总次数   
    i=0    
    while i<1 :  #一次打开浏览器访问的循环次数
        for url in urllist:
           #  webbrowser.get('firefox').open(url)  #访问网址地址，语法 .open(url,new=0,Autorasise=True),设置 new 的值不同有不同的效果0、1、2  
            webbrowser.open(url)
            i=i+1    
            time.sleep(2)  #设置每次打开新页面的等待时间
			
    else:    
        print('第%d遍刷完!'%(j+1))
        time.sleep(10) #设置每次等待关闭浏览器的时间  
        os.system('killall firefox')  #关闭进程。其他的更换下就行 #/F强制关闭进程  /T关闭的进程树及子树  /IM进程的映像名称


print('全部刷完收工！')
