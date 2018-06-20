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


class V1DomainPresetSpec(object):
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
        'clock': 'V1Clock',
        'cpu': 'V1CPU',
        'devices': 'V1Devices',
        'features': 'V1Features',
        'firmware': 'V1Firmware',
        'machine': 'V1Machine',
        'memory': 'V1Memory',
        'resources': 'V1ResourceRequirements'
    }

    attribute_map = {
        'clock': 'clock',
        'cpu': 'cpu',
        'devices': 'devices',
        'features': 'features',
        'firmware': 'firmware',
        'machine': 'machine',
        'memory': 'memory',
        'resources': 'resources'
    }

    def __init__(self, clock=None, cpu=None, devices=None, features=None, firmware=None, machine=None, memory=None, resources=None):
        """
        V1DomainPresetSpec - a model defined in Swagger
        """

        self._clock = None
        self._cpu = None
        self._devices = None
        self._features = None
        self._firmware = None
        self._machine = None
        self._memory = None
        self._resources = None

        if clock is not None:
          self.clock = clock
        if cpu is not None:
          self.cpu = cpu
        if devices is not None:
          self.devices = devices
        if features is not None:
          self.features = features
        if firmware is not None:
          self.firmware = firmware
        if machine is not None:
          self.machine = machine
        if memory is not None:
          self.memory = memory
        if resources is not None:
          self.resources = resources

    @property
    def clock(self):
        """
        Gets the clock of this V1DomainPresetSpec.
        Clock sets the clock and timers of the vmi. +optional

        :return: The clock of this V1DomainPresetSpec.
        :rtype: V1Clock
        """
        return self._clock

    @clock.setter
    def clock(self, clock):
        """
        Sets the clock of this V1DomainPresetSpec.
        Clock sets the clock and timers of the vmi. +optional

        :param clock: The clock of this V1DomainPresetSpec.
        :type: V1Clock
        """

        self._clock = clock

    @property
    def cpu(self):
        """
        Gets the cpu of this V1DomainPresetSpec.
        CPU allow specified the detailed CPU topology inside the vmi. +optional

        :return: The cpu of this V1DomainPresetSpec.
        :rtype: V1CPU
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """
        Sets the cpu of this V1DomainPresetSpec.
        CPU allow specified the detailed CPU topology inside the vmi. +optional

        :param cpu: The cpu of this V1DomainPresetSpec.
        :type: V1CPU
        """

        self._cpu = cpu

    @property
    def devices(self):
        """
        Gets the devices of this V1DomainPresetSpec.
        Devices allows adding disks, network interfaces, ... +optional

        :return: The devices of this V1DomainPresetSpec.
        :rtype: V1Devices
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """
        Sets the devices of this V1DomainPresetSpec.
        Devices allows adding disks, network interfaces, ... +optional

        :param devices: The devices of this V1DomainPresetSpec.
        :type: V1Devices
        """

        self._devices = devices

    @property
    def features(self):
        """
        Gets the features of this V1DomainPresetSpec.
        Features like acpi, apic, hyperv +optional

        :return: The features of this V1DomainPresetSpec.
        :rtype: V1Features
        """
        return self._features

    @features.setter
    def features(self, features):
        """
        Sets the features of this V1DomainPresetSpec.
        Features like acpi, apic, hyperv +optional

        :param features: The features of this V1DomainPresetSpec.
        :type: V1Features
        """

        self._features = features

    @property
    def firmware(self):
        """
        Gets the firmware of this V1DomainPresetSpec.
        Firmware +optional

        :return: The firmware of this V1DomainPresetSpec.
        :rtype: V1Firmware
        """
        return self._firmware

    @firmware.setter
    def firmware(self, firmware):
        """
        Sets the firmware of this V1DomainPresetSpec.
        Firmware +optional

        :param firmware: The firmware of this V1DomainPresetSpec.
        :type: V1Firmware
        """

        self._firmware = firmware

    @property
    def machine(self):
        """
        Gets the machine of this V1DomainPresetSpec.
        Machine type +optional

        :return: The machine of this V1DomainPresetSpec.
        :rtype: V1Machine
        """
        return self._machine

    @machine.setter
    def machine(self, machine):
        """
        Sets the machine of this V1DomainPresetSpec.
        Machine type +optional

        :param machine: The machine of this V1DomainPresetSpec.
        :type: V1Machine
        """

        self._machine = machine

    @property
    def memory(self):
        """
        Gets the memory of this V1DomainPresetSpec.
        Memory allow specifying the VMI memory features. +optional

        :return: The memory of this V1DomainPresetSpec.
        :rtype: V1Memory
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """
        Sets the memory of this V1DomainPresetSpec.
        Memory allow specifying the VMI memory features. +optional

        :param memory: The memory of this V1DomainPresetSpec.
        :type: V1Memory
        """

        self._memory = memory

    @property
    def resources(self):
        """
        Gets the resources of this V1DomainPresetSpec.
        Resources describes the Compute Resources required by this vmi.

        :return: The resources of this V1DomainPresetSpec.
        :rtype: V1ResourceRequirements
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """
        Sets the resources of this V1DomainPresetSpec.
        Resources describes the Compute Resources required by this vmi.

        :param resources: The resources of this V1DomainPresetSpec.
        :type: V1ResourceRequirements
        """

        self._resources = resources

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
        if not isinstance(other, V1DomainPresetSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other