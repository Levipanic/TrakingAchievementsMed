import csv

# задача, возможно, содержит опечатку. прошу пересмотреть условие задачи (путаница с датой и названием препарата)

with open("scientist.csv", encoding="utf-8") as file:
    scientists = list(csv.DictReader(file, delimiter=','))
    while True:
        prepname=input()
        if prepname=='эксперимент':
            break
        for line in scientists:
            if prepname in line['preparation']:
                scientistname= line['ScientistName'].split()
                print(f'Ученый {scientistname[0]} {scientistname[1][0]}.{scientistname[2][0]}. создал препарат: {line['preparation']}')
            else:
                print('Этот препарат еще не создан')
