import modules.systemApi as systemApi
from time import sleep
import modules.colorsLog as colorsLog
import modules.errors as errors
import modules.art as art
import modules.activeWin as activeWin

colorsLog.greenlog(art.title)

# obtener version de windows
colorsLog.log('Obteniendo version de Windows...')
winVersion = systemApi.winVersion()
colorsLog.bluelog(winVersion)
colorsLog.log('---------------------------------------------')

# chequear si es administrador
colorsLog.log('Chequeando priviligios...')
isAdmin = systemApi.checkAdmin()
if (not(isAdmin)):
    colorsLog.log('Es administrador: ', ' ')
    colorsLog.errorlog(isAdmin)
    colorsLog.errorlog('|----------------------------------------------------------------|')
    colorsLog.errorlog('|----------------------------------------------------------------|')
    colorsLog.errorlog('|Este programa se debe ejecutar con privilegios de administrador.|')
    colorsLog.errorlog('|----------------------------------------------------------------|')
    colorsLog.errorlog('|----------------------------------------------------------------|')
    raise errors.NotAdmin('You are not admin')
colorsLog.log('Es administrador: ', ' ')
colorsLog.greenlog(isAdmin)

# chequear windows defender RTP (real time protection)
showstatus = True
if systemApi.checkWinDefender():
    windowsDefenderStatus = systemApi.checkWinDefender()
    while windowsDefenderStatus:
        colorsLog.log('Chequeando Windows defender...')
        windowsDefenderStatus = systemApi.checkWinDefender()
        colorsLog.log('Windows defender Real Time Protection: ', ' ')
        if windowsDefenderStatus:
            colorsLog.greenlog(windowsDefenderStatus)
        else:
            colorsLog.errorlog(windowsDefenderStatus)
            showstatus = False
            colorsLog.log('---------------------------------------------')
        colorsLog.errorlog('Windows defender está activado, por favor apaguelo por un momento')
        res = input('Presione la tecla Enter para volver a escanear')

if showstatus:
    colorsLog.log('Chequeando Windows defender...')
    _windowsDefenderStatus = systemApi.checkWinDefender()
    colorsLog.log('Windows defender Real Time Protection: ', ' ')
    colorsLog.errorlog(_windowsDefenderStatus)
colorsLog.log('---------------------------------------------')
sleep(2)

# activar
systemApi.clear()
colorsLog.greenlog('\nEmpezando activación\n')

colorsLog.log('Edición: ', ' ')
colorsLog.bluelog(winVersion)
colorsLog.log('Clave: ', ' ')
_key = activeWin.versions[winVersion[:-2]]

for key in _key:
    colorsLog.greenlog(key)

    colorsLog.log('\n|--------------------------------------------------------------------|')
    colorsLog.log('|--------------------------------------------------------------------|')
    colorsLog.log('|   A continuación acepte los 4 cuadros de dialogos que emergerán.   |')
    colorsLog.log('|           Si no ve alguno revise en la barra de tareas.            |')
    colorsLog.log('|--------------------------------------------------------------------|')
    colorsLog.log('|--------------------------------------------------------------------|\n')

    isActive = systemApi.active(key)

    if isActive:
        colorsLog.greenlog('La instalación ha sido exitosa.')
    else:
        colorsLog.errorlog('Un error ha ocurrido en algún punto de la activación.')
        colorsLog.errorlog('Se volverá a ejecutar la activación con otra clave')