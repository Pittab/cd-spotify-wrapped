import json
cdmeta={}

def add():
    artist=input("artist: ").lower().strip()
    if artist not in cdmeta:
        cdmeta[artist]=[]
    cdmeta[artist].append([input("album: ").lower(),int(input("runtime (in mins): ")), 0])

def recordplayed():
    artist = input("artist: ").lower().strip()
    album = input("album: ").lower().strip()
    for item in cdmeta[artist]:
        if item[0] == album:
            item[2]+=1

def fetchcddata(loc):
    global cdmeta
    try:
      with open(loc, 'r') as f:
        cdmeta = json.load(f)
    except Exception:
        print("local metadata file doesn't exist, returning empty metadata...")
        return {}

def dumpmeta(loc):
    with open(loc, 'w') as f:
        json.dump(cdmeta, f, indent=2)

def stats():
    totalmins=0
    totalalbums=0
    artists={}
    for artist in cdmeta:
        artisttotal=0
        for album in cdmeta[artist]:
            totalmins+=album[1]*album[2]
            totalalbums+=album[2]
            artisttotal+=album[2]
        artists[artist]=' '.join([artist,"played",str(artisttotal),"times"])
    print(str(totalmins / 60) + " hours of music played\n"+ str(totalalbums) + " albums listened to")
    for item in artists:
        print(artists[item])

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
            stats()
        case "q":
            dumpmeta(metaloc)
            break

menu()