from fer import FER
import streamlit as st
import cv2
import numpy as np
import json
import datetime
import os


def draw_result(frame=None, result=None):
    for i in range(len(result)):
        result_max = max(result[i]["emotions"].items(), key=lambda x: x[1])
        emotion_type, emotion_value = result_max
        text = str(i)+emotion_type + ":" + str(emotion_value)
        
        x, y, w, h = result[i]["box"]
        point_top = np.array([x, y])
        point_bot = np.array([x + w, y + h])

        point_color = (0, 255, 0)
        thickness = 2
        lineType = 4

        cv2.rectangle(frame, tuple(point_top), tuple(point_bot), point_color, thickness, lineType)
        t_size = cv2.getTextSize(text, 1, cv2.FONT_HERSHEY_PLAIN, 1)[0]  # 获取文字框大小
        text_bot = point_top + np.array(list(t_size))
        cv2.rectangle(frame, tuple(point_top), tuple(text_bot), point_color, -1)

        # 计算文字偏移
        point_top[1] = point_top[1] + (t_size[1] / 2 + 4)

        cv2.putText(frame, text, tuple(point_top), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 0, 255), 1)

    else:
        print("detect None")

    return frame


img_dir = "img/"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

# 设置标题
st.title('''
情绪检测器
''')

# 描述文字
st.write("一个网络应用 检测图片中人物情绪 基于 streamlit")

# 上传图片
uploaded_file = st.file_uploader("上传一张图片，格式为 jpg、png", type=['jpg', 'png'])

if uploaded_file is None:
    st.text("请上传图片")
else:
    # image = Image.open(file)
    # # image = cv2.imread(file)
    # 读取图片
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)

    # 识别
    detector = FER(mtcnn=True)
    result = detector.detect_emotions(opencv_image)
    now = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    st.write(now)
    # 处理结果
    opencv_image = draw_result(opencv_image, result)
    st.image(cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB), use_column_width=True)
    cv2.imwrite(img_dir + now + ".jpg", opencv_image)

    # 日志处理：
    result[0]["time"] = now
    st.write(result)
    if not os.path.exists("streamlit_log.json"):  # 新写入
        with open("streamlit_log.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, separators=(',', ': '))
    else:  # 追加
        with open("streamlit_log.json", "r", encoding="utf-8") as f:
            old_data = json.load(f)
            old_data.append(result[0])
        with open("streamlit_log.json", "w", encoding="utf-8") as f:
            json.dump(old_data, f, indent=4, separators=(',', ': '))
