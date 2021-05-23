import time
from playsound import playsound



filename = "boxing-bell-start.mp3" 
campana = "campana.mp3" 



PomodoroTime = int(input("Dime el tiempo para las sesiones de estudio en minutos:  "));
PomodoroTime = PomodoroTime * 60; #para transformar a segundos

NumeroSesiones = int(input("Dime el numero de las sesiones de estudio :  "));
TiempoDescanso = int(input("Dime el tiempo de descanso entre las sesiones de estudio en minutos:  "));
TiempoDescanso = TiempoDescanso * 60; #para transformarconda a segundos

PomodoroTimeconst = PomodoroTime;
TiempoDescansoconst = TiempoDescanso;

ConteoSesiones = 1;

while NumeroSesiones > 0:
    
    print('--------------ESTUDIO----------------------')
    print('Empieza la sesion de estudio numero: ', ConteoSesiones)
    print('El tiempo de estudio empieza ahora')
    playsound(campana)
    while PomodoroTime:    
        mins = PomodoroTime // 60;  #*para tener en minutos*/
            #print(mins)
        secs = PomodoroTime % 60;  #para poder sacar el residuo y segundos
        timer = '{:02d}:{:02d}'.format(mins,secs)

        print(timer, end = "\r")  #\r para ponder en en la misma linea
        time.sleep(1)
        PomodoroTime -=1
    playsound(filename)
    print('Se acabo el tiempo de estudio')
    print('Se completaron los ',PomodoroTimeconst,' minutos de estudio')
    PomodoroTime = PomodoroTimeconst

    print('---------------DESCANSO---------------------')
    print('El tiempo de descanso empieza ahora')
    
    

    while TiempoDescanso:    
        minsDescanso = TiempoDescanso // 60;  #*para tener en minutos*/
            #print(mins)
        secsDescanso = TiempoDescanso % 60;  #para poder sacar el residuo y segundos
        timerDescanso = '{:02d}:{:02d}'.format(minsDescanso,secsDescanso)

        print(timerDescanso, end = "\r")  #\r para ponder en en la misma linea
        time.sleep(1)
        TiempoDescanso -=1

    print('Se acabo el tiempo de descanso')
    print('Se completaron los ',TiempoDescansoconst,' minutos de descanso')
    #print(NumeroSesiones)
    TiempoDescanso = TiempoDescansoconst;

    NumeroSesiones -=1
    ConteoSesiones += 1

print('*******************************************')
print('Se acabaron todas las sesiones de estudio')
print('Estudiaste ', ConteoSesiones-1, ' sesiones, por un tiempo total de ',PomodoroTimeconst*(ConteoSesiones-1), 'minutos de estudio')
