#!/usr/bin/env python3
import sys


def 失败(话):
    sys.stderr.write(话 + "\n")
    return 2


def 主程序(参数):
    if len(参数) < 3 or len(参数) > 5:
        return 失败("用法不对：请给出文稿路径和要找的词，词后面可以按顺序再写：不含 行首")
    路径 = 参数[1]
    词 = 参数[2]
    if 词 == "":
        return 失败("要找的词不能是空的")
    不含 = False
    行首 = False
    for 说法 in 参数[3:]:
        if 说法 == "不含" and not 不含 and not 行首:
            不含 = True
        elif 说法 == "行首" and not 行首:
            行首 = True
        else:
            return 失败("认不出这个说法：" + 说法 + "（说法只能按顺序写：不含 行首）")
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
            中 = 行.startswith(词)
        else:
            中 = 词 in 行
        if 不含:
            中 = not 中
        if 中:
            sys.stdout.write(行 + "\n")
            打出 = True
    if 打出:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(主程序(sys.argv))
