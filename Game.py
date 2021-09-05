from os import path, terminal_size
import json
import random
import time
from ErrorBook import ErrorBook


class Game():
    def __init__(self, cfg_filename=None) -> None:
        if cfg_filename == None:
            self.cfg_filename = path.join('Cfg', 'cfg.json')
        else:
            self.cfg_filename = cfg_filename
        with open(self.cfg_filename, 'r') as fo:
            self.parameter = json.load(fo)
        print(self.parameter)
        self.next_q = False
        self.is_done = False
        self.num_questions = {'Add': 0,
                              "Subtract": 0,
                              "Multiply": 0,
                              "Divide": 0}
        self.total_counts = self.parameter['num_of_questions'] * \
            len(self.parameter['cases'])
        self.number_pass = 0
        self.errorbook = ErrorBook()
        self.score = 0
        self.number_fail = 0
        self.number_answer = 0
        self.conditions = self.parameter['Conditions']
        self.single_question_duration = self.parameter['time_duration_per_question']

    def getMaxWeight(self):
        weights = []
        for sign in self.conditions:
            weights.append(self.conditions[sign]['weight'])
        return max(weights)

    def provideQuestions(self):
        # for case in self.parameter['cases']:
        #     for count in range(self.parameter['num_of_questions']):
        #         print('current sign is', case, '. Count is ', count)
        #         self.value1, self.sign, self.value2, self.result = self.getEachLabels(
        #             sign=case)
        #         self.wait_until()
        if self.errorbook.exist and len(self.errorbook.qs) > 0:
            return (self.errorbook.qs[0]['value1'],
                    self.errorbook.qs[0]['sign'],
                    self.errorbook.qs[0]['value2'],
                    self.errorbook.qs[0]['result'])
        else:
            while True:
                i = random.randint(0, len(self.parameter['cases'])-1)
                sign = self.parameter["cases"][i]
                if self.num_questions[sign] >= self.parameter['num_of_questions']:
                    sum = 0
                    for key, value in self.num_questions.items():
                        sum += value
                    if sum >= self.parameter['num_of_questions']*len(self.parameter['cases']):
                        self.is_done = True
                        print('Test is Done.')
                        return None
                else:
                    return self.getEachLabels(sign)

    def getEachLabels(self, sign, value1=None, value2=None, result=None):
        # if value1 != None and value2 != None and result != None:
        #     return value1, sign,
        value1 = 0
        value2 = 0
        if sign == 'Add':
            value1, value2, result = self.getValuesForAdd()
            self.num_questions['Add'] += 1
        elif sign == 'Subtract':
            value1, value2, result = self.getValuesForSubtract()
            self.num_questions['Subtract'] += 1
        elif sign == 'Multiply':
            value1, value2, result = self.getValuesForMultiply()
            self.num_questions['Multiply'] += 1
        elif sign == 'Divide':
            value1, value2, result = self.getValuesForDivide()
            self.num_questions['Divide'] += 1
        self.value1 = value1
        self.sign = sign
        self.value2 = value2
        self.result = result
        self.results_array = []
        return value1, sign, value2, result

    def getValuesForAdd(self):
        value1 = random.randint(
            self.parameter["Conditions"]["Add"]["min"], self.parameter["Conditions"]["Add"]["max"])
        value2 = random.randint(
            self.parameter["Conditions"]["Add"]["min"], self.parameter["Conditions"]["Add"]["max"])
        return value1, value2, value1+value2

    def check(self, current_result, time_left):
        if current_result == self.result:  # May have problem if the result is not int
            print("pass")
            self.number_pass += 1
            if time_left > self.single_question_duration * 2/3:
                price = 3 * self.conditions[self.sign]['weight']
            elif time_left > self.single_question_duration / 3:
                price = 2 * self.conditions[self.sign]['weight']
            else:
                price = 1 * self.conditions[self.sign]['weight']
            if len(self.results_array) != 0:
                if self.results_array[-1]['status'] == True:
                    price += self.results_array[-1]['price']
            self.results_array.append({'status': True, 'price': price})
            self.score += price
            return True, price
        else:
            print("fail")
            self.number_fail += 1
            if time_left > self.single_question_duration * 2/3:
                price = (self.getMaxWeight()+1 -
                         self.conditions[self.sign]['weight']) * 3
            elif time_left > self.single_question_duration / 3:
                price = (self.getMaxWeight()+1 -
                         self.conditions[self.sign]['weight']) * 2
            else:
                price = (self.getMaxWeight()+1 -
                         self.conditions[self.sign]['weight']) * 3

            self.results_array.append({'status': False, 'price': price})
            self.score -= price
            self.errorbook.addErrorBook(
                self.value1, self.sign, self.value2, self.result)
            return False, price

    def getValuesForSubtract(self):
        count = 0
        while True:
            value1 = random.randint(
                self.parameter["Conditions"]["Subtract"]["min"], self.parameter["Conditions"]["Subtract"]["max"])
            value2 = random.randint(
                self.parameter["Conditions"]["Subtract"]["min"], self.parameter["Conditions"]["Subtract"]["max"])
            if self.parameter["Conditions"]["Subtract"]['allow_negtive']:
                return value1, value2, value1-value2
            else:
                if value1 > value2:
                    return value1, value2, value1-value2
            if count > 100:
                print('getValuesForSubtract count =', count)
                break
            count += 1

    def getValuesForMultiply(self):

        value1 = random.randint(
            self.parameter["Conditions"]["Multiply"]["min"], self.parameter["Conditions"]["Multiply"]["max"])
        value2 = random.randint(
            self.parameter["Conditions"]["Multiply"]["min"], self.parameter["Conditions"]["Multiply"]["max"])
        return value1, value2, value1*value2

    def getValuesForDivide(self):
        count = 0
        while True:
            value1 = random.randint(
                self.parameter["Conditions"]["Divide"]["min"], self.parameter["Conditions"]["Divide"]["max"])
            value2 = random.randint(
                self.parameter["Conditions"]["Divide"]["min"], self.parameter["Conditions"]["Divide"]["max"])
            if value2 == 0:  # value2 cannot be '0'
                continue
            if self.parameter["Conditions"]["Divide"]['allow_float']:
                # max 4 digists
                return value1, value2, round(value1/value2, 4)
            else:

                if value1 % value2 == 0:
                    return value1, value2, value1/value2
            if count > 10000:
                print('getValuesForDivide count =', count)
                return 1, 1
            count += 1


if __name__ == '__main__':
    game = Game()
