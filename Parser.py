import pickle
with open('table.pickle', 'rb') as f:
	entry = pickle.load(f)   
	print(entry)
