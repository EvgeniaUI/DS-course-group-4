# Прогноз открытия вклада на предложенных условиях
Участники проекта: Короткова Анна, Игнатьева Евгения, Казырид Мария


### Цель: по различным характеристикам клиентов спрогнозировать целевую переменную - открыл ли клиент вклад на предложенных ему условиях или нет.

Описание признаков клиентов
Целевая переменная: deposit - has the client subscribed a term deposit? (binary: 'yes','no')

#### Описание полей

* deposit, (yes/no). Открыл ли клиент срочный депозит?
* age, numerical. Количество полных лет.
* job, categorical. Тип занимаемой должности ('admin.','blue-collar','entrepreneur','housemaid','management','retired','self-employed','services','student','technician','unemployed','unknown').
* marital, categorical. Cемейное положение ('divorced','married','single','unknown'; note: 'divorced' means divorced or widowed).
* education, categorical. Образование ('secondary','tertiary','primary','unknown').
* default, categorical. Имеется ли любой вид кредитования? ('no','yes','unknown').
* housing, categorical. Имеется ли ипотека? ('no','yes','unknown').
* loan, categorical. Имеется ли персональный кредит? ('no','yes','unknown')
* contact, categorical. Вид контакта с клиентом ('cellular','telephone','unknown').
* month, categorical. В каком месяце было сделано предыдущее предложение ('jan', 'feb', 'mar', ..., 'nov', 'dec').
* day, categorical. День недели было предыдущее предложение ('mon','tue','wed','thu','fri')
* duration, numerical. Продолжительность предыдущего общения в секундах. Important note: this attribute highly affects the output target (e.g., if duration=0 then y='no'). Yet, the duration is not known before a call is performed. Also, after the end of the call y is obviously known. Thus, this input should only be included for benchmark purposes and should be discarded if the intention is to have a realistic predictive model.
* campaign, numerical. Количество контактов по этой маркетинговой кампании с этим клиентов (includes last contact).
* pdays, numerical. Количество дней, прошедших с предыдущего предложения (число; -1 означает, что раньше не предлагали).
* previous, numerical. Количество контактов с этим клиентом в другие маркетинговые кампании.
* poutcome, categorical. Результат предыдущего предложения ('failure','other','success','unknown').
* balance, numerical. Закодированное название личной числовой характеристики клиента. (Кажется, это просто баланс на счете)
