import pickle
import sys

my_favorites = ['downtown','photography','jazz','milk tea']
save_file = open('favorites.dat','wb')
pickle.dump(my_favorites, save_file)
save_file.close()
sys.exit()
