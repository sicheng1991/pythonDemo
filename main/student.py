'Student'

__author__ = 'yangzteL'


class student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def printStudent(self):
        print('姓名：%s 分数：%s' % (self.name, self.score))

    # 支持序列化
    def student2dict(std):
        return {
            'name': std.name,
            'score': std.score
        }
    #反序列化
    def dict2student(d):
        return student(d['name'], d['score'])
