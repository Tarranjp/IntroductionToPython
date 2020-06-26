"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Joseph Tarrant.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

joseph = rg.SimpleTurtle('turtle')
joseph.pen = rg.Pen('red', 5)
joseph.speed = 1000

size = 300
for k in range(15) :
     joseph.draw_square(size)

     joseph.pen_up()
     joseph.right(45)
     joseph.forward(10)
     joseph.left(45)
     joseph.pen_down()
     size = size - 20

elliot = rg.SimpleTurtle('turtle')
elliot.pen = rg.Pen('blue', 5)
elliot.speed = 500

size = 200
for k in range(25) :
    elliot.draw_square(size)

    elliot.pen_up()
    elliot.right(45+k)
    elliot.forward(10)
    elliot.left(45)
    elliot.pen_down()
    size = size

