
# coding: utf-8

from qgis.PyQt.QtWidgets import QTreeWidgetItem, QListWidgetItem
from qgis.PyQt.QtGui import QBrush, QColor, QIcon, QMovie


def create_list_resource_element(resource):
    return ListResourceTreeItem(resource)

def create_operation_list_item(oper):
    item = SupportedOperationListItem(oper)
    return item

def create_property_list_item(prop):
    item = SupportedPropertyListItem(prop)
    return item

def create_dummy_list_item(dummy_text):
    item = QListWidgetItem()
    item.setText(dummy_text)

    return item

def create_dummy_tree_item(dummy_text):
    item = QTreeWidgetItem()
    item.setText(0, dummy_text)

    return item

def create_icon(dir_=None):
    return QIcon(dir_)

def create_gif_icon(dir_=None):
    icon = QIcon()
    movie = QMovie(dir_)

    def update_icon():
        i = QIcon(movie.currentPixmap())
        icon.swap(i)

    movie.frameChanged.connect(update_icon)
    movie.start()

    return icon



# Classe de itens que serão adicionados à list_resource em dialog_construct_url_2
class ListResourceTreeItem(QTreeWidgetItem):
    # 0 - name
    # 1 - url
    def __init__(self, resource):
        super(ListResourceTreeItem, self).__init__()

        self.resource = resource

        self.setName(resource.name)
        self.setUrl(resource.iri)

        #self.setBackground(0, QBrush(QColor(255, 252, 226)))

    def setName(self, name):
        self.setText(0, name)

    def name(self):
        return self.text(0)

    def setUrl(self, url):
        self.setText(1, url)

        if self.resource.error:
            msg = u'Indisponível - {}'.format(self.resource.iri)
        else:
            msg = self.resource.iri

        self.setToolTip(0, msg)

    def url(self):
        return self.text(1)

    def set_icon_error(self):
        entry_point_icon = QIcon(':/plugins/IBGEVisualizer/icon_error.png')
        self.setIcon(0, entry_point_icon)

    def set_icon_entry_point(self):
        entry_point_icon = QIcon(':/plugins/IBGEVisualizer/icon-entry-point.png')
        self.setIcon(0, entry_point_icon)

    def set_color_user_resource(self):
        yellow = QBrush(QColor(255, 252, 226))
        self.setBackground(0, yellow)


# Classe de itens que serão adicionados à list_attributes em dialog_construct_url_2
class SupportedOperationListItem(QListWidgetItem):
    def __init__(self, oper):
        super(SupportedOperationListItem, self).__init__()

        self.property = oper
        self.type_ = 'supported_operation'
        self.name = self.property.name

        self.setText(self.name)

        self.setToolTip(str(self.property))
        self.setBackground(QBrush(QColor(255, 252, 226)))


from IBGEVisualizer.HyperResource import SupportedProperty
class SupportedPropertyListItem(QListWidgetItem):
    def __init__(self, prop: SupportedProperty):
        super(SupportedPropertyListItem, self).__init__()

        self.property = prop
        self.type_ = 'supported_property'
        self.name = self.property.name

        self.setText(self.name)

        self.setToolTip(str(self.property))
        self.setBackground(QBrush(QColor(255, 237, 248)))
