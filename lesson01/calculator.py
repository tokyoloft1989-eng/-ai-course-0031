"""第三步：比较年复利与单利，并完成输入校验。"""


def read_number(prompt, *, minimum=0, strict=False):
    """读取符合范围要求的数值，遇到无效输入时继续询问。"""
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("请输入数字。")
            continue
        if (value <= minimum) if strict else (value < minimum):
            if "利率" in prompt:
                print("利率不能为负，请重新输入。")
            else:
                print("请输入大于 0 的数值。")
            continue
        return value


def compound(principal, annual_rate, years, times_per_year=1):
    """复利终值：FV = PV × (1 + r/n) ** (n×t)。"""
    return principal * (1 + annual_rate / times_per_year) ** (
        times_per_year * years
    )


def simple(principal, annual_rate, years):
    """单利终值：FV = PV × (1 + r×t)。"""
    return principal * (1 + annual_rate * years)


def comparison_table(principal, annual_rate):
    header = f"{'年限':>4}  {'复利终值':>14}  {'单利终值':>14}  {'差额':>14}"
    rows = [header, "-" * len(header)]
    for years in (10, 20, 30):
        compound_value = compound(principal, annual_rate, years)
        simple_value = simple(principal, annual_rate, years)
        rows.append(
            f"{years:>4}  {compound_value:>14.2f}  {simple_value:>14.2f}  "
            f"{compound_value - simple_value:>14.2f}"
        )
    return "\n".join(rows)


def main():
    principal = read_number("请输入本金（元）：", strict=True)
    rate = read_number("请输入年利率（如 0.05 表示 5%）：")
    years = read_number("请输入年限：", strict=True)
    print(f"{years:g} 年后复利本息和：{compound(principal, rate, years):.2f} 元")
    print("\n复利与单利对比（年复利一次）")
    print(comparison_table(principal, rate))


if __name__ == "__main__":
    main()
