import os, re

folder = 'D:/Codigo Abierto/ApuntesJapones/Subagent/unidades/'
# Fix lines like: \chapter{title with no closing brace
# Pattern: line starts with \chapter{ but doesn't end with }
pattern = re.compile(r'^(\\chapter\{[^}]*)$', re.MULTILINE)

for fname in sorted(os.listdir(folder)):
    if not fname.endswith('.tex'):
        continue
    fpath = os.path.join(folder, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = pattern.sub(r'\1}', content)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(fname, 'fixed')

print('Done.')
