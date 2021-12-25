import curses
from time import sleep

s = [
[
'　∩　.∩',
'　.い_cノ　　／￣＞Ｏ',
'.c/･ ･っ　(ニニﾆ)△△',
'.（"●" )　.(･ω･ )[∥]　　',
'Ｏ┳Ｏﾉ)=[￣てﾉ￣￣]　　',
'◎┻し◎　◎――◎=  3',
],
[
'　∩　.∩',
'　.い_cノ　　／￣＞Ｏ',
'.c/･ ･っ　(ニニﾆ)△△',
'.（"●" )　.(･ω･ )[∥]　　',
'Ｏ┳Ｏﾉ)=[￣てﾉ￣￣]　　',
'◎┻し◎　◎――◎=    3',
],
[
'　∩　.∩',
'　.い_cノ　　／￣＞Ｏ',
'.c/･ ･っ　(ニニﾆ)△△',
'.（"●" )　.(･ω･ )[∥]　　',
'Ｏ┳Ｏﾉ)=[￣てﾉ￣￣]　　',
'◎┻し◎　◎――◎=     3',
],
[
'　∩　.∩',
'　.い_cノ　　／￣＞Ｏ',
'.c/･ ･っ　(ニニﾆ)△△',
'.（"●" )　.(･ω･ )[∥]　　',
'Ｏ┳Ｏﾉ)=[￣てﾉ￣￣]　　',
'◎┻し◎　◎――◎=       3',
],
[
'　∩　.∩',
'　.い_cノ　　／￣＞Ｏ',
'.c/･ ･っ　(ニニﾆ)△△',
'.（"●" )　.(･ω･ )[∥]　　',
'Ｏ┳Ｏﾉ)=[￣てﾉ￣￣]　　',
'◎┻し◎　◎――◎=          3',
],
]

mxs = -10**100
for i in range(len(s)):
   mxs = max(mxs, len(s[i]))

t = [
"                                _               ",
" _____                    __ __| |              ",
"|     |___ ___ ___ _ _   |  |  |_|_____ ___ ___ ",
"| | | | -_|  _|  _| | |  |-   -| |     | .'|_ -|",
"|_|_|_|___|_| |_| |_  |  |__|__| |_|_|_|__,|___|",
"                  |___|                         ",
]

# 初期化
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)

h, w = stdscr.getmaxyx()
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)

for shift in range(w - mxs - 10):
   stdscr.erase()
   # タイトル
   for i in range(len(t)):
      stdscr.addstr(i + 1, w // 2 - len(t[i]) // 2, t[i], curses.color_pair(1))

   # サンタさん
   for i in range(len(s[shift // 4 % len(s)])):
      stdscr.addstr(i + 15, w - shift - mxs - 10, s[shift // 4 % len(s)][i])
   stdscr.refresh()
   sleep(0.045)

# 終了処理
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()