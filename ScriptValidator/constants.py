ROOT_OPEN = str.encode('<root>')
ROOT_CLOSE = str.encode('</root>')
END_LINE_OPEN = str.encode('<end_line>')
END_LINE_CLOSED = str.encode('<end_line/>')
THREE_DOTS_OPEN = str.encode('<three_dots>')
THREE_DOTS_CLOSED = str.encode('<three_dots/>')
PLAYER_NAME_OPEN = str.encode('<player_name>')
PLAYER_NAME_CLOSED = str.encode('<player_name/>')
PLAYER_NICKNAME_OPEN = str.encode('<player_nickname>')
PLAYER_NICKNAME_CLOSED = str.encode('<player_nickname/>')
ASCII_OPEN = str.encode('<ascii>')
ASCII_CLOSE = str.encode('<ascii/>')
HEARTH_OPEN = str.encode('<hearth>')
HEARTH_CLOSED = str.encode('<hearth/>')
PAW_OPEN = str.encode('<paw>')
PAW_CLOSED = str.encode('<paw/>')
PARTNER_OPEN =str.encode('<partner>')
PARTNER_CLOSED = str.encode('<partner/>')

NEWLINE = str.encode('\n')
PARTNER_LINE = str.encode('<partner ')
INFO_LINE = str.encode('<info')
PORTRAIT_L_LINE = str.encode('<portrait_l')
PORTRAIT_R_LINE = str.encode('<portrait_r')


LINE_ELS = [INFO_LINE, PORTRAIT_L_LINE, PORTRAIT_R_LINE, PARTNER_LINE]
SYMBOLS = ['three_dots', 'hearth', 'paw']
NAME_ELS = ['player_name', 'player_nickname', 'partner']

MAX_LINE_LENGTH = 36
SYMBOL_LEN = 2
NAME_EL_LEN = 8
