

from os import path
import json


class ErrorBook:
    def __init__(self) -> None:
        self.filename = path.join('Log', 'errorbook.json')
        if path.exists(self.filename):
            self.exist = True
            with open(self.filename, 'r') as fo:
                self.qs = json.load(fo)
        else:
            self.exist = False
            self.qs = []

    def addErrorBook(self, value1, sign, value2, result):

        error_q = {'value1': value1,
                   'sign': sign,
                   'value2': value2,
                   'result': result,
                   'error_count': 1
                   }
        is_same_question = False
        for q in self.qs:
            if q['value1'] == value1 and q['sign'] == sign and q['value2'] == value2:
                q['error_count'] += 1
                is_same_question = True
                break
        if is_same_question == False:
            self.qs.append(error_q)

    def reduceErrorCount(self, id):
        for q in self.qs:
            print(q)
        print(self.qs[id])
        self.qs[id]['error_count'] -= 1

    def uploadErrorBook(self):
        with open(self.filename, 'w') as fi:
            json.dump(self.qs, fi)
