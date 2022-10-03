import pyautogui as pt
from PIL import Image

class clicker:
	def __init__(self, target_png, speed):
		self.target_png = target_png
		self.speed = speed
		pt.FAILSAFE = True

	def nav_to_image(self):
		x, y= pt.size()
		try:
			position = pt.locateOnScreen(self.targer_png, confidence=.8)
			print(position)
			pt.moveTo(position[0] + 15, position[1] + 15, duration=self.speed)
			pt.doubleClick()

		except:
			print("image Not Found")
			return(0)

if __name__ == '__main__':
	clicker = clicker("dot2.png", speed=.001)

end = 0

print("size : %d", pt.size())
while True:
	#print("mause pos : %d", pt.position())
	if clicker.nav_to_image() == 0:
		end += 1
	
	if end > 20:
		break