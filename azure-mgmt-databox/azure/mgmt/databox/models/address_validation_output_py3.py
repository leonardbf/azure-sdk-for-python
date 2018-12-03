# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AddressValidationOutput(Model):
    """Output of the address validation api.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar validation_status: The address validation status. Possible values
     include: 'Valid', 'Invalid', 'Ambiguous'
    :vartype validation_status: str or
     ~azure.mgmt.databox.models.AddressValidationStatus
    :ivar alternate_addresses: List of alternate addresses.
    :vartype alternate_addresses:
     list[~azure.mgmt.databox.models.ShippingAddress]
    """

    _validation = {
        'validation_status': {'readonly': True},
        'alternate_addresses': {'readonly': True},
    }

    _attribute_map = {
        'validation_status': {'key': 'properties.validationStatus', 'type': 'AddressValidationStatus'},
        'alternate_addresses': {'key': 'properties.alternateAddresses', 'type': '[ShippingAddress]'},
    }

    def __init__(self, **kwargs) -> None:
        super(AddressValidationOutput, self).__init__(**kwargs)
        self.validation_status = None
        self.alternate_addresses = None