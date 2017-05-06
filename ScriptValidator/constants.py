ROOT_OPEN = str.encode('<root>')
ROOT_CLOSE = str.encode('</root>')
NEWLINE = str.encode('\n')
END_LINE_OPEN = str.encode('<end_line>')
END_LINE_CLOSED = str.encode('<end_line/>')
THREE_DOTS_OPEN = str.encode('<three_dots>')
THREE_DOTS_CLOSED = str.encode('<three_dots/>')
INFO_OPEN = str.encode('<info')
PLAYER_NAME_OPEN = str.encode('<player_name>')
PLAYER_NAME_CLOSED = str.encode('<player_name/>')
PLAYER_NICKNAME_OPEN = str.encode('<player_nickname>')
PLAYER_NICKNAME_CLOSED = str.encode('<player_nickname/>')
PORTRAIT_L_OPEN = str.encode('<portrait_l')
PORTRAIT_R_OPEN = str.encode('<portrait_r')
ASCII_OPEN = str.encode('<ascii>')
ASCII_CLOSE = str.encode('<ascii/>')
HEARTH_OPEN = str.encode('<hearth>')
HEARTH_CLOSED = str.encode('<hearth/>')
PAW_OPEN = str.encode('<paw>')
PAW_CLOSED = str.encode('<paw/>')

LINE_ELS = [INFO_OPEN, PORTRAIT_L_OPEN, PORTRAIT_R_OPEN]
SYMBOLS = ['three_dots', 'hearth', 'paw']
NAME_ELS = ['player_name', 'player_nickname']

MAX_LINE_LENGTH = 36
SYMBOL_LEN = 2
NAME_EL_LEN = 8
