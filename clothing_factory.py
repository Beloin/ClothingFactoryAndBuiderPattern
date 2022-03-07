from typing import Literal

from clothing_builders.clother_builder import ClothingBuilder
from clothing_builders.clothing_builder_2000s import ClothingBuilder2000s
from clothing_builders.clothing_builder_20s import ClothingBuilder20s
from clothing_builders.clothing_builder_70s import ClothingBuilder70s
from clothing_builders.clothing_builder_80s import ClothingBuilder80s

clothing_type = Literal['20s', '70s', '80s', '2000s']

builders: dict[clothing_type, type(ClothingBuilder)] = {
    '20s': ClothingBuilder20s,
    '70s': ClothingBuilder70s,
    '80s': ClothingBuilder80s,
    '2000s': ClothingBuilder2000s
}


class ClothingFactory:

    def create_builder(self, clt_tp: clothing_type) -> ClothingBuilder:
        b = builders.get(clt_tp)
        if b:
            return b()
        else:
            raise NotImplementedError('Clother Not implemented')
