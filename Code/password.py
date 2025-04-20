from random import sample


def random_generator(length: int) -> str:
    """
    The password is ASCII characters and the maximum length of the password is 95 characters.
    """

    PASSWORD = sample(
        " !'\"#$%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~",
        95,
    )
    return "".join(PASSWORD[:length])


if __name__ == "__main__":
    length = int(input("\n請輸入密碼長度："))
    print(f"生成的密碼：\n{random_generator(length)}")
