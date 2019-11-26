![自建邮局](http://www.chinapost.com.cn/res/chinapostplan/structure/181041269.png)

---
**自建邮局服务器**

* 系统环境

            ubuntu16.04
            2 cpu+ 4gb+

* 安装 python3.7

            wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
            bash Anaconda3-2019.10-Linux-x86_64.sh

* 安装环境

            pip install requirements.txt

* 运行

            nohup python -u web_server_api.py > send_email.log 2>&1 &
