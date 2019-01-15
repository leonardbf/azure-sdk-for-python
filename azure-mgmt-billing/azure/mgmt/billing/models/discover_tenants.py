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


class DiscoverTenants(Model):
    """A Tenant properties Resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar billing_profile_name: The Billing Profile name.
    :vartype billing_profile_name: str
    :ivar billing_account_id: The Billing AccountId.
    :vartype billing_account_id: str
    :ivar tenant_id: The TenantId.
    :vartype tenant_id: str
    """

    _validation = {
        'billing_profile_name': {'readonly': True},
        'billing_account_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'billing_profile_name': {'key': 'billingProfileName', 'type': 'str'},
        'billing_account_id': {'key': 'billingAccountId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DiscoverTenants, self).__init__(**kwargs)
        self.billing_profile_name = None
        self.billing_account_id = None
        self.tenant_id = None