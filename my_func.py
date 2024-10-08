def hex_change(arg):
  arg_list = arg.split()
  arg_list = [f"0x{i}" for i in arg_list]
  arg_list = [int(i,16) for i in arg_list]
  print(arg_list)

def ror(n, d, bits=8):
  return ((n >> d) | n << (bits - d)) & 0xff

def rol(n, d, bits=8):
  return ((n << d) | n >> (bits - d)) & 0xff
