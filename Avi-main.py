
# this is my first github addition

def decode(encoded_password):
	new_string=""
	for i in encoded_password:
		new_string+=str(int(i)-3)
	
	return new_string

print("Hello world")
