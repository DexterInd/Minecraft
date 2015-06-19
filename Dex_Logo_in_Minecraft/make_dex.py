# Create Dex in Minecraft!
# See our blog post at Dexterindustries.com to see how you can
# make your own name or logo in Minecraft!

from mcpi import minecraft
import time

fname = "Dex_4_Minecraft.txt"

# Load up the file into memory.
with open(fname) as f:
	dex_tex = f.readlines()
	f.close()

# Fire up minecraft.
mc = minecraft.Minecraft.create()

# Get our initial coordinates.
x1, y1, z1 = mc.player.getPos()

# Make coordinates into integers.
x = int(x1)
y = int(y1)
z = int(z1)

block = 1

print "START!"
line_number = 0

# We'll go through each line of the file, and we'll go backwards since we want to build
# from the ground up!
for i in reversed(dex_tex):

	line = list(i)
	line_number += 1
	for j in range(0,len(line)):
		if line[j] != ' ':
			print "Pos: " + str(line_number) + ", " + str(j)
			mc.setBlock((x+j+1), (y+line_number+1), z, block)
			time.sleep(0.1)
