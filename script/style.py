import os
import re
import json

problem_dir = '../../LeetCodeProblems'
problems = {}
for tag in os.listdir(problem_dir):
    tag_dir = os.path.join(problem_dir, tag)
    if not tag[0].isupper() or not os.path.isdir(tag_dir):
        continue
    for filename in os.listdir(tag_dir):
        num, name, _ = filename.split('.')
        num = '{:03}'.format(int(num))
        if num in problems:
            problems[num]['tags'].append(tag)
        else:
            problems[num] = {'id': num, 'title': name, 'tags': [tag]}

solution_dir = '..'
base_url_cn = 'https://leetcode-cn.com/problems'
base_url_en = 'https://leetcode.com/problems'
difficulty_stars = {'Easy': '★', 'Medium': '★★', 'Hard': '★★★'}
for tag in os.listdir(solution_dir):
    tag_dir = os.path.join(solution_dir, tag)
    if not tag[0].isupper() or not os.path.isdir(tag_dir):
        continue
    for filename in os.listdir(tag_dir):
        if filename == 'about.md':
            continue
        num, name, _ = filename.split('.')
        tags = problems[num]['tags']

        filepath = os.path.join(tag_dir, filename)
        with open(filepath) as fr:
            text = fr.readlines()
        title, difficulty = text[0].strip().split('）')
        title += '）'
        difficulty = difficulty_stars[difficulty.strip('*')]

        info = []
        info.append(title)
        info.append('## 概况')
        info.append('**标签**：{}<br>'.format('  '.join(['*`{}`*'.format(tag) for tag in tags])))
        info.append('**难度**：{}<br>'.format(difficulty))
        info.append('**评分**：★★★★★<br>')
        info.append('**原题**：[中文]({0}/{2}) / [英文]({1}/{2})'.format(base_url_cn, base_url_en, name))
        text = info + text[2:]

        with open(filepath, 'w') as fw:
            fw.write('\n'.join(text))