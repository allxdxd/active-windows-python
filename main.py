import systemApi
from time import sleep
from colorsLog import errorlog, log, greenlog, bluelog
from errors import NotAdmin
from art import title, actived
from activeWin import versions
from options import menu

greenlog(title)

# obtener version de windows
log('Obteniendo version de Windows...')
winVersion = systemApi.winVersion()
bluelog(winVersion)
log('---------------------------------------------')

# chequear si es administrador
log('Chequeando priviligios...')
isAdmin = systemApi.checkAdmin()
if (not(isAdmin)):
    log('Es administrador: ', ' ')
    errorlog(isAdmin)
    errorlog('|----------------------------------------------------------------|')
    errorlog('|----------------------------------------------------------------|')
    errorlog('|Este programa se debe ejecutar con privilegios de administrador.|')
    errorlog('|----------------------------------------------------------------|')
    errorlog('|----------------------------------------------------------------|')
    raise NotAdmin('You are not admin')
log('Es administrador: ', ' ')
greenlog(isAdmin)

# chequear windows defender RTP (real time protection)
showstatus = True
if systemApi.checkWinDefender():
    windowsDefenderStatus = systemApi.checkWinDefender()
    while windowsDefenderStatus:
        log('Chequeando Windows defender...')
        windowsDefenderStatus = systemApi.checkWinDefender()
        log('Windows defender Real Time Protection: ', ' ')
        if windowsDefenderStatus:
            greenlog(windowsDefenderStatus)
        else:
            errorlog(windowsDefenderStatus)
            showstatus = False
            continue
        log('---------------------------------------------')
        errorlog('Windows defender está activado, por favor apaguelo por un momento')
        res = input('Presione la tecla Enter para volver a escanear')

if showstatus:
    log('Chequeando Windows defender...')
    _windowsDefenderStatus = systemApi.checkWinDefender()
    log('Windows defender Real Time Protection: ', ' ')
    errorlog(_windowsDefenderStatus)
log('---------------------------------------------')
sleep(2)

# activar
systemApi.clear()
greenlog('\nEmpezando activación\n')

log('Edición: ', ' ')
bluelog(winVersion)
log('Clave: ', ' ')
_key = versions[winVersion[:-2]]

for key in _key:
    greenlog(key)

    log('\n|--------------------------------------------------------------------|')
    log('|--------------------------------------------------------------------|')
    log('|   A continuación acepte los 4 cuadros de dialogos que emergerán.   |')
    log('|           Si no ve alguno revise en la barra de tareas.            |')
    log('|--------------------------------------------------------------------|')
    log('|--------------------------------------------------------------------|\n')

    isActive = systemApi.active(key)

    if isActive:
        greenlog(actived)
        print('Recuerde volver activar Windows defender\n')
        _input = input('Presione la letra "m" para ver otras opciones o cualquier otra tecla para terminar el programa. ')
        if _input == 'm':
            menu()
        else:
            exit()
    else:
        errorlog('Un error ha ocurrido en algún punto de la activación.')