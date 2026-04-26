"""
公司新聞爬蟲
"""

from .base import CompanyFetcher, CompanyDocument

from .adm import AdmFetcher
from .bunge import BungeFetcher
from .cargill import CargillFetcher
from .coca_cola import CocaColaFetcher
from .costco import CostcoFetcher
from .general_mills import GeneralMillsFetcher
from .kraft_heinz import KraftHeinzFetcher
from .mondelez import MondelezFetcher
from .nestle import NestleFetcher
from .pepsico import PepsicoFetcher
from .standard_foods import StandardFoodsFetcher
from .ttet import TtetFetcher
from .tyson import TysonFetcher
from .uni_president import UniPresidentFetcher
from .walmart import WalmartFetcher
from .wei_chuan import WeiChuanFetcher

FETCHERS = {
    "adm": AdmFetcher,
    "bunge": BungeFetcher,
    "cargill": CargillFetcher,
    "coca_cola": CocaColaFetcher,
    "costco": CostcoFetcher,
    "general_mills": GeneralMillsFetcher,
    "kraft_heinz": KraftHeinzFetcher,
    "mondelez": MondelezFetcher,
    "nestle": NestleFetcher,
    "pepsico": PepsicoFetcher,
    "standard_foods": StandardFoodsFetcher,
    "ttet": TtetFetcher,
    "tyson": TysonFetcher,
    "uni_president": UniPresidentFetcher,
    "walmart": WalmartFetcher,
    "wei_chuan": WeiChuanFetcher,
}
