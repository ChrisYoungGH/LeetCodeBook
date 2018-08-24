import os
import shutil

with open('../data/chpt_name.txt') as fr:
    chpt_names = fr.readlines()

for name_pair in chpt_names:
	ch_name, en_name = name_pair.strip().split('\t')
	# os.makedirs('../' + ch_name.strip(), exist_ok=True)
	os.rename('../'+ch_name, '../'+en_name)
