from pox.core import core
import pox.openflow.libopenflow_01 as of
import pox.lib.packet as pkt
from pox.lib.revent import *
from pox.lib.addresses import EthAddr, IPAddr

block_nodes = [['00:00:00:00:00:03','00:00:00:00:00:06'], ['00:00:00:00:00:04', '00:00:00:00:00:12'], ['00:00:00:00:00:05','00:00:00:00:00:01'], ['00:00:00:00:00:01','00:00:00:00:00:10']]

class Murofogo(EventMixin):
    
    def __init__(self):
        self.listenTo(core.openflow)
        
    def _handle_ConnectionUp(self, event):
        for block_node in block_nodes:
            block = of.ofp_match()
            block.dl_src = EthAddr(block_node[0])
            block.dl_dst = EthAddr(block_node[1])
            flow_mod = of.ofp_flow_mod()
            flow_mod.match = block
            event.connection.send(flow_mod)
         
  
def launch ():
    core.registerNew(Murofogo)
