#!/C:\Program Files\Python 3.5
# coding=utf-8
# ll 微信 monkeyrunner
import time,sys
def pro(num,to):
    rt=float(num)/to
    rn=int(100*rt)
    r='\r[{}{}]{}%'.format('*'*rn,' '*(100-rn),rn)
    sys.stdout.write(r)
    sys.stdout.flush()
i,n=0,100
for i in range(n):
    time.sleep(0.1)
    pro(i+1,n)


# http://www.asciiworld.com/-Logos,50-.html
# /***
#  *_______________#########_______________________
#  *______________############_____________________
#  *______________#############____________________
#  *_____________##__###########___________________
#  *____________###__######_#####__________________
#  *____________###_#######___####_________________
#  *___________###__##########_####________________
#  *__________####__###########_####_______________
#  *________#####___###########__#####_____________
#  *_______######___###_########___#####___________
#  *_______#####___###___########___######_________
#  *______######___###__###########___######_______
#  *_____######___####_##############__######______
#  *____#######__#####################_#######_____
#  *____#######__##############################____
#  *___#######__######_#################_#######___
#  *___#######__######_######_#########___######___
#  *___#######____##__######___######_____######___
#  *___#######________######____#####_____#####____
#  *____######________#####_____#####_____####_____
#  *_____#####________####______#####_____###______
#  *______#####______;###________###______#________
#  *________##_______####________####______________
#  */