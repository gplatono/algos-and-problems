from typing import *

class Solution:
    def processLine(self, line: List[str], maxWidth: int) -> str:
        spaces_num = maxWidth - sum([len(word) for word in line])
        gaps = (len(line) - 1) if len(line) > 1 else 1
        result = ""
        for word in line:
            result += word
            if (gaps > 0):
                spaces = ceil(spaces_num / gaps)
                spaces_num -= spaces
                gaps -= 1
                result += " "*spaces
        
        return result

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        justify = []
        line = []
        cur_line = ""
        for word in words:
            if cur_line != "" and len(cur_line) + 1 + len(word) > maxWidth:
                justify.append(self.processLine(line, maxWidth))
                cur_line = ""
                line = []
            if cur_line != "":
                cur_line += " "
            cur_line += word
            line.append(word)

        last_line = " ".join(line)
        justify.append(last_line + " "*(maxWidth - len(last_line)))
        return justify