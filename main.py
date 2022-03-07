from clothing_factory import ClothingFactory, builders, clothing_type


def build_clothing(b: clothing_type):
    builder = factory.create_builder(b)

    builder.build_hair()
    builder.build_shoes()
    builder.build_bracelet()
    builder.build_collar()
    builder.build_upper_half()
    builder.build_lower_half()

    return builder.get_clothing()


if __name__ == '__main__':
    factory = ClothingFactory()

    print('Select Your Clothing Choices: ')

    s = {}
    for i, value in enumerate(builders.keys()):
        s[i] = value
        print(i, '-', value)

    v = s[int(input('Choose: '))]

    clothing = build_clothing(v)

    print(repr(clothing))
