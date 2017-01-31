from struct import *

# Store as bytes data
packed_data = pack("iif", 5, 34, 34.00)
print(packed_data)

print(calcsize("i"))
print(calcsize("f"))
print(calcsize("iif"))

# original_data = unpack("iif", packed_data)
original_data = unpack("iif", b'\x05\x00\x00\x00"\x00\x00\x00\x00\x00\x08B')
print(original_data)

