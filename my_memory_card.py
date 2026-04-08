#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
QHBoxLayout, QVBoxLayout, QPushButton, QRadioButton,
QLabel, QGroupBox, QButtonGroup)
from random import shuffle, randint

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(700, 500)

lb_Question = QLabel('Як буте на анліській словмо "мащина"?')
btn_Ok = QPushButton('Відповісти')

RadioGroupBox = QGroupBox('Варіанти відповілей')

rbnt_1 = QRadioButton('Bus')
rbnt_2 = QRadioButton('Car')
rbnt_3 = QRadioButton('Taxi')
rbnt_4 = QRadioButton('Ship')

RadioGroup = QButtonGroup()

RadioGroup.addButton(rbnt_1)
RadioGroup.addButton(rbnt_2)
RadioGroup.addButton(rbnt_3)
RadioGroup.addButton(rbnt_4)


layuot_ans1 = QHBoxLayout()
layuot_ans2 = QVBoxLayout()
layuot_ans3 = QVBoxLayout()

layuot_ans2.addWidget(rbnt_1)
layuot_ans2.addWidget(rbnt_2)

layuot_ans3.addWidget(rbnt_3)
layuot_ans3.addWidget(rbnt_4)

layuot_ans1.addLayout(layuot_ans2)
layuot_ans1.addLayout(layuot_ans3)

RadioGroupBox.setLayout(layuot_ans1)

AnsGroupBox = QGroupBox('Результат')
lb_Result = QLabel('Правильно / Неправльно')
lb_Correct = QLabel('писати правильну відповідь')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = Qt.AlignLeft | Qt.AlignTop)
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch = 2)

AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = Qt.AlignHCenter | Qt.AlignVCenter)
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_Ok, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1,stretch = 2)
layout_card.addLayout(layout_line2,stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch = 1)
layout_card.addStretch(1)

window.setLayout(layout_card)


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_Ok.setText('Відповісти')
    RadioGroup.setExclusive(False)
    rbnt_1.setChecked(False)
    rbnt_2.setChecked(False)
    rbnt_3.setChecked(False)
    rbnt_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_relust():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_Ok.setText('Наступне питання')

def show_correct(res):
    lb_Result.setText(res)
    show_relust()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


answers = [rbnt_1, rbnt_2, rbnt_3, rbnt_4]

def ask(q: Question):
    shuffle(answers) # [rbnt_3, rbnt_2, rbnt_4, rbnt_1]
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1    
        print('Statistics \n Total: ', window.total, '\n Right answer:', window.score) 
        print('Rating:', (window.score / window.total * 100), '%') 
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Statistics \n Total: ', window.total, '\n Right answer:', window.score) 
            print('Rating:', (window.score / window.total * 100), '%') 

def next_question(): ##################
    window.total += 1
    print('Statistics \n Total: ', window.total, '\n Right answer:', window.score) 
    print('Rating:', (window.score / window.total * 100), '%')
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_Ok():
    if btn_Ok.text() == 'Відповісти':
        check_answer()
    else:
        next_question()

question_list = []##################
question_list.append(Question('Як буте на анліській словмо "мащина"?', 'Car', 'Bus','Taxi', 'Ship'))
question_list.append(Question('Як буте на анліській словмо "яблуко"?', 'Apple', 'App','Application', 'Abroud'))##################

window.score = 0 
window.total = 0 

btn_Ok.clicked.connect(click_Ok)
next_question() ##################
window.show()
app.exec_()