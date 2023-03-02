# emotions


### streamlit

这是一个超级简单的，免费的，能够快速帮助你部署你的python工程在web端的工具，你还可以用他提供的免费的 cloud云服务器 部署你的web应用。

1. 下载：

   `pip install streamlit`

2. 编写一个简单的 app.py

   ```python
   import streamlit as st
   st.write("Hello !!")
   ```

3. 运行：

   `streamlit run app.py`

4. 查看运行结果：在浏览器上


官网 https://streamlit.io/


#### 使用步骤：

此处我使用一个案例 一个检测图片情绪 的python应用(项目地址: [基于streamlit的识别应用 (github.com)](https://github.com/yjy249/emotions)) 介绍。

**视频检测**：<https://live.csdn.net/v/279590>

 编写你的 app.py文件

   文件名为：emotion_web.py

   主要功能是，上传图片，检测人脸，检测情绪，保存结果，输出结果
 

 尝试本地运行

   下载 streamlit : `pip install streamlit`

   开启：`streamlit run emotion_web.py`

   之后就会有一个连接出来，点击连接或者回自动跳到浏览器上显示运行结果。

 部署到云端 

   1. 使用 streamlit could [Cloud • Streamlit](https://streamlit.io/cloud)

      1. 申请一个免费的 could，过后你会收到一封邮件教你怎么部署 : [Your apps · Streamlit](https://share.streamlit.io/)

         1. 申请通过后会有一份邮件通知
         
      2. 将代码上传到github上

         1. 在github上新建一个仓库

            复制此仓库链接。

         2. clone到本地

             在本地打开终端 cd到你想要放工程的目录 ，然后输入命令 `git clone 链接`

         3. 将工程丢进去 clone 到本地的仓库


         4. 在本地目录下依次执行命令 `git add .` 、`git commit -m "push a streamlit project"`、`git push`

         

      3. 在 网站添加一个应用

         申请通过后 进入 [Your apps · Streamlit](https://share.streamlit.io/) 这个网址会提示你创建一个app就是你部署的应用
 

      4. 点击连接

         又可能会出现环境问题：如果运行不了查看管理终端，查看问题反馈。

         出现环境问题可以尝试更改 环境依赖文件 requirements.txt 等

         如果出错可以将requirements.txt文件内容用下面的内容替换
         

         

#### share your app

[Your apps · Streamlit](https://share.streamlit.io/)

1. 使用官网介绍的 share.streamlit.io
2. 结合github 仓库部署 
3. 免费社区版 可以拥有3个公共应用可以部署


#### 1.1.3. 遇到问题

1. 环境问题
2. 查找网站的 discuss：[Streamlit - Streamlit is the fastest way to build data apps.](https://discuss.streamlit.io/) 搜索你所出现的问题
3. 搜索引擎

