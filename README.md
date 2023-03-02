# emotions


### 1.1 streamlit

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

官方文档介绍：

<img src="关于python项目部署这件事_md_files\image-20211024122616622.png" alt="image-20211024122616622" style="zoom:50%;" />

> 红色框住的是官方文档的集合

<img src="关于python项目部署这件事_md_files\image-20211024122646256.png" alt="image-20211024122646256" style="zoom:50%;" />

> 进去之后会看到三部分 分别是：基础教程"get started"、接口文档“API reference”、社区“app gallery”





#### 1.1.1 使用步骤：

此处我使用一个案例 一个检测图片情绪 的python应用(项目地址: [joker507/my_streamlit: 基于streamlit的识别应用 (github.com)](https://github.com/joker507/my_streamlit)) 介绍。

1. 编写你的 app.py文件

   文件名为：emotion_web.py

   主要功能是，上传图片，检测人脸，检测情绪，保存结果，输出结果


   

2. 导出你的环境文件

   可以环境文件可以使用多种之一：

   ### Add Python dependencies

   Streamlit looks at your requirements file's filename to determine which Python dependency manager to use in the order below. Streamlit will stop and install the first requirements file found.

   | **Filename**       | **Dependency Manager** | **Documentation**                                            |
   | ------------------ | ---------------------- | ------------------------------------------------------------ |
   | `Pipfile`          | pipenv                 | **[docs](https://pipenv-fork.readthedocs.io/en/latest/basics.html)** |
   | `environment.yml`  | conda                  | **[docs](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-file-manually)** |
   | `requirements.txt` | pip                    | **[docs](https://pip.pypa.io/en/stable/user_guide/#)**       |
   | `pyproject.toml`   | poetry                 | **[docs](https://python-poetry.org/docs/basic-usage/)**      |

   生产 requirements.txt :这是由pip软件管理的环境，你可以在**此工程环境** 下 使用命令生产 `pip freeze > requirementx.txt`

   `environment.yml` 是由 conda管理的环境生产，在 **此工程**环境下 使用 命令 `conda env export > environment.yml`

   

   下面是例程的 requirements.txt文件

   文件名：requirements.txt

   ```tex
   fer
   tensorflow>=1.7 
   opencv-contrib-python==3.3.0.9
   ```

   

3. 尝试本地运行

   下载 streamlit : `pip install streamlit`

   开启：`streamlit run emotion_web.py`

   之后就会有一个连接出来，点击连接或者回自动跳到浏览器上显示运行结果。

   ![image-20211025171130936](关于python项目部署这件事_md_files\image-20211025171130936.png)

   <img src="关于python项目部署这件事_md_files\image-20211025171148140.png" alt="image-20211025171148140" style="zoom:50%;" />

   

4. 部署到云端 

   1. 使用 streamlit could [Cloud • Streamlit](https://streamlit.io/cloud)

      1. 申请一个免费的 could，过后你会收到一封邮件教你怎么部署 : [Your apps · Streamlit](https://share.streamlit.io/)

         1. 申请通过后会有一份邮件通知
         2. ![image-20211025171521349](关于python项目部署这件事_md_files\image-20211025171521349.png)

      2. 将代码上传到github上

         1. 在github上新建一个仓库

            1. ![image-20211025191045040](关于python项目部署这件事_md_files\image-20211025191045040.png)
            2. ![image-20211025191138785](关于python项目部署这件事_md_files\image-20211025191138785.png)
            3. ![image-20211025191223308](关于python项目部署这件事_md_files\image-20211025191223308.png)
            4. 复制此仓库链接。

         2. clone到本地

            1. 在本地 打开终端 cd到你想要放工程的目录 ，然后输入命令 `git clone 链接`

         3. 将工程丢进去 clone 到本地的仓库

            ![image-20211025191342414](关于python项目部署这件事_md_files\image-20211025191342414.png)

            

         4. 在本地目录下依次执行命令 `git add .` 、`git commit -m "push a streamlit project"`、`git push`

         

      3. 在 网站添加一个应用

         申请通过后 进入 [Your apps · Streamlit](https://share.streamlit.io/) 这个网址会提示你创建一个app就是你部署的应用

         1. 

         ![image-20211025191407544](关于python项目部署这件事_md_files\image-20211025191407544.png)

         2. ![image-20211025191512502](关于python项目部署这件事_md_files\image-20211025191512502.png)

         3. ![image-20211025191613991](关于python项目部署这件事_md_files\image-20211025191613991.png)

         

      4. 点击连接

         ![image-20211025191818686](关于python项目部署这件事_md_files\image-20211025191818686.png)

         又可能会出现环境问题：如果运行不了查看管理终端，查看问题反馈。

         出现环境问题可以尝试更改 环境依赖文件 requirements.txt 等

         如果出错可以将requirements.txt文件内容用下面的内容替换，然后再本地工程目录下执行**将代码上传到github上**步骤

         ```tex
         fer
         tensorflow>=1.7 
         opencv-contrib-python==3.4.4.19
         opencv-python-headless
         
         ```

         

#### 1.1.2 share your app

[Your apps · Streamlit](https://share.streamlit.io/)

1. 使用官网介绍的 share.streamlit.io
2. 结合github 仓库部署 
3. 免费社区版 可以拥有3个公共应用可以部署

![image-20211025171442480](关于python项目部署这件事_md_files\image-20211025171442480.png)

问题?:环境 怎么配置 回:在工程中添加一个环境依赖文件



#### 1.1.3. 遇到问题

1. 环境问题

2. 查找网站的 discuss：[Streamlit - Streamlit is the fastest way to build data apps.](https://discuss.streamlit.io/) 搜索你所出现的问题
3. 搜索引擎

#### 1.1.4. 后续

你可以继续学习 streamlit的用法 在官网或者其他博客中

