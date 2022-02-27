# python-ddos
*beta version* 	

Програма для DDOS-атаки на пропагандистські російскі сайти.

## Встановлення
### Windows
1. Встановість программу на ваш пристрій [посиланням](https://drive.google.com/file/d/1whU2-Kc7EvQnrcPaZk9RCXeD56dOyn6A/view?usp=sharing)
2. Запустіть main.exe 
### Linux/MacOS
1. Встановість Docker:
```
 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io
```
2. Закачайте собі локально мій docker-образ:
```
 docker pull grayder/python-ddos:ddos
```
3. Запустіть контейнер:
```
 docker run --rm python-ddos
```
За замовчуванням скрипт працює в 200 потоків та із ввімкнутим логуванням.\
Якщо ви хочете змінити кількість потоків або вимкнути логування, виконайте наступну команду:
```
 docker run --rm python-ddos -t 1000 -wl
```
-t N - програма буде працювати в N потоків;\
-wl - програма буде працювати без логування;
  
Якщо ви хочете використати свій файл сайтів(файл формату .txt, в якому кожне посилання на сайт починається з нового рядка) виконайте наступну команду:
 
```
 docker run --rm -v <Повний шлях до вашого файлу>:/app/site_for_attack.txt python-ddos
```

### Для прохаваних

1) Клонуйте цей проєкт собі:
```
 git clone https://github.com/Grayder0152/python-ddos.git
```
2) Встановіть залежності:
```
 pip install -r requirements.txt
```
3) Запустіть програму:
```
  python3 main.py
```
 Думаю, далі самі розберетесь :)
