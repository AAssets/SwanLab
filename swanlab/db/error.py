#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
@DATE: 2024-01-18 15:16:55
@File: swanlab/db/error.py
@IDE: vscode
@Description:
    在此处定义所有的错误类型，以便于在其他地方引用
"""


class ExistedError(Exception):
    """某条数据已存在

    Parameters
    ----------
    Exception : class
        python内置异常类
    """

    pass


class NotExistedError(Exception):
    """某条数据不存在

    Parameters
    ----------
    Exception : class
        python内置异常类
    """

    pass


class ForeignExpNotExistedError(NotExistedError):
    """实验外键不存在"""

    pass


class ForeignProNotExistedError(NotExistedError):
    """项目外键不存在"""

    pass


class ParameterError(Exception):
    """参数错误"""

    pass
