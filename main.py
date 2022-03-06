from clothing_factory import ClothingFactory

if __name__ == '__main__':
    factory = ClothingFactory()
    builder = factory.create_builder('20s')

    builder.build_hair()
    builder.build_shoes()
    builder.build_bracelet()
    builder.build_collar()
    builder.build_upper_half()
    builder.build_lower_half()

    clothing = builder.get_clothing()

    print(repr(clothing))