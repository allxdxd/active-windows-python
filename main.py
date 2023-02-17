import checkSystem
from colorsLog import errorlog, log, greenlog
from errors import NotAdmin
from art import title

greenlog(title)

log('Chekeando priviligios...')
isAdmin = checkSystem.checkAdmin()
if (not(isAdmin)):
    log(f'Es administrador: {isAdmin}')
    errorlog('|----------------------------------------------------------------|')
    errorlog('|----------------------------------------------------------------|')
    errorlog('|Este programa se debe ejecutar con privilegios de administrador.|')
    errorlog('|----------------------------------------------------------------|')
    errorlog('|----------------------------------------------------------------|')
    raise NotAdmin('You are not admin')

log('Es administrador: ', ' ')
greenlog(isAdmin)

log('Chekeando Windows defender...')
windowsDefender = checkSystem.checkWinDefender()

