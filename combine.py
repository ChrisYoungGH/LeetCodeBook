import os
import shutil

to_dir = '/home/chris/Documents/LeetCodeBook/Array'
from_dir = '/home/chris/Documents/problems/Array/'
others_dir = os.path.join(to_dir, 'others')
os.makedirs(others_dir, exist_ok=True)

to_files = [f for f in os.listdir(to_dir) if f.endswith('md') and f != 'about.md']
from_files = os.listdir(from_dir)

search = {}
for name in from_files:
	num, title = name.split('.', 1)
	search[num] = name
	search[title] = name

for name in to_files:
	old_file = os.path.join(to_dir, name)
	num, title = name.split('.', 1)
	if ' ' in name:
		key = num
	else:
		key = title
	if key not in search:
		new_file = os.path.join(others_dir, name)
		shutil.move(old_file, new_file)
		continue

	real_name = search[key]
	real_file = os.path.join(from_dir, real_name)
	with open(real_file) as fr:
		descption = fr.read()
	with open(old_file) as fr:
		solution = fr.read()

	new_file = os.path.join(to_dir, real_name)
	with open(new_file, 'w') as fw:
		fw.write(descption + '\n' + solution)

	os.rename(old_file, old_file+'__')

	print(real_name)