#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:40:02 2020

@author: nicksclater1
"""
import numpy as np
from mgrs import MGRS
from OSGridConverter import grid2latlong, latlong2grid
m = MGRS()
import re

def convert_2_deg(input_str: str) -> tuple: # mgrs or bng

  input_str = str(input_str)

  try:

    if input_str[0].isnumeric():

      input_str = input_str.replace(' ', '')
      alphas = input_str[:5]
      digs = input_str[5:]
      east = digs[:int(len(digs)/2)]
      north = digs[int(len(digs)/2):]

      while len(east) < 5:

        east = east + '0'
        north = north + '0'

      digs = east + north
      string = alphas + digs
      result = m.toLatLon(string.encode('utf-8'))

    else:

      input_str = input_str.replace(' ', '')
      alphas = input_str[:2]
      digs = input_str[2:]
      east = digs[:int(len(digs)/2)]
      north = digs[int(len(digs)/2):]

      while len(east) < 5:

        east = east + '0'
        north = north + '0'

      digs = east + north
      string = alphas + digs
      result = (grid2latlong(string).latitude, grid2latlong(string).longitude)

  except:
    result = 'input error'

  return result


def convert_dm_deg(lat_lon_str: str) -> tuple: # dm

  try:

    lat_lon_str = lat_lon_str.lower()

    lat_lon_str = lat_lon_str.replace(' ','').replace(':', '')
    hemi = [i for i in lat_lon_str if i == 's' or i == 'w']
    digs = re.split('n|s|e|w', lat_lon_str)
    digs.remove('')

    try:

      north = digs[0].split('.') ; east = digs[1].split('.')
      north_flt = float(north[0][:-2]) + float(north[0][-2:]) / 60 + float('.' + north[1]) / 60
      east_flt = float(east[0][:-2]) + float(east[0][-2:]) / 60 + float('.' + east[1]) / 60

    except:

      north_flt = float(north[0][:-2]) + (float(north[0][-2:])) / 60
      east_flt = float(east[0][:-2]) + (float(east[0][-2:])) / 60


    if hemi.__contains__('s'):
      north_flt *= -1

    if hemi.__contains__('w'):
      east_flt *= -1

    if abs(north_flt) <= 90 and abs(east_flt) <= 180:

      return (north_flt, east_flt)

    else:
      return ('input error')

  except:

    return ('input error')

def convert_deg_dm(lat_lon: tuple) -> [str]:

  ddmm = []

  try:

    for i in lat_lon:

      string = str(abs(int(np.trunc(i)))) + ':' + str(round(abs(i - np.trunc(i))*60,2))
      ddmm.append(string)

    while len(ddmm[1].split(':')[0]) < 2:

      ddmm[1] = '0' + ddmm[1]

    result = ['N' + ddmm[0] if lat_lon[0] >= 0 else 'S' + ddmm[0]]
    result.append('E' + ddmm[1] if lat_lon[1] >= 0 else 'W' + ddmm[1])

    return result

  except:

    return lat_lon


def convert_deg_dms(lat_lon: tuple) -> [str]:

  ddmmss = []

  try:

    for i in lat_lon:

      string = str(abs(int(np.trunc(i))))\
          + ':' + str(int(np.trunc(abs(i - np.trunc(i)) * 60)))\
              + ':' + str(round(abs((i - np.trunc(i)) * 60 - np.trunc((i - np.trunc(i)) * 60)) * 60 , 1))


      ddmmss.append(string)

    while len(ddmmss[1].split(':')[0]) < 2:

      ddmmss[1] = '0' + ddmmss[1]

    result = ['N' + ddmmss[0] if lat_lon[0] >= 0 else 'S' + ddmmss[0]]
    result.append('E' + ddmmss[1] if lat_lon[1] >= 0 else 'W' + ddmmss[1])

    return result

  except:

    return lat_lon


def convert_deg_mgrs(input_tup: tuple) -> str:

  try:

    temp = m.toMGRS(input_tup[0], input_tup[1])
    temp = temp.decode('utf-8')
    temp = temp[:5] + ' ' + temp[5:10] + ' ' + temp[10:]

    return temp

  except:

    return input_tup


def convert_deg_bng(input_tup: tuple) -> tuple:

  try:

    temp = latlong2grid(input_tup[0], input_tup[1])

    return str(temp)

  except:

    return input_tup


