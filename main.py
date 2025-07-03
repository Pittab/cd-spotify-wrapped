import json
cdmeta={}

def add():
    artist=input("artist: ")
    if artist not in cdmeta:
        cdmeta[artist]=[]
    cdmeta[artist].append([input("album: "),int(input("runtime (in mins): ")), 0])

def recordplayed():
    cdmeta[input("artist: ")][input("album: ")][2]+=1

def fetchcddata(loc):
    try:
      with open(loc, 'r') as f:
        cdmeta = json.load(f)
    except Exception:
        print("local metadata file doesn't exist, returning empty metadata...")
        return {}

def dumpmeta(loc):
    with open(loc, 'w') as f:
        json.dump(cdmeta, f, indent=2)

def menu():
    metaloc= input("metadata location in relation to where this is being run: ")
    fetchcddata(metaloc)
    while True:
      match input("welcome to le dingus mcwrapper, a to add, r to record a played album, s to see stats and q to quit: "):
        case "a":
            add()
        case "r":
            recordplayed()
        case "s":
            print("oop")
        case "q":
            dumpmeta(metaloc)
            break

menu()
