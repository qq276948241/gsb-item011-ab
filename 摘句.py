#!/usr/bin/env python3
import sys


def 失败(话):
    sys.stderr.write(话 + "\n")
    return 2


def 主程序(参数):
    if len(参数) < 3 or len(参数) > 5:
        return 失败("用法不对：请给出文稿路径和要找的词，词后面可以再写不含和行首")
    路径 = 参数[1]
    词 = 参数[2]
    if 词 == "":
        return 失败("要找的词不能是空的")
    不含 = False
    行首 = False
    说法们 = 参数[3:]
    if len(说法们) == 1:
        if 说法们[0] == "不含":
            不含 = True
        elif 说法们[0] == "行首":
            行首 = True
        else:
            return 失败("认不出这个说法：" + 说法们[0])
    elif len(说法们) == 2:
        if 说法们[0] == "不含" and 说法们[1] == "行首":
            不含 = True
            行首 = True
        elif 说法们[0] == "行首" and 说法们[1] == "不含":
            return 失败("说法顺序不对：要先写不含再写行首")
        else:
            return 失败("认不出这个说法：" + 说法们[0] + " " + 说法们[1])
    try:
        import os
        if os.path.isdir(路径):
            return 失败("这不是一份文稿：" + 路径)
        文件 = open(路径, "r", encoding="utf-8", newline="")
    except OSError:
        return 失败("读不了这份文稿：" + 路径)
    try:
        正文 = 文件.read()
    finally:
        文件.close()
    if 正文 == "":
        return 1
    行们 = 正文.split("\n")
    if 正文.endswith("\n"):
        行们 = 行们[:-1]
    打出 = False
    for 行 in 行们:
        if 行首:
            碰上 = 行.startswith(词)
        else:
            碰上 = 词 in 行
        if 不含:
            碰上 = not 碰上
        if 碰上:
            sys.stdout.write(行 + "\n")
            打出 = True
    if 打出:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(主程序(sys.argv))
