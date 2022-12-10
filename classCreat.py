import os
import random
import shutil

class1 = {"min":1,"max":9215}
class2 = {"min":9216,"max":10103}
class3 = {"min":10104,"max":11218,}

def wjhdfhj(basePath,path,fileList):
    if not os.path.isdir(path+"/0"):
        os.makedirs(path+"/0")
    if not os.path.isdir(path+"/1"):
        os.makedirs(path+"/1")
    if not os.path.isdir(path+"/2"):
        os.makedirs(path+"/2")

    for fichier in fileList:
        if fichier.endswith(".png"):
            x = int(fichier.split(".")[0])
            if(class1["min"] <= x <= class1["max"]):
                try:
                    shutil.move(basePath+"/" + fichier , path+"/0/" + fichier)
                except:
                    pass
            elif(class2["min"] <= x <= class2["max"]):
                try:
                    shutil.move(basePath+"/" + fichier , path+"/1/" + fichier)
                except:
                    pass
            elif(class3["min"] <= x <= class3["max"]):
                try:
                    shutil.move(basePath+"/" + fichier , path+"/2/" + fichier)
                except:
                    pass


pathLearn = "ddsmROI"
pathTest = "ddsmROI/ddtest"
pathValid = "ddsmROI/ddvalid"

filelist=os.listdir(pathLearn)
nbFiles = 11218
validFiles = random.choices(filelist, k=int(nbFiles*0.25))
filelist = [a for a in filelist if a not in validFiles]
testFiles = random.choices(filelist, k=int(nbFiles*0.05))
filelist = [a for a in filelist if a not in testFiles]
learnFiles = filelist

wjhdfhj(pathLearn,pathTest,testFiles)
wjhdfhj(pathLearn,pathValid,validFiles)
wjhdfhj(pathLearn,pathLearn+"/ddslearn",learnFiles)



