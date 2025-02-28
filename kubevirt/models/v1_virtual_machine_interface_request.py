# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1VirtualMachineInterfaceRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'add_interface_options': 'V1AddInterfaceOptions'
    }

    attribute_map = {
        'add_interface_options': 'addInterfaceOptions'
    }

    def __init__(self, add_interface_options=None):
        """
        V1VirtualMachineInterfaceRequest - a model defined in Swagger
        """

        self._add_interface_options = None

        if add_interface_options is not None:
          self.add_interface_options = add_interface_options

    @property
    def add_interface_options(self):
        """
        Gets the add_interface_options of this V1VirtualMachineInterfaceRequest.
        AddInterfaceOptions when set indicates a network interface should be added. The details within this field specify how to add the interface

        :return: The add_interface_options of this V1VirtualMachineInterfaceRequest.
        :rtype: V1AddInterfaceOptions
        """
        return self._add_interface_options

    @add_interface_options.setter
    def add_interface_options(self, add_interface_options):
        """
        Sets the add_interface_options of this V1VirtualMachineInterfaceRequest.
        AddInterfaceOptions when set indicates a network interface should be added. The details within this field specify how to add the interface

        :param add_interface_options: The add_interface_options of this V1VirtualMachineInterfaceRequest.
        :type: V1AddInterfaceOptions
        """

        self._add_interface_options = add_interface_options

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1VirtualMachineInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
