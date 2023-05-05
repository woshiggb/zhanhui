from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

def get_file_icon(filename):
    # 根据文件类型返回不同的按钮颜色
    ext = os.path.splitext(filename)[-1]
    if ext == '.txt':
        return 'secondary'
    elif ext in ('.jpg', '.jpeg', '.png', '.gif'):
        return 'info'
    elif ext == '.pdf':
        return 'danger'
    else:
        return 'primary'

@app.route('/')
def index():
    # 获取 './ziyuan' 目录中的所有文件名
    file_names = os.listdir('./ziyuan')
    # 过滤掉非文件的子目录
    file_names = [f for f in file_names if os.path.isfile(os.path.join('./ziyuan', f))]
    # 对文件名进行排序
    file_names.sort()
    # 构造文件路径列表
    file_paths = ['/ziyuan/' + name for name in file_names]
    # 将文件名和对应的路径打包为元组列表
    files = zip(file_names, file_paths)
    # 渲染 HTML 模板
    return render_template('index.html', files=files, get_file_icon=get_file_icon)

@app.route('/ziyuan/<path:filename>')
def serve_file(filename):
    # 返回文件内容
    return send_from_directory('./ziyuan', filename)

if __name__ == '__main__':
    app.run()
