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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.backup_fabrics_operations import BackupFabricsOperations
from .operations.scoped_backup_policies_operations import ScopedBackupPoliciesOperations
from .operations.scoped_protection_policies_operations import ScopedProtectionPoliciesOperations
from .operations.scoped_protection_policy_operation_results_operations import ScopedProtectionPolicyOperationResultsOperations
from .operations.scoped_protection_policy_operation_statuses_operations import ScopedProtectionPolicyOperationStatusesOperations
from .operations.backup_protection_containers_in_fabric_operations import BackupProtectionContainersInFabricOperations
from .operations.backup_protected_items_in_container_operations import BackupProtectedItemsInContainerOperations
from .operations.protection_containers_operations import ProtectionContainersOperations
from .operations.protection_intent_operations import ProtectionIntentOperations
from .operations.backup_status_operations import BackupStatusOperations
from .operations.feature_support_operations import FeatureSupportOperations
from .operations.backup_jobs_operations import BackupJobsOperations
from .operations.job_details_operations import JobDetailsOperations
from .operations.export_jobs_operation_results_operations import ExportJobsOperationResultsOperations
from .operations.jobs_operations import JobsOperations
from .operations.backup_policies_operations import BackupPoliciesOperations
from .operations.backup_protected_items_operations import BackupProtectedItemsOperations
from .operations.backup_protection_intent_operations import BackupProtectionIntentOperations
from .operations.backup_usage_summaries_operations import BackupUsageSummariesOperations
from .operations.operation_operations import OperationOperations
from .operations.backup_resource_vault_configs_operations import BackupResourceVaultConfigsOperations
from .operations.backup_engines_operations import BackupEnginesOperations
from .operations.protection_container_refresh_operation_results_operations import ProtectionContainerRefreshOperationResultsOperations
from .operations.protectable_containers_operations import ProtectableContainersOperations
from .operations.backup_workload_items_operations import BackupWorkloadItemsOperations
from .operations.protection_container_operation_results_operations import ProtectionContainerOperationResultsOperations
from .operations.protected_items_operations import ProtectedItemsOperations
from .operations.backups_operations import BackupsOperations
from .operations.protected_item_operation_results_operations import ProtectedItemOperationResultsOperations
from .operations.protected_item_operation_statuses_operations import ProtectedItemOperationStatusesOperations
from .operations.recovery_points_operations import RecoveryPointsOperations
from .operations.item_level_recovery_connections_operations import ItemLevelRecoveryConnectionsOperations
from .operations.restores_operations import RestoresOperations
from .operations.job_cancellations_operations import JobCancellationsOperations
from .operations.job_operation_results_operations import JobOperationResultsOperations
from .operations.backup_operation_results_operations import BackupOperationResultsOperations
from .operations.backup_operation_statuses_operations import BackupOperationStatusesOperations
from .operations.protection_policies_operations import ProtectionPoliciesOperations
from .operations.protection_policy_operation_results_operations import ProtectionPolicyOperationResultsOperations
from .operations.protection_policy_operation_statuses_operations import ProtectionPolicyOperationStatusesOperations
from .operations.backup_protectable_items_operations import BackupProtectableItemsOperations
from .operations.backup_protection_containers_operations import BackupProtectionContainersOperations
from .operations.security_pi_ns_operations import SecurityPINsOperations
from .operations.backup_resource_storage_configs_operations import BackupResourceStorageConfigsOperations
from .operations.backup_resource_storage_config_operations import BackupResourceStorageConfigOperations
from .operations.operations import Operations
from . import models


class RecoveryServicesBackupClientConfiguration(AzureConfiguration):
    """Configuration for RecoveryServicesBackupClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(RecoveryServicesBackupClientConfiguration, self).__init__(base_url)

        self.add_user_agent('azure-mgmt-recoveryservicesbackup/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class RecoveryServicesBackupClient(SDKClient):
    """Open API 2.0 Specs for Azure RecoveryServices Backup service

    :ivar config: Configuration for client.
    :vartype config: RecoveryServicesBackupClientConfiguration

    :ivar backup_fabrics: BackupFabrics operations
    :vartype backup_fabrics: azure.mgmt.recoveryservicesbackup.operations.BackupFabricsOperations
    :ivar scoped_backup_policies: ScopedBackupPolicies operations
    :vartype scoped_backup_policies: azure.mgmt.recoveryservicesbackup.operations.ScopedBackupPoliciesOperations
    :ivar scoped_protection_policies: ScopedProtectionPolicies operations
    :vartype scoped_protection_policies: azure.mgmt.recoveryservicesbackup.operations.ScopedProtectionPoliciesOperations
    :ivar scoped_protection_policy_operation_results: ScopedProtectionPolicyOperationResults operations
    :vartype scoped_protection_policy_operation_results: azure.mgmt.recoveryservicesbackup.operations.ScopedProtectionPolicyOperationResultsOperations
    :ivar scoped_protection_policy_operation_statuses: ScopedProtectionPolicyOperationStatuses operations
    :vartype scoped_protection_policy_operation_statuses: azure.mgmt.recoveryservicesbackup.operations.ScopedProtectionPolicyOperationStatusesOperations
    :ivar backup_protection_containers_in_fabric: BackupProtectionContainersInFabric operations
    :vartype backup_protection_containers_in_fabric: azure.mgmt.recoveryservicesbackup.operations.BackupProtectionContainersInFabricOperations
    :ivar backup_protected_items_in_container: BackupProtectedItemsInContainer operations
    :vartype backup_protected_items_in_container: azure.mgmt.recoveryservicesbackup.operations.BackupProtectedItemsInContainerOperations
    :ivar protection_containers: ProtectionContainers operations
    :vartype protection_containers: azure.mgmt.recoveryservicesbackup.operations.ProtectionContainersOperations
    :ivar protection_intent: ProtectionIntent operations
    :vartype protection_intent: azure.mgmt.recoveryservicesbackup.operations.ProtectionIntentOperations
    :ivar backup_status: BackupStatus operations
    :vartype backup_status: azure.mgmt.recoveryservicesbackup.operations.BackupStatusOperations
    :ivar feature_support: FeatureSupport operations
    :vartype feature_support: azure.mgmt.recoveryservicesbackup.operations.FeatureSupportOperations
    :ivar backup_jobs: BackupJobs operations
    :vartype backup_jobs: azure.mgmt.recoveryservicesbackup.operations.BackupJobsOperations
    :ivar job_details: JobDetails operations
    :vartype job_details: azure.mgmt.recoveryservicesbackup.operations.JobDetailsOperations
    :ivar export_jobs_operation_results: ExportJobsOperationResults operations
    :vartype export_jobs_operation_results: azure.mgmt.recoveryservicesbackup.operations.ExportJobsOperationResultsOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.mgmt.recoveryservicesbackup.operations.JobsOperations
    :ivar backup_policies: BackupPolicies operations
    :vartype backup_policies: azure.mgmt.recoveryservicesbackup.operations.BackupPoliciesOperations
    :ivar backup_protected_items: BackupProtectedItems operations
    :vartype backup_protected_items: azure.mgmt.recoveryservicesbackup.operations.BackupProtectedItemsOperations
    :ivar backup_protection_intent: BackupProtectionIntent operations
    :vartype backup_protection_intent: azure.mgmt.recoveryservicesbackup.operations.BackupProtectionIntentOperations
    :ivar backup_usage_summaries: BackupUsageSummaries operations
    :vartype backup_usage_summaries: azure.mgmt.recoveryservicesbackup.operations.BackupUsageSummariesOperations
    :ivar operation: Operation operations
    :vartype operation: azure.mgmt.recoveryservicesbackup.operations.OperationOperations
    :ivar backup_resource_vault_configs: BackupResourceVaultConfigs operations
    :vartype backup_resource_vault_configs: azure.mgmt.recoveryservicesbackup.operations.BackupResourceVaultConfigsOperations
    :ivar backup_engines: BackupEngines operations
    :vartype backup_engines: azure.mgmt.recoveryservicesbackup.operations.BackupEnginesOperations
    :ivar protection_container_refresh_operation_results: ProtectionContainerRefreshOperationResults operations
    :vartype protection_container_refresh_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectionContainerRefreshOperationResultsOperations
    :ivar protectable_containers: ProtectableContainers operations
    :vartype protectable_containers: azure.mgmt.recoveryservicesbackup.operations.ProtectableContainersOperations
    :ivar backup_workload_items: BackupWorkloadItems operations
    :vartype backup_workload_items: azure.mgmt.recoveryservicesbackup.operations.BackupWorkloadItemsOperations
    :ivar protection_container_operation_results: ProtectionContainerOperationResults operations
    :vartype protection_container_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectionContainerOperationResultsOperations
    :ivar protected_items: ProtectedItems operations
    :vartype protected_items: azure.mgmt.recoveryservicesbackup.operations.ProtectedItemsOperations
    :ivar backups: Backups operations
    :vartype backups: azure.mgmt.recoveryservicesbackup.operations.BackupsOperations
    :ivar protected_item_operation_results: ProtectedItemOperationResults operations
    :vartype protected_item_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectedItemOperationResultsOperations
    :ivar protected_item_operation_statuses: ProtectedItemOperationStatuses operations
    :vartype protected_item_operation_statuses: azure.mgmt.recoveryservicesbackup.operations.ProtectedItemOperationStatusesOperations
    :ivar recovery_points: RecoveryPoints operations
    :vartype recovery_points: azure.mgmt.recoveryservicesbackup.operations.RecoveryPointsOperations
    :ivar item_level_recovery_connections: ItemLevelRecoveryConnections operations
    :vartype item_level_recovery_connections: azure.mgmt.recoveryservicesbackup.operations.ItemLevelRecoveryConnectionsOperations
    :ivar restores: Restores operations
    :vartype restores: azure.mgmt.recoveryservicesbackup.operations.RestoresOperations
    :ivar job_cancellations: JobCancellations operations
    :vartype job_cancellations: azure.mgmt.recoveryservicesbackup.operations.JobCancellationsOperations
    :ivar job_operation_results: JobOperationResults operations
    :vartype job_operation_results: azure.mgmt.recoveryservicesbackup.operations.JobOperationResultsOperations
    :ivar backup_operation_results: BackupOperationResults operations
    :vartype backup_operation_results: azure.mgmt.recoveryservicesbackup.operations.BackupOperationResultsOperations
    :ivar backup_operation_statuses: BackupOperationStatuses operations
    :vartype backup_operation_statuses: azure.mgmt.recoveryservicesbackup.operations.BackupOperationStatusesOperations
    :ivar protection_policies: ProtectionPolicies operations
    :vartype protection_policies: azure.mgmt.recoveryservicesbackup.operations.ProtectionPoliciesOperations
    :ivar protection_policy_operation_results: ProtectionPolicyOperationResults operations
    :vartype protection_policy_operation_results: azure.mgmt.recoveryservicesbackup.operations.ProtectionPolicyOperationResultsOperations
    :ivar protection_policy_operation_statuses: ProtectionPolicyOperationStatuses operations
    :vartype protection_policy_operation_statuses: azure.mgmt.recoveryservicesbackup.operations.ProtectionPolicyOperationStatusesOperations
    :ivar backup_protectable_items: BackupProtectableItems operations
    :vartype backup_protectable_items: azure.mgmt.recoveryservicesbackup.operations.BackupProtectableItemsOperations
    :ivar backup_protection_containers: BackupProtectionContainers operations
    :vartype backup_protection_containers: azure.mgmt.recoveryservicesbackup.operations.BackupProtectionContainersOperations
    :ivar security_pi_ns: SecurityPINs operations
    :vartype security_pi_ns: azure.mgmt.recoveryservicesbackup.operations.SecurityPINsOperations
    :ivar backup_resource_storage_configs: BackupResourceStorageConfigs operations
    :vartype backup_resource_storage_configs: azure.mgmt.recoveryservicesbackup.operations.BackupResourceStorageConfigsOperations
    :ivar backup_resource_storage_config: BackupResourceStorageConfig operations
    :vartype backup_resource_storage_config: azure.mgmt.recoveryservicesbackup.operations.BackupResourceStorageConfigOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.recoveryservicesbackup.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = RecoveryServicesBackupClientConfiguration(credentials, subscription_id, base_url)
        super(RecoveryServicesBackupClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.backup_fabrics = BackupFabricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scoped_backup_policies = ScopedBackupPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scoped_protection_policies = ScopedProtectionPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scoped_protection_policy_operation_results = ScopedProtectionPolicyOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.scoped_protection_policy_operation_statuses = ScopedProtectionPolicyOperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protection_containers_in_fabric = BackupProtectionContainersInFabricOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protected_items_in_container = BackupProtectedItemsInContainerOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_containers = ProtectionContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_intent = ProtectionIntentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_status = BackupStatusOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.feature_support = FeatureSupportOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_jobs = BackupJobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_details = JobDetailsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.export_jobs_operation_results = ExportJobsOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_policies = BackupPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protected_items = BackupProtectedItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protection_intent = BackupProtectionIntentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_usage_summaries = BackupUsageSummariesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operation = OperationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_resource_vault_configs = BackupResourceVaultConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_engines = BackupEnginesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_container_refresh_operation_results = ProtectionContainerRefreshOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protectable_containers = ProtectableContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_workload_items = BackupWorkloadItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_container_operation_results = ProtectionContainerOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protected_items = ProtectedItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backups = BackupsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protected_item_operation_results = ProtectedItemOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protected_item_operation_statuses = ProtectedItemOperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.recovery_points = RecoveryPointsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.item_level_recovery_connections = ItemLevelRecoveryConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.restores = RestoresOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_cancellations = JobCancellationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.job_operation_results = JobOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_operation_results = BackupOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_operation_statuses = BackupOperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_policies = ProtectionPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_policy_operation_results = ProtectionPolicyOperationResultsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.protection_policy_operation_statuses = ProtectionPolicyOperationStatusesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protectable_items = BackupProtectableItemsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_protection_containers = BackupProtectionContainersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.security_pi_ns = SecurityPINsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_resource_storage_configs = BackupResourceStorageConfigsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.backup_resource_storage_config = BackupResourceStorageConfigOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
