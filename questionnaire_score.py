# 平时作业02：简易焦虑问卷计分函数
def calc_anxiety_score(q1, q2, q3, q4):
    """
    简易焦虑问卷计分函数
    :param q1: 第1题得分，1‑4分
    :param q2: 第2题得分，1‑4分
    :param q3: 第3题得分，1‑4分
    :param q4: 第4题得分，1‑4分
    :return: total(问卷总分), level(焦虑等级)
    """
    total = q1 + q2 + q3 + q4
    if total <= 8:
        level = "低焦虑水平"
    elif total <=12:
        level = "中等焦虑水平"
    else:
        level = "高焦虑水平"
    # return返回多个结果
    return total, level


# ==========主程序，调用上面自定义函数==========
if __name__ == "__main__":
    print("====简易焦虑问卷计分程序====")
    s1 = int(input("请输入第1题得分(1‑4)："))
    s2 = int(input("请输入第2题得分(1‑4)："))
    s3 = int(input("请输入第3题得分(1‑4)："))
    s4 = int(input("请输入第4题得分(1‑4)："))

    # 调用自定义函数，传入实参，接收return返回值
    score_result, grade = calc_anxiety_score(s1, s2, s3, s4)
    print(f"问卷总分为：{score_result}")
    print(f"评估等级：{grade}")
