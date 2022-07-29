import curses 
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.refresh()
    stdscr.nodelay(True)
    curses.curs_set(0)
    wallsCol = False
    
    x, y = 1, 2
    while True:
        try:
            key = stdscr.getkey()
        except:
            key = None
    
        if key == "a":
            if stdscr.getch() != "#":
                y -= 2
        elif key == "d":
             if stdscr.getch() != "#":
                y += 2
        elif key == "w":
             if stdscr.getch() != "#":
                x -= 1
        elif key == "s":
             if stdscr.getch() != "#":
                x += 1
        
        stdscr.clear()
        
        stdscr.addstr(0, 0,"#############################################################")
        stdscr.addstr(1, 0,"# . . . . . . . . . . . . . . . . . . . . . . S H O P - - > ")      
        stdscr.addstr(2, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(3, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(4, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(5, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(6, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(7, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(8, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(9, 0,"# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #")
        stdscr.addstr(10, 0,"#############################################################")
         
        stdscr.addstr(x, y, "@")
        stdscr.refresh()
        
        
                
    
wrapper(main)