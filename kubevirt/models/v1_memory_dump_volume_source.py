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


class V1MemoryDumpVolumeSource(object):
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
        'claim_name': 'str',
        'hotpluggable': 'bool',
        'read_only': 'bool'
    }

    attribute_map = {
        'claim_name': 'claimName',
        'hotpluggable': 'hotpluggable',
        'read_only': 'readOnly'
    }

    def __init__(self, claim_name=None, hotpluggable=None, read_only=None):
        """
        V1MemoryDumpVolumeSource - a model defined in Swagger
        """

        self._claim_name = None
        self._hotpluggable = None
        self._read_only = None

        self.claim_name = claim_name
        if hotpluggable is not None:
          self.hotpluggable = hotpluggable
        if read_only is not None:
          self.read_only = read_only

    @property
    def claim_name(self):
        """
        Gets the claim_name of this V1MemoryDumpVolumeSource.
        ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

        :return: The claim_name of this V1MemoryDumpVolumeSource.
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """
        Sets the claim_name of this V1MemoryDumpVolumeSource.
        ClaimName is the name of a PersistentVolumeClaim in the same namespace as the pod using this volume. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims

        :param claim_name: The claim_name of this V1MemoryDumpVolumeSource.
        :type: str
        """
        if claim_name is None:
            raise ValueError("Invalid value for `claim_name`, must not be `None`")

        self._claim_name = claim_name

    @property
    def hotpluggable(self):
        """
        Gets the hotpluggable of this V1MemoryDumpVolumeSource.
        Hotpluggable indicates whether the volume can be hotplugged and hotunplugged.

        :return: The hotpluggable of this V1MemoryDumpVolumeSource.
        :rtype: bool
        """
        return self._hotpluggable

    @hotpluggable.setter
    def hotpluggable(self, hotpluggable):
        """
        Sets the hotpluggable of this V1MemoryDumpVolumeSource.
        Hotpluggable indicates whether the volume can be hotplugged and hotunplugged.

        :param hotpluggable: The hotpluggable of this V1MemoryDumpVolumeSource.
        :type: bool
        """

        self._hotpluggable = hotpluggable

    @property
    def read_only(self):
        """
        Gets the read_only of this V1MemoryDumpVolumeSource.
        Will force the ReadOnly setting in VolumeMounts. Default false.

        :return: The read_only of this V1MemoryDumpVolumeSource.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1MemoryDumpVolumeSource.
        Will force the ReadOnly setting in VolumeMounts. Default false.

        :param read_only: The read_only of this V1MemoryDumpVolumeSource.
        :type: bool
        """

        self._read_only = read_only

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
        if not isinstance(other, V1MemoryDumpVolumeSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
