import os
import re

for tag_dir, _, problem_list in os.walk('..'):
	if tag_dir == '..' or not tag_dir.split('/')[1][0].isupper():
		continue
	with open(os.path.join(tag_dir, 'about.md'), 'w') as fw:
		for name in problem_list:
			if name == 'about.md':
				continue
			problem_path = os.path.join(tag_dir, name)
			# print(problem_path)
			with open(problem_path) as fr:
				title = fr.readline().strip().strip('# ')
			# print(title)
			title_cn, title_en, difficulty = re.split('[（）]', title)
			# print(title_cn, title_en, difficulty)
			fw.write('* [{}({})]({})\n'.format(title_cn, difficulty, problem_path[1:]))
