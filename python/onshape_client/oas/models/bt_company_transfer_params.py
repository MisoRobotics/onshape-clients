# coding: utf-8

"""
    Onshape REST API

    The Onshape REST API consumed by all clients.  # noqa: E501

    The version of the OpenAPI document: 1.103
    Contact: api-support@onshape.zendesk.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class BTCompanyTransferParams(object):
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
        'current_owner_id': 'str',
        'new_owner_id': 'str'
    }

    attribute_map = {
        'current_owner_id': 'currentOwnerId',
        'new_owner_id': 'newOwnerId'
    }

    def __init__(self, current_owner_id=None, new_owner_id=None):  # noqa: E501
        """BTCompanyTransferParams - a model defined in OpenAPI"""  # noqa: E501

        self._current_owner_id = None
        self._new_owner_id = None
        self.discriminator = None

        if current_owner_id is not None:
            self.current_owner_id = current_owner_id
        if new_owner_id is not None:
            self.new_owner_id = new_owner_id

    @property
    def current_owner_id(self):
        """Gets the current_owner_id of this BTCompanyTransferParams.  # noqa: E501


        :return: The current_owner_id of this BTCompanyTransferParams.  # noqa: E501
        :rtype: str
        """
        return self._current_owner_id

    @current_owner_id.setter
    def current_owner_id(self, current_owner_id):
        """Sets the current_owner_id of this BTCompanyTransferParams.


        :param current_owner_id: The current_owner_id of this BTCompanyTransferParams.  # noqa: E501
        :type: str
        """

        self._current_owner_id = current_owner_id

    @property
    def new_owner_id(self):
        """Gets the new_owner_id of this BTCompanyTransferParams.  # noqa: E501


        :return: The new_owner_id of this BTCompanyTransferParams.  # noqa: E501
        :rtype: str
        """
        return self._new_owner_id

    @new_owner_id.setter
    def new_owner_id(self, new_owner_id):
        """Sets the new_owner_id of this BTCompanyTransferParams.


        :param new_owner_id: The new_owner_id of this BTCompanyTransferParams.  # noqa: E501
        :type: str
        """

        self._new_owner_id = new_owner_id

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
        if not isinstance(other, BTCompanyTransferParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other