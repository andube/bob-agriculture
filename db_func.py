from replit import db
import time

def conditionIndex(con, li):
  return [i for i, el in enumerate(li) if con(el)]

def check_valid(user):
  if user not in db.keys():
     db[user] = {}
  else:
    if 'animals' not in db[user].keys(): db[user]['animals'] = []
    if 'plant_farm' not in db[user].keys(): db[user]['plant_farm'] = []
    if 'timestamp' not in db[user].keys(): db[user]['timestamp'] = ''
    if 'circles' not in db[user].keys(): db[user]['circles'] = []

    db[user]['animals'] = sorted(db[user]['animals'], key=lambda d: d['amount'], reverse = True) 
    db[user]['plant_farm'] = sorted(db[user]['plant_farm'], key=lambda d: d['name'])
    db[user]['circles'] = sorted(db[user]["circles"], key = str.lower)
      

def add_animal(user, animal):
  check_valid(user)
  ar = conditionIndex(lambda e: e['emoji'] == animal['emoji'], db[user]['animals'])
  if len(ar) < 1: db[user]['animals'].append(animal)
  else: db[user]['animals'][ar[0]]['amount'] = db[user]['animals'][ar[0]]['amount'] + 1

def plant_crop(user, crop):
  check_valid(user)
  db[user]['plant_farm'].append(crop)

def add_circle(user, circle):
  check_valid(user)
  if circle in db[str(user)]["circles"]:
    pass
  else:
    db[str(user)]["circles"].append(circle)

def handle_timestamp(user):
  check_valid(user)
  db[user]['timestamp'] = time.time()
