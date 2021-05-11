
def print_hota(d : dict):
   """Print HOTA fancy way

   Args:
       d (dict): HOTA dictionnari in extract_dict list
   """
   upper_line : str = "||"
   down_line : str = "||"
   for i,key in enumerate(d.keys()):
      upper_line += "{:^10}".format(key) + "||"
      down_line += "{:^10.2f}".format(d[key]) + "||"
      if (i+1) % 7 == 0:
         print(upper_line + '\n' + down_line)
         upper_line : str = "||"
         down_line : str = "||"
   if (i+1) % 7 != 0:
      print(upper_line + '\n' + down_line)

        