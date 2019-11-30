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


class BTPStatementConstantDeclaration273AllOf(object):
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
        'standard_type': 'str',
        'type_name': 'str',
        'name': 'BTPIdentifier8',
        'value': 'BTPExpression9',
        'type': 'BTPTypeName290'
    }

    attribute_map = {
        'standard_type': 'standardType',
        'type_name': 'typeName',
        'name': 'name',
        'value': 'value',
        'type': 'type'
    }

    def __init__(self, standard_type=None, type_name=None, name=None, value=None, type=None):  # noqa: E501
        """BTPStatementConstantDeclaration273AllOf - a model defined in OpenAPI"""  # noqa: E501

        self._standard_type = None
        self._type_name = None
        self._name = None
        self._value = None
        self._type = None
        self.discriminator = None

        if standard_type is not None:
            self.standard_type = standard_type
        if type_name is not None:
            self.type_name = type_name
        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type

    @property
    def standard_type(self):
        """Gets the standard_type of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501


        :return: The standard_type of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :rtype: str
        """
        return self._standard_type

    @standard_type.setter
    def standard_type(self, standard_type):
        """Sets the standard_type of this BTPStatementConstantDeclaration273AllOf.


        :param standard_type: The standard_type of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNDEFINED", "BOOLEAN", "NUMBER", "STRING", "ARRAY", "MAP", "BOX", "BUILTIN", "FUNCTION", "UNKNOWN"]  # noqa: E501
        if standard_type not in allowed_values:
            raise ValueError(
                "Invalid value for `standard_type` ({0}), must be one of {1}"  # noqa: E501
                .format(standard_type, allowed_values)
            )

        self._standard_type = standard_type

    @property
    def type_name(self):
        """Gets the type_name of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501


        :return: The type_name of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this BTPStatementConstantDeclaration273AllOf.


        :param type_name: The type_name of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    @property
    def name(self):
        """Gets the name of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501


        :return: The name of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :rtype: BTPIdentifier8
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BTPStatementConstantDeclaration273AllOf.


        :param name: The name of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :type: BTPIdentifier8
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501


        :return: The value of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :rtype: BTPExpression9
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BTPStatementConstantDeclaration273AllOf.


        :param value: The value of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :type: BTPExpression9
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501


        :return: The type of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :rtype: BTPTypeName290
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BTPStatementConstantDeclaration273AllOf.


        :param type: The type of this BTPStatementConstantDeclaration273AllOf.  # noqa: E501
        :type: BTPTypeName290
        """

        self._type = type

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
        if not isinstance(other, BTPStatementConstantDeclaration273AllOf):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other