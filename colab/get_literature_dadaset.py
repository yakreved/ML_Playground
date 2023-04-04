import pandas as pd
import re

def get_literature_dataset(samples_num=15_000):
    import os
    raw_literature = []
    for (root, dirs, files) in os.walk('./RusLit', topdown=True):
        for f in files:
            f_name = os.path.join(root, f)
            if f_name.endswith('.txt'):
                x = 200
                # print(f_name)
                with open(f_name, 'r', encoding='utf-8') as file:
                    try:
                        paragraph = file.read()
                        raw_literature.extend([paragraph[i: i + x] for i in range(0, len(paragraph), x)])
                    except:
                        pass

    print(len(raw_literature))
    raw_literature_2 = list(map(lambda x: re.sub(r'\n+', ' \n', x), raw_literature))
    raw_literature_2 = list(map(lambda x: re.sub(r'[ \t]+', ' ', x), raw_literature_2))
    # print(songs[0])
    raw_literature_2 = list(map(lambda x: x.replace('\n', ' endline\n'), raw_literature_2))
    # print(songs[0])
    print(raw_literature_2[:10])
    dataset = pd.DataFrame(raw_literature_2[:10_000], columns=['text'])
    return dataset