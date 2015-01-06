from yowsup.layers import YowLayer, YowLayerEvent, YowProtocolLayer
from .protocolentities import ImageDownloadableMediaMessageProtocolEntity
from .protocolentities import AudioDownloadableMediaMessageProtocolEntity
from .protocolentities import LocationMediaMessageProtocolEntity
from .protocolentities import VCardMediaMessageProtocolEntity

class YowMediaProtocolLayer(YowProtocolLayer):
    def __init__(self):
        handleMap = {
            "message": (self.recvMessageStanza, self.sendMessageEntity)
        }
        super(YowMediaProtocolLayer, self).__init__(handleMap)

    def __str__(self):
        return "Media Layer"

    def sendMessageEntity(self, entity):
        if entity.getType() == "media":
            self.entityToLower(entity)

    def recvMessageStanza(self, node):
        if node.getAttributeValue("type") == "media":
            mediaNode = node.getChild("media")
            if mediaNode.getAttributeValue("type") == "image":
                entity = ImageDownloadableMediaMessageProtocolEntity.fromProtocolTreeNode(node)
                self.toUpper(entity)
            elif mediaNode.getAttributeValue("type") == "audio":
                entity = AudioDownloadableMediaMessageProtocolEntity.fromProtocolTreeNode(node)
                self.toUpper(entity)
            elif mediaNode.getAttributeValue("type") == "location":
                entity = LocationMediaMessageProtocolEntity.fromProtocolTreeNode(node)
                self.toUpper(entity)
            elif mediaNode.getAttributeValue("type") == "vcard":
                entity = VCardMediaMessageProtocolEntity.fromProtocolTreeNode(node)
                self.toUpper(entity)
