FROM ubuntu:20.04

# переменные окружения через которые можно передать ключи для запуска тестов
ENV BROWSER='chrome'
ENV URL='https://mebel.max-demo.ru/'
ENV EXECUTOR='192.168.31.145'
ENV BROWSER_VER='92'
ENV XDIST='1'
ENV VNC=''
ENV VIDEO=''
# переменная для выбора тестов, которые следует запустить (например: -e "TEST=-k test_currency")
ENV TEST=''

# создание директория для тестов
RUN mkdir tests_mebel_max

# смена рабочего директория
WORKDIR /tests_mebel_max

# копирование файла окружения с хоста
COPY requirements.txt .

# установка всех необходимых зависимостей
RUN apt update && \
    apt install software-properties-common -y && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt install python3.8 -y && \
    apt install pip -y && \
    pip install -r requirements.txt

# копирование всех тестов с хоста
COPY . .

# смена рабочего директория
WORKDIR /tests_mebel_max/tests

# запуск тестов в зависимости от установок в переменных окружения
CMD pytest -v --tb=short --url=${URL} --browser=${BROWSER} --browser_ver=${BROWSER_VER} --executor=${EXECUTOR} -n=${XDIST} ${VNC} ${VIDEO} ${TEST}
