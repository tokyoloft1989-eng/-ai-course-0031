"""第一步：用已知数据验证年复利公式。"""

principal = 10000.0  # 本金，单位：元
annual_rate = 0.05  # 年利率 5%，写作小数 0.05
years = 3  # 存款年数
compounds_per_year = 1  # 每年复利一次

# FV = PV × (1 + r/n) ** (n×t)
future_value = principal * (1 + annual_rate / compounds_per_year) ** (
    compounds_per_year * years
)
print(f"最终本息和：{future_value:.2f} 元")
