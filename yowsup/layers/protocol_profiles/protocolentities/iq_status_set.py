from yowsup.layers.protocol_iq.protocolentities import IqProtocolEntity
from yowsup.structs import ProtocolTreeNode

class SetStatusIqProtocolEntity(IqProtocolEntity):
    '''
    <iq to="s.whatsapp.net" xmlns="status" type="set" id="{{IQ_ID}}">
        <status>{{MSG}}</status>
    </notification>
    '''

    def __init__(self, _id=None, msg=None):
        super(SetStatusIqProtocolEntity, self).__init__(_id, _type = "set", to = "s.whatsapp.net")
        self.setData(msg)
        
    def setData(self, msg):
        self.msg = msg

    def toProtocolTreeNode(self):
        node = super(SetStatusIqProtocolEntity, self).toProtocolTreeNode()
        statusNode = ProtocolTreeNode("status", {}, [], self.msg)
        node.addChild(statusNode)
        return node

    @staticmethod
    def fromProtocolTreeNode(node):
        entity = IqProtocolEntity.fromProtocolTreeNode(node)
        entity.__class__ = SetStatusIqProtocolEntity
        statusNode = node.getChild("status")
        entity.setData(statusNode.getData())
        return entity
