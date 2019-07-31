#!/usr/bin/env python3

# -*- coding: utf-8 -*-
import pandas as pd
from deprecation import deprecated

from .common import _getJson, _toDatetime


@deprecated(details='Deprecated: IEX Cloud status unknown')
def markets(token='', version='', filter=''):
    """https://iextrading.com/developer/docs/#intraday"""
    return _getJson('market', token, version, filter)


@deprecated(details='Deprecated: IEX Cloud status unknown')
def marketsDF(token='', version='', filter=''):
    """https://iextrading.com/developer/docs/#intraday"""
    df = pd.DataFrame(markets(token, version, filter))
    _toDatetime(df)
    return df
