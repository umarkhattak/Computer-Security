# Umar Khattak
# 177009705 | uk50
# CS419 Assignment 1

tp = "./tables"
from json.decoder import JSONDecodeError as jde
from os import path as p
# import pandas as pd
import os as operatingSystem
import json as js
# import numpy as np
# from pandas import DataFrame
import sys as system
# from collections import defaultdict

# Some Helper Methods
def SetDomainHelper(domain):
    if not p.exists("./tables/databasedomain.js"):
        return False
    file = open("./tables/databasedomain.js")
    try:
        domains = js.load(file)
        if domain in domains:
            return True
#     print("Testing stoppage 1")        
    except jde:
        return False
    
    return False

def SetTypeHelper(typeSTH):
    if not p.exists("./tables/databasetype.js"):
        return False
    
    file = open("./tables/databasetype.js")
    
    try:
        tpDict = js.load(file)
        if typeSTH in tpDict:
            return True
        
    except jde:
        return False
#     print("Testing stoppage 2")    
    return False

def addUserCheck(user):
    if not p.exists("./tables/databaseuser.js"):
        return False
    
    file = open("./tables/databaseuser.js", "r")
    
    try:
        databaseDict = js.load(file)
        if user in databaseDict:
            return True
    except jde:
        return False
    
    return False

def pushingPHelper(string):
    if not p.exists("./tables/pushingPdict.js"):
        return False
    
    file = open("./tables/pushingPdict.js")
    
    try:
        tpDict = js.load(file)
        if string in tpDict:
            return True
#     print("Testing stoppage 3")       
    except jde:
        return False
    
    return False

# Main Functions
def AddUser(user, password):

    if user == "":
        print("Error: username missing")
        return
#     print("Testing stoppage 4")
    if not p.exists("./tables/databaseuser.js"):
        open("./tables/databaseuser.js", "w+")
#     print("Testing stoppage 5")
    file = open("./tables/databaseuser.js", "r")
    
    try:
        databaseDict = js.load(file)

        if addUserCheck(user):
            print("Error: user exists") 
            return

        databaseDict[user] = {"userDict" : user, "passwordDict" : password, "domainsDict":[]}
        file = open("./tables/databaseuser.js", "w+")
        js.dump(databaseDict, file, indent = 5)
#     print("Testing stoppage 6")
    except jde:
        file = open("./tables/databaseuser.js", "w+")
        databaseDict = {user: {"userDict" : user, "passwordDict": password, "domainsDict": []}}
        js.dump(databaseDict, file, indent = 5)

    print("Success")
    
#     array = []
#     dictionary = {}

#     with open (f, "r") as file:
#         array = file.readlines()
#     file.close()

#     for i in range(len(array)):
#         temp = array[i][:-1].split("|")
#         array[i] = [temp[0], float(temp[1])] 

def Authenticate(user, password):

    if not p.exists("./tables/databaseuser.js"):
        print("Error: no such user")
        return
#     print("Testing stoppage 7")  
    file = open("./tables/databaseuser.js", "r")

    try:
        databaseDict = js.load(file)

        if user in databaseDict:
            if databaseDict[user]["passwordDict"] != password:
                print("Error: bad password")
                return
        else:
            print("Error: no such user")
            return
#     print("Testing stoppage 8")
    except jde:
        print("Error: no such user")
        return
    
    print("Success")

def SetDomain(user, domain):
    
    if not addUserCheck(user):
        print("Error: no such user")
        return
    
    if domain == "":
        print("Error: missing domain")
        return
#     print("Testing stoppage 9")
    if not p.exists("./tables/databasedomain.js"):
        open("./tables/databasedomain.js", "w+")

    file = open("./tables/databasedomain.js", "r")

    try:
        domainDict = js.load(file)
        file = open("./tables/databasedomain.js", "w+")

        if domain not in domainDict:
            domainDict[domain] = {"domain_nameDict": domain,  "userDict": [user]}
        else:
            if user not in domainDict[domain]["userDict"]:
                domainDict[domain]["userDict"].append(user)
        
        js.dump(domainDict, file, indent = 5)

    except jde:
        domainDict = {domain: {"domain_nameDict": domain, "userDict": [user]}}
        file = open("./tables/databasedomain.js", "w+")
        js.dump(domainDict, file, indent = 5)
#     print("Testing stoppage 10")
    file = open("./tables/databaseuser.js", "r")
    databaseDict = js.load(file)
    
    if domain not in databaseDict[user]["domainsDict"]:
        databaseDict[user]["domainsDict"].append(domain)
        
    file = open("./tables/databaseuser.js", "w+")
    js.dump(databaseDict, file, indent = 5)
    
    print("Success")

def DomainInfo(domain):
    if domain == "":
        print("Error: missing domain")
        return

    if not p.exists("./tables/databasedomain.js"):
        open("./tables/databasedomain.js", "w+")
        return
#     print("Testing stoppage 11")
    file = open("./tables/databasedomain.js", "r")
    
    try:
        domains = js.load(file)

        if domain in domains:
            for x in domains[domain]["userDict"]:
                print(x)

    except jde:
        return

def SetType(objectST, typeST):
    if objectST == "":
        print("Error:")
        return

    if not p.exists("./tables/databasetype.js"):
        open("./tables/databasetype.js", "w+")
    
    file = open("./tables/databasetype.js", "r")
    
    try:
        tpDict = js.load(file)
#     print("Testing stoppage 12")
        if typeST in tpDict:
            if objectST not in tpDict[typeST]["Objects"]:
                tpDict[typeST]["Objects"].append(objectST)
            else:
                return
        else:
            tpDict[typeST] = {"typeNameDict": typeST, "Objects": [objectST]}
            
    except jde:
        tpDict = {typeST: {"typeNameDict": typeST, "Objects": [objectST]}}

    file = open("./tables/databasetype.js", "w+" )
    js.dump( tpDict, file, indent = 5)

    print("Success")

def TypeInfo(typeTI):
    if typeTI == "":
        print("Error:")
        return
#     print("Testing stoppage 13")
    if not p.exists("./tables/databasetype.js"):
        open("./tables/databasetype.js", "w+")
        return

    file = open("./tables/databasetype.js", "r")

    try:
        tpDict = js.load( file)

        if typeTI in tpDict:
            for x in tpDict[typeTI]["Objects"]:
                print(x)
#     print("Testing stoppage 14")
    except jde:
        return

def AddAccess(op, dn, tn):
    if op == "":
        print("Error: missing operation")
        return
#     print("Testing stoppage 15")   
    if dn == "":
        print("Error: missing domain")
        return
    
    if tn == "":
        print("Error: missing type")
        return

#     print("Testing stoppage 16")
    if not SetDomainHelper(dn):
        if not p.exists("./tables/databasedomain.js"):
            open("./tables/databasedomain.js", "w+")
            
        file = open("./tables/databasedomain.js", "r")
        
        try:
            dictDomain = js.load(file)
            dictDomain[dn] = {"typeNameDict": dn, "Bruh": []}
        
        except jde:
            dictDomain = {dn: {"typeNameDict": dn, "Bruh": []}}
            
        file = open("./tables/databasedomain.js", "w+")
        js.dump(dictDomain, file, indent = 5)

    if not SetTypeHelper(tn):
        if not p.exists("./tables/databasetype.js"):
            open("./tables/databasetype.js", "w+")
            
        file = open("./tables/databasetype.js", "r")
#     print("Testing stoppage 17")     
        try:
            tpDict = js.load(file)
            tpDict[tn] = {"typeNameDict": tn, "Objects": []}
            
        except jde:
            tpDict = {tn: {"typeNameDict": tn, "Objects": []}}
            
        file = open("./tables/databasetype.js", "w+")
        js.dump( tpDict, file, indent=5 )

    if not p.exists("./tables/pushingPdict.js"):
        open("./tables/pushingPdict.js", "w+")
    
    file = open("./tables/pushingPdict.js", "r")
    
    try:
        pushingP = js.load(file)
        
        if op not in pushingP:
            pushingP[op] = {"typeNameDict": op, "domainsDict": {dn: [tn]}}
        
        else:
            if dn in pushingP[op]["domainsDict"]:
                if tn not in pushingP[op]["domainsDict"][dn]:
                    pushingP[op]["domainsDict"][dn].append(tn)
            else:
                pushingP[op]["domainsDict"][dn] = [tn]


    except jde:
        pushingP = {op: {"typeNameDict": op, "domainsDict": {dn: [tn]}}}
#     print("Testing stoppage 18")
    file = open("./tables/pushingPdict.js", "w+")
    js.dump(pushingP, file, indent = 5)

    print("Success")

def CanAccess(op, resu, ob):
    
    if op == "" or resu == "" or ob == "":
        print("Error: access denied")
        return

    if not p.exists("./tables/databaseuser.js"):
        open("./tables/databaseuser.js", "w+")
        return

    if not addUserCheck(resu):
        print("Error: access denied")
        return

    file = open("./tables/databaseuser.js", "r")
    
    try:
        databaseDict = js.load(file)
        dictUD = databaseDict[resu]["domainsDict"]

    except jde:
        print("Error: access denied")
        return

    if not p.exists("./tables/pushingPdict.js"):
        open( "./tables/permission.js", "w+" )
        return

    if not pushingPHelper(op):
        print("Error: Operation is not valid")
        return

    file = open("./tables/pushingPdict.js", "r")
#     print("Testing stoppage 19")   
    try:
        pushingP = js.load(file)
        pushingPd = pushingP[op]["domainsDict"]

    except jde:
        print("Error: access denied")
        return
        
    commonGround = []
    commonTypes = []
    
    for x in dictUD:
        if x in pushingPd:
            commonGround.append(x)

    for x in commonGround:
        for y in pushingPd[x]:
            if y not in commonTypes and SetTypeHelper(y):
                commonTypes.append(y)

    if not p.exists("./tables/databasetype.js"):
        open("./tables/databasetype.js", "w+")
        return
    
    file = open("./tables/databasetype.js", "r")
    
    try:
        tpDict = js.load( file )
#     print("Testing stoppage 20")
    except jde:
        print("Error: access denied")
        return

    for x in commonTypes:
        if ob in tpDict[x]["Objects"]:
            print("Success")
            return
        
    print("Error: access denied")

# Main 
def main():
    if len(system.argv) <= 1:
        print("Error: Invalid Input")
        return
#call functions
    if len(system.argv) == 4 and system.argv[1] == "AddUser":
        AddUser(system.argv[2], system.argv[3])

    elif len(system.argv) == 4 and system.argv[1] == "Authenticate":
        Authenticate(system.argv[2], system.argv[3])

    elif len(system.argv) == 4 and system.argv[1] == "SetDomain":
        SetDomain(system.argv[2], system.argv[3])
        
    elif len(system.argv) == 3 and system.argv[1] == "DomainInfo":
        DomainInfo(system.argv[2])
#     print("Testing stoppage 21")        
    elif len(system.argv) == 4 and system.argv[1] == "SetType":
        SetType(system.argv[2], system.argv[3])

    elif len(system.argv) == 3 and system.argv[1] == "TypeInfo":
        TypeInfo(system.argv[2])
    
    elif len(system.argv) == 5 and system.argv[1] == "AddAccess":
        AddAccess(system.argv[2], system.argv[3], system.argv[4])

    elif len(system.argv) == 5 and system.argv[1] == "CanAccess":
        CanAccess( system.argv[2], system.argv[3], system.argv[4])
#erroes    
    elif len(system.argv) <= 3 and system.argv[1] == "AddUser":
        print("Error: username/password missing. Please try again.")
        
    elif len(system.argv) <= 3 and system.argv[1] == "Authenticate":
        print("Error: user/password missing. Please try again.")
        
    elif len(system.argv) <= 3 and system.argv[1] == "SetDomain":
        print("Error: user/domain missing. Please try again")
        
    elif len(system.argv) <= 2 and system.argv[1] == "DomainInfo":
        print("Error: missing domain. Please try again.")
        
    elif len(system.argv) <= 3 and system.argv[1] == "SetType":
        print("Error:")
        
    elif len(system.argv) <= 2 and system.argv[1] == "TypeInfo":
        print("Error:")
        
    elif len(system.argv) <= 4 and system.argv[1] == "AddAccess":
        print("Error: missing operation/domain/type. Please try again")
        
    elif len(system.argv) <= 4 and system.argv[1] == "CanAccess":
        print("Error: access denied")
# too many arguments   
    elif len(system.argv) > 4 and system.argv[1] == "AddUser":
        print("Error: too many arguments for AddUser")
        
    elif len(system.argv) > 4 and system.argv[1] == "Authenticate":
        print("Error: too many arguments for Authenticate")
#     print("Testing stoppage 22")   
    elif len(system.argv) > 4 and system.argv[1] == "SetDomain":
        print("Error: too many arguments for SetDomain")

    elif len(system.argv) > 3 and system.argv[1] == "DomainInfo":
        print("Error: too many arguments for DomainInfo")
        
    elif len(system.argv) > 4 and system.argv[1] == "SetType":
        print("Error: too many arguments for SetType")
        
    elif len(system.argv) > 3 and system.argv[1] == "TypeInfo":
        print("Error: too many arguments for TypeInfo")
        
    elif len(system.argv) > 5 and system.argv[1] == "AddAccess":
        print("Error: too many arguments for AddAccess")
        
    elif len(system.argv) > 5 and system.argv[1] == "CanAccess":
        print("Error: too many arguments for CanAccess")
    else:
        print("Error: Imporper Command. Please try again.")
    
    if not p.exists(tp):
        operatingSystem.mkdir(tp)
#     print("Testing stoppage 23")
if __name__ == '__main__':
    main()