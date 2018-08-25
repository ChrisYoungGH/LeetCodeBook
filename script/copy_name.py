import os

tags = [name for name in os.listdir('..') if name[0].isupper() and name[1].islower()]

with open('../SUMMARAY.md', 'a') as fw:
	fw.write('\n\n\n')
	for tag in tags:
		plist_file = os.path.join('..', tag, 'about.md')
		print(plist_file)

		fw.write('* []({})\n'.format(plist_file[1:]))
		with open(plist_file) as fr:
			plist = fr.readlines()
		for line in plist:
			fw.write('\t{}'.format(line))
		fw.write('\n')
