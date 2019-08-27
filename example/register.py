from uint import Register


# Now let's create a brand new register.

reg = Register('reg')
print(f'Hi! I am {reg}.')

# This has four 8-bits fields so they're 32-bit in total.
# Declared fields are in Register.fields and are ordered by declaration.
# Be careful that the range of fields are "closed interval" unlike ordinary Python slices.

reg[31:24] = 'val1'
reg[23:16] = 'val2'
reg[15:8] = 'val3'
reg[7:0] = 'val4'

# Specify values individually.

reg['val1'] = 0x01
reg['val2'] = 0x23
reg['val3'] = 0x45
reg['val4'] = 0x67

print(f'{reg.encode():#010x} == 0x01234567')

# Decoding from existing raw int is also supported.

reg.decode(0xfe_dc_ba_98)
print(f'{reg.encode():#010x} == 0xfedcba98')

vals = [v.value for v in reg.fields]
print(f"0x{vals[0]:02x}_{vals[1]:02x}_{vals[2]:02x}_{vals[3]:02x} == 0xfe_dc_ba_98")
