from clothing import Clothing, ClothingPart
from clothing_builders.clother_builder import ClothingBuilder


class ClothingBuilder20s(ClothingBuilder):
    _clothing = Clothing()

    def get_clothing(self) -> Clothing:
        return self._clothing

    def build_lower_half(self) -> 'ClothingBuilder':
        self._clothing.set_lower_half(ClothingPart('Pink Pretty Skirt'))
        return self

    def build_upper_half(self) -> 'ClothingBuilder':
        self._clothing.set_upper_half(ClothingPart('Pink Pretty Skirt'))
        return self

    def build_shoes(self) -> 'ClothingBuilder':
        self._clothing.set_shoes(ClothingPart('Black High Heels'))
        return self

    def build_collar(self) -> 'ClothingBuilder':
        self._clothing.set_collar(ClothingPart('Pearl Collar'))
        return self

    def build_hair(self) -> 'ClothingBuilder':
        self._clothing.set_hair(ClothingPart('Pretty Rounded Hair'))
        return self

    def build_bracelet(self) -> 'ClothingBuilder':
        self._clothing.set_bracelet(None)
        return self

