from enum import Enum


class Parameters(str, Enum):
    ACTION = "action"
    ADDRESS = "address"
    APIKEY = "apikey"
    CONTRACTADDRESS = "contractaddress"
    ENDBLOCK = "endblock"
    MODULE = "module"
    OFFSET = "offset"
    PAGE = "page"
    SORT = "sort"
    STARTBLOCK = "startblock"
    TAG = "tag"
    URL = "url"


class Modules(str, Enum):
    ACCOUNT = "account"
    CONTRACT = "contract"
    STATS = "stats"


class Actions(str, Enum):
    BALANCEMULTI = "balancemulti"
    GETABI = "getabi"
    TOKENBALANCE = "tokenbalance"
    TOKENTX = "tokentx"
    TXLIST = "txlist"
    GETSOURCECODE = "getsourcecode"
