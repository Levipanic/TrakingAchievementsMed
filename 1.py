import csv

months = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь",
          10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}

with open("scientist.csv", encoding="utf-8") as file:
    scientists = list(csv.DictReader(file, delimiter=','))
    count_prep = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, }
    for line in scientists:
        count_prep[int(line['date'][5:7])] += 1 #устанавливаем соотношение месяца и числа препаратов в этом месяце

    resulted=[] #список словарей  в формате месяц - название месяца, число - число препаратов в этом месяце
    for x in range(1,13):
        resulted.append({'month':months[x], 'count': count_prep[x]})



with open('scientist_new.csv', 'w', encoding='utf-8', newline='') as newfile:
    w = csv.DictWriter(newfile, delimiter=',', fieldnames=['month', 'count'])
    w.writeheader()
    w.writerows(resulted)

with open('scientist_new.csv',  encoding='utf-8', newline='') as file:
    lines=list(csv.DictReader(file, delimiter=','))
    maxedprep=0 #наибольшее число препаратов
    maxedmonth=0 #соответствующий максимальному числу перапатов месяц
    for i in lines:
        if int(i['count'])>maxedprep:
            maxedprep=max(maxedprep,int(i['count']))
            if maxedprep==int(i['count']):
                maxedmonth=i['month']
    print(f'{maxedmonth} наиболее благоприятен для ученых. В этом месяце было создано - {maxedprep} препарат(-а)')
