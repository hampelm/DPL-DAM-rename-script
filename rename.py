from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join

# Path to files:
PATH="25July2013"

# Store the renamed files in this directory:
RENAMED_PATH="renamed"

# Get the list of files to process
processed_so_far = dict()
files = listdir(PATH)
print len(files);

for name in files:
	# open the file and get the contents
	f = open(PATH + '/' + name, 'r')
	xml_doc = f.read()
	f.close()

	# find the <altid> tag and get the text
	soup = BeautifulSoup(xml_doc)
	new_names = soup.find_all('altid')

	# Make sure we only have one altid
	if len(new_names) != 1:
		print len(new_names) + " altids found in file " + name

	new_name = new_names[0].text

	# Check if we're overwriting a file
	if new_name in processed_so_far:
		print "Overwriting " + new_name
		print "From file " + name
		print "Last seen in " + processed_so_far[new_name]

	processed_so_far[new_name] = name

	# write the new file
	f = open(RENAMED_PATH + '/' + new_name + '.xml', 'w')
	text = soup.prettify()
	f.write(text.encode('utf-8'))
