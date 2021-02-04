#Hands On #2
#Exercise 8-7
print("-----Exercise 8-7-----\n")

def make_album(artist_name,album_name,number_songs=None):
    album = {'artist':artist_name, 'album':album_name}
    if number_songs:
        album['number_songs']=number_songs

    print(f"Artist: {artist_name}")
    print(f"Album: {album_name}")  
    if number_songs != None:
        print(f"Number of Songs: {number_songs}")
    print("\n")
    return album

make_album('Neil Young', 'Harvest Moon')
make_album('Tom Misch','Geography')
make_album('Black Pumas','Black Pumas')
make_album('Rayland Baxter','Good Mornin',5)
make_album('Tom Misch','What Kind of Music',14)

#Exercise 8-8
print("\n-----Exercise 8-8-----")
def make_album2(artist_name,album_name,number_songs=0):
    album = {'artist':artist_name, 'album':album_name,'songs':number_songs}
    return album

while True: 
    print("\nEnter Artist and Album Information: ")
    print("---enter 'q' at any time to quit---")

    art_name = input("\nEnter Artist name: ")
    if art_name == 'q':
        break   

    alb_name = input("Enter Albumn name: ")
    if alb_name == 'q':
        break

    num_songs = input("Enter # of songs: ")
    if num_songs == 'q':
        break

    formatted_album = make_album2(art_name,alb_name,num_songs)
    print(f"Album Info: {formatted_album}")