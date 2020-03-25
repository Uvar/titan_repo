# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 23:39:26 2020

@author: idh
"""

ttn_list = titans.copy()
ttn_names = [ttn.name for ttn in ttn_list]
ttn_dict = {k:v for k,v in zip(ttn_names, ttn_list)}

def lookup_titan(ttn_string):
    return [ttn_dict[ttn] for ttn in ttn_string.split(", ")]

def fwin(serie):
    return (serie.Result == 1).mean().round(2)
ser = pd.DataFrame(grid.iloc[:,0].copy())
ser.columns = ["Result"]
ser["titans"] = ser.index.to_series()

ser = ser.assign(n_fire = ser.titans.apply(lookup_titan).apply(check_amount_fire),
           n_water = ser.titans.apply(lookup_titan).apply(check_amount_water),
           n_earth = ser.titans.apply(lookup_titan).apply(check_amount_earth),
           n_tank = ser.titans.apply(lookup_titan).apply(check_amount_tanks))
ser3fire = ser.loc[ser.n_fire == 3].copy()
ser4fire = ser.loc[ser.n_fire ==4].copy()
ser3water = ser.loc[ser.n_water==3].copy()
ser4water = ser.loc[ser.n_water==4].copy()
ser3earth = ser.loc[ser.n_earth==3].copy()
ser4earth = ser.loc[ser.n_earth==4].copy()
ser0tank = ser.loc[ser.n_tank==0].copy()
ser1tank = ser.loc[ser.n_tank==1].copy()
ser2tank = ser.loc[ser.n_tank==2].copy()
ser3tank = ser.loc[ser.n_tank==3].copy()

print("Overall win fraction: {}".format(fwin(ser)),
      "3 fire titans win fraction: {}".format(fwin(ser3fire)),
      "4 fire titans win fraction: {}".format(fwin(ser4fire)),
      "3 earth titans win fraction: {}".format(fwin(ser3earth)),
      "4 earth titans win fraction: {}".format(fwin(ser4earth)),
      "3 water titans win fraction: {}".format(fwin(ser3water)),
      "4 water titans win fraction: {}".format(fwin(ser4water)),
      "0 tank titans win fraction: {}".format(fwin(ser0tank)),
      "1 tank titans win fraction: {}".format(fwin(ser1tank)),
      "2 tank titans win fraction: {}".format(fwin(ser2tank)),
      "3 tank titans win fraction: {}".format(fwin(ser3tank)),
      sep="\n")

