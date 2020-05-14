import os

save = open('clicker_save.txt', 'w+')

if os.stat("clicker_save.txt").st_size == 0:
    save.write('Cheating isn\'t cool.\n5\n11\n0\n1\n0')

save.seek(0)
lines = save.readlines()
needed_clicks_1 = int(lines[1])
needed_clicks_2 = int(lines[2])
clicks_per_sec = int(lines[3])
click_value = int(lines[4])
clicks = int(lines[5])

save.close()

clicks += 10

save = open('clicker_save.txt', 'w+')

list_of_lines = [lines[0], str(needed_clicks_1), str(needed_clicks_2), str(clicks_per_sec), str(click_value), str(clicks)]

save.write("\n".join(list_of_lines))