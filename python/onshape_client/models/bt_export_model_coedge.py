# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    OpenAPI spec version: 1.94
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTExportModelCoedge(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'edge_id': 'str',
        'orientation': 'bool',
        'export_type_name': 'str',
        'connection_source': 'BTConnection',
        'unknown_class': 'bool',
        'type_id': 'int'
    }

    attribute_map = {
        'edge_id': 'edgeId',
        'orientation': 'orientation',
        'export_type_name': 'exportTypeName',
        'connection_source': 'connectionSource',
        'unknown_class': 'unknownClass',
        'type_id': 'typeId'
    }

    def __init__(self, edge_id=None, orientation=None, export_type_name=None, connection_source=None, unknown_class=None, type_id=None):  # noqa: E501
        """BTExportModelCoedge - a model defined in OpenAPI"""  # noqa: E501

        self._edge_id = None
        self._orientation = None
        self._export_type_name = None
        self._connection_source = None
        self._unknown_class = None
        self._type_id = None
        self.discriminator = None

        if edge_id is not None:
            self.edge_id = edge_id
        if orientation is not None:
            self.orientation = orientation
        if export_type_name is not None:
            self.export_type_name = export_type_name
        if connection_source is not None:
            self.connection_source = connection_source
        if unknown_class is not None:
            self.unknown_class = unknown_class
        if type_id is not None:
            self.type_id = type_id

    @property
    def edge_id(self):
        """Gets the edge_id of this BTExportModelCoedge.  # noqa: E501


        :return: The edge_id of this BTExportModelCoedge.  # noqa: E501
        :rtype: str
        """
        return self._edge_id

    @edge_id.setter
    def edge_id(self, edge_id):
        """Sets the edge_id of this BTExportModelCoedge.


        :param edge_id: The edge_id of this BTExportModelCoedge.  # noqa: E501
        :type: str
        """

        self._edge_id = edge_id

    @property
    def orientation(self):
        """Gets the orientation of this BTExportModelCoedge.  # noqa: E501


        :return: The orientation of this BTExportModelCoedge.  # noqa: E501
        :rtype: bool
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this BTExportModelCoedge.


        :param orientation: The orientation of this BTExportModelCoedge.  # noqa: E501
        :type: bool
        """

        self._orientation = orientation

    @property
    def export_type_name(self):
        """Gets the export_type_name of this BTExportModelCoedge.  # noqa: E501


        :return: The export_type_name of this BTExportModelCoedge.  # noqa: E501
        :rtype: str
        """
        return self._export_type_name

    @export_type_name.setter
    def export_type_name(self, export_type_name):
        """Sets the export_type_name of this BTExportModelCoedge.


        :param export_type_name: The export_type_name of this BTExportModelCoedge.  # noqa: E501
        :type: str
        """

        self._export_type_name = export_type_name

    @property
    def connection_source(self):
        """Gets the connection_source of this BTExportModelCoedge.  # noqa: E501


        :return: The connection_source of this BTExportModelCoedge.  # noqa: E501
        :rtype: BTConnection
        """
        return self._connection_source

    @connection_source.setter
    def connection_source(self, connection_source):
        """Sets the connection_source of this BTExportModelCoedge.


        :param connection_source: The connection_source of this BTExportModelCoedge.  # noqa: E501
        :type: BTConnection
        """

        self._connection_source = connection_source

    @property
    def unknown_class(self):
        """Gets the unknown_class of this BTExportModelCoedge.  # noqa: E501


        :return: The unknown_class of this BTExportModelCoedge.  # noqa: E501
        :rtype: bool
        """
        return self._unknown_class

    @unknown_class.setter
    def unknown_class(self, unknown_class):
        """Sets the unknown_class of this BTExportModelCoedge.


        :param unknown_class: The unknown_class of this BTExportModelCoedge.  # noqa: E501
        :type: bool
        """

        self._unknown_class = unknown_class

    @property
    def type_id(self):
        """Gets the type_id of this BTExportModelCoedge.  # noqa: E501


        :return: The type_id of this BTExportModelCoedge.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this BTExportModelCoedge.


        :param type_id: The type_id of this BTExportModelCoedge.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BTExportModelCoedge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other