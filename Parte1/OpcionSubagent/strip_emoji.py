import os, re

folder = 'D:/Codigo Abierto/ApuntesJapones/Subagent/unidades/'
pattern = re.compile(r'\\chapter\{([^}]+)\}')

for fname in sorted(os.listdir(folder)):
    if not fname.endswith('.tex'):
        continue
    fpath = os.path.join(folder, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    def strip_emoji(m):
        inner = m.group(1)
        i = 0
        while i < len(inner):
            cp = ord(inner[i])
            if (0x2000 <= cp <= 0x2FFF or
                    0xFE00 <= cp <= 0xFE0F or
                    cp >= 0x1F000 or
                    cp == 0x200D):
                i += 1
                continue
            break
        while i < len(inner) and inner[i] == ' ':
            i += 1
        return '\\chapter{' + inner[i:] + '}'

    new_content = pattern.sub(strip_emoji, content)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(fname, 'updated')

print('Done.')
