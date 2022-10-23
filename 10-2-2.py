import pickle

load_file = open('favorites.dat','rb')
loaded_data = pickle.load(load_file)
load_file.close()
print(loaded_data)