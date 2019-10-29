import random

def 变(天地之数):
    tmp = random.randint(0,49)
    left = 天地之数 -tmp
    right = tmp
    # print(left, right)
    # 挂一
    left = left - 1
    # print(left)
    # 揲四 归奇
    left_rem = left % 4 if left % 4 != 0 else 4
    right_rem = right % 4 if right % 4 != 0 else 4
    # print(left_rem, right_rem)
    策 = left + right - left_rem - right_rem + 1
    return 策

def 爻():
    天地之数 = 55 - 6
    for _ in range(3):
        天地之数 = 变(天地之数)
        # print(f'天地之数{天地之数}')
    # print(f'一爻{天地之数 - 1}')
    if (天地之数 - 1) / 4 % 2 == 0:
        # print('阴')
        return '阴'
    else:
        # print('阳')
        return '阳'
# 乾（☰）、震（☳）、坎（☵）、艮（☶）、坤（☷）、巽（☴）、离（☲）、兑（☱）
八卦 = {
    '阳阳阳': '乾（☰）',
    '阴阴阳': '震（☳）',
    '阴阳阴': '坎（☵）',
    '阳阴阴': '艮（☶）',
    '阴阴阴': '坤（☷）',
    '阳阳阴': '巽（☴）',
    '阳阴阳': '离（☲）',
    '阴阳阳': '兑（☱）',
}

def 卦():
    一卦 = []
    for _ in range(6):
        一爻 = 爻()
        一卦.append(一爻)
    一卦.reverse()
    上卦 = 八卦.get(''.join(_ for _ in 一卦[0:3]))
    下卦 = 八卦.get(''.join(_ for _ in 一卦[3:6]))
    print(一卦)  # 这里是从上往下
    print(f'上{上卦}下{下卦}')
卦()