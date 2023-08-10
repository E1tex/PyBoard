import pyautogui
import time
import random

time.sleep(10)
file_path = 'test.txt'
lines = []

with open(file_path, 'r') as file:
	for line in file:
		line = line.rstrip('\n')

		first_index = next((i for i, char in enumerate(line) if char != ' '), len(line))

		space_count = line[:first_index].count(' ')

		line_content = line[first_index:]

		line_data = [space_count, line_content]
		lines.append(line_data)

checker = 0
for line_data in lines:
	space_count, line_content = line_data
	tabs_count = space_count // 4
	if checker > tabs_count:
		for i in range(checker - tabs_count):
			pyautogui.press('backspace')

	pyautogui.typewrite(line_content, interval=random.uniform(0.1, 0.2))
	time.sleep(0.5)
	pyautogui.press("enter")
	checker = tabs_count
