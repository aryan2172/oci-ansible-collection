# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class ConnectivityValidationActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)


class DetachDataAssetInfoActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)


class AttachDataAssetInfoActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)


class DataPreviewActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)


class DataProfileActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)


class FullPushDownTaskActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)


class ConnectionValidationHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        """
        need this customisation because the codegen doesnt handle the GET apis that have query params
        """
        return oci_common_utils.call_with_backoff(
            self.client.get_connection_validation,
            registry_id=self.module.params.get("registry_id"),
            connection_validation_key=summary_model.key,
        ).data


class DataEntityActionsHelperCustom:
    """
    generated code has data_entity_key but we need to pass the key.
    """

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_entity,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            schema_resource_name=self.module.params.get("schema_resource_name"),
            data_entity_key=self.module.params.get("key"),
        )


class ReferenceInfoActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)


class TestNetworkConnectivityActionsHelperCustom:
    def get_resource(self):
        """
        Resource doesn't have get_resource method and perform_action calls get_resource.
        So, overriding get_resource to return default response.
        """
        return oci_common_utils.get_default_response_from_resource(resource=None)
