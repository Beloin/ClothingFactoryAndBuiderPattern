import abc

from clothing import Clothing


class ClothingBuilder(abc.ABC):
    def get_clothing(self) -> Clothing:
        pass

    def build_lower_half(self) -> 'ClothingBuilder':
        pass

    def build_upper_half(self) -> 'ClothingBuilder':
        pass

    def build_shoes(self) -> 'ClothingBuilder':
        pass

    def build_collar(self) -> 'ClothingBuilder':
        pass

    def build_hair(self) -> 'ClothingBuilder':
        pass

    def build_bracelet(self) -> 'ClothingBuilder':
        pass
