"""第二步：交互输入并拦截负利率。"""


def read_rate():
    """读取年利率；负数需要重新输入。"""
    while True:
        try:
            rate = float(input("请输入年利率（如 0.05 表示 5%）："))
        except ValueError:
            print("请输入数字，例如 0.05。")
            continue
        if rate < 0:
            print("利率不能为负，请重新输入。")
            continue
        return rate


def main():
    principal = float(input("请输入本金（元）："))
    rate = read_rate()
    years = float(input("请输入年限："))
    future_value = principal * (1 + rate) ** years
    print(f"最终本息和：{future_value:.2f} 元")


if __name__ == "__main__":
    main()
