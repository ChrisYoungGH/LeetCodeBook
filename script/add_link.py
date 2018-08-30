import os
import re
url_cn = 'https://leetcode-cn.com/problems/'
url_en = 'https://leetcode.com/problems/'
root_dir = '..'
for tag_name in os.listdir(root_dir):
    tag_dir = os.path.join(root_dir, tag_name)
    if not os.path.isdir(tag_dir) or not tag_name[0].isupper():
        continue
    for filename in os.listdir(tag_dir):
        if not filename[0].isdigit():
            continue
        name = filename.split('.')[1]
        filepath = os.path.join(tag_dir, filename)
        with open(filepath) as fr:
            data = fr.readlines()
        title = data[0].strip()
        _, cn, en, diffc = re.split('[#（）]', title)
        cn = cn.strip()
        data[0] = '# [{}]({})（[{}]({})）*{}*\n'.format(cn, url_cn+name, en, url_en+name, diffc)
        with open(filepath, 'w') as fw:
            for line in data:
                fw.write(line)