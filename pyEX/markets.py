#!/usr/bin/env python3

import pandas as pd
from deprecation import deprecated

from .common import _getJson, _toDatetime


@deprecated(details='Deprecated: IEX Cloud status unknown')
def markets(token='', version=''):
    """https://iextrading.com/developer/docs/#intraday"""
    return _getJson('market', token, version)


@deprecated(details='Deprecated: IEX Cloud status unknown')
def marketsDF(token='', version=''):
    """https://iextrading.com/developer/docs/#intraday"""
    df = pd.DataFrame(markets(token, version))
    _toDatetime(df)
    return df
