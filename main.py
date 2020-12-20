# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    """
    更新Gui界面及接口位置、传入参数等
    """
    app = QApplication(sys.argv)
    # 创建一个应用（Application）对象
    # sys.argv参数是一个来自命令行的参数列表。Python脚本可以在shell中运行。这是我们用来控制我们应用启动的一种方法。
    w = QWidget()
    # Qwidget组件是PyQt5中所有用户界面类的基础类。我们给QWidget提供了默认的构造方法。默认构造方法没有父类。
    # 没有父类的widget组件将被作为窗口使用。

    w.resize(1000, 1000)  # 窗口大小
    w.move(30, 30)  # 窗口初始位置
    w.setWindowTitle('Simple')  # 标题
    w.show()  # 将窗口显示出来

    sys.exit(app.exec_())
    # 最后，应用进入主循环。在这个地方，事件处理开始执行。主循环用于接收来自窗口触发的事件，并且转发他们到widget应用上处理。
    # 如果我们调用exit()方法或主widget组件被销毁，主循环将退出。
    # sys.exit()方法确保一个不留垃圾的退出。系统环境将会被通知应用是怎样被结束的。
    # exec_()方法有一个下划线。因为exec是Python保留关键字。因此，用exec_()来代替。
