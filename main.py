import systemApi
from colorsLog import errorlog, log, greenlog, bluelog
from errors import NotAdmin
from art import title
from activeWin import versions

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

systemApi.clear()
greenlog('\nEmpezando activación\n')

log('Edición: ', ' ')
bluelog(winVersion)
log('Clave: ', ' ')
greenlog(versions[winVersion[:-2]])

log('\n|--------------------------------------------------------------------|')
log('|--------------------------------------------------------------------|')
log('| A continuación acepte todos los cuadros de dialogos que emergerán. |')
log('|            si no ve alguno revise en a barra de tareas             |')
log('|--------------------------------------------------------------------|')
log('|--------------------------------------------------------------------|')


