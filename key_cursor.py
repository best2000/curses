import curses, time, threading



def main(win):
    def c_mov(y, x):
        if y == maxs[0]:
            y = 0
        elif y < 0:
            y = maxs[0]-1
        elif x == maxs[1]-1:
            x = 0
        elif x < 0:
            x = maxs[1]-2
        win.move(c['y'], c['x'])
        win.delch()
        win.addstr(y, x, "#")
        c['y'] = y
        c['x'] = x  
        
    curses.echo(False)
    curses.cbreak(True)
    win.keypad(True)
    #win.nodelay(True) #no waiting
    curses.flash()
    maxs = win.getmaxyx()
    c = {'y':int(maxs[0]/2), 'x':int(maxs[1]/2)}
    win.addstr(c['y'], c['x'], "#")

    #default place
    win.addstr(0,0, "({}/{}, {}/{})".format(str(c['y']), str(maxs[0]), str(c['x']), str(maxs[1])))
    win.addstr(1,0, "no_input")
    while True:
        inp = win.getch()
        #time.sleep(0.1)
        #if inp == -1: #no input in buffer
            #inp = "no_input"
          #  win.addstr(0,0, inp)
           # win.refresh()
            #continue
            #c_mov(c['y'], c['x']+1)
        if inp == 358: #End key
            break
        elif inp == 258: #Down
            inp = 'Down'
            c_mov(c['y']+1, c['x'])
        elif inp == 259: #Up
            inp = 'Up'
            c_mov(c['y']-1, c['x'])
        elif inp == 260: #Left
            inp = 'Left'
            c_mov(c['y'], c['x']-1)
        elif inp == 261: #Right
            inp = 'Right'
            c_mov(c['y'], c['x']+1)
        else:
            inp = str(inp)
        win.move(0,0)
        win.clrtoeol() 
        win.move(1,0)
        win.clrtoeol()    
        win.addstr(0,0, "({}/{}, {}/{})".format(str(c['y']), str(maxs[0]), str(c['x']), str(maxs[1])))
        win.addstr(1,0, inp)
        win.refresh()
        #curses.flash()


win = curses.initscr()
curses.wrapper(main(win))
