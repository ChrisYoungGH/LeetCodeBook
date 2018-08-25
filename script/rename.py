import os
import re

for tag_dir, _, problem_list in os.walk('..'):
	if tag_dir == '..' or not tag_dir.split('/')[1][0].isupper():
		continue
	for name in problem_list:
		if not re.match('^\\d.+$', name):
			continue
		old_path = os.path.join(tag_dir, name)
		num, title = name.split('.', 1)
		name = '{:03d}.{}'.format(int(num), title)
		new_path = os.path.join(tag_dir, name)
		os.rename(old_path, new_path)
