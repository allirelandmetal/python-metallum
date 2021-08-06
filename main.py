import metallum

#Using a basic python API for the amazing www.metal-archives.com
#pip install python-metallum - run if not working 

#API Ref : https://github.com/lcharlick/python-metallum

  
choice = input("Enter your band choice: ")
print("Searching for" + "..." + choice + "...") 

bands = metallum.band_search(choice)

bands[0].name

# Fetch band page
bands = bands[0].get()

# Get all albums
bb = bands.albums

print(bands)
print(bb)

from pprint import pprint
pprint(bands)
