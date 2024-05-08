import sys
from operator import itemgetter
"""
Generator for a Floyd Triangle
eg.
1
2 3
4 5 6
7 8 9 10

Note: num_max will be exceeded, if needed, to complete
the last row. So floyd_triangle(7) and floyd_triangle(9)
will both produce the 10 item example triangle above 
"""
def floyd_triangle(num_max):
	row,num,flag = 1,1,True
	while flag:
		result = [n for n in range(num,num+row)]
		yield result
		num += row
		if num > num_max:
			flag = False
		row += 1
""" Decode a file format: integer<tab>word and only
output word if integer occurs as the last item of a row
in a Floyd triangle.
"""
def decode_message_data(filename):
	return_data = []
	"""Read the message"""
	with open(str(filename)) as f:
		x = f.readlines()
	"""Get an appropriate amount of Floyd triangle
	rows and capture a list of all the last items"""
	floyd_seq = [t[-1] for t in floyd_triangle(len(x)+1)]
	"""Map and sort just the matching lines"""
	c = [[int(d[0]),d[1]] for d in [i.split() for i in x] if int(d[0]) in floyd_seq]
	"""Print out the words in the sorted message"""
	for w in [i[1] for i in sorted(c,key=itemgetter(0))]:
		print(w,end=" ")
	print()

# """Hack for handling command line"""
# if __name__ == "__main__":
# 	try:
# 		decode_message_data(str(sys.argv[1:]))
# 	except:
decode_message_data('message.txt')
