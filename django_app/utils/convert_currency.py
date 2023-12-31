pounds = 19281

def convert_gbp_to_idr(money):
  if money == None:
    money = 0
    
  return '{:,.0f}'.format(money * pounds)

def convert_idr_to_gpb(idr):
  return float("{:.2f}".format(idr / pounds))