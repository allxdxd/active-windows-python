import systemApi
from colorsLog import errorlog, log, greenlog
from errors import NotAdmin
from art import title

greenlog(title)

# chequea si es administrador
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

# chequea windows defender RTP (real time protection)
log('Chequeando Windows defender...')
windowsDefenderStatus = systemApi.checkWinDefender()
if windowsDefenderStatus:
    log('Windows defender Real Time Protection: ', ' ')
    greenlog(windowsDefenderStatus)
    errorlog('Windows defender está activado')
