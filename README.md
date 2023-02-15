# Прогноз открытия вклада на подложенных условиях
Участники проекта: Короткова Анна, Игнатьева Евгения, Казырид Мария


### Цель: по различным характеристикам клиентов спрогнозировать целевую переменную - открыл ли клиент вклад на предложенных ему условиях или нет.

Описание признаков клиентов
Целевая переменная: deposit - has the client subscribed a term deposit? (binary: 'yes','no')

#### Описание полей

* age (numeric): количество полных лет
* job : тип занимаемой должности (categorical: 'admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown')
* marital : семейное положение (categorical: 'divorced','married','single','unknown'; note: 'divorced' means divorced or widowed)
* education (categorical: 'basic.4y','basic.6y','basic.9y','high.school','illiterate','professional.course','university.degree','unknown')
* default: имеется ли любой вид кредитования? (categorical: 'no','yes','unknown')
* housing: имеется ли ипотека? (categorical: 'no','yes','unknown')
* loan: имеется ли персональный кредит? (categorical: 'no','yes','unknown')
* contact: вид контакта с клиентом (categorical: 'cellular','telephone')
* month: в каком месяце было сделано предыдущее предложение (categorical: 'jan', 'feb', 'mar', ..., 'nov', 'dec')
* day: день недели было предыдущее предложение (categorical: 'mon','tue','wed','thu','fri')
* duration: продолжительность предыдущего общения в секундах. Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
* campaign: количество контактов по этой маркетинговой кампании с этим клиентов(numeric, includes last contact)
* pdays: количество дней, прошедших с предыдущего предложения(число; 999 означает, что раньше не предлагали)
* previous: количество контактов с этим лиентов в другие маркетинговые кампании(numeric)
* poutcome: результат предыдущего предложения (categorical: 'failure','nonexistent','success')
* balance - закодированное название личной числовой характеристики клиента

