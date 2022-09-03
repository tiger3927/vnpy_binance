from vnpy.trader.setting import SETTINGS
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp

from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp
from vnpy_spreadtrading import SpreadTradingApp
from vnpy_algotrading import AlgoTradingApp
from vnpy_optionmaster import OptionMasterApp
from vnpy_portfoliostrategy import PortfolioStrategyApp
from vnpy_scripttrader import ScriptTraderApp
from vnpy_chartwizard import ChartWizardApp
#from vnpy_rpcservice import RpcServiceApp
#from vnpy_excelrtd import ExcelRtdApp
from vnpy_datamanager import DataManagerApp
from vnpy_datarecorder import DataRecorderApp
from vnpy_riskmanager import RiskManagerApp
#from vnpy_webtrader import WebTraderApp
from vnpy_portfoliomanager import PortfolioManagerApp


from vnpy_binance import (
    BinanceSpotGateway,
    BinanceUsdtGateway,
    BinanceInverseGateway
)


SETTINGS["datafeed.name"]="coinapi"
SETTINGS["datafeed.username"]="key"
SETTINGS["datafeed.password"]="E0AE25FD-6790-4AAF-A313-9DD1E49A9AD1"


#   1131329-896E-4FD2-9F-85DF1E8

def main():
    """主入口函数"""

    SETTINGS["datafeed.name"] = "coinapi"
    SETTINGS["datafeed.username"] = "key"
    SETTINGS["datafeed.password"] = "E0AE25FD-6790-4AAF-A313-9DD1E49A9AD1"

    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    #main_engine.add_gateway(BinanceSpotGateway)
    main_engine.add_gateway(BinanceUsdtGateway)
    #main_engine.add_gateway(BinanceInverseGateway)

    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)
    main_engine.add_app(SpreadTradingApp)
    main_engine.add_app(AlgoTradingApp)
    main_engine.add_app(OptionMasterApp)
    main_engine.add_app(PortfolioStrategyApp)
    main_engine.add_app(ScriptTraderApp)
    main_engine.add_app(ChartWizardApp)
    #main_engine.add_app(RpcServiceApp)
    #main_engine.add_app(ExcelRtdApp)
    main_engine.add_app(DataManagerApp)
    main_engine.add_app(DataRecorderApp)
    main_engine.add_app(RiskManagerApp)
    #main_engine.add_app(WebTraderApp)
    main_engine.add_app(PortfolioManagerApp)



    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()


if __name__ == "__main__":
    main()
