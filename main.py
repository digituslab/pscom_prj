from pscom import *

object = Pscom()
object.open_port('COM3',115200)

times:int
times = 1000
while times > 0:
    answer = result = object.send_text(hex(times)+" ")
    print(answer)
    times = times - 1

