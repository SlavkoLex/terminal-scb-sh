#!/bin/bash

# Internet connection verification function
function checkNetConnect {

    curlList=(https://www.google.com https://www.yandex.com)
    netStat=0

    for url in ${curlList[@]}; do

        if [[ $(curl -I $url | grep "HTTP/2 200") != "" ]]; then
            netStat=1
            break
        fi
    done

    return $(( $netStat ))
}

localization=()

pyVersion=$(python3 -V 2>/dev/null)


# Modules in requirements.txt
minimalmodbus=$(grep -E "minimalmodbus" requirements.txt 2>/dev/null)
pyserial=$(grep -E "pyserial" requirements.txt 2>/dev/null)
termcolor=$(grep -E "termcolor" requirements.txt 2>/dev/null)
requests=$(grep -E "requests" requirements.txt 2>/dev/null)


# Localization indexes
prepar=0
noPyWarn=1
pyInst=2
pyWarnStop=3
pySuccess=4
checkRequirements=5
noRequirements=6
crashRequirements=7
thereRequirements=8
checkEnv=9
initEnv=10
hiEnv=11
installModules=12
modules=13
successPrep=14
startProg=15
connectVerif=16


R=(
    "Подготовка программы Terminal SCB-Sh v0.0.0.1 ..." # $prepar
    "Проверьте установлен ли Python, это необходимо для выполнения программы Terminal SCB-Sh v0.0.0.1!
 -----------------------------------------
 Выполнить установку Python: Да[Y] или Нет[N]" # $noPyWarn
 "Идет процесс установки Python..." # $pyInst
 "!!Процесс подготовки программы Terminal SCB-Sh v0.0.0.1 прерван!!" # $pyWarnStop
 "- Используемая версия ${pyVersion}" # $pySuccess
 "Проверка наличия файла requirements.txt в корневом каталоге ..." # $checkRequirements
 "Файл requirements.txt отсутствует в корневом каталоге, что может привести к некорректной работе программы!
 ----------------------------------------------------
 Для загрузки данного файла следует перейти по ссылке: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev" # $noRequirements
 "Файл requirements.txt не содержит указания необходимых модулей, возможно данный файл был изменен локально! 
 --------------------------------------------------------------------------
 Для загрузки актуальной версии requirements.txt следует перейти по ссылке: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev" # $crashRequirements
 "- Проверка requirements.txt пройдена успешно!" # $thereRequirements
 "Проверка виртуального окружения (env) ..." # $checkEnv
 "Идет процесс создания виртуального окружения ..." # $initEnv
 "- Виртуальное окружение (env) успешно создано" # $hiEnv
 "Идет процесс установки необходимых модулей ..." # $installModules
 "- Модули:
    ${minimalmodbus}
    ${pyserial}
    ${termcolor}
    ${requests}\n успешно установлены!" # $modules
 "- Среда исполнения успешно подготовлена для запуска программы Terminal SCB-Sh v0.0.0.1!" # $successPrep
 "Запуск программы ..." # $startProg
 "!!Процесс подготовки программы Terminal SCB-Sh v0.0.0.1 прерван. Сбой интернет-соединения!!" # $connectVerif
)

E=(
    "Preparation of the Terminal SCB-Sh v0.0.0.1 program ..."
    "Check if Python is installed, it is necessary to run the Terminal SCB-Sh v0.0.0.1 program!
 -----------------------------------------
 Perform the Python installation: Yes[Y] or No[N]"
    "The Python installation process is underway ..."
    "!!The Terminal SCB-Sh v0.0.0.1 program preparation process has been interrupted!!"
    "- The ${pyVersion} version used"
    "Checking for file availability requirements.txt in the root directory ..."
    "The file requirements.txt it is missing from the root directory, which may cause the program to malfunction!
 ---------------------------------------------------------------
 To download this file, follow the link: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev"
    "The file requirements.txt It does not specify the necessary modules!
 --------------------------------------------------------------------------
 This file may have been modified locally to download the current version. requirements.txt follow the link: https://github.com/RailwayAutomationSolutions/Terminal_SCB_Sh/tree/dev"
 "- Verification requirements.txt completed successfully!" # The check was completed successfully!
 "Checking the virtual environment (env) ..."
 "The process of creating a virtual environment is underway ..."
 "- The virtual environment (env) has been successfully created"
 "The necessary modules are being installed ..."
 "- Modules:
    ${minimalmodbus}
    ${pyserial}
    ${termcolor}
    ${requests}\n have been successfully installed!"
 "- The execution environment has been successfully prepared for the launch of Terminal SCB-Sh v0.0.0.1!"
 "Launching the program ..."
 "!!The process of preparing the Terminal SCB-Sh v0.0.0.1 program has been interrupted. Internet connection failure!!"
)

# Вывод диалогового окна локализации 
while [ 1 -eq 1 ]
do

    printf "\033[1;39m Terminal SCB-Sh v0.0.0.1
 
 ----------------------------------------------------------
 Select a language: English [E] (Выберите язык: Русский [R]) \033[0m " 
    
    read input

    if [[ $input = "R" ]]; then
        localization=("${R[@]}")
        break
    
    elif [[ $input = "E" ]]; then
        localization=("${E[@]}")
        break

    fi

done

printf "\033[1;97m\n ${localization[$prepar]} \033[0m\n"

# Check Python
if [ "$pyVersion" = "" ]; then

    printf "\033[1;93m WARNING!\033[0;93m ${localization[$noPyWarn]} \033[0m\n"

    while [ 1 -eq 1 ]
    do
        read input 

        if [ $input = "Y" ]; then

            printf "\033[1;39m ${localization[$pyInst]} \033[0m\n"
            
            checkNetConnect

            if [[ $? -eq 1 ]]; then
                sudo apt-get update 
                pyVersion=$(sudo apt-get install python3)
            else
                printf "\033[1;31m ${localization[$connectVerif]}\n"
                exit 0
            fi

            break

        elif [ $input = "N" ]; then

            printf "\033[1;31m ${localization[$pyWarnStop]}\n"
            exit 0
    
        fi
    done
fi

printf "\033[1;32m ${localization[$pySuccess]} \033[0m\n"

# Check requirements.txt
printf "\033[1;97m ${localization[$checkRequirements]} \033[0m\n"

if [[ $(ls | grep -E requirements.txt) = "" ]]; then

    printf "\033[1;93m WARNING!\033[0;93m ${localization[$noRequirements]} \033[0m\n"

    exit 0

elif [[ "$minimalmodbus" = "" || "$pyserial" = "" || "$termcolor" = "" || "$requests" = "" ]]; then

    printf "\033[1;93m WARNING!\033[0;93m ${localization[$crashRequirements]} \033[0m\n"

    exit 0   

fi

printf "\033[1;32m ${localization[$thereRequirements]} \033[0m\n"

# Check env
printf "\033[1;97m ${localization[$checkEnv]}\033[0m\n"

if [[ $(ls | grep "env") = "" ]]; then 

    printf "\033[1;97m ${localization[$initEnv]} \033[0m\n"
    python3 -m venv env

    printf "\033[1;32m ${localization[$hiEnv]} \033[0m\n"

    printf "\033[1;97m ${localization[$installModules]} \033[0m\n"

    checkNetConnect

    if [[ $? -eq 1 ]]; then
        sudo apt-get update 
        env/bin/python3 env/bin/pip3 install -r requirements.txt
    else
        printf "\033[1;31m ${localization[$connectVerif]}\n"
        exit 0
    fi

    printf "\033[1;32m ${localization[$modules]}\033[0m\n"

    printf "\033[1;32m ${localization[$successPrep]} \033[0m\n"
    printf "\033[1;97m ${localization[$startProg]} \033[0m\n"
    env/bin/python3 src/main.py $input

else
        
    pipModules=$(env/bin/python3 env/bin/pip3 freeze | grep -E "minimalmodbus|pyserial|termcolor|requests")
    reqModules=$(grep -E "minimalmodbus|pyserial|termcolor|requests" requirements.txt)

    if [ "$pipModules" = "$reqModules" ]; then

        printf "\033[1;32m ${localization[$successPrep]} \033[0m\n"
        printf "\033[1;97m ${localization[$startProg]} \033[0m\n"
        env/bin/python3 src/main.py $input

    else 

        printf "\033[1;97m ${localization[$installModules]} \033[0m\n"

        checkNetConnect

        if [[ $? -eq 1 ]]; then
            sudo apt-get update 
            env/bin/python3 env/bin/pip3 install -r requirements.txt
        else
            printf "\033[1;31m ${localization[$connectVerif]}\n"
            exit 0
        fi
        
        printf "\033[1;32m ${localization[$modules]}\033[0m\n"

        printf "\033[1;32m ${localization[$successPrep]} \033[0m\n"
        printf "\033[1;97m ${localization[$startProg]} \033[0m\n"
        env/bin/python3 src/main.py $input

    fi

fi

exit 0
