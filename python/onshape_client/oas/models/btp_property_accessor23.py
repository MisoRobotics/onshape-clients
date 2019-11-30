# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.106
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTPPropertyAccessor23(object):
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
        'start_source_location': 'int',
        'end_source_location': 'int',
        'short_descriptor': 'str',
        'atomic': 'bool',
        'documentation_type': 'str',
        'space_before': 'BTPSpace10',
        'space_default': 'bool',
        'space_after': 'BTPSpace10',
        'node_id': 'str',
        'bt_type': 'str'
    }

    attribute_map = {
        'start_source_location': 'startSourceLocation',
        'end_source_location': 'endSourceLocation',
        'short_descriptor': 'shortDescriptor',
        'atomic': 'atomic',
        'documentation_type': 'documentationType',
        'space_before': 'spaceBefore',
        'space_default': 'spaceDefault',
        'space_after': 'spaceAfter',
        'node_id': 'nodeId',
        'bt_type': 'btType'
    }

    discriminator_value_class_map = {
        'BTPExpression-9': 'BTPExpression9',
        'BTPIdentifier-8': 'BTPIdentifier8'
    }

    def __init__(self, start_source_location=None, end_source_location=None, short_descriptor=None, atomic=None, documentation_type=None, space_before=None, space_default=None, space_after=None, node_id=None, bt_type=None):  # noqa: E501
        """BTPPropertyAccessor23 - a model defined in OpenAPI"""  # noqa: E501

        self._start_source_location = None
        self._end_source_location = None
        self._short_descriptor = None
        self._atomic = None
        self._documentation_type = None
        self._space_before = None
        self._space_default = None
        self._space_after = None
        self._node_id = None
        self._bt_type = None
        self.discriminator = 'bt_type'

        if start_source_location is not None:
            self.start_source_location = start_source_location
        if end_source_location is not None:
            self.end_source_location = end_source_location
        if short_descriptor is not None:
            self.short_descriptor = short_descriptor
        if atomic is not None:
            self.atomic = atomic
        if documentation_type is not None:
            self.documentation_type = documentation_type
        if space_before is not None:
            self.space_before = space_before
        if space_default is not None:
            self.space_default = space_default
        if space_after is not None:
            self.space_after = space_after
        if node_id is not None:
            self.node_id = node_id
        if bt_type is not None:
            self.bt_type = bt_type

    @property
    def start_source_location(self):
        """Gets the start_source_location of this BTPPropertyAccessor23.  # noqa: E501


        :return: The start_source_location of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: int
        """
        return self._start_source_location

    @start_source_location.setter
    def start_source_location(self, start_source_location):
        """Sets the start_source_location of this BTPPropertyAccessor23.


        :param start_source_location: The start_source_location of this BTPPropertyAccessor23.  # noqa: E501
        :type: int
        """

        self._start_source_location = start_source_location

    @property
    def end_source_location(self):
        """Gets the end_source_location of this BTPPropertyAccessor23.  # noqa: E501


        :return: The end_source_location of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: int
        """
        return self._end_source_location

    @end_source_location.setter
    def end_source_location(self, end_source_location):
        """Sets the end_source_location of this BTPPropertyAccessor23.


        :param end_source_location: The end_source_location of this BTPPropertyAccessor23.  # noqa: E501
        :type: int
        """

        self._end_source_location = end_source_location

    @property
    def short_descriptor(self):
        """Gets the short_descriptor of this BTPPropertyAccessor23.  # noqa: E501


        :return: The short_descriptor of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: str
        """
        return self._short_descriptor

    @short_descriptor.setter
    def short_descriptor(self, short_descriptor):
        """Sets the short_descriptor of this BTPPropertyAccessor23.


        :param short_descriptor: The short_descriptor of this BTPPropertyAccessor23.  # noqa: E501
        :type: str
        """

        self._short_descriptor = short_descriptor

    @property
    def atomic(self):
        """Gets the atomic of this BTPPropertyAccessor23.  # noqa: E501


        :return: The atomic of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: bool
        """
        return self._atomic

    @atomic.setter
    def atomic(self, atomic):
        """Sets the atomic of this BTPPropertyAccessor23.


        :param atomic: The atomic of this BTPPropertyAccessor23.  # noqa: E501
        :type: bool
        """

        self._atomic = atomic

    @property
    def documentation_type(self):
        """Gets the documentation_type of this BTPPropertyAccessor23.  # noqa: E501


        :return: The documentation_type of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: str
        """
        return self._documentation_type

    @documentation_type.setter
    def documentation_type(self, documentation_type):
        """Sets the documentation_type of this BTPPropertyAccessor23.


        :param documentation_type: The documentation_type of this BTPPropertyAccessor23.  # noqa: E501
        :type: str
        """
        allowed_values = ["FUNCTION", "PREDICATE", "CONSTANT", "ENUM", "USER_TYPE", "FEATURE_DEFINITION", "FILE_HEADER", "UNDOCUMENTABLE", "UNKNOWN"]  # noqa: E501
        if documentation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `documentation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(documentation_type, allowed_values)
            )

        self._documentation_type = documentation_type

    @property
    def space_before(self):
        """Gets the space_before of this BTPPropertyAccessor23.  # noqa: E501


        :return: The space_before of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_before

    @space_before.setter
    def space_before(self, space_before):
        """Sets the space_before of this BTPPropertyAccessor23.


        :param space_before: The space_before of this BTPPropertyAccessor23.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_before = space_before

    @property
    def space_default(self):
        """Gets the space_default of this BTPPropertyAccessor23.  # noqa: E501


        :return: The space_default of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: bool
        """
        return self._space_default

    @space_default.setter
    def space_default(self, space_default):
        """Sets the space_default of this BTPPropertyAccessor23.


        :param space_default: The space_default of this BTPPropertyAccessor23.  # noqa: E501
        :type: bool
        """

        self._space_default = space_default

    @property
    def space_after(self):
        """Gets the space_after of this BTPPropertyAccessor23.  # noqa: E501


        :return: The space_after of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: BTPSpace10
        """
        return self._space_after

    @space_after.setter
    def space_after(self, space_after):
        """Sets the space_after of this BTPPropertyAccessor23.


        :param space_after: The space_after of this BTPPropertyAccessor23.  # noqa: E501
        :type: BTPSpace10
        """

        self._space_after = space_after

    @property
    def node_id(self):
        """Gets the node_id of this BTPPropertyAccessor23.  # noqa: E501


        :return: The node_id of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this BTPPropertyAccessor23.


        :param node_id: The node_id of this BTPPropertyAccessor23.  # noqa: E501
        :type: str
        """

        self._node_id = node_id

    @property
    def bt_type(self):
        """Gets the bt_type of this BTPPropertyAccessor23.  # noqa: E501


        :return: The bt_type of this BTPPropertyAccessor23.  # noqa: E501
        :rtype: str
        """
        return self._bt_type

    @bt_type.setter
    def bt_type(self, bt_type):
        """Sets the bt_type of this BTPPropertyAccessor23.


        :param bt_type: The bt_type of this BTPPropertyAccessor23.  # noqa: E501
        :type: str
        """

        self._bt_type = bt_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, BTPPropertyAccessor23):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other