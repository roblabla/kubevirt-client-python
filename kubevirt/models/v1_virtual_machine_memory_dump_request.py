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


class V1VirtualMachineMemoryDumpRequest(object):
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
        'end_timestamp': 'K8sIoApimachineryPkgApisMetaV1Time',
        'file_name': 'str',
        'message': 'str',
        'phase': 'str',
        'remove': 'bool',
        'start_timestamp': 'K8sIoApimachineryPkgApisMetaV1Time'
    }

    attribute_map = {
        'claim_name': 'claimName',
        'end_timestamp': 'endTimestamp',
        'file_name': 'fileName',
        'message': 'message',
        'phase': 'phase',
        'remove': 'remove',
        'start_timestamp': 'startTimestamp'
    }

    def __init__(self, claim_name=None, end_timestamp=None, file_name=None, message=None, phase=None, remove=None, start_timestamp=None):
        """
        V1VirtualMachineMemoryDumpRequest - a model defined in Swagger
        """

        self._claim_name = None
        self._end_timestamp = None
        self._file_name = None
        self._message = None
        self._phase = None
        self._remove = None
        self._start_timestamp = None

        self.claim_name = claim_name
        if end_timestamp is not None:
          self.end_timestamp = end_timestamp
        if file_name is not None:
          self.file_name = file_name
        if message is not None:
          self.message = message
        self.phase = phase
        if remove is not None:
          self.remove = remove
        if start_timestamp is not None:
          self.start_timestamp = start_timestamp

    @property
    def claim_name(self):
        """
        Gets the claim_name of this V1VirtualMachineMemoryDumpRequest.
        ClaimName is the name of the pvc that will contain the memory dump

        :return: The claim_name of this V1VirtualMachineMemoryDumpRequest.
        :rtype: str
        """
        return self._claim_name

    @claim_name.setter
    def claim_name(self, claim_name):
        """
        Sets the claim_name of this V1VirtualMachineMemoryDumpRequest.
        ClaimName is the name of the pvc that will contain the memory dump

        :param claim_name: The claim_name of this V1VirtualMachineMemoryDumpRequest.
        :type: str
        """
        if claim_name is None:
            raise ValueError("Invalid value for `claim_name`, must not be `None`")

        self._claim_name = claim_name

    @property
    def end_timestamp(self):
        """
        Gets the end_timestamp of this V1VirtualMachineMemoryDumpRequest.
        EndTimestamp represents the time the memory dump was completed

        :return: The end_timestamp of this V1VirtualMachineMemoryDumpRequest.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        """
        Sets the end_timestamp of this V1VirtualMachineMemoryDumpRequest.
        EndTimestamp represents the time the memory dump was completed

        :param end_timestamp: The end_timestamp of this V1VirtualMachineMemoryDumpRequest.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._end_timestamp = end_timestamp

    @property
    def file_name(self):
        """
        Gets the file_name of this V1VirtualMachineMemoryDumpRequest.
        FileName represents the name of the output file

        :return: The file_name of this V1VirtualMachineMemoryDumpRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this V1VirtualMachineMemoryDumpRequest.
        FileName represents the name of the output file

        :param file_name: The file_name of this V1VirtualMachineMemoryDumpRequest.
        :type: str
        """

        self._file_name = file_name

    @property
    def message(self):
        """
        Gets the message of this V1VirtualMachineMemoryDumpRequest.
        Message is a detailed message about failure of the memory dump

        :return: The message of this V1VirtualMachineMemoryDumpRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this V1VirtualMachineMemoryDumpRequest.
        Message is a detailed message about failure of the memory dump

        :param message: The message of this V1VirtualMachineMemoryDumpRequest.
        :type: str
        """

        self._message = message

    @property
    def phase(self):
        """
        Gets the phase of this V1VirtualMachineMemoryDumpRequest.
        Phase represents the memory dump phase

        :return: The phase of this V1VirtualMachineMemoryDumpRequest.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1VirtualMachineMemoryDumpRequest.
        Phase represents the memory dump phase

        :param phase: The phase of this V1VirtualMachineMemoryDumpRequest.
        :type: str
        """
        if phase is None:
            raise ValueError("Invalid value for `phase`, must not be `None`")

        self._phase = phase

    @property
    def remove(self):
        """
        Gets the remove of this V1VirtualMachineMemoryDumpRequest.
        Remove represents request of dissociating the memory dump pvc

        :return: The remove of this V1VirtualMachineMemoryDumpRequest.
        :rtype: bool
        """
        return self._remove

    @remove.setter
    def remove(self, remove):
        """
        Sets the remove of this V1VirtualMachineMemoryDumpRequest.
        Remove represents request of dissociating the memory dump pvc

        :param remove: The remove of this V1VirtualMachineMemoryDumpRequest.
        :type: bool
        """

        self._remove = remove

    @property
    def start_timestamp(self):
        """
        Gets the start_timestamp of this V1VirtualMachineMemoryDumpRequest.
        StartTimestamp represents the time the memory dump started

        :return: The start_timestamp of this V1VirtualMachineMemoryDumpRequest.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        """
        Sets the start_timestamp of this V1VirtualMachineMemoryDumpRequest.
        StartTimestamp represents the time the memory dump started

        :param start_timestamp: The start_timestamp of this V1VirtualMachineMemoryDumpRequest.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._start_timestamp = start_timestamp

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
        if not isinstance(other, V1VirtualMachineMemoryDumpRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
