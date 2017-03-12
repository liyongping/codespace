"""
Extract more readable content from .xml of safaris online books

"""

import os
from bs4 import BeautifulSoup



def list_files(root):
	"""
	list all files in current root folder
	"""
	for path, dir, files in os.walk(root):
		for name in files:
			yield os.path.join(path,name)

def format_content(filename):
	"""
	formate the content 
	from:
	    <p begin="00:00:06.066" end="00:00:07.586">- [Voiceover] Python<br/>includes syntax for slicing</p>
	to:
	    00:00:06     Python includes syntax for slicing
	"""
	soup = BeautifulSoup(open(filename))

	new_filename = filename.split(".")[0] + ".txt"
	new_file = open(new_filename,"w")

	content = []
	for p in soup.find_all('p'):
		ptag = BeautifulSoup(str(p).replace("<br/>", " "))
		text = ptag.p['begin'].split(".")[0] + "     " + ptag.get_text()
		content.append(text)

	contents = "\n".join(content).replace("- [Voiceover] ","")
	new_file.write(contents)
	new_file.close()

def main():
	for file in list_files("case\\effective python59"):
		format_content(file)
		print file
	
if __name__ == '__main__': 
	main()