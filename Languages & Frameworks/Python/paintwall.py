import time
import threading

class PaintBrush:
    def PaintWall(self):
        time.sleep(2)
        print(f'Painted wall color green')

    def __init__(self):
        paint_thread = threading.Thread(target=self.PaintWall)
        paint_thread.start()
for i in range(1,100):
    PaintBrush()
    print(i)
