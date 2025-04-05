# __Terminal SCB-Sh__

_Введение_

`Terminal SCB-Sh` используется для взаимодействия с устройством БФС-Ш, позволяет обрабатывать получаемые от устройства БФС-Ш данные и формировать их вывод, а так же позволяет обеспечить сохраняемость получаемых данных, как локально, так
и на удаленном сервере, позволяет выполнять настройку устройства БФС-Ш.

_Коротко об устройстве БФС-Ш_

Данное устройство выступает в качестве контрольной точки, служит для контроля прохода Ж/Д составов, фиксируя их проход по вагонно.

Информация формируемая устройством БФС-Ш в момент прохода Ж/Д состава:

- Направление по которому следует Ж/Д состав (наименование контрольной точки);
- Дата и время прохода Ж/Д состава через контрольную точку;
- Количество прошедших вагонов через контрольную точку;
- Количество колесных пар проходящего вагона прошедших через контрольную точку 
  (дает понимание о полном проходе вагона контрольной точки, расчет ведется отталкиваясь от осевой формулы 2о-2о);
- Скорость прохода контрольной точки каждого вагона проходящего Ж/Д состава;
 
Так же устройством БФС-Ш фиксируется и момент отсутствия прохода Ж/Д составом контрольной точки, о чем также будет сформированна соответствующая информация.

---

### __Детально о Terminal SCB-Sh__ ###

_Подготовка **Terminal SCB-Sh** через выполнение инструкций **StartTerminal.sh**_

Программа `Terminal SCB-Sh` представляет собой консольное приложение, для ее запуска используется файл 
`StartTerminal.sh` располагаемый в каталоге `Terminal_SCB_Sh/v0.0.0.1`. Его основная задача проверить и подготовить среду для выполнения программы `Terminal SCB-Sh`, а так же настроить локализацию для `Terminal SCB-Sh`.


```
./StartTerminal.sh
```


При запуске `Terminal SCB-Sh` появится первое диалоговое окно, где будет предложено выбрать язык для дальнейшей работы,
на данный момент доступны En и Ru. 

##### _ДОПОЛНЕНИЕ! Стоит помнить о "регистрочувствительности", по этому вводимые символы выбора языка должны быть в верхнем регистре._ #####

```
Terminal SCB-Sh v0.0.0.1
 
 ----------------------------------------------------------
 Select a language: English [E] (Выберите язык: Русский [R])
 ```
                                                         
Далее в процессе выполнения `StartTerminal.sh` будет выполнена проверка наличия `Python`, если `Python` установлен будет выведено сообщение: 

```
- Используемая версия Python 3.12.3
```

Если не установлен, появится диалоговое окно, в котором будет предложено установить `Python`.

```
WARNING! Проверьте установлен ли Python, это необходимо для выполнения программы Terminal SCB-Sh v0.0.0.1!
-----------------------------------------
Выполнить установку Python: Да[Y] или Нет[N]
```

Если отказаться от процесса установки будет сформировано сообщение: 

```
!!Процесс подготовки программы Terminal SCB-Sh v0.0.0.1 прерван!!
```

Если продолжить установку, первично будет выполнена проверка интернет-соединения, в случае отсутствия интернет-соединения будет сформировано сообщение:

```
!!Процесс подготовки программы Terminal SCB-Sh v0.0.0.1 прерван. Сбой интернет-соединения!!
```

В случае если проверка интернет-соединения пройдет успешно, установка `Python` будет продолжена, по ее завершению будет также сформировано сообщение:

```
- Используемая версия Python 3.12.3
```

Следующим шагом будет выполнена проверка файла `requirements.txt` о чем будет выведено сообщение:

```
Проверка наличия файла requirements.txt в корневом каталоге ...
```

Данный файл содержит перечень необходимых для работы `Terminal SCB-Sh` модулей, в случае его наличия будет продолжена корректная работа `StartTerminal.sh` с последующим выводом сообщения:

```
- Проверка requirements.txt пройдена успешно!
```

В случае его отсутствия будет сформировано сообщение, а работа `StartTerminal.sh` будет прекращена:

```
WARNING! Файл requirements.txt отсутствует в корневом каталоге, что может привести к некорректной работе программы!
-----------------------------------------------------
Для загрузки данного файла следует перейти по ссылке: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev
```

Так же `StartTerminal.sh` предусматривает ситуацию когда файл `requirements.txt` может быть изменен, поэтому в случае 
когда необходимые модули в файле `requirements.txt` не указаны, будет сформировано сообщение:

```
WARNING! Файл requirements.txt не содержит указания необходимых модулей, возможно данный файл был изменен локально! 
--------------------------------------------------------------------------
Для загрузки актуальной версии requirements.txt следует перейти по ссылке: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev
```

Следующим этапом будет проверено наличие `env` каталога о чем будет выведено сообщение:

```
Проверка виртуального окружения (env) ...
```

Если `env` каталог был ранее создан, далее происходит проверка установленных модулей в соответствии с модулями указанными в `requirements.txt`, если необходимые модули установлены, будет сформировано сообщение:

```
- Среда исполнения успешно подготовлена для запуска программы Terminal SCB-Sh v0.0.0.1!
```

Далее будет выполнен запуск программы `Terminal SCB-Sh` с последующим выводом сообщения:

```
Запуск программы ...
```

Если необходимые модули из `requirements.txt` отсутствуют, первично будет выполнена проверка интернет-соединения, в случае отсутствия интернет-соединения будет сформировано сообщение:

```
!!Процесс подготовки программы Terminal SCB-Sh v0.0.0.1 прерван. Сбой интернет-соединения!!
```

В случае если проверка интернет-соединения пройдет успешно, будет инициирован процесс установки модулей из 
`requirements.txt` с последующим выводом сообщения:

```
Идет процесс установки необходимых модулей ...
```

После завершения установки необходимых модулей будет выведено сообщение:

```
- Модули:
    <<Module_Name>>=<<Module_Version>>
    ...
    успешно установлены!
```

Далее будет сформировано сообщение о завершении подготовки среды для работы программы `Terminal SCB-Sh`:

```
- Среда исполнения успешно подготовлена для запуска программы Terminal SCB-Sh v0.0.0.1!
```

После чего будет выполнен запуск программы `Terminal SCB-Sh` с последующим выводом сообщения:

```
Запуск программы ...
```

В случае отсутствия каталога `env`, тот будет создан с последующим выводом сообщения:

```
Идет процесс создания виртуального окружения ...
```

После того как `env` каталог создан, будет сформировано сообщение:

```
- Виртуальное окружение (env) успешно создано
```

Далее будет выполнена установка необходимых модулей указанных в `requirements.txt`, но предварительно будет выполнена проверка интернет-соединения, если проверка интернет-соединения пройдет успешно, будет продолжен процесс установки необходимых модулей с последующим выводом сообщения:

```
Идет процесс установки необходимых модулей ...
```

В случае отсутствия интернет-соединения будет сформировано сообщение:

```
!!Процесс подготовки программы Terminal SCB-Sh v0.0.0.1 прерван. Сбой интернет-соединения!!
```

В случае успешной установки необходимых модулей будет сформировано сообщение:

```
- Модули:
    <<Module_Name>>=<<Module_Version>>
    ...
    успешно установлены!
```

Далее будет сформировано сообщение о завершении подготовки среды для работы программы `Terminal SCB-Sh`:

```
- Среда исполнения успешно подготовлена для запуска программы Terminal SCB-Sh v0.0.0.1!
```

После чего будет выполнен запуск программы `Terminal SCB-Sh` с последующим выводом сообщения:

```
Запуск программы ...
```
---

### __Работа Terminal SCB-Sh__ ###

При запуске программы `Terminal SCB-Sh` последовательно будет выведено следующее:

```
<< Терминал для взаимодействия с устройством БФС-Ш v0.0.0.1 >>

** Введите имя для файла логирования. (ПРИМЕР для Linux-based ОС: /home/UserName/TestLog) -> 
** Введите абсолютный путь для порта USB/RS-485. (ПРИМЕР для Linux-based ОС: /dev/ttyUSB0) ->
** Введите адрес устройства БФС-Ш. (ПРИМЕР: 5) ->
** Введите название контролируемого участка пути. (ПРИМЕР: (1361 Километр) станция Техникум) -> 
```
Если указать имя файла куда будут сохраняться данные получаемые от устройства БФС-Ш без указания абсолютного пути, данный файл будет создан в корневой директории.

Если при указании порта к которому подключено устройство БФС-Ш в имени порта допущена ошибка или устройство к данному порту не подключено, будет сформировано сообщение об ошибке:

```
!!! Убедитесь, что введенное вами название для порта USB/RS-485 правильно и адрес устройства БФС-Ш указан верно !!!
```

Так же данное сообщение будет выведено в случае если не верно указан адрес устройства БФС-Ш.
В заключении необходимо указать наименование места, где размещено устройство БФС-Ш, это может быть название станции или что-то подобное.

После того как вся необходимая информация указана, будет выполнена проверка наличия файла `ModbusRTUportConf.ini` в нем указаны необходимые настройки для порта по которому подключено устройство БФС-Ш, в случае его отсутствия будет сформировано сообщение:

```
!!! Файл конфигурации для порта USB/RS-485 не найден в корневом каталоге. Имя файла: ModbusRTUportConf.ini !!!
```
И выполнение программы `Terminal SCB-Sh` будет прервано, если указанный файл присутствует, выполнение программы будет продолжено.

Следующим шагом, будет выполнена корректировка времени на устройстве БФС-Ш в соответствии со временем установленном на устройстве, где функционирует программа `Terminal SCB-Sh`, о чем и будет сформировано сообщение:

```
Автокорректировка Даты и Времени на устройстве БФС-Ш выполнена Успешно!
```

Стоит учитывать, что программа  `Terminal SCB-Sh`  предполагает синхронизацию времени устройства на котором она работает в соответствии с протоколом  `NTP` , по этому так же будет выполнена проверка соединения с сетью, если соединение отсутствует, будет выведено предупреждающее сообщение:

```
Подключение к сети отсутствует!, Убедитесь, что Дата и Время PC/Laptop установлены верно!
```

Далее программа `Terminal SCB-Sh` переходит к опросу устройства БФС-Ш, о чем будет сформировано следующее сообщение:

```
************ Начат процесс контроля (прослушивания) Ж/Д пути. Направление: << Контролируемый участок пути >> ************
```

Если в этот момент времени нет проходящего состава будет сформировано  сообщение:

```
Движение на Ж/Д пути отсутствует. Направление: << Контролируемый участок пути >>
```

В момент прохода состава будет формироваться следующий вывод:

###### *пример выводимых данных* ######

```
Контрольная Точка: (1361 Километр) станция Техникум
Дата: 2025 Февраль 18 13:46:50
Дефект: Колесо без дефекта
Номер колесной пары проходящего вагона: 2
Количество прошедших вагонов: 2
Скорость прохода вагона контрольной точки (км/ч): 9.12
```

Полученные данные будут записаны в созданный ранее (на первом шаге) файл данных. Далее программа `Terminal SCB-Sh` ожидает прохода следующего колеса, если колесо не прошло через планируемый промежуток времени (данный промежуток так же рассчитывается программой  `Terminal SCB-Sh` исходя из скорости с которой прошло предыдущее колесо над точкой фиксации прохода), будет сформировано сообщение: 

```
Движение на Ж/Д пути отсутствует. Направление: << Контролируемый участок пути >>
```
В этот момент времени программа `Terminal SCB-Sh` возвращается к опросу устройства БФС-Ш, для получения информации.
Таким образом данная программа и выполняет функции по настройке устройства БФС-Ш, по визуализации данных, по обеспечению сохраняемости получаемых данных.

---

En Version Doc.

# __Terminal SCB-Sh__

_Introduction_

The `Terminal SCB-Sh` program is used to interact with the SCB-Sh device, allows you to process the data received from the SCB-Sh device and generate their output, as well as allows you to ensure the preservation of the received data, both locally and on a remote server, allows you to configure the SCB-Sh device.

_Briefly about the SCB-Sh device_

This device acts as a control point, it serves to control the passage of railway trains, fixing their passage along the carriage.

Information generated by the SCB-Sh device at the time of passage of the railway train:

- The direction followed by the railway train (name of the control point);
- Date and time of passage of the railway train through the checkpoint;
- The number of wagons passing through the checkpoint;
- The number of wheelsets of the passing car that passed through the checkpoint 
  (it gives an understanding of the complete passage of the control point car, the calculation is based on the axial formula 2o-2o);
- The speed of passage of the control point of each car of the passing railway train;

The SCB-Sh device also records the moment when the train does not pass through the checkpoint, which will also provide relevant information.

---

### __More information about Terminal SCB-Sh__ ###

_The preparation of **Terminal SCB-Sh** by following instructions **StartTerminal.sh**_

The Terminal SCB-Sh program is a console application that uses a file to run it. 
`StartTerminal.sh `located in the `Terminal_SCB_Sh/v0.0.0.1` directory. Its main task is to test and prepare the environment for the execution of the program `Terminal SCB-Sh`, as well as to configure localization for `Terminal SCB-Sh`.

```
./StartTerminal.sh
```

When you start `Terminal SCB-Sh`, the first dialog box will appear, where you will be prompted to select a language for further work, currently En and Ru are available.

##### _ADDITION! It is worth remembering about "case sensitivity", so the input characters of the language selection should be in uppercase._ #####

```
Terminal SCB-Sh v0.0.0.1
 
----------------------------------------------------------
Select a language: English [E] (Выберите язык: Русский [R])
```

Further in the execution process `StartTerminal.sh `the check for `Python` will be performed, if `Python` is installed, the message will be displayed:

```
- The Python 3.12.3 version used
```

If not installed, a dialog box will appear asking you to install `Python`.

```
WARNING! Check if Python is installed, it is necessary to run the Terminal SCB-Sh v0.0.0.1 program!
-----------------------------------------
Perform the Python installation: Yes[Y] or No[N] 
```

If you cancel the installation process, a message will be generated:

```
!!The Terminal SCB-Sh v0.0.0.1 program preparation process has been interrupted!!
```

If the Internet connection check is successful, the `Python` installation will continue, and a message will also be generated upon completion:

```
- The Python 3.12.3 version used
```

The next step is to check the file `requirements.txt ` what will the message be displayed about:

```
Checking for file availability requirements.txt in the root directory ...
```

This file contains a list of modules necessary for the operation of `Terminal SCB-Sh`. If available, correct operation will continue. `StartTerminal.sh ` followed by the output of the message:

```
- Verification requirements.txt completed successfully! 
```

In case of his absence, a message will be generated, and the work `StartTerminal.sh ` will be terminated:

```
WARNING! The file requirements.txt it is missing from the root directory, which may cause the program to malfunction! 
--------------------------------------------------------------------------
To download this file, follow the link: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev
```

The same way `StartTerminal.sh ` provides for a situation where the file `requirements.txt ` can be changed, so in case
the necessary modules are in the file `requirements.txt ` not specified, a message will be generated:

```
WARNING! The file requirements.txt It does not specify the necessary modules!
--------------------------------------------------------------------------
This file may have been modified locally to download the current version. requirements.txt follow the link: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev
```

The next step will be to check for the presence of an `env` directory, which will be indicated by a message:

```
Checking the virtual environment (env) ...
```

If the `env` directory was previously created, then the installed modules are checked in accordance with the modules specified in `requirements.txt `, if the necessary modules are installed, a message will be generated:

```
- The execution environment has been successfully prepared for the launch of Terminal SCB-Sh v0.0.0.1!
```

Next, the program `Terminal SCB-Sh` will be launched, followed by the output of the message:


```
Launching the program ...
```

If the required modules are from `requirements.txt ` missing, the Internet connection will be checked first, and if there is no Internet connection, a message will be generated:

```
!!The process of preparing the Terminal SCB-Sh v0.0.0.1 program has been interrupted. Internet connection failure!!
```

If the Internet connection check is successful, the module installation process will be initiated from 
`requirements.txt ` followed by the output of the message:

```
The necessary modules are being installed ...
```

After the installation of the necessary modules is completed, a message will be displayed:

```
- Modules:
    <<Module_Name>>=<<Module_Version>>
    .
    .
    .
  have been successfully installed!
```

Next, a message will be generated about the completion of the preparation of the environment for the operation of the Terminal SCB-Sh program`:

```
- The execution environment has been successfully prepared for the launch of Terminal SCB-Sh v0.0.0.1!
```

After that, the `Terminal SCB-Sh` program will be launched, followed by a message output:

```
Launching the program ...
```

If there is no `env` directory, it will be created and a message will be displayed:

```
The process of creating a virtual environment is underway ...
```

After the `env` directory is created, a message will be generated:

```
- The virtual environment (env) has been successfully created
```

Next, the installation of the necessary modules specified in `requirements.txt `, but an Internet connection check will be performed first, if the Internet connection check is successful, the installation process of the necessary modules will continue, followed by the output of the message:

```
The necessary modules are being installed ...
```

If there is no internet connection, a message will be generated:

```
!!The process of preparing the Terminal SCB-Sh v0.0.0.1 program has been interrupted. Internet connection failure!!
```

If the necessary modules are successfully installed, a message will be generated:

```
- Modules:
    <<Module_Name>>=<<Module_Version>>
    .
    .
    .
  have been successfully installed!
```

Next, a message will be generated about the completion of the preparation of the environment for the operation of the `Terminal SCB-Sh` program`:

```
Launching the program ...
```
---

### __Operation of the Terminal SCB-Sh program__ ###

When the program `Terminal SCB-Sh` is started, the following will be output sequentially:

```
<< Terminal for SCB-Sh Device v0.0.0.1 >>

** Enter some name for log file. (EXAMPLE for Linux based OS: /home/UserName/TestLog) -> 
** Enter Absolute path to USB/RS-485 port. (EXAMPLE for Linux based OS: /dev/ttyUSB0) -> 
** Enter Slave ModbusRTU Address. (EXAMPLE: 5) -> 
** Enter the name of the controlled path. (EXAMPLE: (1361 kilometers) Tekhnikum station) -> 
```

If you specify the file name where the data received from the SCB-Sh device will be saved without specifying the absolute path, this file will be created in the root directory.

If an error is made in the port name when specifying the port to which the SCB-Sh device is connected or the device is not connected to this port, an error message will be generated:

```
!!! Make sure the port name you enter is correct for USB/RS-485 and the address you enter for the Slave device is correct !!!
```

This message will also be displayed if the address of the SCB-Sh device is incorrect.
In conclusion, it is necessary to indicate the name of the place where the SCB-Sh device is located, it may be the name of the station or something similar.

```
!!! The configuration file for the USB/RS-485 port was not found in the root directory. File name: ModbusRTUportConf.ini !!!
```

And the execution of the program `Terminal SCB-Sh` will be interrupted, if the specified file is present, the program execution will continue. The next step is to adjust the time on the SCB-Sh device in accordance with the time set on the device where the `Terminal SCB-Sh` program is running, and a message will be generated about this:

```
The automatic Date and Time correction on the SCB-Sh device has been completed successfully!
```

It should be borne in mind that the `Terminal SCB-Sh` program assumes time synchronization of the device on which it runs in accordance with the `NTP` protocol, according to this, a network connection check will also be performed, if there is no connection, a warning message will be displayed:

```
There is no network connection!, Make sure that the Date and Time of the PC/Laptop is set correctly!
```

Next, the `Terminal SCB-Sh` program proceeds to query the SCB-Sh device, which will generate the following message:

```
************ Railway track listening started. Name of the direction: << Controlled section of the railway >> ************
```

If there is no passing train at this point in time, a message will be generated:

```
No train movement on the railway track. Name of the direction: << Controlled section of the railway >>
```

At the time of the train's passage, the following conclusion will be formed:

###### *example of output data* ######

```
Direction: (1361 kilometers) Tekhnikum station
Date: 2025 February 18 13:46:50
Defect: Wheel has no defects
Wheel: 2
Wagon: 2
Speed (km/h): 9.12
```

The received data will be written to the previously created (in the first step) data file. Next, the Terminal SCB-Sh program waits for the passage of the next wheel, if the wheel has not passed through the planned time interval (this interval is also calculated by the `Terminal SCB-Sh` program based on the speed at which the previous wheel passed over the passage fixation point), a message will be generated:

```
No train movement on the railway track. Name of the direction: << Controlled section of the railway >>
```

At this point in time, the program `Terminal SC-Sh` returns to the issue of the SCB-Sh device to receive information.
Thus, this program performs the functions of configuring the SCB-Sh device, visualizing data, and ensuring the preservation of the received data.