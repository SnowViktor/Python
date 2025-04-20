def generate_pascals_triangle(max_row_index: int) -> list[list[int]]:
    """
    生成並回傳巴斯卡三角形的列表，包含從第 0 列到第 max_row_index 列。
    """

    triangle = [[1]]

    for i in range(1, max_row_index + 1):
        prev_row = triangle[i - 1]
        current_row = [1]

        for j in range(len(prev_row) - 1):
            next_number = prev_row[j] + prev_row[j + 1]
            current_row.append(next_number)

        current_row.append(1)
        triangle.append(current_row)

    return triangle


def print_pascals_triangle_centered(triangle: list[list[int]]) -> None:
    """
    以居中對齊的方式印出整個巴斯卡三角形。
    """

    # 1. 將每一列轉換為用空格隔開的字串，方便計算寬度
    row_strings = []
    for row in triangle:
        row_strings.append(" ".join(map(str, row)))

    # 2. 找出最寬的字串的長度（最後一列），用於計算每列需要多少前導空白來居中
    max_width = len(row_strings[-1])

    # 3. 遍歷每一列的字串，計算並印出前導空白
    for row_str in row_strings:
        current_width = len(row_str)
        padding = (max_width - current_width) // 2

        print(" " * padding + row_str)


if __name__ == "__main__":
    while True:
        try:
            max_row_index = int(input("\n巴斯卡三角形，請輸入顯示至第幾列："))
            if max_row_index >= 0:
                break
            else:
                print("請輸入非負整數。")
        except ValueError:
            print("輸入無效，請輸入非負整數。")

    print(
        "\n第 0 "
        + (f"～ {max_row_index} " if max_row_index > 0 else "")
        + "列的巴斯卡三角形如下：\n"
    )
    print_pascals_triangle_centered(generate_pascals_triangle(max_row_index))
