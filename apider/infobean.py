'Student'


class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def printStudent(self):
        print('姓名：%s 分数：%s' % (self.name, self.score))

