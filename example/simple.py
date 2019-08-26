from uint import Uint, Int, Register

# Make a new integer by instantiating Uint or Int.
# Here's an example to make unsigned integer in 8-bits wide.

char = Uint(0xff, 8)
print(char.wire.bin)

# 8'b11111111 will be printed.
# Let's have 2 bits overflow.

char <<= 2
print(char.wire.bin)

# 8'b11111100 will be printed. Pretty easy!
# And then shift them back to right a bit.

char >>= 1
print(char.wire.bin)

# Now it's 8'b01111110.
# Leftmost bit is zero as it's unsigned. It's called "logical shift".

# Okay, next we're going to make an signed int.

int32 = Int(0x7FFFFFFF, 32)
print(int32.literal.dec)

# 0x7FFFFFFF (2147483647) is so-called INT_MAX in 32-bit systems.
# What do we see when 1 is added to INT_MAX? Let's check it!

int32 += 1
print(int32.literal.dec)

# It's now a minus number. This (usually) unwanted effect is called "overflow".
