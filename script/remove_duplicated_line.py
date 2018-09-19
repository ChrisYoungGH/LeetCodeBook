import os

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
            if line == '\n':
                text[i] = ''

        with open(filepath, 'w') as fw:
            fw.write(''.join(text))
