#!/usr/bin/env python

"""
Hide and show the cursor.

# from jabbapylib.console import cursor
# from jabbapylib.console.cursor import CursorOff
"""

import os
import sys
from time import sleep
from jabbapylib.console.autoflush import unbuffered


#===============================================================================
# CursorOff class
#     can be used in a with block
#     it will set cursor back ON, whatever happens
#===============================================================================
    
class CursorOff(object):
    def __enter__(self):
        off()
        
    def __exit__(self, *args):
        on()

#===============================================================================
# switch the cursor off/on
#===============================================================================
        
def off():
    """Hide cursor."""
    os.system('setterm -cursor off')

    
def on():
    """Show cursor."""
    os.system('setterm -cursor on')


def wait(sec):
    """
    Wait X seconds and refresh the countdown every second.

    Return values:
    0 - OK, no interruption
    1 - countdown was interrupted
    """
    while sec > 0:
        sys.stdout.write(str(sec) + '     \r')
        sec -= 1
        try:
            sleep(1)
        except KeyboardInterrupt:
            print
            return 1
    #
    return 0

#############################################################################

if __name__ == "__main__":
    unbuffered()
    print '# cursor on:'
    on()
    wait(3)
    print '# cursor off:'
    off()
    wait(3)
    on()
    print '# with cursorOff:'
    with CursorOff():
        wait(3)