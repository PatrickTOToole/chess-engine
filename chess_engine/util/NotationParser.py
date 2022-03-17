import re

class NotationParser:
    def __init__(self, mode=0):
        self.mode = mode
        self.move_pattern = re.compile('([KNQBR][a-h][1-8]||[KNQBR][1-8]||[KNQBR][a-h]||[a-h][1-8]||[KNQBR]||[a-h])([x]?)([a-h][1-8])')
    def parse(self, value):
        if self.mode == 0:
            res = re.fullmatch(self.move_pattern, value)
            piece = res.group(1)
            isAttack = res.group(2)
            space = res.group(3)
            return piece, isAttack, space
