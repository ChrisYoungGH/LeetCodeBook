import os

with open('../../LeetCodeProblems/scripts/hot.txt') as fr:
    data = fr.readlines()
hot_dict = {}
for line in data:
    num, like, dislike = [int(item) for item in line.strip().split(' ')]
    hot = int(round(like / (like + dislike) / 0.2))
    hot_dict['{:03d}'.format(num)] = hot

solution_dir = '..'
for tag in os.listdir(solution_dir):
    tag_dir = os.path.join(solution_dir, tag)
    if not tag[0].isupper() or not os.path.isdir(tag_dir):
        continue
    for filename in os.listdir(tag_dir):
        if filename == 'about.md':
            continue
        num = filename.split('.')[0]
        filepath = os.path.join(tag_dir, filename)
        with open(filepath) as fr:
            text = fr.readlines()

        for i, line in enumerate(text):
            if '评分' in line:
                text[i] = line.replace('★★★★★', '★' * hot_dict[num])
                break

        with open(filepath, 'w') as fw:
            fw.write(''.join(text))
