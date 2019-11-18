magic_numbers = {'png': bytes([0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A])}
max_read_size = max(len(m) for m in magic_numbers.values()) # get max size of magic numbers of the dict
 
with open('YourFile.png', 'rb') as fd:
    file_head = fd.read(max_read_size)
 
if file_head.startswith(magic_numbers['png']):
    print("Type filenya PNG")
else:
    print("Ini bukan PNG)
