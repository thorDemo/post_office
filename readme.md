![自建邮局](http://www.chinapost.com.cn/res/chinapostplan/structure/181041269.png)

---
**自建邮局服务器**

* 系统环境
<code>
    <br/>
    ubuntu16.04
    <br/>
    2 cpu+ 4gb+
</code>

* 安装 python3.7
<code>
    <br/>
    wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
    <br/>
    bash Anaconda3-2019.10-Linux-x86_64.sh
</code>
* 安装环境
<code>
    <br/>
    pip install requirements.txt
</code>
* 运行
<code>
    <br/>
    nohup python -u web_server_api.py > send_email.log 2>&1 &
</code>
