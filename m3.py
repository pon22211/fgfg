9from PyQt5.QtWidgets import Qwidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win=Qwidget()

lb_quest=Qwidget('Введіть запитання:')
lb_right_ans=QLabel('Введіть правильну відповідь:')
lb_wrong_ans1=QLabel('Введіть першу неправильну відповідь:')
lb_wrong_ans2=QLabel('Введіть другу неправильну відповідь:')
lb_wrong_ans3=QLabel('Введіть трутю неправильну відповідь:')

le_question=QLineEdit()
le_right_ans=QLineEdit()
le_right_ans1=QLineEdit()
le_right_ans2=QLineEdit()
le_right_ans3=QLineEdit()
lb_header_start=QLabel('Статистика')
lb_statistic=QLabel()

v1_labels=QVBoxLayout()
v1_labels.addWidget(lb_quest)
v1_labels.addWidget(lb_right_ans)
v1_labels.addWidget(lb_wrong_ans1)
v1_labels.addWidget(lb_wrong_ans2)
v1_labels.addWidget(lb_wrong_ans3)

v1_LineEdits=QVBoxLayout()
v1_LineEdits.addWidget(le_question)
v1_LineEdits.addWidget(le_right_ans)
v1_LineEdits.addWidget(le_wrong_ans1)
v1_LineEdits.addWidget(le_wrong_ans2)
v1_LineEdits.addWidget(le_wrong_ans3)

h1_question=QHBoxLayout()
h1_question.addLayout(v1_labels)
h1_question.addLayout(v1_LineEdits)

btn_back=QPushButton('Назад')
btn_add_question=QPushButton('Додати запитання')
btn_clear=QPushButton("Очистити")

h1_buttons=QHBoxLayout()
h1_buttons.addWidget(btn_add_question)
h1_buttons.addWidget(btn_clear)

v1_res=QVBoxLayout()
v1_res.addWidget(h1_question)
v1_res.addLayout(h1_buttons)
v1_res.addWidget(lb_header_start)
v1_res.addWidget(lb_statistic)
v1_res.addWidget(btn_back)
menu_win.setLayout(v1_res)
menu_win.resize(400, 300)