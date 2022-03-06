from typing import Literal

from clothing_builders.clother_builder import ClothingBuilder
from clothing_builders.clothing_builder_20s import ClothingBuilder20s

clothing_type = Literal['20s', '2000s']


class ClothingFactory:

    def create_builder(self, clt_tp: clothing_type) -> ClothingBuilder:
        if clt_tp == '20s':
            return ClothingBuilder20s()
        elif clt_tp == '2000s':
            return None
        else:
            raise NotImplementedError('Clother Not implemented')
