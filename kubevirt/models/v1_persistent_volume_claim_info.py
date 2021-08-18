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


class V1PersistentVolumeClaimInfo(object):
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
        'access_modes': 'list[str]',
        'capacity': 'dict(str, K8sIoApimachineryPkgApiResourceQuantity)',
        'preallocated': 'bool',
        'volume_mode': 'str'
    }

    attribute_map = {
        'access_modes': 'accessModes',
        'capacity': 'capacity',
        'preallocated': 'preallocated',
        'volume_mode': 'volumeMode'
    }

    def __init__(self, access_modes=None, capacity=None, preallocated=None, volume_mode=None):
        """
        V1PersistentVolumeClaimInfo - a model defined in Swagger
        """

        self._access_modes = None
        self._capacity = None
        self._preallocated = None
        self._volume_mode = None

        if access_modes is not None:
          self.access_modes = access_modes
        if capacity is not None:
          self.capacity = capacity
        if preallocated is not None:
          self.preallocated = preallocated
        if volume_mode is not None:
          self.volume_mode = volume_mode

    @property
    def access_modes(self):
        """
        Gets the access_modes of this V1PersistentVolumeClaimInfo.
        AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

        :return: The access_modes of this V1PersistentVolumeClaimInfo.
        :rtype: list[str]
        """
        return self._access_modes

    @access_modes.setter
    def access_modes(self, access_modes):
        """
        Sets the access_modes of this V1PersistentVolumeClaimInfo.
        AccessModes contains the desired access modes the volume should have. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1

        :param access_modes: The access_modes of this V1PersistentVolumeClaimInfo.
        :type: list[str]
        """

        self._access_modes = access_modes

    @property
    def capacity(self):
        """
        Gets the capacity of this V1PersistentVolumeClaimInfo.
        Capacity represents the capacity set on the corresponding PVC spec

        :return: The capacity of this V1PersistentVolumeClaimInfo.
        :rtype: dict(str, K8sIoApimachineryPkgApiResourceQuantity)
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Sets the capacity of this V1PersistentVolumeClaimInfo.
        Capacity represents the capacity set on the corresponding PVC spec

        :param capacity: The capacity of this V1PersistentVolumeClaimInfo.
        :type: dict(str, K8sIoApimachineryPkgApiResourceQuantity)
        """

        self._capacity = capacity

    @property
    def preallocated(self):
        """
        Gets the preallocated of this V1PersistentVolumeClaimInfo.
        Preallocated indicates if the PVC's storage is preallocated or not

        :return: The preallocated of this V1PersistentVolumeClaimInfo.
        :rtype: bool
        """
        return self._preallocated

    @preallocated.setter
    def preallocated(self, preallocated):
        """
        Sets the preallocated of this V1PersistentVolumeClaimInfo.
        Preallocated indicates if the PVC's storage is preallocated or not

        :param preallocated: The preallocated of this V1PersistentVolumeClaimInfo.
        :type: bool
        """

        self._preallocated = preallocated

    @property
    def volume_mode(self):
        """
        Gets the volume_mode of this V1PersistentVolumeClaimInfo.
        VolumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.

        :return: The volume_mode of this V1PersistentVolumeClaimInfo.
        :rtype: str
        """
        return self._volume_mode

    @volume_mode.setter
    def volume_mode(self, volume_mode):
        """
        Sets the volume_mode of this V1PersistentVolumeClaimInfo.
        VolumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.

        :param volume_mode: The volume_mode of this V1PersistentVolumeClaimInfo.
        :type: str
        """

        self._volume_mode = volume_mode

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
        if not isinstance(other, V1PersistentVolumeClaimInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other