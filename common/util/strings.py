# coding=utf-8
"""
    create by pymu
    on 2020/12/28
    at 16:24
    字符串处理工具
"""
# qss变量定义正则匹配公式
import re
from typing import List

REGEX_DEFINED = re.compile("DEFINED_VALUE\{(.*?)\}", re.S)


def format_style_file(text: str) -> str:
    """对样式表进行变量替换"""
    values: List[str] = re.findall(REGEX_DEFINED, text)
    text = re.sub(REGEX_DEFINED, "", text)
    if values:
        for i in values[0].split("\n"):
            if i:
                i = i.replace(" ", "").replace("\t", "").split(":")
                text = text.replace(f"var({i[0]});", i[1])
    return text
