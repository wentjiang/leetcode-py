import collections
import re
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph_list = list(
            filter(lambda word: (word != "" and word not in banned), re.split(r"[ !?',;.]", paragraph.lower())))
        counter = collections.Counter(paragraph_list)
        return counter.most_common(1)[0][0]
