#!/usr/bin/env python3
import sys


def 失败(话):
    sys.stderr.write(话 + "\n")
    return 2


def 主程序(参数):
    if len(参数) != 3:
        return 失败("用法不对：请给出文稿路径和要找的词")
    路径 = 参数[1]
    词 = 参数[2]
    if 词 == "":
        return 失败("要找的词不能是空的")
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
        if 词 in 行:
            sys.stdout.write(行 + "\n")
            打出 = True
    if 打出:
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(主程序(sys.argv))
