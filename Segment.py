#Jusr R&D for Second FiPy to display on Segment Display. #NB execfile('/flash/Segment.py')
from machine import Pin
from utime import ticks_ms as ut
init_ut=ut()//1000
global ML_T,ML_M,ML_B,VL_RT,VL_LT,VL_LB,VL_RB,GL,GR
ML_T=Pin('P10', mode=Pin.OUT)#Middle Line Top            (ML_T)
ML_M=Pin('P5', mode=Pin.OUT)#Middle Line Middle           (ML_M)
ML_B=Pin('P7', mode=Pin.OUT)#Middle Line Bottom           (ML_B)
VL_RT=Pin('P11', mode=Pin.OUT)#Vertical Line Right Top    (VL_RT)
VL_LT=Pin('P12', mode=Pin.OUT)#Vertical Line Left Top     (VL_LT)
VL_RB=Pin('P6', mode=Pin.OUT)#Vertical Line Right Bottom   (VL_RB)
VL_LB=Pin('P9', mode=Pin.OUT)#Vertical Line Left Bottom    (VL_LB)
GL=Pin('P22', mode=Pin.OUT)#1=Right Int Active
GR=Pin('P23', mode=Pin.OUT)#1=Left Int Active
ML_T.value(0)
ML_M.value(0)
ML_B.value(0)
VL_RT.value(0)
VL_LT.value(0)
VL_RB.value(0)
VL_LB.value(0)
GL.value(0)
GR.value(0)
setting=100
number=0
def display(num):
    global ML_T,ML_M,ML_B,VL_RT,VL_LT,VL_LB,VL_RB,GL,GR
while (ut()//1000-init_ut)<setting:
    GR.value(1)
    GL.value(1)
    number=ut()//1000-init_ut
    num=number-(number//10)*10
    if num==0:
        ML_T.value(1)
        ML_M.value(0)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(1)
    elif num==1:
        ML_T.value(0)
        ML_M.value(0)
        ML_B.value(0)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==2:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(0)
        VL_LB.value(1)
    elif num==3:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==4:
        ML_T.value(0)
        ML_M.value(1)
        ML_B.value(0)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==5:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(0)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==6:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(0)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(1)
    elif num==7:
        ML_T.value(1)
        ML_M.value(0)
        ML_B.value(0)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==8:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(1)
    elif num==9:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(0)
    GR.value(0)
    ts(0.01)
    GR.value(1)
    GL.value(1)
    num=number//10
    if num==0:
        ML_T.value(1)
        ML_M.value(0)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(1)
    elif num==1:
        ML_T.value(0)
        ML_M.value(0)
        ML_B.value(0)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==2:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(0)
        VL_LB.value(1)
    elif num==3:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==4:
        ML_T.value(0)
        ML_M.value(1)
        ML_B.value(0)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==5:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(0)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==6:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(0)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(1)
    elif num==7:
        ML_T.value(1)
        ML_M.value(0)
        ML_B.value(0)
        VL_RT.value(1)
        VL_LT.value(0)
        VL_RB.value(1)
        VL_LB.value(0)
    elif num==8:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(1)
    elif num==9:
        ML_T.value(1)
        ML_M.value(1)
        ML_B.value(1)
        VL_RT.value(1)
        VL_LT.value(1)
        VL_RB.value(1)
        VL_LB.value(0)
    GL.value(0)
    ts(0.01)
ML_T.value(0)
ML_M.value(0)
ML_B.value(0)
VL_RT.value(0)
VL_LT.value(0)
VL_RB.value(0)
VL_LB.value(0)
GL.value(0)
GR.value(0)
