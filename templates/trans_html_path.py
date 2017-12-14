"""
    将html文件中的css js img绝对路径更改为static..
    如
        <link href="assets/css/bootstrap.min.css" rel="stylesheet">
        改为
        <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
    并在首行加上
        {% load static %}

    转换静态地址
    如
        hr_info.html
        改为
        {% url 'hr_info' %}


"""
import os

# 原始静态文件夹
static_name = 'assets'

postfix = ('css', 'js', 'jpg', 'png', 'gif')

# replace = {'.css': ".css' %"}
replace = {'.' + p: '.' + p + "'" + ' %}' for p in postfix}
replace[static_name + '/'] = "{% static '"

# 获取所有html
listdir = os.listdir()
htmls = [f for f in listdir if os.path.isfile(f) and os.path.splitext(f)[-1] == '.html']

# 跳转的静态地址
for html in htmls:
    html_name = html.split('.')[0]
    # {'hr_info.html': "{% url 'hr_info' %}"}
    replace['"{}"'.format(html)] = '\"{% url \'' + html_name + '\' %}\"'

for html in htmls:
    with open(html, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # 重写该文件
    with open(html, 'w', encoding='utf-8') as f_new:
        if 'load static' not in lines[0]:
            f_new.write('{% load static %}\n')
        for line in lines:
            # 替换掉所有
            if '{% static' not in line:
                for old, new in replace.items():
                    if old in line:
                        line = line.replace(old, new)
            f_new.write(line)
