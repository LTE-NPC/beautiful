# 人脸识别评分，python3.6.6(代码比较乱，不喜欢迎来喷，谢谢)
# 需要安装pip install baidu-aip

from aip import AipFace
import base64


# 百度开发者官网获取key、id注册后就可以获取。
APP_ID = ''
API_KEY = ''
SECRET_KEY = ' '


# 初始化AipFace对象
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)


imageType = "BASE64"
options = {}
options["face_field"] = "age,gender,beauty"




def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        content = base64.b64encode(fp.read())
        return content.decode('utf-8')




# 读取图片
for j in range(1, 5):
    filePath = './img/%s.jpg' % j

    # 调用人脸识别
    result = aipFace.detect(get_file_content(filePath), imageType, options)
    # print(result)
    # print(type(result))
    results = result['result']
    face_list = results['face_list']
    i = face_list[-1]
    # 遍历字典
    print('评分越低[1-4]颜值越高')
    for key in i.keys():
        if isinstance(i[key], float):
            if i[key] >= 80:
                if i['gender']['type'] == 'female':
                    print('年龄:', i['age'], '性别:女 评分:1 得分:', i[key])
                else:
                    print('年龄:', i['age'], '性别:男 评分:1 得分:', i[key])
            elif i[key] >= 70:
                if i['gender']['type'] == 'female':
                    print('年龄:', i['age'], '性别:女 评分:2 得分:', i[key])
                else:
                    print('年龄:', i['age'], '性别:男 评分:2 得分:', i[key])
            elif i[key] >= 60:
                if i['gender']['type'] == 'female':
                    print('年龄:', i['age'], '性别:女 评分:3 得分:', i[key])
                else:
                    print('年龄:', i['age'], '性别:男 评分:3 得分:', i[key])
            elif i[key] < 60:
                if i['gender']['type'] == 'female':
                    print('年龄:', i['age'], '性别:女 评分:4 得分:', i[key])
                else:
                    print('年龄:', i['age'], '性别:男 评分:4 得分:', i[key])
