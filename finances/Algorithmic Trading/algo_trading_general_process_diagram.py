from diagrams import Diagram, Cluster
from diagrams.aws.database import Redshift
from diagrams.gcp.iot import IotCore
from diagrams.gcp.compute import AppEngine, Functions

graph_attr = {"fontsize": "45",
              "bgcolor": "transparent",
              # 'center': 'true'
              # 'concentrate':'false'
              'labelloc':"t"
              }

with Diagram('Algorithmic Trading General Process', direction='LR', filename='finances/Algorithmic Trading/algo_trading_general_process_diagram',graph_attr=graph_attr) as d:
  with Cluster('Researcg'):
    data = IotCore('Data')
    data_time = IotCore('Real-time/Historical')
    data_type = IotCore('Market/Non-market Data')

  data_time - data
  data_type - data

  with Cluster('Pre-trade Analysis'):
    pretrade_analysis = [Redshift('Alpha Model'),
                          Redshift('Risk Model'),
                          Redshift('Transaction Cost Model')]
  data >> pretrade_analysis

  with Cluster('Trading Signal'):
    trading_signal = AppEngine('Portfolio Construction Model')

  data >> trading_signal
  pretrade_analysis >> trading_signal

  with Cluster('Trade Execution'):
    trade_execution = Functions('Execution Model')

  data >> trade_execution
  trading_signal >> trade_execution

  post_trade_analysis = Redshift('Post-trade Analysis')

  trade_execution >> post_trade_analysis

d
