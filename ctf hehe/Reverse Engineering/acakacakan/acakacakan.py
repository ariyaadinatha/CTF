# -*- coding: utf-8 -*-

import random
random.seed("wadidaw")


flag = "REDACTED"
out = ""

for c in flag:
	out += chr( ((ord(c) ^ random.randint(0x00, 0xFF)) + random.randint(0x00, 0xFF) ) % 0xFF)

print out