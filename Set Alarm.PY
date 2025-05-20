def set_alarm(employed, vacation):
 if employed == vacation:
     return False
 elif employed == True and vacation == False:
     return True
 elif employed == False and vacation == True:
     return False
print(set_alarm(True, False))