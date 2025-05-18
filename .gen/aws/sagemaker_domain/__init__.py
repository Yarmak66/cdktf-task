r'''
# `aws_sagemaker_domain`

Refer to the Terraform Registry for docs: [`aws_sagemaker_domain`](https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain).
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

import typeguard
from importlib.metadata import version as _metadata_package_version
TYPEGUARD_MAJOR_VERSION = int(_metadata_package_version('typeguard').split('.')[0])

def check_type(argname: str, value: object, expected_type: typing.Any) -> typing.Any:
    if TYPEGUARD_MAJOR_VERSION <= 2:
        return typeguard.check_type(argname=argname, value=value, expected_type=expected_type) # type:ignore
    else:
        if isinstance(value, jsii._reference_map.InterfaceDynamicProxy): # pyright: ignore [reportAttributeAccessIssue]
           pass
        else:
            if TYPEGUARD_MAJOR_VERSION == 3:
                typeguard.config.collection_check_strategy = typeguard.CollectionCheckStrategy.ALL_ITEMS # type:ignore
                typeguard.check_type(value=value, expected_type=expected_type) # type:ignore
            else:
                typeguard.check_type(value=value, expected_type=expected_type, collection_check_strategy=typeguard.CollectionCheckStrategy.ALL_ITEMS) # type:ignore

from .._jsii import *

import cdktf as _cdktf_9a9027ec
import constructs as _constructs_77d1e7e8


class SagemakerDomain(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomain",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain aws_sagemaker_domain}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        auth_mode: builtins.str,
        default_user_settings: typing.Union["SagemakerDomainDefaultUserSettings", typing.Dict[builtins.str, typing.Any]],
        domain_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_network_access_type: typing.Optional[builtins.str] = None,
        app_security_group_management: typing.Optional[builtins.str] = None,
        default_space_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        domain_settings: typing.Optional[typing.Union["SagemakerDomainDomainSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        retention_policy: typing.Optional[typing.Union["SagemakerDomainRetentionPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_propagation: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain aws_sagemaker_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param auth_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#auth_mode SagemakerDomain#auth_mode}.
        :param default_user_settings: default_user_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_user_settings SagemakerDomain#default_user_settings}
        :param domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_name SagemakerDomain#domain_name}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#subnet_ids SagemakerDomain#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#vpc_id SagemakerDomain#vpc_id}.
        :param app_network_access_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_network_access_type SagemakerDomain#app_network_access_type}.
        :param app_security_group_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_security_group_management SagemakerDomain#app_security_group_management}.
        :param default_space_settings: default_space_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_space_settings SagemakerDomain#default_space_settings}
        :param domain_settings: domain_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_settings SagemakerDomain#domain_settings}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#id SagemakerDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kms_key_id SagemakerDomain#kms_key_id}.
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#retention_policy SagemakerDomain#retention_policy}
        :param tag_propagation: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tag_propagation SagemakerDomain#tag_propagation}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tags SagemakerDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tags_all SagemakerDomain#tags_all}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__650f7b8434805310d757aaa0d233efacec64617bda5906df5766e3e4e3a6b7cb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SagemakerDomainConfig(
            auth_mode=auth_mode,
            default_user_settings=default_user_settings,
            domain_name=domain_name,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            app_network_access_type=app_network_access_type,
            app_security_group_management=app_security_group_management,
            default_space_settings=default_space_settings,
            domain_settings=domain_settings,
            id=id,
            kms_key_id=kms_key_id,
            retention_policy=retention_policy,
            tag_propagation=tag_propagation,
            tags=tags,
            tags_all=tags_all,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="generateConfigForImport")
    @builtins.classmethod
    def generate_config_for_import(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        import_to_id: builtins.str,
        import_from_id: builtins.str,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    ) -> _cdktf_9a9027ec.ImportableResource:
        '''Generates CDKTF code for importing a SagemakerDomain resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the SagemakerDomain to import.
        :param import_from_id: The id of the existing SagemakerDomain that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the SagemakerDomain to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cbc910ae71c114601d9d1c7569efab3b2f2c0de56fa601fdf158184c6d66f1c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putDefaultSpaceSettings")
    def put_default_space_settings(
        self,
        *,
        execution_role: builtins.str,
        custom_file_system_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_posix_user_config: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_lab_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        space_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role SagemakerDomain#execution_role}.
        :param custom_file_system_config: custom_file_system_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_file_system_config SagemakerDomain#custom_file_system_config}
        :param custom_posix_user_config: custom_posix_user_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_posix_user_config SagemakerDomain#custom_posix_user_config}
        :param jupyter_lab_app_settings: jupyter_lab_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_lab_app_settings SagemakerDomain#jupyter_lab_app_settings}
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_groups SagemakerDomain#security_groups}.
        :param space_storage_settings: space_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#space_storage_settings SagemakerDomain#space_storage_settings}
        '''
        value = SagemakerDomainDefaultSpaceSettings(
            execution_role=execution_role,
            custom_file_system_config=custom_file_system_config,
            custom_posix_user_config=custom_posix_user_config,
            jupyter_lab_app_settings=jupyter_lab_app_settings,
            jupyter_server_app_settings=jupyter_server_app_settings,
            kernel_gateway_app_settings=kernel_gateway_app_settings,
            security_groups=security_groups,
            space_storage_settings=space_storage_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultSpaceSettings", [value]))

    @jsii.member(jsii_name="putDefaultUserSettings")
    def put_default_user_settings(
        self,
        *,
        execution_role: builtins.str,
        auto_mount_home_efs: typing.Optional[builtins.str] = None,
        canvas_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        code_editor_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCodeEditorAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_file_system_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsCustomFileSystemConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_posix_user_config: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCustomPosixUserConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        default_landing_uri: typing.Optional[builtins.str] = None,
        jupyter_lab_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        r_session_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsRSessionAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        r_studio_server_pro_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        sharing_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSharingSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        space_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSpaceStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        studio_web_portal: typing.Optional[builtins.str] = None,
        studio_web_portal_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsStudioWebPortalSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        tensor_board_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role SagemakerDomain#execution_role}.
        :param auto_mount_home_efs: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#auto_mount_home_efs SagemakerDomain#auto_mount_home_efs}.
        :param canvas_app_settings: canvas_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#canvas_app_settings SagemakerDomain#canvas_app_settings}
        :param code_editor_app_settings: code_editor_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_editor_app_settings SagemakerDomain#code_editor_app_settings}
        :param custom_file_system_config: custom_file_system_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_file_system_config SagemakerDomain#custom_file_system_config}
        :param custom_posix_user_config: custom_posix_user_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_posix_user_config SagemakerDomain#custom_posix_user_config}
        :param default_landing_uri: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_landing_uri SagemakerDomain#default_landing_uri}.
        :param jupyter_lab_app_settings: jupyter_lab_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_lab_app_settings SagemakerDomain#jupyter_lab_app_settings}
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        :param r_session_app_settings: r_session_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_session_app_settings SagemakerDomain#r_session_app_settings}
        :param r_studio_server_pro_app_settings: r_studio_server_pro_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_server_pro_app_settings SagemakerDomain#r_studio_server_pro_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_groups SagemakerDomain#security_groups}.
        :param sharing_settings: sharing_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sharing_settings SagemakerDomain#sharing_settings}
        :param space_storage_settings: space_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#space_storage_settings SagemakerDomain#space_storage_settings}
        :param studio_web_portal: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#studio_web_portal SagemakerDomain#studio_web_portal}.
        :param studio_web_portal_settings: studio_web_portal_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#studio_web_portal_settings SagemakerDomain#studio_web_portal_settings}
        :param tensor_board_app_settings: tensor_board_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tensor_board_app_settings SagemakerDomain#tensor_board_app_settings}
        '''
        value = SagemakerDomainDefaultUserSettings(
            execution_role=execution_role,
            auto_mount_home_efs=auto_mount_home_efs,
            canvas_app_settings=canvas_app_settings,
            code_editor_app_settings=code_editor_app_settings,
            custom_file_system_config=custom_file_system_config,
            custom_posix_user_config=custom_posix_user_config,
            default_landing_uri=default_landing_uri,
            jupyter_lab_app_settings=jupyter_lab_app_settings,
            jupyter_server_app_settings=jupyter_server_app_settings,
            kernel_gateway_app_settings=kernel_gateway_app_settings,
            r_session_app_settings=r_session_app_settings,
            r_studio_server_pro_app_settings=r_studio_server_pro_app_settings,
            security_groups=security_groups,
            sharing_settings=sharing_settings,
            space_storage_settings=space_storage_settings,
            studio_web_portal=studio_web_portal,
            studio_web_portal_settings=studio_web_portal_settings,
            tensor_board_app_settings=tensor_board_app_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultUserSettings", [value]))

    @jsii.member(jsii_name="putDomainSettings")
    def put_domain_settings(
        self,
        *,
        docker_settings: typing.Optional[typing.Union["SagemakerDomainDomainSettingsDockerSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        execution_role_identity_config: typing.Optional[builtins.str] = None,
        r_studio_server_pro_domain_settings: typing.Optional[typing.Union["SagemakerDomainDomainSettingsRStudioServerProDomainSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param docker_settings: docker_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#docker_settings SagemakerDomain#docker_settings}
        :param execution_role_identity_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_identity_config SagemakerDomain#execution_role_identity_config}.
        :param r_studio_server_pro_domain_settings: r_studio_server_pro_domain_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_server_pro_domain_settings SagemakerDomain#r_studio_server_pro_domain_settings}
        :param security_group_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_group_ids SagemakerDomain#security_group_ids}.
        '''
        value = SagemakerDomainDomainSettings(
            docker_settings=docker_settings,
            execution_role_identity_config=execution_role_identity_config,
            r_studio_server_pro_domain_settings=r_studio_server_pro_domain_settings,
            security_group_ids=security_group_ids,
        )

        return typing.cast(None, jsii.invoke(self, "putDomainSettings", [value]))

    @jsii.member(jsii_name="putRetentionPolicy")
    def put_retention_policy(
        self,
        *,
        home_efs_file_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param home_efs_file_system: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#home_efs_file_system SagemakerDomain#home_efs_file_system}.
        '''
        value = SagemakerDomainRetentionPolicy(
            home_efs_file_system=home_efs_file_system
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionPolicy", [value]))

    @jsii.member(jsii_name="resetAppNetworkAccessType")
    def reset_app_network_access_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppNetworkAccessType", []))

    @jsii.member(jsii_name="resetAppSecurityGroupManagement")
    def reset_app_security_group_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppSecurityGroupManagement", []))

    @jsii.member(jsii_name="resetDefaultSpaceSettings")
    def reset_default_space_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultSpaceSettings", []))

    @jsii.member(jsii_name="resetDomainSettings")
    def reset_domain_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomainSettings", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsKeyId")
    def reset_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsKeyId", []))

    @jsii.member(jsii_name="resetRetentionPolicy")
    def reset_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicy", []))

    @jsii.member(jsii_name="resetTagPropagation")
    def reset_tag_propagation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagPropagation", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTagsAll")
    def reset_tags_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagsAll", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.member(jsii_name="synthesizeHclAttributes")
    def _synthesize_hcl_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeHclAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="arn")
    def arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "arn"))

    @builtins.property
    @jsii.member(jsii_name="defaultSpaceSettings")
    def default_space_settings(
        self,
    ) -> "SagemakerDomainDefaultSpaceSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultSpaceSettingsOutputReference", jsii.get(self, "defaultSpaceSettings"))

    @builtins.property
    @jsii.member(jsii_name="defaultUserSettings")
    def default_user_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsOutputReference", jsii.get(self, "defaultUserSettings"))

    @builtins.property
    @jsii.member(jsii_name="domainSettings")
    def domain_settings(self) -> "SagemakerDomainDomainSettingsOutputReference":
        return typing.cast("SagemakerDomainDomainSettingsOutputReference", jsii.get(self, "domainSettings"))

    @builtins.property
    @jsii.member(jsii_name="homeEfsFileSystemId")
    def home_efs_file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeEfsFileSystemId"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(self) -> "SagemakerDomainRetentionPolicyOutputReference":
        return typing.cast("SagemakerDomainRetentionPolicyOutputReference", jsii.get(self, "retentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdForDomainBoundary")
    def security_group_id_for_domain_boundary(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityGroupIdForDomainBoundary"))

    @builtins.property
    @jsii.member(jsii_name="singleSignOnApplicationArn")
    def single_sign_on_application_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleSignOnApplicationArn"))

    @builtins.property
    @jsii.member(jsii_name="singleSignOnManagedApplicationInstanceId")
    def single_sign_on_managed_application_instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "singleSignOnManagedApplicationInstanceId"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="appNetworkAccessTypeInput")
    def app_network_access_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appNetworkAccessTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="appSecurityGroupManagementInput")
    def app_security_group_management_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appSecurityGroupManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="authModeInput")
    def auth_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authModeInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultSpaceSettingsInput")
    def default_space_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettings"], jsii.get(self, "defaultSpaceSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultUserSettingsInput")
    def default_user_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettings"], jsii.get(self, "defaultUserSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="domainSettingsInput")
    def domain_settings_input(self) -> typing.Optional["SagemakerDomainDomainSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDomainSettings"], jsii.get(self, "domainSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyIdInput")
    def kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyInput")
    def retention_policy_input(
        self,
    ) -> typing.Optional["SagemakerDomainRetentionPolicy"]:
        return typing.cast(typing.Optional["SagemakerDomainRetentionPolicy"], jsii.get(self, "retentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdsInput")
    def subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagPropagationInput")
    def tag_propagation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagPropagationInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsAllInput")
    def tags_all_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsAllInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcIdInput")
    def vpc_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIdInput"))

    @builtins.property
    @jsii.member(jsii_name="appNetworkAccessType")
    def app_network_access_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appNetworkAccessType"))

    @app_network_access_type.setter
    def app_network_access_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da86f98b35012a6438bc87e6edcbf9ef948efe8749ca8e1bb95332e367e5de6d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appNetworkAccessType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="appSecurityGroupManagement")
    def app_security_group_management(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appSecurityGroupManagement"))

    @app_security_group_management.setter
    def app_security_group_management(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e81288f06b5774dda2f36d07735792a84409d8f852a3f827da5151f53f19e47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appSecurityGroupManagement", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="authMode")
    def auth_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMode"))

    @auth_mode.setter
    def auth_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efc3541c2d8406aebd8d743b93716cb5e9e8ae1cbfe9591d36570393074cd829)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authMode", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6192a792e9e6502b90adad646ddb07e164c2229b99b9f32c157bd378205c4d9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ebfc81a49c9174dd1add3ebe9f51484209c027ef20d548fd3a10d52045b3f7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8bdc0da6f7f47013770cb4d1d39626195d3d96f0559972fddd3c52300de9b40)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__733c3c6a865d488b9ad38a638497555cb18dbfb01b8e72bc1a7a38d6aaf55fde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagPropagation")
    def tag_propagation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagPropagation"))

    @tag_propagation.setter
    def tag_propagation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d1391862b19d51601a44b6fd1e98f6dd398ad61c5b5d7657e3c172cf49b0ee7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagPropagation", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63ba84d2072211247bd8c7cabc1c60c84c9637c08c86ef38cbdb57f19f07b8ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tagsAll")
    def tags_all(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tagsAll"))

    @tags_all.setter
    def tags_all(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0424b7faa03fd3a1ef81a34474d4ad5ee3200e5faf2efb7f1da1b7eb923a7202)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsAll", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9128e511f49b5ed158e2dd3840f9205838af10e7a523f9fde45fbc1124c98f02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "auth_mode": "authMode",
        "default_user_settings": "defaultUserSettings",
        "domain_name": "domainName",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "app_network_access_type": "appNetworkAccessType",
        "app_security_group_management": "appSecurityGroupManagement",
        "default_space_settings": "defaultSpaceSettings",
        "domain_settings": "domainSettings",
        "id": "id",
        "kms_key_id": "kmsKeyId",
        "retention_policy": "retentionPolicy",
        "tag_propagation": "tagPropagation",
        "tags": "tags",
        "tags_all": "tagsAll",
    },
)
class SagemakerDomainConfig(_cdktf_9a9027ec.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
        auth_mode: builtins.str,
        default_user_settings: typing.Union["SagemakerDomainDefaultUserSettings", typing.Dict[builtins.str, typing.Any]],
        domain_name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        app_network_access_type: typing.Optional[builtins.str] = None,
        app_security_group_management: typing.Optional[builtins.str] = None,
        default_space_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        domain_settings: typing.Optional[typing.Union["SagemakerDomainDomainSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        retention_policy: typing.Optional[typing.Union["SagemakerDomainRetentionPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        tag_propagation: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param auth_mode: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#auth_mode SagemakerDomain#auth_mode}.
        :param default_user_settings: default_user_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_user_settings SagemakerDomain#default_user_settings}
        :param domain_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_name SagemakerDomain#domain_name}.
        :param subnet_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#subnet_ids SagemakerDomain#subnet_ids}.
        :param vpc_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#vpc_id SagemakerDomain#vpc_id}.
        :param app_network_access_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_network_access_type SagemakerDomain#app_network_access_type}.
        :param app_security_group_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_security_group_management SagemakerDomain#app_security_group_management}.
        :param default_space_settings: default_space_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_space_settings SagemakerDomain#default_space_settings}
        :param domain_settings: domain_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_settings SagemakerDomain#domain_settings}
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#id SagemakerDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kms_key_id SagemakerDomain#kms_key_id}.
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#retention_policy SagemakerDomain#retention_policy}
        :param tag_propagation: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tag_propagation SagemakerDomain#tag_propagation}.
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tags SagemakerDomain#tags}.
        :param tags_all: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tags_all SagemakerDomain#tags_all}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(default_user_settings, dict):
            default_user_settings = SagemakerDomainDefaultUserSettings(**default_user_settings)
        if isinstance(default_space_settings, dict):
            default_space_settings = SagemakerDomainDefaultSpaceSettings(**default_space_settings)
        if isinstance(domain_settings, dict):
            domain_settings = SagemakerDomainDomainSettings(**domain_settings)
        if isinstance(retention_policy, dict):
            retention_policy = SagemakerDomainRetentionPolicy(**retention_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ac367461aed0b3ecc30172747fccc340b4ee32e6a4d1fbe360c36a7b659b7a2)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument auth_mode", value=auth_mode, expected_type=type_hints["auth_mode"])
            check_type(argname="argument default_user_settings", value=default_user_settings, expected_type=type_hints["default_user_settings"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument app_network_access_type", value=app_network_access_type, expected_type=type_hints["app_network_access_type"])
            check_type(argname="argument app_security_group_management", value=app_security_group_management, expected_type=type_hints["app_security_group_management"])
            check_type(argname="argument default_space_settings", value=default_space_settings, expected_type=type_hints["default_space_settings"])
            check_type(argname="argument domain_settings", value=domain_settings, expected_type=type_hints["domain_settings"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
            check_type(argname="argument tag_propagation", value=tag_propagation, expected_type=type_hints["tag_propagation"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tags_all", value=tags_all, expected_type=type_hints["tags_all"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "auth_mode": auth_mode,
            "default_user_settings": default_user_settings,
            "domain_name": domain_name,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if app_network_access_type is not None:
            self._values["app_network_access_type"] = app_network_access_type
        if app_security_group_management is not None:
            self._values["app_security_group_management"] = app_security_group_management
        if default_space_settings is not None:
            self._values["default_space_settings"] = default_space_settings
        if domain_settings is not None:
            self._values["domain_settings"] = domain_settings
        if id is not None:
            self._values["id"] = id
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy
        if tag_propagation is not None:
            self._values["tag_propagation"] = tag_propagation
        if tags is not None:
            self._values["tags"] = tags
        if tags_all is not None:
            self._values["tags_all"] = tags_all

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, _cdktf_9a9027ec.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(
        self,
    ) -> typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]], result)

    @builtins.property
    def depends_on(
        self,
    ) -> typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[_cdktf_9a9027ec.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[_cdktf_9a9027ec.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[_cdktf_9a9027ec.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[_cdktf_9a9027ec.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[_cdktf_9a9027ec.FileProvisioner, _cdktf_9a9027ec.LocalExecProvisioner, _cdktf_9a9027ec.RemoteExecProvisioner]]], result)

    @builtins.property
    def auth_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#auth_mode SagemakerDomain#auth_mode}.'''
        result = self._values.get("auth_mode")
        assert result is not None, "Required property 'auth_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_user_settings(self) -> "SagemakerDomainDefaultUserSettings":
        '''default_user_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_user_settings SagemakerDomain#default_user_settings}
        '''
        result = self._values.get("default_user_settings")
        assert result is not None, "Required property 'default_user_settings' is missing"
        return typing.cast("SagemakerDomainDefaultUserSettings", result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_name SagemakerDomain#domain_name}.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#subnet_ids SagemakerDomain#subnet_ids}.'''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#vpc_id SagemakerDomain#vpc_id}.'''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def app_network_access_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_network_access_type SagemakerDomain#app_network_access_type}.'''
        result = self._values.get("app_network_access_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def app_security_group_management(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_security_group_management SagemakerDomain#app_security_group_management}.'''
        result = self._values.get("app_security_group_management")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_space_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettings"]:
        '''default_space_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_space_settings SagemakerDomain#default_space_settings}
        '''
        result = self._values.get("default_space_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettings"], result)

    @builtins.property
    def domain_settings(self) -> typing.Optional["SagemakerDomainDomainSettings"]:
        '''domain_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_settings SagemakerDomain#domain_settings}
        '''
        result = self._values.get("domain_settings")
        return typing.cast(typing.Optional["SagemakerDomainDomainSettings"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#id SagemakerDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kms_key_id SagemakerDomain#kms_key_id}.'''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_policy(self) -> typing.Optional["SagemakerDomainRetentionPolicy"]:
        '''retention_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#retention_policy SagemakerDomain#retention_policy}
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional["SagemakerDomainRetentionPolicy"], result)

    @builtins.property
    def tag_propagation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tag_propagation SagemakerDomain#tag_propagation}.'''
        result = self._values.get("tag_propagation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tags SagemakerDomain#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tags_all(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tags_all SagemakerDomain#tags_all}.'''
        result = self._values.get("tags_all")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettings",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role": "executionRole",
        "custom_file_system_config": "customFileSystemConfig",
        "custom_posix_user_config": "customPosixUserConfig",
        "jupyter_lab_app_settings": "jupyterLabAppSettings",
        "jupyter_server_app_settings": "jupyterServerAppSettings",
        "kernel_gateway_app_settings": "kernelGatewayAppSettings",
        "security_groups": "securityGroups",
        "space_storage_settings": "spaceStorageSettings",
    },
)
class SagemakerDomainDefaultSpaceSettings:
    def __init__(
        self,
        *,
        execution_role: builtins.str,
        custom_file_system_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_posix_user_config: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_lab_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        space_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role SagemakerDomain#execution_role}.
        :param custom_file_system_config: custom_file_system_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_file_system_config SagemakerDomain#custom_file_system_config}
        :param custom_posix_user_config: custom_posix_user_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_posix_user_config SagemakerDomain#custom_posix_user_config}
        :param jupyter_lab_app_settings: jupyter_lab_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_lab_app_settings SagemakerDomain#jupyter_lab_app_settings}
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_groups SagemakerDomain#security_groups}.
        :param space_storage_settings: space_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#space_storage_settings SagemakerDomain#space_storage_settings}
        '''
        if isinstance(custom_posix_user_config, dict):
            custom_posix_user_config = SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig(**custom_posix_user_config)
        if isinstance(jupyter_lab_app_settings, dict):
            jupyter_lab_app_settings = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings(**jupyter_lab_app_settings)
        if isinstance(jupyter_server_app_settings, dict):
            jupyter_server_app_settings = SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings(**jupyter_server_app_settings)
        if isinstance(kernel_gateway_app_settings, dict):
            kernel_gateway_app_settings = SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings(**kernel_gateway_app_settings)
        if isinstance(space_storage_settings, dict):
            space_storage_settings = SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings(**space_storage_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d74e00c91ab3c174f7621417bde6ca95e8f43b9dc078d8e45b7695a26e5dd90b)
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument custom_file_system_config", value=custom_file_system_config, expected_type=type_hints["custom_file_system_config"])
            check_type(argname="argument custom_posix_user_config", value=custom_posix_user_config, expected_type=type_hints["custom_posix_user_config"])
            check_type(argname="argument jupyter_lab_app_settings", value=jupyter_lab_app_settings, expected_type=type_hints["jupyter_lab_app_settings"])
            check_type(argname="argument jupyter_server_app_settings", value=jupyter_server_app_settings, expected_type=type_hints["jupyter_server_app_settings"])
            check_type(argname="argument kernel_gateway_app_settings", value=kernel_gateway_app_settings, expected_type=type_hints["kernel_gateway_app_settings"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument space_storage_settings", value=space_storage_settings, expected_type=type_hints["space_storage_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_role": execution_role,
        }
        if custom_file_system_config is not None:
            self._values["custom_file_system_config"] = custom_file_system_config
        if custom_posix_user_config is not None:
            self._values["custom_posix_user_config"] = custom_posix_user_config
        if jupyter_lab_app_settings is not None:
            self._values["jupyter_lab_app_settings"] = jupyter_lab_app_settings
        if jupyter_server_app_settings is not None:
            self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
        if kernel_gateway_app_settings is not None:
            self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if space_storage_settings is not None:
            self._values["space_storage_settings"] = space_storage_settings

    @builtins.property
    def execution_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role SagemakerDomain#execution_role}.'''
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_file_system_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig"]]]:
        '''custom_file_system_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_file_system_config SagemakerDomain#custom_file_system_config}
        '''
        result = self._values.get("custom_file_system_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig"]]], result)

    @builtins.property
    def custom_posix_user_config(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig"]:
        '''custom_posix_user_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_posix_user_config SagemakerDomain#custom_posix_user_config}
        '''
        result = self._values.get("custom_posix_user_config")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig"], result)

    @builtins.property
    def jupyter_lab_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings"]:
        '''jupyter_lab_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_lab_app_settings SagemakerDomain#jupyter_lab_app_settings}
        '''
        result = self._values.get("jupyter_lab_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings"], result)

    @builtins.property
    def jupyter_server_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings"]:
        '''jupyter_server_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        '''
        result = self._values.get("jupyter_server_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings"], result)

    @builtins.property
    def kernel_gateway_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings"]:
        '''kernel_gateway_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        '''
        result = self._values.get("kernel_gateway_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings"], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_groups SagemakerDomain#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def space_storage_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings"]:
        '''space_storage_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#space_storage_settings SagemakerDomain#space_storage_settings}
        '''
        result = self._values.get("space_storage_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig",
    jsii_struct_bases=[],
    name_mapping={"efs_file_system_config": "efsFileSystemConfig"},
)
class SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig:
    def __init__(
        self,
        *,
        efs_file_system_config: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_system_config: efs_file_system_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#efs_file_system_config SagemakerDomain#efs_file_system_config}
        '''
        if isinstance(efs_file_system_config, dict):
            efs_file_system_config = SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig(**efs_file_system_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9583a8ad8ef11574079c180ed61f9aeadbaa09794c12d05535d900e45fefe90e)
            check_type(argname="argument efs_file_system_config", value=efs_file_system_config, expected_type=type_hints["efs_file_system_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if efs_file_system_config is not None:
            self._values["efs_file_system_config"] = efs_file_system_config

    @builtins.property
    def efs_file_system_config(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig"]:
        '''efs_file_system_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#efs_file_system_config SagemakerDomain#efs_file_system_config}
        '''
        result = self._values.get("efs_file_system_config")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "file_system_path": "fileSystemPath",
    },
)
class SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        file_system_path: builtins.str,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_id SagemakerDomain#file_system_id}.
        :param file_system_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_path SagemakerDomain#file_system_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3928de76a1d29034baf9be5cf0a4760021e5762239fee4d687ddad6fbb9558)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument file_system_path", value=file_system_path, expected_type=type_hints["file_system_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
            "file_system_path": file_system_path,
        }

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_id SagemakerDomain#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_system_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_path SagemakerDomain#file_system_path}.'''
        result = self._values.get("file_system_path")
        assert result is not None, "Required property 'file_system_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fff1045f9215d09f90a5d7644d83f84e6cdd13df949704772e7666ca269a647e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemPathInput")
    def file_system_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemPathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66809853d1240f6bf6aa20df0a4d5418073fa2849c47cd2d658e2fd7cc566cf5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileSystemPath")
    def file_system_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemPath"))

    @file_system_path.setter
    def file_system_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f6ccf3227918a8b9e66d3d938d1baee1b3feeee075b557df9b4351289116171)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee208fbacb75c8b41702f810cb469798c4842ba14d8bcfad97a830dafee3174e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a457e7a6875ef874797e895608206d8d30ee192993f777e878b09978dae6639)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2a2e3f84d08b125013232a04dc217d34e4e0111f3f7f7e0ac39fb20bca6f621)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__135469d197234761a7aec39b668567be77adb3b8e816d430958642ba75a4895e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a257d675195faf2790e2d316adbd312043476d2c7f284d2d9b4e356748f6b4b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f9d993162834ae200cc1b6cb7cb5ea0aaef22c9b464d7a2445e6228acf6a8a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56e37db9ae7e24db5f741032313743fe38c8464d6ad3b8ffbd906d140dd8892e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b09a0ea4ed060a09bfbb38f795d22df2f1c55cd6ac1a6a32eaabbf8f4af80eb2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEfsFileSystemConfig")
    def put_efs_file_system_config(
        self,
        *,
        file_system_id: builtins.str,
        file_system_path: builtins.str,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_id SagemakerDomain#file_system_id}.
        :param file_system_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_path SagemakerDomain#file_system_path}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig(
            file_system_id=file_system_id, file_system_path=file_system_path
        )

        return typing.cast(None, jsii.invoke(self, "putEfsFileSystemConfig", [value]))

    @jsii.member(jsii_name="resetEfsFileSystemConfig")
    def reset_efs_file_system_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsFileSystemConfig", []))

    @builtins.property
    @jsii.member(jsii_name="efsFileSystemConfig")
    def efs_file_system_config(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference, jsii.get(self, "efsFileSystemConfig"))

    @builtins.property
    @jsii.member(jsii_name="efsFileSystemConfigInput")
    def efs_file_system_config_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig], jsii.get(self, "efsFileSystemConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8c3394136dc5f06c3ac310c54c942285d2e1d2f89a33cb3c79bb3a6dd92318e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig",
    jsii_struct_bases=[],
    name_mapping={"gid": "gid", "uid": "uid"},
)
class SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig:
    def __init__(self, *, gid: jsii.Number, uid: jsii.Number) -> None:
        '''
        :param gid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#gid SagemakerDomain#gid}.
        :param uid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#uid SagemakerDomain#uid}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__538cdb15884da460b5fad0da25ece03f898d6d419173e685193ecdeb82fe16c0)
            check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gid": gid,
            "uid": uid,
        }

    @builtins.property
    def gid(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#gid SagemakerDomain#gid}.'''
        result = self._values.get("gid")
        assert result is not None, "Required property 'gid' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def uid(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#uid SagemakerDomain#uid}.'''
        result = self._values.get("uid")
        assert result is not None, "Required property 'uid' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6138000690bf20e7ef60334eada24b5ba7ec528c0ef5488dcebea4fa03a9df7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="gidInput")
    def gid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gidInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="gid")
    def gid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gid"))

    @gid.setter
    def gid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e61c4f89596fb4270a5d3964e0af151da90cb3afb684d4a1ec3df7ab4b81c24b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__204ffa67f1a553fc10301e1dc2d0a11c79c76e98add0e005499f743a7a36793f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2f6e0472cc8689a7d1a221d07f16d4fe1b9a103bb9f53cc68b88981f9c71371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "app_lifecycle_management": "appLifecycleManagement",
        "built_in_lifecycle_config_arn": "builtInLifecycleConfigArn",
        "code_repository": "codeRepository",
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
        "emr_settings": "emrSettings",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings:
    def __init__(
        self,
        *,
        app_lifecycle_management: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement", typing.Dict[builtins.str, typing.Any]]] = None,
        built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        emr_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_lifecycle_management: app_lifecycle_management block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        :param built_in_lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param emr_settings: emr_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_settings SagemakerDomain#emr_settings}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(app_lifecycle_management, dict):
            app_lifecycle_management = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement(**app_lifecycle_management)
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec(**default_resource_spec)
        if isinstance(emr_settings, dict):
            emr_settings = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings(**emr_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__995ec60bbbe3bd48bcffd04f83dcb6883574cc06011e2fe9fbfb4ed4ea39378f)
            check_type(argname="argument app_lifecycle_management", value=app_lifecycle_management, expected_type=type_hints["app_lifecycle_management"])
            check_type(argname="argument built_in_lifecycle_config_arn", value=built_in_lifecycle_config_arn, expected_type=type_hints["built_in_lifecycle_config_arn"])
            check_type(argname="argument code_repository", value=code_repository, expected_type=type_hints["code_repository"])
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument emr_settings", value=emr_settings, expected_type=type_hints["emr_settings"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if app_lifecycle_management is not None:
            self._values["app_lifecycle_management"] = app_lifecycle_management
        if built_in_lifecycle_config_arn is not None:
            self._values["built_in_lifecycle_config_arn"] = built_in_lifecycle_config_arn
        if code_repository is not None:
            self._values["code_repository"] = code_repository
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if emr_settings is not None:
            self._values["emr_settings"] = emr_settings
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def app_lifecycle_management(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement"]:
        '''app_lifecycle_management block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        '''
        result = self._values.get("app_lifecycle_management")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement"], result)

    @builtins.property
    def built_in_lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.'''
        result = self._values.get("built_in_lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_repository(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository"]]]:
        '''code_repository block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        '''
        result = self._values.get("code_repository")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository"]]], result)

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def emr_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings"]:
        '''emr_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_settings SagemakerDomain#emr_settings}
        '''
        result = self._values.get("emr_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement",
    jsii_struct_bases=[],
    name_mapping={"idle_settings": "idleSettings"},
)
class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement:
    def __init__(
        self,
        *,
        idle_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_settings: idle_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        if isinstance(idle_settings, dict):
            idle_settings = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(**idle_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__580f11d0210e6bc1aaaa37c57a097504299853dd4470c6fc19f38c2f5d953358)
            check_type(argname="argument idle_settings", value=idle_settings, expected_type=type_hints["idle_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_settings is not None:
            self._values["idle_settings"] = idle_settings

    @builtins.property
    def idle_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings"]:
        '''idle_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        result = self._values.get("idle_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings",
    jsii_struct_bases=[],
    name_mapping={
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "lifecycle_management": "lifecycleManagement",
        "max_idle_timeout_in_minutes": "maxIdleTimeoutInMinutes",
        "min_idle_timeout_in_minutes": "minIdleTimeoutInMinutes",
    },
)
class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings:
    def __init__(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        lifecycle_management: typing.Optional[builtins.str] = None,
        max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.
        :param lifecycle_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.
        :param max_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.
        :param min_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7afb3319df1de19eb793ffd9d7edf02f031cd7f6d5ea9cb270dede9cd025ec47)
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
            check_type(argname="argument lifecycle_management", value=lifecycle_management, expected_type=type_hints["lifecycle_management"])
            check_type(argname="argument max_idle_timeout_in_minutes", value=max_idle_timeout_in_minutes, expected_type=type_hints["max_idle_timeout_in_minutes"])
            check_type(argname="argument min_idle_timeout_in_minutes", value=min_idle_timeout_in_minutes, expected_type=type_hints["min_idle_timeout_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        if lifecycle_management is not None:
            self._values["lifecycle_management"] = lifecycle_management
        if max_idle_timeout_in_minutes is not None:
            self._values["max_idle_timeout_in_minutes"] = max_idle_timeout_in_minutes
        if min_idle_timeout_in_minutes is not None:
            self._values["min_idle_timeout_in_minutes"] = min_idle_timeout_in_minutes

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lifecycle_management(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.'''
        result = self._values.get("lifecycle_management")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.'''
        result = self._values.get("max_idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.'''
        result = self._values.get("min_idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b403f368a8abb768f32efe9e1e0592eed145df7326aad4539896506dc17b2aa8)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetLifecycleManagement")
    def reset_lifecycle_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleManagement", []))

    @jsii.member(jsii_name="resetMaxIdleTimeoutInMinutes")
    def reset_max_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetMinIdleTimeoutInMinutes")
    def reset_min_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinIdleTimeoutInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutesInput")
    def idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleManagementInput")
    def lifecycle_management_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleTimeoutInMinutesInput")
    def max_idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="minIdleTimeoutInMinutesInput")
    def min_idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minIdleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b33d4d9581bb6a3ca3dce3aa32933569a705e9fadf2f442a52f7785640782485)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleManagement")
    def lifecycle_management(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleManagement"))

    @lifecycle_management.setter
    def lifecycle_management(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30367fd982a4bd3e9c4b6d36ef7274368964ce3816d7ea57102b11b545d035b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleManagement", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleTimeoutInMinutes"))

    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c5471495db964be3932fb1b232c260c61b8a99c6291f80b606d5fb6bfb9300)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minIdleTimeoutInMinutes"))

    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8daba92f978d6422f54c1b5bce7eb504cefa5d77586922908a31533da9b6ad1d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minIdleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__654c4be39b0e9ec2ca918e9b7cf8ee05ea59af7663bad7481ca002c7ab8c080e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e6551da586deedd11010edaea3e5c593ded2c1668e4abf83b08fe7aedc6e0b6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdleSettings")
    def put_idle_settings(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        lifecycle_management: typing.Optional[builtins.str] = None,
        max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.
        :param lifecycle_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.
        :param max_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.
        :param min_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(
            idle_timeout_in_minutes=idle_timeout_in_minutes,
            lifecycle_management=lifecycle_management,
            max_idle_timeout_in_minutes=max_idle_timeout_in_minutes,
            min_idle_timeout_in_minutes=min_idle_timeout_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putIdleSettings", [value]))

    @jsii.member(jsii_name="resetIdleSettings")
    def reset_idle_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleSettings", []))

    @builtins.property
    @jsii.member(jsii_name="idleSettings")
    def idle_settings(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference, jsii.get(self, "idleSettings"))

    @builtins.property
    @jsii.member(jsii_name="idleSettingsInput")
    def idle_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings], jsii.get(self, "idleSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b34974ac2149421b60a27d7a876813f47cda85a47569903886033603295cb3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository",
    jsii_struct_bases=[],
    name_mapping={"repository_url": "repositoryUrl"},
)
class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository:
    def __init__(self, *, repository_url: builtins.str) -> None:
        '''
        :param repository_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__930bc7db0f6b5fe7316c642ee7d31513497a2a722262e98aeaca9784339554e4)
            check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_url": repository_url,
        }

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.'''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8144abd8c9dafbae8aeb5fd5f0678f11796d388073d98745a6cf8ee92e0c438a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28464adfc480be381dc45c7666fb2e896c0eb3358774629212cb5c9d4a4e899e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bc8ebaa8f0dee1551495c0755184d2f894caa14bd02b2d90d7a15ff514cbd19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef54abfcf10296131d32e2c4dde2526bebe870e695a69f857bfd2983e4712529)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3bb56d9d4bfa2eb2aa5bbe2325ff91f4d55e589df8b07aaab36ccc4c2fc77c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45bb5287f63de03edfe5defe595e7d8eacfe4e896e5618227dcd337ec93c7706)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04a9c9882e4d952e70c07834a690e32b942ef8c2ced960d7e16842bf2c22f254)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="repositoryUrlInput")
    def repository_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))

    @repository_url.setter
    def repository_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc0a28b618d87087cc64a9008d775d5b592fce773fd35931bc43c2089a7969dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dc1deacc2f1a459588b9d00166d332070f9e716b2b3e13326fea5c278a1fb8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3aca4ff21a9d79440a2cb4b49dba8eeb9fbb829c07ae32d3d7db70ba93014e1)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d2c4518dcf2196966167263cc4b6596a76060916b2fecced0c7b0ebc5f30853)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd6941b02bca3daa850de7f73143b232706d013269ee175e75529f8f61bea95a)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__facc6d3b1cf3928ef092fb2e13efc361ec5da9e882f81152013875fed70c09d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8beb68c98a6f4177d58ff9ec6cb9441057c4b94d0edc5ec41b0e03c4949516f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__676321d6c60638dd9e2dafeafba2b22678ee45880448d9968bbf6905491e4f39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__414695ec925c10118a7496712e3a72626c35c7ccc8a17247573296b9a3f51ca9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1e3ea2bc892eddac4596ee9e451050258fc32aeb09a74a3d3ea63ec76028a58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2307771c7c7b70637f5bfa1ec0ec19211013efb78e536a4a3a962968d5ccf11a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e301cc5b19b0227fedebf84711bf81011c16548662735af0871812c6a8dc7c44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1475c8c365d256bb675c82e90d1074b09d6c53e898bad4d57906099098e3d28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8083f8b0d3d69117265da4336ab010923be26a31f36606e5988fa5a24428231)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73cfc4c0c7d8f5c6d40d98ff9de454e4b47d94281fcdd00b8da9bb32af5d221c)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9970c3e8a8270a9bdcfd0dd23c34fd3408d64a244d057218939c848deddd6c75)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac112f5ba7aad546f955ae1642bd4e227e2cd5a3f1eaf0f938b3598a1b60a9d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__536cc75837d26d7729583548889ad10827cd3b485bf45bbcb7338bf9672605bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d8c31dea618ad411c6f5351a8218a2566b3949486e110cd9b3706d2136ec4fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb535c521d3a8668eea2c7f5b50050d03e0923b238af30883b4762fde3f00a5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b310a01bcde4aec3c655c60b6c6f161d39ed409c48b954b5a1043653279027a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe0542e79c62bd186cd4cd271495483e5ff4dba30cf40fc765bc0c488247c7ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings",
    jsii_struct_bases=[],
    name_mapping={
        "assumable_role_arns": "assumableRoleArns",
        "execution_role_arns": "executionRoleArns",
    },
)
class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings:
    def __init__(
        self,
        *,
        assumable_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        execution_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param assumable_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#assumable_role_arns SagemakerDomain#assumable_role_arns}.
        :param execution_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arns SagemakerDomain#execution_role_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8b667429c1bd85283161fb998d67c6b9961b20826a651cf699c2dc1076262a1)
            check_type(argname="argument assumable_role_arns", value=assumable_role_arns, expected_type=type_hints["assumable_role_arns"])
            check_type(argname="argument execution_role_arns", value=execution_role_arns, expected_type=type_hints["execution_role_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assumable_role_arns is not None:
            self._values["assumable_role_arns"] = assumable_role_arns
        if execution_role_arns is not None:
            self._values["execution_role_arns"] = execution_role_arns

    @builtins.property
    def assumable_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#assumable_role_arns SagemakerDomain#assumable_role_arns}.'''
        result = self._values.get("assumable_role_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def execution_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arns SagemakerDomain#execution_role_arns}.'''
        result = self._values.get("execution_role_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39bd2bd2f4bf047e03156f719cf3e3a6fb571bc490219eca1256f1d83fc988e2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAssumableRoleArns")
    def reset_assumable_role_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssumableRoleArns", []))

    @jsii.member(jsii_name="resetExecutionRoleArns")
    def reset_execution_role_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleArns", []))

    @builtins.property
    @jsii.member(jsii_name="assumableRoleArnsInput")
    def assumable_role_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "assumableRoleArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnsInput")
    def execution_role_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "executionRoleArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="assumableRoleArns")
    def assumable_role_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "assumableRoleArns"))

    @assumable_role_arns.setter
    def assumable_role_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0f25d47018169a701844b2a1b92788174866acf78e684759e6a044788ff791b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assumableRoleArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArns")
    def execution_role_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "executionRoleArns"))

    @execution_role_arns.setter
    def execution_role_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6206b0dccd704b95fe47a91a6613b11a87f90a301709459ba82d497deaefaa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fca0c2fa8f267e6727a2ee572ad9f281e9972c2177be076101fd4d057496cc50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49dd8a59b066a04f05182ed66dd59a14659757ab94c9b47d466f37eeea29608d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAppLifecycleManagement")
    def put_app_lifecycle_management(
        self,
        *,
        idle_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_settings: idle_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        value = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement(
            idle_settings=idle_settings
        )

        return typing.cast(None, jsii.invoke(self, "putAppLifecycleManagement", [value]))

    @jsii.member(jsii_name="putCodeRepository")
    def put_code_repository(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5be887a8fe9be03d7133e1de94290157b715474027d90a94107f6c4bd7b354f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCodeRepository", [value]))

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32cce408dd6bee51e07d7895a6fd693ca127ea935d300b6231303a2746f57f0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="putEmrSettings")
    def put_emr_settings(
        self,
        *,
        assumable_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        execution_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param assumable_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#assumable_role_arns SagemakerDomain#assumable_role_arns}.
        :param execution_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arns SagemakerDomain#execution_role_arns}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings(
            assumable_role_arns=assumable_role_arns,
            execution_role_arns=execution_role_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putEmrSettings", [value]))

    @jsii.member(jsii_name="resetAppLifecycleManagement")
    def reset_app_lifecycle_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppLifecycleManagement", []))

    @jsii.member(jsii_name="resetBuiltInLifecycleConfigArn")
    def reset_built_in_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuiltInLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetCodeRepository")
    def reset_code_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeRepository", []))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetEmrSettings")
    def reset_emr_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmrSettings", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference, jsii.get(self, "appLifecycleManagement"))

    @builtins.property
    @jsii.member(jsii_name="codeRepository")
    def code_repository(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryList:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryList, jsii.get(self, "codeRepository"))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageList:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="emrSettings")
    def emr_settings(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsOutputReference, jsii.get(self, "emrSettings"))

    @builtins.property
    @jsii.member(jsii_name="appLifecycleManagementInput")
    def app_lifecycle_management_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement], jsii.get(self, "appLifecycleManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="builtInLifecycleConfigArnInput")
    def built_in_lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "builtInLifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="codeRepositoryInput")
    def code_repository_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]]], jsii.get(self, "codeRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="emrSettingsInput")
    def emr_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings], jsii.get(self, "emrSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "builtInLifecycleConfigArn"))

    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaf6d71bcc143bf2d611a13c4d936ea520d03a6b86fc146ec40db20807801f6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "builtInLifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a53b435809e2be1bbd825563644d4c50a3165ff7022b4d416cf0b2bd5ea28a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7710bc82623e0c8ed649a66bfa6bafc7dce650c7585ad856479735cfa8f1a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "code_repository": "codeRepository",
        "default_resource_spec": "defaultResourceSpec",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings:
    def __init__(
        self,
        *,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5154f237ee2b8507f6421ee32a6539564f23ed763cb38cbaeacc257edc85cca3)
            check_type(argname="argument code_repository", value=code_repository, expected_type=type_hints["code_repository"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if code_repository is not None:
            self._values["code_repository"] = code_repository
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def code_repository(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository"]]]:
        '''code_repository block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        '''
        result = self._values.get("code_repository")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository",
    jsii_struct_bases=[],
    name_mapping={"repository_url": "repositoryUrl"},
)
class SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository:
    def __init__(self, *, repository_url: builtins.str) -> None:
        '''
        :param repository_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3254acf9f19ddd5d3bf7cc43b236a82fa035c3fccfcbb4d12e8af9a055b2115)
            check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_url": repository_url,
        }

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.'''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab6f8a5a42226bbe15fcff88138729fa0e790e2a2477661e1a6257b82fb26f4c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45a2ccc785dc49201afcab1fa3d22b359ac3b755608c491798509a939fc6634d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20b601efc5d3c066ff83dcb8f5c3413ea177645cfb2624799b88ec020bbae99b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe3552e704ab49cadabcac64bc36719ce2c9fdefb21d0ee0d0579cb064566f06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7be93016f1804dd02d692d9461bce3702bad69cf45a62c1b342ef9c9e48492ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5bd1e72746108a85ea60ce50bbb6fe038f50adda179306c2c85c8827f882850)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3bbb68f9753f4e2a3b92b4f8548953d9d80889b69e8406ff205680d11e1b888)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="repositoryUrlInput")
    def repository_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))

    @repository_url.setter
    def repository_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7ecb6401847524a3d4da168758d44d9822d8872115b654f826a36a919d7cecb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e21ee74cf164eb51ab896f739ff2a0474206a82b9098c26cea0e3ffc2539dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__609812c3bf3e7cc9fa3ed0fc9bd3e96e4779215025a0d6c47402e25f371a8140)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fdb00443375cf1ee212b6e2241efada44f7fcab25fb1ff06be4ab8ef02a7c33)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37fc018365f9bf0426f9e65769821c321122909157a7c88c53f6d1f9e0f9f774)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0900adfdd391c977541fc0ce3f4154fe6c1a0c883d4938be2192c60f7c1ad2fe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01eaf757b8e8703d72867ff904432ee2d2251f5780d62f23c7f1586a86c54f76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a384686e7f69b12d9a1c352e0b02a3469ecbb369e5b68431b5dad088679fcb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57f80745fbd9eb14f965c048fd294dcad878a97b7af6b2b0b02b83a5542bb77)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82bb7ec117acaf099e00220e3af66564fe7fb6d2706a7497f56cd44e4644565f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bda23e5fd96bf833f314326e70ca4ee51ebc25efd4825cd4de1af8acadacfb0)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeRepository")
    def put_code_repository(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd02f5259a981dae250a23d8f03b3fc61f03c4cdec1e7840f4c3d4c52f9521bb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCodeRepository", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCodeRepository")
    def reset_code_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeRepository", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="codeRepository")
    def code_repository(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryList:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryList, jsii.get(self, "codeRepository"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="codeRepositoryInput")
    def code_repository_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]]], jsii.get(self, "codeRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c218637f0bd9a7fbfa39ce6ff70508f543640c1ccba76f1bee5cbce21702c52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b509518d952b62168889b933b53f917f4771c145cc34f67f70824f4cc78399e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings:
    def __init__(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc7338cd6ac83eaae60db20cee9d1a20cd295b8830add8f4be630749b8803c0)
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3273ad019499422dac19ba9ea05a581c473ba498db14f68905cc4f9c5b974253)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46d7df5f1ef05c9304d9d613f8a13d5598be70a33addbb2c9a2041e0d7a20170)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3df185394ab8ae4e5d989c3e563b4f5214014f07b7d9017662b41ebc7ad70114)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f79c5ea60bea0c69f5d2658ea1aa464c9f0d0d9ef225b53b0475a547ff17d93)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8af5a2cec8839fc03027e89066ae4478382f70d11bfde8af695d7ef0bb69d372)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__774d6c26b121152beb5ec1b8c808f32730310d35689e41558d83119b09d19b58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfe65595b7ca1577c6dd0cf0507c7ee6eb6e31c428dca34bb8ab56bcfb4ae288)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7aff8b411f65329f2e3ea8a475aa5e32b1c84753a5a24e5205c9904f003747d9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b991d28e1c533f3d2cc626eea4b62ff1db378fd9508edc878dfe9b1649f4bff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8893476181e33dad23c8b74754dbd9c00e55312b3705e2d076c86a0567f143ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e204cd8fd472639335b9bcdd615111574ba7dee9c4bdaef626d2de52ed799c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974b31bc311a86ed66d7ffded809ee9f73ccc4b55334ebc960a611c2140e38f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f3d1c2ef281b7851c10c5016c3cbf6fecbda5bd62b03bb5eeaea6f5489f1d9b)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b62d08dffc7b7f84b7ae8b522b8bc2c3c7fbf405c9e3947d741eed11144dfce)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f87d61a95a3611bb64775c2bb130e9c996c39ee5dce9185ffb6eb32e946ac882)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73b8af28877b84469110dc1bc98bcf9ee26607be04c98ee19afb1acb7c875bfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e544c96fb672ba5ce95eeaf549a272c6cab0d1874dc12be479a9b7736db3dac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8adeef9ab41d4b9172bb948f58bd00fbd8a6addbd18ec9136edefff83e3fdc98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98a2b96b8c1b56bf122e90864ca070648e94473cf034262ea15e1dbf221b1bb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd77160b904b15d1dc31a5d9091be80c4258456aa7bc87e3cc4e43027cc0f97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66d37a0ec834d50af22c3ff4070fc0d052e0e3f788a247e680ec07a218381c8a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6417ba3d0a5acd1aa737f248d1f3a9d81c5e79321a974a767df24123eeb569ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageList:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb31eafdac64d3e6e3bfd15f3583bd20ceccf3c68b569c26b90f829240739757)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31b050007d6c6a399a121f781b3bef5f31f06439a10c8822d842333458b5e3e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce6e0894a3843bd3e642bc9d3d758e17bb1c66fa48a4ed96c7757a5772de38cf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomFileSystemConfig")
    def put_custom_file_system_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc80e64d21b3af95625a8f1962ef5a8cfa62aae0ab52399cc27aee2a593bf5de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomFileSystemConfig", [value]))

    @jsii.member(jsii_name="putCustomPosixUserConfig")
    def put_custom_posix_user_config(
        self,
        *,
        gid: jsii.Number,
        uid: jsii.Number,
    ) -> None:
        '''
        :param gid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#gid SagemakerDomain#gid}.
        :param uid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#uid SagemakerDomain#uid}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig(
            gid=gid, uid=uid
        )

        return typing.cast(None, jsii.invoke(self, "putCustomPosixUserConfig", [value]))

    @jsii.member(jsii_name="putJupyterLabAppSettings")
    def put_jupyter_lab_app_settings(
        self,
        *,
        app_lifecycle_management: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement, typing.Dict[builtins.str, typing.Any]]] = None,
        built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
        emr_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_lifecycle_management: app_lifecycle_management block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        :param built_in_lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param emr_settings: emr_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_settings SagemakerDomain#emr_settings}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings(
            app_lifecycle_management=app_lifecycle_management,
            built_in_lifecycle_config_arn=built_in_lifecycle_config_arn,
            code_repository=code_repository,
            custom_image=custom_image,
            default_resource_spec=default_resource_spec,
            emr_settings=emr_settings,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putJupyterLabAppSettings", [value]))

    @jsii.member(jsii_name="putJupyterServerAppSettings")
    def put_jupyter_server_app_settings(
        self,
        *,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings(
            code_repository=code_repository,
            default_resource_spec=default_resource_spec,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putJupyterServerAppSettings", [value]))

    @jsii.member(jsii_name="putKernelGatewayAppSettings")
    def put_kernel_gateway_app_settings(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings(
            custom_image=custom_image,
            default_resource_spec=default_resource_spec,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putKernelGatewayAppSettings", [value]))

    @jsii.member(jsii_name="putSpaceStorageSettings")
    def put_space_storage_settings(
        self,
        *,
        default_ebs_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_ebs_storage_settings: default_ebs_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_storage_settings SagemakerDomain#default_ebs_storage_settings}
        '''
        value = SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings(
            default_ebs_storage_settings=default_ebs_storage_settings
        )

        return typing.cast(None, jsii.invoke(self, "putSpaceStorageSettings", [value]))

    @jsii.member(jsii_name="resetCustomFileSystemConfig")
    def reset_custom_file_system_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomFileSystemConfig", []))

    @jsii.member(jsii_name="resetCustomPosixUserConfig")
    def reset_custom_posix_user_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPosixUserConfig", []))

    @jsii.member(jsii_name="resetJupyterLabAppSettings")
    def reset_jupyter_lab_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJupyterLabAppSettings", []))

    @jsii.member(jsii_name="resetJupyterServerAppSettings")
    def reset_jupyter_server_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJupyterServerAppSettings", []))

    @jsii.member(jsii_name="resetKernelGatewayAppSettings")
    def reset_kernel_gateway_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernelGatewayAppSettings", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSpaceStorageSettings")
    def reset_space_storage_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpaceStorageSettings", []))

    @builtins.property
    @jsii.member(jsii_name="customFileSystemConfig")
    def custom_file_system_config(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigList:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigList, jsii.get(self, "customFileSystemConfig"))

    @builtins.property
    @jsii.member(jsii_name="customPosixUserConfig")
    def custom_posix_user_config(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfigOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfigOutputReference, jsii.get(self, "customPosixUserConfig"))

    @builtins.property
    @jsii.member(jsii_name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsOutputReference, jsii.get(self, "jupyterLabAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsOutputReference, jsii.get(self, "jupyterServerAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsOutputReference, jsii.get(self, "kernelGatewayAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="spaceStorageSettings")
    def space_storage_settings(
        self,
    ) -> "SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsOutputReference", jsii.get(self, "spaceStorageSettings"))

    @builtins.property
    @jsii.member(jsii_name="customFileSystemConfigInput")
    def custom_file_system_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]]], jsii.get(self, "customFileSystemConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="customPosixUserConfigInput")
    def custom_posix_user_config_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig], jsii.get(self, "customPosixUserConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleInput")
    def execution_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="jupyterLabAppSettingsInput")
    def jupyter_lab_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings], jsii.get(self, "jupyterLabAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettingsInput")
    def jupyter_server_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings], jsii.get(self, "jupyterServerAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettingsInput")
    def kernel_gateway_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings], jsii.get(self, "kernelGatewayAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="spaceStorageSettingsInput")
    def space_storage_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings"], jsii.get(self, "spaceStorageSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d86f052e667b6a80c5843b8c426e49d78556856863017cfd74068aed90375e5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__430740fe3a75ec98683fa696634abb8a78562846f0f65b5e4b359dda3cf7188c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerDomainDefaultSpaceSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1baf7357a6a619975f802f0da1e14c7790a16bfd8690c09873915019c3b12f27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings",
    jsii_struct_bases=[],
    name_mapping={"default_ebs_storage_settings": "defaultEbsStorageSettings"},
)
class SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings:
    def __init__(
        self,
        *,
        default_ebs_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_ebs_storage_settings: default_ebs_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_storage_settings SagemakerDomain#default_ebs_storage_settings}
        '''
        if isinstance(default_ebs_storage_settings, dict):
            default_ebs_storage_settings = SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings(**default_ebs_storage_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__805edd6253c40f2698faac414884fe288bd743d9dff3c1fda5ad142afb0a92ae)
            check_type(argname="argument default_ebs_storage_settings", value=default_ebs_storage_settings, expected_type=type_hints["default_ebs_storage_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_ebs_storage_settings is not None:
            self._values["default_ebs_storage_settings"] = default_ebs_storage_settings

    @builtins.property
    def default_ebs_storage_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings"]:
        '''default_ebs_storage_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_storage_settings SagemakerDomain#default_ebs_storage_settings}
        '''
        result = self._values.get("default_ebs_storage_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings",
    jsii_struct_bases=[],
    name_mapping={
        "default_ebs_volume_size_in_gb": "defaultEbsVolumeSizeInGb",
        "maximum_ebs_volume_size_in_gb": "maximumEbsVolumeSizeInGb",
    },
)
class SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings:
    def __init__(
        self,
        *,
        default_ebs_volume_size_in_gb: jsii.Number,
        maximum_ebs_volume_size_in_gb: jsii.Number,
    ) -> None:
        '''
        :param default_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_volume_size_in_gb SagemakerDomain#default_ebs_volume_size_in_gb}.
        :param maximum_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#maximum_ebs_volume_size_in_gb SagemakerDomain#maximum_ebs_volume_size_in_gb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7fa0ee7bec01fb410f270af32f2469c6516e056171b39bb558526178b0478484)
            check_type(argname="argument default_ebs_volume_size_in_gb", value=default_ebs_volume_size_in_gb, expected_type=type_hints["default_ebs_volume_size_in_gb"])
            check_type(argname="argument maximum_ebs_volume_size_in_gb", value=maximum_ebs_volume_size_in_gb, expected_type=type_hints["maximum_ebs_volume_size_in_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_ebs_volume_size_in_gb": default_ebs_volume_size_in_gb,
            "maximum_ebs_volume_size_in_gb": maximum_ebs_volume_size_in_gb,
        }

    @builtins.property
    def default_ebs_volume_size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_volume_size_in_gb SagemakerDomain#default_ebs_volume_size_in_gb}.'''
        result = self._values.get("default_ebs_volume_size_in_gb")
        assert result is not None, "Required property 'default_ebs_volume_size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def maximum_ebs_volume_size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#maximum_ebs_volume_size_in_gb SagemakerDomain#maximum_ebs_volume_size_in_gb}.'''
        result = self._values.get("maximum_ebs_volume_size_in_gb")
        assert result is not None, "Required property 'maximum_ebs_volume_size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1a667d234b927a66e7b164b23201c3430b5736e25cfa9b640291cd794a463be)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultEbsVolumeSizeInGbInput")
    def default_ebs_volume_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultEbsVolumeSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumEbsVolumeSizeInGbInput")
    def maximum_ebs_volume_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumEbsVolumeSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultEbsVolumeSizeInGb"))

    @default_ebs_volume_size_in_gb.setter
    def default_ebs_volume_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6b82fa07aec15a069867109c0a50bb87b2be1b519d506aecfb9a531439278ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultEbsVolumeSizeInGb", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumEbsVolumeSizeInGb"))

    @maximum_ebs_volume_size_in_gb.setter
    def maximum_ebs_volume_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__619834be4c40a9e4739d32f3299306b4c73844dee1ec4cf84d49128b131e79c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumEbsVolumeSizeInGb", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2877358a825b0ebe24e0c9e23aa9f3c56a066e7c4dc4a00e162390b0499feab3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__532dc8b3d2c196af721aed9b74e3e72493fe2932d79ffa70a08f84adcaca2475)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultEbsStorageSettings")
    def put_default_ebs_storage_settings(
        self,
        *,
        default_ebs_volume_size_in_gb: jsii.Number,
        maximum_ebs_volume_size_in_gb: jsii.Number,
    ) -> None:
        '''
        :param default_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_volume_size_in_gb SagemakerDomain#default_ebs_volume_size_in_gb}.
        :param maximum_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#maximum_ebs_volume_size_in_gb SagemakerDomain#maximum_ebs_volume_size_in_gb}.
        '''
        value = SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings(
            default_ebs_volume_size_in_gb=default_ebs_volume_size_in_gb,
            maximum_ebs_volume_size_in_gb=maximum_ebs_volume_size_in_gb,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultEbsStorageSettings", [value]))

    @jsii.member(jsii_name="resetDefaultEbsStorageSettings")
    def reset_default_ebs_storage_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultEbsStorageSettings", []))

    @builtins.property
    @jsii.member(jsii_name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(
        self,
    ) -> SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference, jsii.get(self, "defaultEbsStorageSettings"))

    @builtins.property
    @jsii.member(jsii_name="defaultEbsStorageSettingsInput")
    def default_ebs_storage_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings], jsii.get(self, "defaultEbsStorageSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1655fdbbdeb55603a7c1c49191308a7aee52c6f77221f6285dca31c80a17febd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettings",
    jsii_struct_bases=[],
    name_mapping={
        "execution_role": "executionRole",
        "auto_mount_home_efs": "autoMountHomeEfs",
        "canvas_app_settings": "canvasAppSettings",
        "code_editor_app_settings": "codeEditorAppSettings",
        "custom_file_system_config": "customFileSystemConfig",
        "custom_posix_user_config": "customPosixUserConfig",
        "default_landing_uri": "defaultLandingUri",
        "jupyter_lab_app_settings": "jupyterLabAppSettings",
        "jupyter_server_app_settings": "jupyterServerAppSettings",
        "kernel_gateway_app_settings": "kernelGatewayAppSettings",
        "r_session_app_settings": "rSessionAppSettings",
        "r_studio_server_pro_app_settings": "rStudioServerProAppSettings",
        "security_groups": "securityGroups",
        "sharing_settings": "sharingSettings",
        "space_storage_settings": "spaceStorageSettings",
        "studio_web_portal": "studioWebPortal",
        "studio_web_portal_settings": "studioWebPortalSettings",
        "tensor_board_app_settings": "tensorBoardAppSettings",
    },
)
class SagemakerDomainDefaultUserSettings:
    def __init__(
        self,
        *,
        execution_role: builtins.str,
        auto_mount_home_efs: typing.Optional[builtins.str] = None,
        canvas_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        code_editor_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCodeEditorAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        custom_file_system_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsCustomFileSystemConfig", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_posix_user_config: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCustomPosixUserConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        default_landing_uri: typing.Optional[builtins.str] = None,
        jupyter_lab_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        jupyter_server_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        kernel_gateway_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        r_session_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsRSessionAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        r_studio_server_pro_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        sharing_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSharingSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        space_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSpaceStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        studio_web_portal: typing.Optional[builtins.str] = None,
        studio_web_portal_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsStudioWebPortalSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        tensor_board_app_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param execution_role: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role SagemakerDomain#execution_role}.
        :param auto_mount_home_efs: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#auto_mount_home_efs SagemakerDomain#auto_mount_home_efs}.
        :param canvas_app_settings: canvas_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#canvas_app_settings SagemakerDomain#canvas_app_settings}
        :param code_editor_app_settings: code_editor_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_editor_app_settings SagemakerDomain#code_editor_app_settings}
        :param custom_file_system_config: custom_file_system_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_file_system_config SagemakerDomain#custom_file_system_config}
        :param custom_posix_user_config: custom_posix_user_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_posix_user_config SagemakerDomain#custom_posix_user_config}
        :param default_landing_uri: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_landing_uri SagemakerDomain#default_landing_uri}.
        :param jupyter_lab_app_settings: jupyter_lab_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_lab_app_settings SagemakerDomain#jupyter_lab_app_settings}
        :param jupyter_server_app_settings: jupyter_server_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        :param kernel_gateway_app_settings: kernel_gateway_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        :param r_session_app_settings: r_session_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_session_app_settings SagemakerDomain#r_session_app_settings}
        :param r_studio_server_pro_app_settings: r_studio_server_pro_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_server_pro_app_settings SagemakerDomain#r_studio_server_pro_app_settings}
        :param security_groups: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_groups SagemakerDomain#security_groups}.
        :param sharing_settings: sharing_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sharing_settings SagemakerDomain#sharing_settings}
        :param space_storage_settings: space_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#space_storage_settings SagemakerDomain#space_storage_settings}
        :param studio_web_portal: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#studio_web_portal SagemakerDomain#studio_web_portal}.
        :param studio_web_portal_settings: studio_web_portal_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#studio_web_portal_settings SagemakerDomain#studio_web_portal_settings}
        :param tensor_board_app_settings: tensor_board_app_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tensor_board_app_settings SagemakerDomain#tensor_board_app_settings}
        '''
        if isinstance(canvas_app_settings, dict):
            canvas_app_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettings(**canvas_app_settings)
        if isinstance(code_editor_app_settings, dict):
            code_editor_app_settings = SagemakerDomainDefaultUserSettingsCodeEditorAppSettings(**code_editor_app_settings)
        if isinstance(custom_posix_user_config, dict):
            custom_posix_user_config = SagemakerDomainDefaultUserSettingsCustomPosixUserConfig(**custom_posix_user_config)
        if isinstance(jupyter_lab_app_settings, dict):
            jupyter_lab_app_settings = SagemakerDomainDefaultUserSettingsJupyterLabAppSettings(**jupyter_lab_app_settings)
        if isinstance(jupyter_server_app_settings, dict):
            jupyter_server_app_settings = SagemakerDomainDefaultUserSettingsJupyterServerAppSettings(**jupyter_server_app_settings)
        if isinstance(kernel_gateway_app_settings, dict):
            kernel_gateway_app_settings = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings(**kernel_gateway_app_settings)
        if isinstance(r_session_app_settings, dict):
            r_session_app_settings = SagemakerDomainDefaultUserSettingsRSessionAppSettings(**r_session_app_settings)
        if isinstance(r_studio_server_pro_app_settings, dict):
            r_studio_server_pro_app_settings = SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings(**r_studio_server_pro_app_settings)
        if isinstance(sharing_settings, dict):
            sharing_settings = SagemakerDomainDefaultUserSettingsSharingSettings(**sharing_settings)
        if isinstance(space_storage_settings, dict):
            space_storage_settings = SagemakerDomainDefaultUserSettingsSpaceStorageSettings(**space_storage_settings)
        if isinstance(studio_web_portal_settings, dict):
            studio_web_portal_settings = SagemakerDomainDefaultUserSettingsStudioWebPortalSettings(**studio_web_portal_settings)
        if isinstance(tensor_board_app_settings, dict):
            tensor_board_app_settings = SagemakerDomainDefaultUserSettingsTensorBoardAppSettings(**tensor_board_app_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84027cf9e196018ec72042a2255ea078b318e0785b2c0e48697f1db2b8c2c45d)
            check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
            check_type(argname="argument auto_mount_home_efs", value=auto_mount_home_efs, expected_type=type_hints["auto_mount_home_efs"])
            check_type(argname="argument canvas_app_settings", value=canvas_app_settings, expected_type=type_hints["canvas_app_settings"])
            check_type(argname="argument code_editor_app_settings", value=code_editor_app_settings, expected_type=type_hints["code_editor_app_settings"])
            check_type(argname="argument custom_file_system_config", value=custom_file_system_config, expected_type=type_hints["custom_file_system_config"])
            check_type(argname="argument custom_posix_user_config", value=custom_posix_user_config, expected_type=type_hints["custom_posix_user_config"])
            check_type(argname="argument default_landing_uri", value=default_landing_uri, expected_type=type_hints["default_landing_uri"])
            check_type(argname="argument jupyter_lab_app_settings", value=jupyter_lab_app_settings, expected_type=type_hints["jupyter_lab_app_settings"])
            check_type(argname="argument jupyter_server_app_settings", value=jupyter_server_app_settings, expected_type=type_hints["jupyter_server_app_settings"])
            check_type(argname="argument kernel_gateway_app_settings", value=kernel_gateway_app_settings, expected_type=type_hints["kernel_gateway_app_settings"])
            check_type(argname="argument r_session_app_settings", value=r_session_app_settings, expected_type=type_hints["r_session_app_settings"])
            check_type(argname="argument r_studio_server_pro_app_settings", value=r_studio_server_pro_app_settings, expected_type=type_hints["r_studio_server_pro_app_settings"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument sharing_settings", value=sharing_settings, expected_type=type_hints["sharing_settings"])
            check_type(argname="argument space_storage_settings", value=space_storage_settings, expected_type=type_hints["space_storage_settings"])
            check_type(argname="argument studio_web_portal", value=studio_web_portal, expected_type=type_hints["studio_web_portal"])
            check_type(argname="argument studio_web_portal_settings", value=studio_web_portal_settings, expected_type=type_hints["studio_web_portal_settings"])
            check_type(argname="argument tensor_board_app_settings", value=tensor_board_app_settings, expected_type=type_hints["tensor_board_app_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "execution_role": execution_role,
        }
        if auto_mount_home_efs is not None:
            self._values["auto_mount_home_efs"] = auto_mount_home_efs
        if canvas_app_settings is not None:
            self._values["canvas_app_settings"] = canvas_app_settings
        if code_editor_app_settings is not None:
            self._values["code_editor_app_settings"] = code_editor_app_settings
        if custom_file_system_config is not None:
            self._values["custom_file_system_config"] = custom_file_system_config
        if custom_posix_user_config is not None:
            self._values["custom_posix_user_config"] = custom_posix_user_config
        if default_landing_uri is not None:
            self._values["default_landing_uri"] = default_landing_uri
        if jupyter_lab_app_settings is not None:
            self._values["jupyter_lab_app_settings"] = jupyter_lab_app_settings
        if jupyter_server_app_settings is not None:
            self._values["jupyter_server_app_settings"] = jupyter_server_app_settings
        if kernel_gateway_app_settings is not None:
            self._values["kernel_gateway_app_settings"] = kernel_gateway_app_settings
        if r_session_app_settings is not None:
            self._values["r_session_app_settings"] = r_session_app_settings
        if r_studio_server_pro_app_settings is not None:
            self._values["r_studio_server_pro_app_settings"] = r_studio_server_pro_app_settings
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if sharing_settings is not None:
            self._values["sharing_settings"] = sharing_settings
        if space_storage_settings is not None:
            self._values["space_storage_settings"] = space_storage_settings
        if studio_web_portal is not None:
            self._values["studio_web_portal"] = studio_web_portal
        if studio_web_portal_settings is not None:
            self._values["studio_web_portal_settings"] = studio_web_portal_settings
        if tensor_board_app_settings is not None:
            self._values["tensor_board_app_settings"] = tensor_board_app_settings

    @builtins.property
    def execution_role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role SagemakerDomain#execution_role}.'''
        result = self._values.get("execution_role")
        assert result is not None, "Required property 'execution_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_mount_home_efs(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#auto_mount_home_efs SagemakerDomain#auto_mount_home_efs}.'''
        result = self._values.get("auto_mount_home_efs")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def canvas_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettings"]:
        '''canvas_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#canvas_app_settings SagemakerDomain#canvas_app_settings}
        '''
        result = self._values.get("canvas_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettings"], result)

    @builtins.property
    def code_editor_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettings"]:
        '''code_editor_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_editor_app_settings SagemakerDomain#code_editor_app_settings}
        '''
        result = self._values.get("code_editor_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettings"], result)

    @builtins.property
    def custom_file_system_config(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsCustomFileSystemConfig"]]]:
        '''custom_file_system_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_file_system_config SagemakerDomain#custom_file_system_config}
        '''
        result = self._values.get("custom_file_system_config")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsCustomFileSystemConfig"]]], result)

    @builtins.property
    def custom_posix_user_config(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCustomPosixUserConfig"]:
        '''custom_posix_user_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_posix_user_config SagemakerDomain#custom_posix_user_config}
        '''
        result = self._values.get("custom_posix_user_config")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCustomPosixUserConfig"], result)

    @builtins.property
    def default_landing_uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_landing_uri SagemakerDomain#default_landing_uri}.'''
        result = self._values.get("default_landing_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jupyter_lab_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettings"]:
        '''jupyter_lab_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_lab_app_settings SagemakerDomain#jupyter_lab_app_settings}
        '''
        result = self._values.get("jupyter_lab_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettings"], result)

    @builtins.property
    def jupyter_server_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings"]:
        '''jupyter_server_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#jupyter_server_app_settings SagemakerDomain#jupyter_server_app_settings}
        '''
        result = self._values.get("jupyter_server_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettings"], result)

    @builtins.property
    def kernel_gateway_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings"]:
        '''kernel_gateway_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kernel_gateway_app_settings SagemakerDomain#kernel_gateway_app_settings}
        '''
        result = self._values.get("kernel_gateway_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings"], result)

    @builtins.property
    def r_session_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsRSessionAppSettings"]:
        '''r_session_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_session_app_settings SagemakerDomain#r_session_app_settings}
        '''
        result = self._values.get("r_session_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsRSessionAppSettings"], result)

    @builtins.property
    def r_studio_server_pro_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings"]:
        '''r_studio_server_pro_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_server_pro_app_settings SagemakerDomain#r_studio_server_pro_app_settings}
        '''
        result = self._values.get("r_studio_server_pro_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings"], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_groups SagemakerDomain#security_groups}.'''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sharing_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"]:
        '''sharing_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sharing_settings SagemakerDomain#sharing_settings}
        '''
        result = self._values.get("sharing_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"], result)

    @builtins.property
    def space_storage_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsSpaceStorageSettings"]:
        '''space_storage_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#space_storage_settings SagemakerDomain#space_storage_settings}
        '''
        result = self._values.get("space_storage_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsSpaceStorageSettings"], result)

    @builtins.property
    def studio_web_portal(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#studio_web_portal SagemakerDomain#studio_web_portal}.'''
        result = self._values.get("studio_web_portal")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def studio_web_portal_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsStudioWebPortalSettings"]:
        '''studio_web_portal_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#studio_web_portal_settings SagemakerDomain#studio_web_portal_settings}
        '''
        result = self._values.get("studio_web_portal_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsStudioWebPortalSettings"], result)

    @builtins.property
    def tensor_board_app_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"]:
        '''tensor_board_app_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#tensor_board_app_settings SagemakerDomain#tensor_board_app_settings}
        '''
        result = self._values.get("tensor_board_app_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "direct_deploy_settings": "directDeploySettings",
        "emr_serverless_settings": "emrServerlessSettings",
        "generative_ai_settings": "generativeAiSettings",
        "identity_provider_oauth_settings": "identityProviderOauthSettings",
        "kendra_settings": "kendraSettings",
        "model_register_settings": "modelRegisterSettings",
        "time_series_forecasting_settings": "timeSeriesForecastingSettings",
        "workspace_settings": "workspaceSettings",
    },
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettings:
    def __init__(
        self,
        *,
        direct_deploy_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings", typing.Dict[builtins.str, typing.Any]]] = None,
        emr_serverless_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        generative_ai_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        identity_provider_oauth_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        kendra_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        model_register_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        time_series_forecasting_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        workspace_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param direct_deploy_settings: direct_deploy_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#direct_deploy_settings SagemakerDomain#direct_deploy_settings}
        :param emr_serverless_settings: emr_serverless_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_serverless_settings SagemakerDomain#emr_serverless_settings}
        :param generative_ai_settings: generative_ai_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#generative_ai_settings SagemakerDomain#generative_ai_settings}
        :param identity_provider_oauth_settings: identity_provider_oauth_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#identity_provider_oauth_settings SagemakerDomain#identity_provider_oauth_settings}
        :param kendra_settings: kendra_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kendra_settings SagemakerDomain#kendra_settings}
        :param model_register_settings: model_register_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#model_register_settings SagemakerDomain#model_register_settings}
        :param time_series_forecasting_settings: time_series_forecasting_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#time_series_forecasting_settings SagemakerDomain#time_series_forecasting_settings}
        :param workspace_settings: workspace_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#workspace_settings SagemakerDomain#workspace_settings}
        '''
        if isinstance(direct_deploy_settings, dict):
            direct_deploy_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings(**direct_deploy_settings)
        if isinstance(emr_serverless_settings, dict):
            emr_serverless_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings(**emr_serverless_settings)
        if isinstance(generative_ai_settings, dict):
            generative_ai_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings(**generative_ai_settings)
        if isinstance(kendra_settings, dict):
            kendra_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings(**kendra_settings)
        if isinstance(model_register_settings, dict):
            model_register_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings(**model_register_settings)
        if isinstance(time_series_forecasting_settings, dict):
            time_series_forecasting_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(**time_series_forecasting_settings)
        if isinstance(workspace_settings, dict):
            workspace_settings = SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings(**workspace_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1c55e9b3a8ce9d4b8d97d76c1ef2b544a58f4b7ec5aff93103dcfe0cae3635a)
            check_type(argname="argument direct_deploy_settings", value=direct_deploy_settings, expected_type=type_hints["direct_deploy_settings"])
            check_type(argname="argument emr_serverless_settings", value=emr_serverless_settings, expected_type=type_hints["emr_serverless_settings"])
            check_type(argname="argument generative_ai_settings", value=generative_ai_settings, expected_type=type_hints["generative_ai_settings"])
            check_type(argname="argument identity_provider_oauth_settings", value=identity_provider_oauth_settings, expected_type=type_hints["identity_provider_oauth_settings"])
            check_type(argname="argument kendra_settings", value=kendra_settings, expected_type=type_hints["kendra_settings"])
            check_type(argname="argument model_register_settings", value=model_register_settings, expected_type=type_hints["model_register_settings"])
            check_type(argname="argument time_series_forecasting_settings", value=time_series_forecasting_settings, expected_type=type_hints["time_series_forecasting_settings"])
            check_type(argname="argument workspace_settings", value=workspace_settings, expected_type=type_hints["workspace_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if direct_deploy_settings is not None:
            self._values["direct_deploy_settings"] = direct_deploy_settings
        if emr_serverless_settings is not None:
            self._values["emr_serverless_settings"] = emr_serverless_settings
        if generative_ai_settings is not None:
            self._values["generative_ai_settings"] = generative_ai_settings
        if identity_provider_oauth_settings is not None:
            self._values["identity_provider_oauth_settings"] = identity_provider_oauth_settings
        if kendra_settings is not None:
            self._values["kendra_settings"] = kendra_settings
        if model_register_settings is not None:
            self._values["model_register_settings"] = model_register_settings
        if time_series_forecasting_settings is not None:
            self._values["time_series_forecasting_settings"] = time_series_forecasting_settings
        if workspace_settings is not None:
            self._values["workspace_settings"] = workspace_settings

    @builtins.property
    def direct_deploy_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings"]:
        '''direct_deploy_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#direct_deploy_settings SagemakerDomain#direct_deploy_settings}
        '''
        result = self._values.get("direct_deploy_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings"], result)

    @builtins.property
    def emr_serverless_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings"]:
        '''emr_serverless_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_serverless_settings SagemakerDomain#emr_serverless_settings}
        '''
        result = self._values.get("emr_serverless_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings"], result)

    @builtins.property
    def generative_ai_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings"]:
        '''generative_ai_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#generative_ai_settings SagemakerDomain#generative_ai_settings}
        '''
        result = self._values.get("generative_ai_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings"], result)

    @builtins.property
    def identity_provider_oauth_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings"]]]:
        '''identity_provider_oauth_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#identity_provider_oauth_settings SagemakerDomain#identity_provider_oauth_settings}
        '''
        result = self._values.get("identity_provider_oauth_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings"]]], result)

    @builtins.property
    def kendra_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings"]:
        '''kendra_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kendra_settings SagemakerDomain#kendra_settings}
        '''
        result = self._values.get("kendra_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings"], result)

    @builtins.property
    def model_register_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings"]:
        '''model_register_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#model_register_settings SagemakerDomain#model_register_settings}
        '''
        result = self._values.get("model_register_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings"], result)

    @builtins.property
    def time_series_forecasting_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"]:
        '''time_series_forecasting_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#time_series_forecasting_settings SagemakerDomain#time_series_forecasting_settings}
        '''
        result = self._values.get("time_series_forecasting_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"], result)

    @builtins.property
    def workspace_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings"]:
        '''workspace_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#workspace_settings SagemakerDomain#workspace_settings}
        '''
        result = self._values.get("workspace_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings:
    def __init__(self, *, status: typing.Optional[builtins.str] = None) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee3ea0b8df0f858249d51f258619343c9a1ada3a3cc84a047a234b90b8ce556)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f6cdb96c24b50176c931d7d7b853a47e08eef7af86b9542b134bdfa7b7c5b9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ccb9312bc3deacf6006aa291d6f3e3b13dc6f88eccf84620e7c841957147ab3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c42b0213addcaf73bc56179be11e0270df6216b3e352a1219a6d8ca172fdc12d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings",
    jsii_struct_bases=[],
    name_mapping={"execution_role_arn": "executionRoleArn", "status": "status"},
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings:
    def __init__(
        self,
        *,
        execution_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param execution_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arn SagemakerDomain#execution_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__134faa03a2412f9526cd54d6e955d709957e79fd1516dba293bf8417f7d2c66d)
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if execution_role_arn is not None:
            self._values["execution_role_arn"] = execution_role_arn
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def execution_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arn SagemakerDomain#execution_role_arn}.'''
        result = self._values.get("execution_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bb231176fbfb4fe12f151b1dbf4ff898c42a70340ef85b2cc5b80fd035005cf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExecutionRoleArn")
    def reset_execution_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleArn", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnInput")
    def execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6262795f39d2a6508d91cdd672a3e2c761683db11b323aa71f0396c01fca669f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab0e3ec0c23ff996340c5c91310075cf5a6a9a9d32cc61d5430433216075f26a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f98407e1af4e5e8d23dfbc2fbf565ff4f56d495f491837728032e308096aea65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings",
    jsii_struct_bases=[],
    name_mapping={"amazon_bedrock_role_arn": "amazonBedrockRoleArn"},
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings:
    def __init__(
        self,
        *,
        amazon_bedrock_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amazon_bedrock_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#amazon_bedrock_role_arn SagemakerDomain#amazon_bedrock_role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e8b17c93261d812bd8929c408c157796a5f9c5a792832bd121ee0f1b2901e7d)
            check_type(argname="argument amazon_bedrock_role_arn", value=amazon_bedrock_role_arn, expected_type=type_hints["amazon_bedrock_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amazon_bedrock_role_arn is not None:
            self._values["amazon_bedrock_role_arn"] = amazon_bedrock_role_arn

    @builtins.property
    def amazon_bedrock_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#amazon_bedrock_role_arn SagemakerDomain#amazon_bedrock_role_arn}.'''
        result = self._values.get("amazon_bedrock_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57bc2595a47a2aa79acb689da2c648638cf59c1cace7e226f53d31bd4c7eee6d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAmazonBedrockRoleArn")
    def reset_amazon_bedrock_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmazonBedrockRoleArn", []))

    @builtins.property
    @jsii.member(jsii_name="amazonBedrockRoleArnInput")
    def amazon_bedrock_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amazonBedrockRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="amazonBedrockRoleArn")
    def amazon_bedrock_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amazonBedrockRoleArn"))

    @amazon_bedrock_role_arn.setter
    def amazon_bedrock_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5535603f782a709fea13bb4dc5293d66b1cddbbe297e102800c7afd30b4c87b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonBedrockRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cf444632b42c4fc90cf7eab821a61d17203dc2d66f69ef2c16b9a9439592991)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings",
    jsii_struct_bases=[],
    name_mapping={
        "secret_arn": "secretArn",
        "data_source_name": "dataSourceName",
        "status": "status",
    },
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings:
    def __init__(
        self,
        *,
        secret_arn: builtins.str,
        data_source_name: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#secret_arn SagemakerDomain#secret_arn}.
        :param data_source_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#data_source_name SagemakerDomain#data_source_name}.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__345a04f420ca45dd51435f7020612229c10ecd7b71934540ca68c84fb865118c)
            check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            check_type(argname="argument data_source_name", value=data_source_name, expected_type=type_hints["data_source_name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "secret_arn": secret_arn,
        }
        if data_source_name is not None:
            self._values["data_source_name"] = data_source_name
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def secret_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#secret_arn SagemakerDomain#secret_arn}.'''
        result = self._values.get("secret_arn")
        assert result is not None, "Required property 'secret_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_source_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#data_source_name SagemakerDomain#data_source_name}.'''
        result = self._values.get("data_source_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69cc747fbf67645e32b1971499bb6073cad1955a34b1618c3150e395a75f87b7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7510efac05f19d62f4b3da82ec52f59cdcbcfb91989a651b83ae44950a86ecf)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__497340397d0357765dd9b809647a09e2cc4dfb94ebcb4d223942b7f07f378ce7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d01b121d82c8db331ea67cfc91c78aba9a7280f1db71fcd68ba726f901b031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b037f848a4008b1b7957a2cf06ae3de4f224ce72bd5e5ae1eda53a95d43c8ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09e36f90def99102856cf5747d5381bd7b2967989e7423b9b836a203b9abc684)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37bfbab9834e3134377f0043e5326a00bc8a4a4aa98f30eed15280ab4ba6429f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDataSourceName")
    def reset_data_source_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataSourceName", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="dataSourceNameInput")
    def data_source_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataSourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretArnInput")
    def secret_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretArnInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="dataSourceName")
    def data_source_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataSourceName"))

    @data_source_name.setter
    def data_source_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddae419aae762c8b0db6cf48ee0c1b9fa2c8027846376b7adb664a150a3c8e10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataSourceName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="secretArn")
    def secret_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretArn"))

    @secret_arn.setter
    def secret_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59b6457ff17dc410e63eefc27f7cfac399186bb6d4abc672ce037ee6d4c219b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__560692b9020fecb2ed047a9b12acab19eb69905f697349c204c88be63f2d04f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__756eb4094e955a2513336736bba012bb45a7075181ea40771fddc2f1b193a899)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings",
    jsii_struct_bases=[],
    name_mapping={"status": "status"},
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings:
    def __init__(self, *, status: typing.Optional[builtins.str] = None) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de7fbd340c3001e203d31b5c9db7d28127ff83d7ed1eb5fe1cf23e31131ecc29)
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b760987680e6f4e3b56c5d464e3face5624fcf1e6801c99a08d14dca749b5da)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26143a41d93c41ad15fd41117cbd5c049e11c10c994fd4eadf9da39f7fcf08ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__254abb492fca1fe2f7f372fc7bcf5be2698ab7345a8aa92210c3a1abf9d88431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings",
    jsii_struct_bases=[],
    name_mapping={
        "cross_account_model_register_role_arn": "crossAccountModelRegisterRoleArn",
        "status": "status",
    },
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings:
    def __init__(
        self,
        *,
        cross_account_model_register_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cross_account_model_register_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#cross_account_model_register_role_arn SagemakerDomain#cross_account_model_register_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29dc19ede1e3214e365de2371ac5bbc6fa7dac50c30b3925cb51961232279832)
            check_type(argname="argument cross_account_model_register_role_arn", value=cross_account_model_register_role_arn, expected_type=type_hints["cross_account_model_register_role_arn"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if cross_account_model_register_role_arn is not None:
            self._values["cross_account_model_register_role_arn"] = cross_account_model_register_role_arn
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def cross_account_model_register_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#cross_account_model_register_role_arn SagemakerDomain#cross_account_model_register_role_arn}.'''
        result = self._values.get("cross_account_model_register_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ead584a3bee88661e7fd863a791e674a908006eb31b722d2882dce2699da075)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCrossAccountModelRegisterRoleArn")
    def reset_cross_account_model_register_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCrossAccountModelRegisterRoleArn", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="crossAccountModelRegisterRoleArnInput")
    def cross_account_model_register_role_arn_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "crossAccountModelRegisterRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="crossAccountModelRegisterRoleArn")
    def cross_account_model_register_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "crossAccountModelRegisterRoleArn"))

    @cross_account_model_register_role_arn.setter
    def cross_account_model_register_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9005731ad3001e61a45644a6997cd8eaa1c7ebd60852ef3bad4b9c6f5511db04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossAccountModelRegisterRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac51449ed2a9befdf80f563cdd1e27373db6c7dda8678400b5470e02dd14d5e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96b809baab14f61f11042fbee9150646c2eb313696c72a1c381b1f787bd63407)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d1a00611932826a10be7923cd7b54717477dd6a75d33786649af12da89712c2)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDirectDeploySettings")
    def put_direct_deploy_settings(
        self,
        *,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings(
            status=status
        )

        return typing.cast(None, jsii.invoke(self, "putDirectDeploySettings", [value]))

    @jsii.member(jsii_name="putEmrServerlessSettings")
    def put_emr_serverless_settings(
        self,
        *,
        execution_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param execution_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arn SagemakerDomain#execution_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings(
            execution_role_arn=execution_role_arn, status=status
        )

        return typing.cast(None, jsii.invoke(self, "putEmrServerlessSettings", [value]))

    @jsii.member(jsii_name="putGenerativeAiSettings")
    def put_generative_ai_settings(
        self,
        *,
        amazon_bedrock_role_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amazon_bedrock_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#amazon_bedrock_role_arn SagemakerDomain#amazon_bedrock_role_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings(
            amazon_bedrock_role_arn=amazon_bedrock_role_arn
        )

        return typing.cast(None, jsii.invoke(self, "putGenerativeAiSettings", [value]))

    @jsii.member(jsii_name="putIdentityProviderOauthSettings")
    def put_identity_provider_oauth_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dac00143b28d3aab1f49f1b1511d6d29970b9094819a83bfbed4fa1416ecf4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putIdentityProviderOauthSettings", [value]))

    @jsii.member(jsii_name="putKendraSettings")
    def put_kendra_settings(
        self,
        *,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings(
            status=status
        )

        return typing.cast(None, jsii.invoke(self, "putKendraSettings", [value]))

    @jsii.member(jsii_name="putModelRegisterSettings")
    def put_model_register_settings(
        self,
        *,
        cross_account_model_register_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cross_account_model_register_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#cross_account_model_register_role_arn SagemakerDomain#cross_account_model_register_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings(
            cross_account_model_register_role_arn=cross_account_model_register_role_arn,
            status=status,
        )

        return typing.cast(None, jsii.invoke(self, "putModelRegisterSettings", [value]))

    @jsii.member(jsii_name="putTimeSeriesForecastingSettings")
    def put_time_series_forecasting_settings(
        self,
        *,
        amazon_forecast_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amazon_forecast_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#amazon_forecast_role_arn SagemakerDomain#amazon_forecast_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(
            amazon_forecast_role_arn=amazon_forecast_role_arn, status=status
        )

        return typing.cast(None, jsii.invoke(self, "putTimeSeriesForecastingSettings", [value]))

    @jsii.member(jsii_name="putWorkspaceSettings")
    def put_workspace_settings(
        self,
        *,
        s3_artifact_path: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_artifact_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_artifact_path SagemakerDomain#s3_artifact_path}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings(
            s3_artifact_path=s3_artifact_path, s3_kms_key_id=s3_kms_key_id
        )

        return typing.cast(None, jsii.invoke(self, "putWorkspaceSettings", [value]))

    @jsii.member(jsii_name="resetDirectDeploySettings")
    def reset_direct_deploy_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectDeploySettings", []))

    @jsii.member(jsii_name="resetEmrServerlessSettings")
    def reset_emr_serverless_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmrServerlessSettings", []))

    @jsii.member(jsii_name="resetGenerativeAiSettings")
    def reset_generative_ai_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerativeAiSettings", []))

    @jsii.member(jsii_name="resetIdentityProviderOauthSettings")
    def reset_identity_provider_oauth_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityProviderOauthSettings", []))

    @jsii.member(jsii_name="resetKendraSettings")
    def reset_kendra_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKendraSettings", []))

    @jsii.member(jsii_name="resetModelRegisterSettings")
    def reset_model_register_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModelRegisterSettings", []))

    @jsii.member(jsii_name="resetTimeSeriesForecastingSettings")
    def reset_time_series_forecasting_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeSeriesForecastingSettings", []))

    @jsii.member(jsii_name="resetWorkspaceSettings")
    def reset_workspace_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkspaceSettings", []))

    @builtins.property
    @jsii.member(jsii_name="directDeploySettings")
    def direct_deploy_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsOutputReference, jsii.get(self, "directDeploySettings"))

    @builtins.property
    @jsii.member(jsii_name="emrServerlessSettings")
    def emr_serverless_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsOutputReference, jsii.get(self, "emrServerlessSettings"))

    @builtins.property
    @jsii.member(jsii_name="generativeAiSettings")
    def generative_ai_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsOutputReference, jsii.get(self, "generativeAiSettings"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderOauthSettings")
    def identity_provider_oauth_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsList:
        return typing.cast(SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsList, jsii.get(self, "identityProviderOauthSettings"))

    @builtins.property
    @jsii.member(jsii_name="kendraSettings")
    def kendra_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettingsOutputReference, jsii.get(self, "kendraSettings"))

    @builtins.property
    @jsii.member(jsii_name="modelRegisterSettings")
    def model_register_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsOutputReference, jsii.get(self, "modelRegisterSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeSeriesForecastingSettings")
    def time_series_forecasting_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference", jsii.get(self, "timeSeriesForecastingSettings"))

    @builtins.property
    @jsii.member(jsii_name="workspaceSettings")
    def workspace_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsOutputReference", jsii.get(self, "workspaceSettings"))

    @builtins.property
    @jsii.member(jsii_name="directDeploySettingsInput")
    def direct_deploy_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings], jsii.get(self, "directDeploySettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="emrServerlessSettingsInput")
    def emr_serverless_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings], jsii.get(self, "emrServerlessSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="generativeAiSettingsInput")
    def generative_ai_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings], jsii.get(self, "generativeAiSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderOauthSettingsInput")
    def identity_provider_oauth_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]]], jsii.get(self, "identityProviderOauthSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kendraSettingsInput")
    def kendra_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings], jsii.get(self, "kendraSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="modelRegisterSettingsInput")
    def model_register_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings], jsii.get(self, "modelRegisterSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeSeriesForecastingSettingsInput")
    def time_series_forecasting_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings"], jsii.get(self, "timeSeriesForecastingSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="workspaceSettingsInput")
    def workspace_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings"], jsii.get(self, "workspaceSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc424aa328649e3e07a2ceaf41a05c9ee924e02d55f0df645888da8feddd7c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings",
    jsii_struct_bases=[],
    name_mapping={
        "amazon_forecast_role_arn": "amazonForecastRoleArn",
        "status": "status",
    },
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings:
    def __init__(
        self,
        *,
        amazon_forecast_role_arn: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param amazon_forecast_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#amazon_forecast_role_arn SagemakerDomain#amazon_forecast_role_arn}.
        :param status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3fe434b6b523c6594fe81696f5b991138396fc0fbb2b0cd9ebce4268b22348e)
            check_type(argname="argument amazon_forecast_role_arn", value=amazon_forecast_role_arn, expected_type=type_hints["amazon_forecast_role_arn"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if amazon_forecast_role_arn is not None:
            self._values["amazon_forecast_role_arn"] = amazon_forecast_role_arn
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def amazon_forecast_role_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#amazon_forecast_role_arn SagemakerDomain#amazon_forecast_role_arn}.'''
        result = self._values.get("amazon_forecast_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#status SagemakerDomain#status}.'''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8785365329a3901a4e83e39db5f7881873cf74d3f6a93a99a3b6fd561e399394)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAmazonForecastRoleArn")
    def reset_amazon_forecast_role_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAmazonForecastRoleArn", []))

    @jsii.member(jsii_name="resetStatus")
    def reset_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatus", []))

    @builtins.property
    @jsii.member(jsii_name="amazonForecastRoleArnInput")
    def amazon_forecast_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "amazonForecastRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="amazonForecastRoleArn")
    def amazon_forecast_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "amazonForecastRoleArn"))

    @amazon_forecast_role_arn.setter
    def amazon_forecast_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf4b9c61e22b74b4f4957152e45f1ec2d69247f08e7fc32e1f3a2433111212a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "amazonForecastRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa11e7da48d6cea4439133902a85d37feb54f579794dbb15a23889fe73a6ca16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__440b9a53353debf15db39bd473678a82cc251fb598dd12c1a9af2646bf309ba7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings",
    jsii_struct_bases=[],
    name_mapping={"s3_artifact_path": "s3ArtifactPath", "s3_kms_key_id": "s3KmsKeyId"},
)
class SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings:
    def __init__(
        self,
        *,
        s3_artifact_path: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param s3_artifact_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_artifact_path SagemakerDomain#s3_artifact_path}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__718365e39a31f0e791cda0850a95d7420c411016309de3a2ebbc248291d52a13)
            check_type(argname="argument s3_artifact_path", value=s3_artifact_path, expected_type=type_hints["s3_artifact_path"])
            check_type(argname="argument s3_kms_key_id", value=s3_kms_key_id, expected_type=type_hints["s3_kms_key_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if s3_artifact_path is not None:
            self._values["s3_artifact_path"] = s3_artifact_path
        if s3_kms_key_id is not None:
            self._values["s3_kms_key_id"] = s3_kms_key_id

    @builtins.property
    def s3_artifact_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_artifact_path SagemakerDomain#s3_artifact_path}.'''
        result = self._values.get("s3_artifact_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.'''
        result = self._values.get("s3_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f01af8dada41e3e96f0d327412032343ab4dfa43aeb49a2e36c145865dc38047)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetS3ArtifactPath")
    def reset_s3_artifact_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3ArtifactPath", []))

    @jsii.member(jsii_name="resetS3KmsKeyId")
    def reset_s3_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KmsKeyId", []))

    @builtins.property
    @jsii.member(jsii_name="s3ArtifactPathInput")
    def s3_artifact_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3ArtifactPathInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyIdInput")
    def s3_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3ArtifactPath")
    def s3_artifact_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3ArtifactPath"))

    @s3_artifact_path.setter
    def s3_artifact_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5e2068431661f5d5be9a51df0efe295a873ee02b5d349ed4d1112e15b5cc3a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3ArtifactPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyId")
    def s3_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KmsKeyId"))

    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00a748cc1d5a90594c32b6a2101dcbd6bad4ff2452a8c4a357858f99f35c4cee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74bf76376ade139f14b8f75153c1b941f519f5ef7d16fe91bcff8d657a7c743c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "app_lifecycle_management": "appLifecycleManagement",
        "built_in_lifecycle_config_arn": "builtInLifecycleConfigArn",
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultUserSettingsCodeEditorAppSettings:
    def __init__(
        self,
        *,
        app_lifecycle_management: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement", typing.Dict[builtins.str, typing.Any]]] = None,
        built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_lifecycle_management: app_lifecycle_management block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        :param built_in_lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(app_lifecycle_management, dict):
            app_lifecycle_management = SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement(**app_lifecycle_management)
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f045f1aa18429b3aca2d473eca7ebe46fed1cb27cfc241b9eb9442365845180)
            check_type(argname="argument app_lifecycle_management", value=app_lifecycle_management, expected_type=type_hints["app_lifecycle_management"])
            check_type(argname="argument built_in_lifecycle_config_arn", value=built_in_lifecycle_config_arn, expected_type=type_hints["built_in_lifecycle_config_arn"])
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if app_lifecycle_management is not None:
            self._values["app_lifecycle_management"] = app_lifecycle_management
        if built_in_lifecycle_config_arn is not None:
            self._values["built_in_lifecycle_config_arn"] = built_in_lifecycle_config_arn
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def app_lifecycle_management(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement"]:
        '''app_lifecycle_management block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        '''
        result = self._values.get("app_lifecycle_management")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement"], result)

    @builtins.property
    def built_in_lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.'''
        result = self._values.get("built_in_lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCodeEditorAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement",
    jsii_struct_bases=[],
    name_mapping={"idle_settings": "idleSettings"},
)
class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement:
    def __init__(
        self,
        *,
        idle_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_settings: idle_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        if isinstance(idle_settings, dict):
            idle_settings = SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings(**idle_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__455473726a7be0cbb8540fbe73946fb99cd4933b8ae9a342fdb73c9fd8b88ccc)
            check_type(argname="argument idle_settings", value=idle_settings, expected_type=type_hints["idle_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_settings is not None:
            self._values["idle_settings"] = idle_settings

    @builtins.property
    def idle_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings"]:
        '''idle_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        result = self._values.get("idle_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings",
    jsii_struct_bases=[],
    name_mapping={
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "lifecycle_management": "lifecycleManagement",
        "max_idle_timeout_in_minutes": "maxIdleTimeoutInMinutes",
        "min_idle_timeout_in_minutes": "minIdleTimeoutInMinutes",
    },
)
class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings:
    def __init__(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        lifecycle_management: typing.Optional[builtins.str] = None,
        max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.
        :param lifecycle_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.
        :param max_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.
        :param min_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ef8e395ed19be6bccad7304554562dc124e97f222b702ec5fb22da0d1763248)
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
            check_type(argname="argument lifecycle_management", value=lifecycle_management, expected_type=type_hints["lifecycle_management"])
            check_type(argname="argument max_idle_timeout_in_minutes", value=max_idle_timeout_in_minutes, expected_type=type_hints["max_idle_timeout_in_minutes"])
            check_type(argname="argument min_idle_timeout_in_minutes", value=min_idle_timeout_in_minutes, expected_type=type_hints["min_idle_timeout_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        if lifecycle_management is not None:
            self._values["lifecycle_management"] = lifecycle_management
        if max_idle_timeout_in_minutes is not None:
            self._values["max_idle_timeout_in_minutes"] = max_idle_timeout_in_minutes
        if min_idle_timeout_in_minutes is not None:
            self._values["min_idle_timeout_in_minutes"] = min_idle_timeout_in_minutes

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lifecycle_management(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.'''
        result = self._values.get("lifecycle_management")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.'''
        result = self._values.get("max_idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.'''
        result = self._values.get("min_idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47eace57243a4ac86795ff57fb0aa86040ad16a6aa4a317fe5de66ee8a5640cf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetLifecycleManagement")
    def reset_lifecycle_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleManagement", []))

    @jsii.member(jsii_name="resetMaxIdleTimeoutInMinutes")
    def reset_max_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetMinIdleTimeoutInMinutes")
    def reset_min_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinIdleTimeoutInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutesInput")
    def idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleManagementInput")
    def lifecycle_management_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleTimeoutInMinutesInput")
    def max_idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="minIdleTimeoutInMinutesInput")
    def min_idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minIdleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd3e70e1ac8333195885ae50c4ae2dd6ad5d51df3773ef847a31ddf31e0abbb7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleManagement")
    def lifecycle_management(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleManagement"))

    @lifecycle_management.setter
    def lifecycle_management(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89947bdf8323558a316343f17c89b30975cf1370bb50e1f7d6d210517b02dd1c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleManagement", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleTimeoutInMinutes"))

    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f165fb9ae8b477327f29cb124ab886002b152d8473e18359a954ab21213e61e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minIdleTimeoutInMinutes"))

    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__012fed8790fe8d7f82be038d52a1587b9b920e78f57dd89d5032a0d894319b8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minIdleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__362772f29d83c875e12359c1a907d41888f7e91917150521285bfdc4808824b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f37a5be7587dabe2afc474e1234790d90e21062cc3b0ad13c5f7635f149b14c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdleSettings")
    def put_idle_settings(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        lifecycle_management: typing.Optional[builtins.str] = None,
        max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.
        :param lifecycle_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.
        :param max_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.
        :param min_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.
        '''
        value = SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings(
            idle_timeout_in_minutes=idle_timeout_in_minutes,
            lifecycle_management=lifecycle_management,
            max_idle_timeout_in_minutes=max_idle_timeout_in_minutes,
            min_idle_timeout_in_minutes=min_idle_timeout_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putIdleSettings", [value]))

    @jsii.member(jsii_name="resetIdleSettings")
    def reset_idle_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleSettings", []))

    @builtins.property
    @jsii.member(jsii_name="idleSettings")
    def idle_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsOutputReference, jsii.get(self, "idleSettings"))

    @builtins.property
    @jsii.member(jsii_name="idleSettingsInput")
    def idle_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings], jsii.get(self, "idleSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1eef3d25929a1510016d0fc29695ae367886bdf17de247c0c3ad41cebbb8d4ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa68764766f52bf75745999485706a17141b2a531757f4f5febc30b4083c5e15)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97634cc73f7afd8ef2e693a144aef2ccca9b9e2ee6516f86ebae2aa7c477238d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d34f70ed27e7a4e23b88284a46acf5b6605fec16c85ac206a8cdbdd42fb60be)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f90231e7040a5caec7cf1820f64c4247967ba071a73b3aa491daecdf4e1f8ee9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__625b628429d02751a097ea58103041e45ad83eb4e322d0d9a953e7c2b5546565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78d2a36a02e45622437917f1aadba44ee0e2b6d24acc51a2c68804d651ded09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3eff2aa777c127e42280ab601ab5ce00ffb5ff8ee21e1ce29900aa45c128fd2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36f27c594c4ca76591abc9f39a56752abcd90a35f96b0c67d1d73bad01889fdb)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__419a7b7fc769f6a4c53b53c62064fb2fb969b700940612867f281229dca71815)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b0e1058a31b978ff13d90773af528913cc41433bdea8a7ca989d7dcc40a45d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63a1a1cbfac5d16a4c75939dc6e6c2b938f7c6b7d2ea49fb60fd89f3612e30b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f5de024d20ea6ae6fbfe19fdd233dd353c1feadc1c49527578a227bf8d33cf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17a79c94351c8b0edf8ca0a2c991eec71c170af7fe9cad5778e0b7c1f84a2e13)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0853b9092d43032aa8dc677c92caacbdcc1c8d75911fee941f0c2a6d432cd77)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cd9bfba41c4c9e62bec14249cc8e0333583c40902fa7b057aa7824368266bad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00db2b924fd2d5d39f9ab1c698bf3ff679b31d45aa9321f7a087f1bb855862d4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3306a758d88ce61feeef6794c9226f1c0a3a53779feb523621384cafac242bd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a2fbbac8b45330bd4aad1c1a8fa675e0dcb9c212e6b569efc388ddc0c1649fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ce79996f13457b20fd79f36a5ee99ace09657f5c90960ba922426504c1d7da3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5eaf06c378f86c3c5f965ce86561a65329cd6e3e9be592a71f8d709c1616ca5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b4edcadf6988c03541327ee99ef03b5f511381ded284e83e9cd4c3f9607eb98)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAppLifecycleManagement")
    def put_app_lifecycle_management(
        self,
        *,
        idle_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_settings: idle_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        value = SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement(
            idle_settings=idle_settings
        )

        return typing.cast(None, jsii.invoke(self, "putAppLifecycleManagement", [value]))

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a33c86a64cda270b09589b5d793e30a1df8bad754a71fe5cf2fa61fe6efe6a3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetAppLifecycleManagement")
    def reset_app_lifecycle_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppLifecycleManagement", []))

    @jsii.member(jsii_name="resetBuiltInLifecycleConfigArn")
    def reset_built_in_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuiltInLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementOutputReference, jsii.get(self, "appLifecycleManagement"))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageList:
        return typing.cast(SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="appLifecycleManagementInput")
    def app_lifecycle_management_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement], jsii.get(self, "appLifecycleManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="builtInLifecycleConfigArnInput")
    def built_in_lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "builtInLifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "builtInLifecycleConfigArn"))

    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff8c4e726b8293b7439363df6b03ea1905f73b4f59a734c7142d6aad201dd7f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "builtInLifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89d7c72b9af4981231dd96e913ae7e6890fd4853b36bf645ca60a07829f0415f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5933a3a6433328b17c8bb90d745334c3c02c6d9a1784f4411e80a84e49d63d67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCustomFileSystemConfig",
    jsii_struct_bases=[],
    name_mapping={"efs_file_system_config": "efsFileSystemConfig"},
)
class SagemakerDomainDefaultUserSettingsCustomFileSystemConfig:
    def __init__(
        self,
        *,
        efs_file_system_config: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param efs_file_system_config: efs_file_system_config block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#efs_file_system_config SagemakerDomain#efs_file_system_config}
        '''
        if isinstance(efs_file_system_config, dict):
            efs_file_system_config = SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig(**efs_file_system_config)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95c0ef8a682bca3e91062c572071a36b4af1b49c1f46974969d26472cc3dcbec)
            check_type(argname="argument efs_file_system_config", value=efs_file_system_config, expected_type=type_hints["efs_file_system_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if efs_file_system_config is not None:
            self._values["efs_file_system_config"] = efs_file_system_config

    @builtins.property
    def efs_file_system_config(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig"]:
        '''efs_file_system_config block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#efs_file_system_config SagemakerDomain#efs_file_system_config}
        '''
        result = self._values.get("efs_file_system_config")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCustomFileSystemConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig",
    jsii_struct_bases=[],
    name_mapping={
        "file_system_id": "fileSystemId",
        "file_system_path": "fileSystemPath",
    },
)
class SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig:
    def __init__(
        self,
        *,
        file_system_id: builtins.str,
        file_system_path: builtins.str,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_id SagemakerDomain#file_system_id}.
        :param file_system_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_path SagemakerDomain#file_system_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c600cbab23634e21c38f4bbea3dd4853a0bf9e8e190d8a66ee9306a8b6cec94b)
            check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
            check_type(argname="argument file_system_path", value=file_system_path, expected_type=type_hints["file_system_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "file_system_id": file_system_id,
            "file_system_path": file_system_path,
        }

    @builtins.property
    def file_system_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_id SagemakerDomain#file_system_id}.'''
        result = self._values.get("file_system_id")
        assert result is not None, "Required property 'file_system_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def file_system_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_path SagemakerDomain#file_system_path}.'''
        result = self._values.get("file_system_path")
        assert result is not None, "Required property 'file_system_path' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8c2a94b1d65b3fa090ca483b538aa13a29bf51ff2123cfa821dd19c3ddbf692)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="fileSystemIdInput")
    def file_system_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemPathInput")
    def file_system_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileSystemPathInput"))

    @builtins.property
    @jsii.member(jsii_name="fileSystemId")
    def file_system_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemId"))

    @file_system_id.setter
    def file_system_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dce20950a05ca382329933f167a4c77912a87fea56af61d149f1708e8dd7cf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="fileSystemPath")
    def file_system_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileSystemPath"))

    @file_system_path.setter
    def file_system_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bd45546bbbeb154305daa13fef5b6ff0c40b14b8010ab5cf219c2876b1bd2fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__479ebaf6fbb33820c90d306f7ebc864edc0586ff2c7b150d5c448cdd86d68c80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsCustomFileSystemConfigList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCustomFileSystemConfigList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06df435e7e048bc650c1fbdfa2e80b330c1a33480b806887d425f60fa090715b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsCustomFileSystemConfigOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65d306ff2ac4ccb3fc6c900d55737656ff7553a0af1a00e639772b1c01fa91bc)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsCustomFileSystemConfigOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe3bf7b9207cd8c3d8ce4e512ff047a485364903fae4c4a2a06ae84c1b00240)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca29aad4591761237e66883043fc56f8826b5057f087eb56f90d6a78a55132b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35f349e95e1649b8704815cbdd980c74cb04033ff688ebe20f96f39793ba026e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be93d4cd47442a92c35bc3b9a4f08374224e4265cc98a17476d26248d972671f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsCustomFileSystemConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCustomFileSystemConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd498b283e1b95a98ea8e56924007acb40b499694b989d6fcc956c467b43080a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putEfsFileSystemConfig")
    def put_efs_file_system_config(
        self,
        *,
        file_system_id: builtins.str,
        file_system_path: builtins.str,
    ) -> None:
        '''
        :param file_system_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_id SagemakerDomain#file_system_id}.
        :param file_system_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#file_system_path SagemakerDomain#file_system_path}.
        '''
        value = SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig(
            file_system_id=file_system_id, file_system_path=file_system_path
        )

        return typing.cast(None, jsii.invoke(self, "putEfsFileSystemConfig", [value]))

    @jsii.member(jsii_name="resetEfsFileSystemConfig")
    def reset_efs_file_system_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEfsFileSystemConfig", []))

    @builtins.property
    @jsii.member(jsii_name="efsFileSystemConfig")
    def efs_file_system_config(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference, jsii.get(self, "efsFileSystemConfig"))

    @builtins.property
    @jsii.member(jsii_name="efsFileSystemConfigInput")
    def efs_file_system_config_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig], jsii.get(self, "efsFileSystemConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2f2a142c712fa27a8244446c7295cc4348415cecfcfc4404b6dc89cc2217d01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCustomPosixUserConfig",
    jsii_struct_bases=[],
    name_mapping={"gid": "gid", "uid": "uid"},
)
class SagemakerDomainDefaultUserSettingsCustomPosixUserConfig:
    def __init__(self, *, gid: jsii.Number, uid: jsii.Number) -> None:
        '''
        :param gid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#gid SagemakerDomain#gid}.
        :param uid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#uid SagemakerDomain#uid}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25df54619d51635ef2b9b5d67c78c1654b7857b621317f8fddc2c8ba368c9ad5)
            check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "gid": gid,
            "uid": uid,
        }

    @builtins.property
    def gid(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#gid SagemakerDomain#gid}.'''
        result = self._values.get("gid")
        assert result is not None, "Required property 'gid' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def uid(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#uid SagemakerDomain#uid}.'''
        result = self._values.get("uid")
        assert result is not None, "Required property 'uid' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsCustomPosixUserConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsCustomPosixUserConfigOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsCustomPosixUserConfigOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5900eeb8b2a46b21af00e0afeae2117f21ca28a0246403c58190c92d8a9bf132)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="gidInput")
    def gid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gidInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="gid")
    def gid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gid"))

    @gid.setter
    def gid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff3a6f385817ddc4597656570ddd1aa1748e042dc8a417fcf291c9c1e0923d5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a02b1bf5e141f360c327be30f3a8806f2dec2021b6b382792bf649e59b2d7208)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCustomPosixUserConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCustomPosixUserConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsCustomPosixUserConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c42382e815d2039497bab8919558ef0e41e8b03536d050b9ac5971861502b88e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "app_lifecycle_management": "appLifecycleManagement",
        "built_in_lifecycle_config_arn": "builtInLifecycleConfigArn",
        "code_repository": "codeRepository",
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
        "emr_settings": "emrSettings",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterLabAppSettings:
    def __init__(
        self,
        *,
        app_lifecycle_management: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement", typing.Dict[builtins.str, typing.Any]]] = None,
        built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository", typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        emr_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_lifecycle_management: app_lifecycle_management block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        :param built_in_lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param emr_settings: emr_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_settings SagemakerDomain#emr_settings}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(app_lifecycle_management, dict):
            app_lifecycle_management = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement(**app_lifecycle_management)
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec(**default_resource_spec)
        if isinstance(emr_settings, dict):
            emr_settings = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings(**emr_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a99a5eba778f2a834421178883d1e5f0336b16396708bed7516c3bba58395c88)
            check_type(argname="argument app_lifecycle_management", value=app_lifecycle_management, expected_type=type_hints["app_lifecycle_management"])
            check_type(argname="argument built_in_lifecycle_config_arn", value=built_in_lifecycle_config_arn, expected_type=type_hints["built_in_lifecycle_config_arn"])
            check_type(argname="argument code_repository", value=code_repository, expected_type=type_hints["code_repository"])
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument emr_settings", value=emr_settings, expected_type=type_hints["emr_settings"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if app_lifecycle_management is not None:
            self._values["app_lifecycle_management"] = app_lifecycle_management
        if built_in_lifecycle_config_arn is not None:
            self._values["built_in_lifecycle_config_arn"] = built_in_lifecycle_config_arn
        if code_repository is not None:
            self._values["code_repository"] = code_repository
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if emr_settings is not None:
            self._values["emr_settings"] = emr_settings
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def app_lifecycle_management(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement"]:
        '''app_lifecycle_management block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        '''
        result = self._values.get("app_lifecycle_management")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement"], result)

    @builtins.property
    def built_in_lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.'''
        result = self._values.get("built_in_lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_repository(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository"]]]:
        '''code_repository block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        '''
        result = self._values.get("code_repository")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository"]]], result)

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def emr_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings"]:
        '''emr_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_settings SagemakerDomain#emr_settings}
        '''
        result = self._values.get("emr_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterLabAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement",
    jsii_struct_bases=[],
    name_mapping={"idle_settings": "idleSettings"},
)
class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement:
    def __init__(
        self,
        *,
        idle_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_settings: idle_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        if isinstance(idle_settings, dict):
            idle_settings = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(**idle_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c89d00afcb07402713dbb71a02780926ed1556c71d3443e4587b5fb2cd3712c)
            check_type(argname="argument idle_settings", value=idle_settings, expected_type=type_hints["idle_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_settings is not None:
            self._values["idle_settings"] = idle_settings

    @builtins.property
    def idle_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings"]:
        '''idle_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        result = self._values.get("idle_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings",
    jsii_struct_bases=[],
    name_mapping={
        "idle_timeout_in_minutes": "idleTimeoutInMinutes",
        "lifecycle_management": "lifecycleManagement",
        "max_idle_timeout_in_minutes": "maxIdleTimeoutInMinutes",
        "min_idle_timeout_in_minutes": "minIdleTimeoutInMinutes",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings:
    def __init__(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        lifecycle_management: typing.Optional[builtins.str] = None,
        max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.
        :param lifecycle_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.
        :param max_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.
        :param min_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a84f3f55d172118ed3b8d33ef3e62862b1f110e7792016262b93d92c69ab046)
            check_type(argname="argument idle_timeout_in_minutes", value=idle_timeout_in_minutes, expected_type=type_hints["idle_timeout_in_minutes"])
            check_type(argname="argument lifecycle_management", value=lifecycle_management, expected_type=type_hints["lifecycle_management"])
            check_type(argname="argument max_idle_timeout_in_minutes", value=max_idle_timeout_in_minutes, expected_type=type_hints["max_idle_timeout_in_minutes"])
            check_type(argname="argument min_idle_timeout_in_minutes", value=min_idle_timeout_in_minutes, expected_type=type_hints["min_idle_timeout_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if idle_timeout_in_minutes is not None:
            self._values["idle_timeout_in_minutes"] = idle_timeout_in_minutes
        if lifecycle_management is not None:
            self._values["lifecycle_management"] = lifecycle_management
        if max_idle_timeout_in_minutes is not None:
            self._values["max_idle_timeout_in_minutes"] = max_idle_timeout_in_minutes
        if min_idle_timeout_in_minutes is not None:
            self._values["min_idle_timeout_in_minutes"] = min_idle_timeout_in_minutes

    @builtins.property
    def idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.'''
        result = self._values.get("idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lifecycle_management(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.'''
        result = self._values.get("lifecycle_management")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.'''
        result = self._values.get("max_idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_idle_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.'''
        result = self._values.get("min_idle_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2c13da4a3a5fc2c2645e949a245ade3fc000578bc0477b1996d49b0087923ee)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIdleTimeoutInMinutes")
    def reset_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetLifecycleManagement")
    def reset_lifecycle_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleManagement", []))

    @jsii.member(jsii_name="resetMaxIdleTimeoutInMinutes")
    def reset_max_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxIdleTimeoutInMinutes", []))

    @jsii.member(jsii_name="resetMinIdleTimeoutInMinutes")
    def reset_min_idle_timeout_in_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinIdleTimeoutInMinutes", []))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutesInput")
    def idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleManagementInput")
    def lifecycle_management_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="maxIdleTimeoutInMinutesInput")
    def max_idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxIdleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="minIdleTimeoutInMinutesInput")
    def min_idle_timeout_in_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minIdleTimeoutInMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "idleTimeoutInMinutes"))

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__618938f2ab6a86c1e1f8fef0cf96fcf8a4abc68564e939b5250ae1af7e51bcbd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleManagement")
    def lifecycle_management(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleManagement"))

    @lifecycle_management.setter
    def lifecycle_management(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dceb096b3314bf482eacbd72e4c01412a41f1c7302e55f3c50437e72b1236762)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleManagement", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maxIdleTimeoutInMinutes")
    def max_idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxIdleTimeoutInMinutes"))

    @max_idle_timeout_in_minutes.setter
    def max_idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6f8fa08081e6b1d613228970633027bacfd9e4920db0bfa44e669cadd8a8a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxIdleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="minIdleTimeoutInMinutes")
    def min_idle_timeout_in_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minIdleTimeoutInMinutes"))

    @min_idle_timeout_in_minutes.setter
    def min_idle_timeout_in_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a2ff581882c67c8154190c9edc0928c8e978df0f4d5c74a8c250c5a2d5ce46f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minIdleTimeoutInMinutes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b578e3bd91b805fd74eec0b5ac9c5370cef3abc7fb070e024837ce5fb6c1bf5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed3d01f350347dec180d1a15d9be20460e9e24464a6d6edb1c8980cfb1fbbcd)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putIdleSettings")
    def put_idle_settings(
        self,
        *,
        idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        lifecycle_management: typing.Optional[builtins.str] = None,
        max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_timeout_in_minutes SagemakerDomain#idle_timeout_in_minutes}.
        :param lifecycle_management: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_management SagemakerDomain#lifecycle_management}.
        :param max_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#max_idle_timeout_in_minutes SagemakerDomain#max_idle_timeout_in_minutes}.
        :param min_idle_timeout_in_minutes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#min_idle_timeout_in_minutes SagemakerDomain#min_idle_timeout_in_minutes}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings(
            idle_timeout_in_minutes=idle_timeout_in_minutes,
            lifecycle_management=lifecycle_management,
            max_idle_timeout_in_minutes=max_idle_timeout_in_minutes,
            min_idle_timeout_in_minutes=min_idle_timeout_in_minutes,
        )

        return typing.cast(None, jsii.invoke(self, "putIdleSettings", [value]))

    @jsii.member(jsii_name="resetIdleSettings")
    def reset_idle_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdleSettings", []))

    @builtins.property
    @jsii.member(jsii_name="idleSettings")
    def idle_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference, jsii.get(self, "idleSettings"))

    @builtins.property
    @jsii.member(jsii_name="idleSettingsInput")
    def idle_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings], jsii.get(self, "idleSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a18e71f001bf61b91a13f586d10708f9bf9d2effa344aac9161a7c5b48d3eb27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository",
    jsii_struct_bases=[],
    name_mapping={"repository_url": "repositoryUrl"},
)
class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository:
    def __init__(self, *, repository_url: builtins.str) -> None:
        '''
        :param repository_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082012904e51873cb6e2b1660533cf0b98add24b443afa87c2cc4075a8754b8a)
            check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_url": repository_url,
        }

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.'''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3950df25dbcd249436d8ec88537e53f8ef8eaa942a12f86bd65251d7c4a74c52)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__deb50972ad14a05db448dbe65b28f428d236189dc598cc63aacd795590ad1ebd)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5573606be8469b6bbbea91282d62e54c08deb5e2bf7a089d6ded34b6ed8391d6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00159e2c0f6b087e063bfafc7056077ff9474107d75efb3996f3f88f25f37816)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__55447606a35ea6e173a4dcc048de44582ec589ee877b7b6268f83d63996103f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1ea44865713d585997ffe3f0bc26d5a83f5855ef53697e88426ebdcc66a7755)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b29dcf66ae582ca04e1bfe656369efbd2649ca5dbc1c145ef41a035c3482dec7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="repositoryUrlInput")
    def repository_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))

    @repository_url.setter
    def repository_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d2db9f312815c69ea16aa7c11bf4c237da5c2835c5429c2396be00279a02d97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da5c6be67404944b458bd191a36ce81608b01facd78af24f41df0e85abe117b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66b3e2ab27db2eb0157d8f02e1766a363119d026d0218d774bd90c9846d0a18e)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fde686806b6d91ad61ac2940ff6b7f863536538ffdc16944972f9fbb5175d29)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dee072c7e91f7fe7b5a38c6a0a8c8df1ffd6e59ae40acdd7fec394e43cc12e8d)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ca271ce3e06873f2b05c136944cb66de0de5d923a7c9757c235d226c9a69bc2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f96271ca2a89e6ebd1291dbe34c8777e1800e7b41b055ae1a15f0aee17a03670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9da61823c9e9102d6e5432565840aec6404b132b3d4e8424822108d89e46968c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b2dcf36edd7bfe30d2a8e13fd169dab1dfe092355a93d6673a18e277fd5052a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd7bdd188053274b65792a37eee58c7f8691c641861e653783144b1e23b53ec7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04df0d629ccdb101b7ff5032705b9ccfe690fde80ead8d75f5745441cbba6466)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d30dbd3465426d516520c17d99e0f6b23e7aa16d60248fd7100bdc52c8d97363)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a4f4c81463e27e19371aa67e34c8a80febdbed037f52ce5a3e80149b53ed2e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda1f1ef33d2f883179751bbbaf34f70b2178df7e16e86dc921d52fcbd4ae15e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bfd73f44a0af57a3455e87acebb44e17baee4dec341c5235beae4646652acde)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60ea2cd4faa14099cc14d148aa4d96d3bf136f37ad56f6e1724ce9a09ff2e55c)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ffa8f7fe9d37221bd460e59fbec479651dd539070febc00a3a1059a1f134c8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b08712bd44c5392a3e1f2fcad8fb06fe5fcf1ae4b6ab7f280ffa4eceb56bf47c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__895292a9bdc21a9a47a993a2a72b508e2c7a03fdb87d37df2057b4f4ffe25d69)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ece5484d37f88cc0d07e8f002c6fb118683978c0598839c27ce82adb48c491af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45148c577319edd334ab59a731853b54fae3aa7a39e9b2f0f56a60bf802afa6b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d30eabce76bb128fb8d1b9e86774a1b19a5c7bf711d59bd723c057b9cc4619e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings",
    jsii_struct_bases=[],
    name_mapping={
        "assumable_role_arns": "assumableRoleArns",
        "execution_role_arns": "executionRoleArns",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings:
    def __init__(
        self,
        *,
        assumable_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        execution_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param assumable_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#assumable_role_arns SagemakerDomain#assumable_role_arns}.
        :param execution_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arns SagemakerDomain#execution_role_arns}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a0854eef5e5bfd1a2df83021d701fe6f3bdc4d9834f4c8256f39da8efea89aa)
            check_type(argname="argument assumable_role_arns", value=assumable_role_arns, expected_type=type_hints["assumable_role_arns"])
            check_type(argname="argument execution_role_arns", value=execution_role_arns, expected_type=type_hints["execution_role_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if assumable_role_arns is not None:
            self._values["assumable_role_arns"] = assumable_role_arns
        if execution_role_arns is not None:
            self._values["execution_role_arns"] = execution_role_arns

    @builtins.property
    def assumable_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#assumable_role_arns SagemakerDomain#assumable_role_arns}.'''
        result = self._values.get("assumable_role_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def execution_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arns SagemakerDomain#execution_role_arns}.'''
        result = self._values.get("execution_role_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5e1800d941fd02fe589270bb913ba80834cca41b80d4f806d77b4398e16ea8e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAssumableRoleArns")
    def reset_assumable_role_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssumableRoleArns", []))

    @jsii.member(jsii_name="resetExecutionRoleArns")
    def reset_execution_role_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleArns", []))

    @builtins.property
    @jsii.member(jsii_name="assumableRoleArnsInput")
    def assumable_role_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "assumableRoleArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleArnsInput")
    def execution_role_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "executionRoleArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="assumableRoleArns")
    def assumable_role_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "assumableRoleArns"))

    @assumable_role_arns.setter
    def assumable_role_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__974af3375823ab7dcbfb030b03c6e5a1afc0b9d831227121651ea2363cb325f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assumableRoleArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRoleArns")
    def execution_role_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "executionRoleArns"))

    @execution_role_arns.setter
    def execution_role_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25cdfd1d63dbe52f77d28cd8fc0aa9bc3eeeff2cc45ce4e3b90fdb0149537b19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__500de7810df35edb024ecba3cf4bf6b557022c6b2247e77a27df703129ad834d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc795a33f4f745d2648dd69ea5cc5dff7089f3b719255d345b0c231f96e243c9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAppLifecycleManagement")
    def put_app_lifecycle_management(
        self,
        *,
        idle_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param idle_settings: idle_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#idle_settings SagemakerDomain#idle_settings}
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement(
            idle_settings=idle_settings
        )

        return typing.cast(None, jsii.invoke(self, "putAppLifecycleManagement", [value]))

    @jsii.member(jsii_name="putCodeRepository")
    def put_code_repository(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78bb1120f40359022a19272e11680eec6fa3eb33f716bc13c2ba37f202159e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCodeRepository", [value]))

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3abca97be5e2757ed6b271ed86be15a7f88434633af84ce1eff921380ab2d73f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="putEmrSettings")
    def put_emr_settings(
        self,
        *,
        assumable_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        execution_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param assumable_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#assumable_role_arns SagemakerDomain#assumable_role_arns}.
        :param execution_role_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_arns SagemakerDomain#execution_role_arns}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings(
            assumable_role_arns=assumable_role_arns,
            execution_role_arns=execution_role_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putEmrSettings", [value]))

    @jsii.member(jsii_name="resetAppLifecycleManagement")
    def reset_app_lifecycle_management(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAppLifecycleManagement", []))

    @jsii.member(jsii_name="resetBuiltInLifecycleConfigArn")
    def reset_built_in_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuiltInLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetCodeRepository")
    def reset_code_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeRepository", []))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetEmrSettings")
    def reset_emr_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmrSettings", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="appLifecycleManagement")
    def app_lifecycle_management(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference, jsii.get(self, "appLifecycleManagement"))

    @builtins.property
    @jsii.member(jsii_name="codeRepository")
    def code_repository(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryList:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryList, jsii.get(self, "codeRepository"))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageList:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="emrSettings")
    def emr_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsOutputReference, jsii.get(self, "emrSettings"))

    @builtins.property
    @jsii.member(jsii_name="appLifecycleManagementInput")
    def app_lifecycle_management_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement], jsii.get(self, "appLifecycleManagementInput"))

    @builtins.property
    @jsii.member(jsii_name="builtInLifecycleConfigArnInput")
    def built_in_lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "builtInLifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="codeRepositoryInput")
    def code_repository_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]]], jsii.get(self, "codeRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="emrSettingsInput")
    def emr_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings], jsii.get(self, "emrSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="builtInLifecycleConfigArn")
    def built_in_lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "builtInLifecycleConfigArn"))

    @built_in_lifecycle_config_arn.setter
    def built_in_lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5f0d6ed6081f278fb014ba2bb2c9d61e1f6c7d6ee339bde715dcabb49733afc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "builtInLifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__302c6131444dceb3936119a8884a93d214ecaa3f5a1d829d1d75cf73098ff6eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beeeb6d1380efc695ee88c91b3b150e1e807223e51eb45a25cee128a3ca2285b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "code_repository": "codeRepository",
        "default_resource_spec": "defaultResourceSpec",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterServerAppSettings:
    def __init__(
        self,
        *,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__817e2c97fa0ba12bf031cbdf7619416d385df4df97b7d447b1a446a88debbcc0)
            check_type(argname="argument code_repository", value=code_repository, expected_type=type_hints["code_repository"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if code_repository is not None:
            self._values["code_repository"] = code_repository
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def code_repository(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository"]]]:
        '''code_repository block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        '''
        result = self._values.get("code_repository")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterServerAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository",
    jsii_struct_bases=[],
    name_mapping={"repository_url": "repositoryUrl"},
)
class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository:
    def __init__(self, *, repository_url: builtins.str) -> None:
        '''
        :param repository_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb74670bb91adb121913daad06d7efb14a46aa43fb2dd44a2ea663da664e7180)
            check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "repository_url": repository_url,
        }

    @builtins.property
    def repository_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#repository_url SagemakerDomain#repository_url}.'''
        result = self._values.get("repository_url")
        assert result is not None, "Required property 'repository_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f004e0d2473af3aff20dfabad440d63eaaf7d80bb7e77e0058124765bb4f4cfe)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d59b481190ac279455e03fc3d65ea3165c366b33c1a383e2ee500ecfa69a5eae)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67707054b0bc7228aa532eaaecb1a2709c38ad0e5d851aae446a2226fbaa8eed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011370d08ceb5edf9a3a784c9085c76909b21102b9f24c804ecf4c7343485836)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5c20d76a226757e994003d170c25fe0d7c6f9d91c387d1666a551f85c5bef17)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c32eb9bd30cb4616c4a3c4e5ebadf996a3a0db14748c797e007dd1c4fc0072b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18771d1a266337ec8142f912c1547544c8a292f4898aabb97f5f544c3b57b91e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="repositoryUrlInput")
    def repository_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryUrl")
    def repository_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repositoryUrl"))

    @repository_url.setter
    def repository_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e033718e628cde7285db5ad0465c0626786322992a8ce5283b2ca9152685da9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68b96730f80aacf3887f6e66f48205854961775f901184e3dfb7cd5645fc973b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4570b1ffd1e2b95358d2c1696375fbcdf56797a929177261c2fff66cba39a7aa)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2923475a8a915c0644154ab30d9fed5c394f76a5bd538ddbfc2daedad1873da4)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd279439ffaff9b063acca71f9acc438a30a680319ae9488dc14fd204b06baae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a135ce64a875857f563c90cb8089c3a0b0c2d498c06a34b5d4f7df76a3ff228c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bc9a8de409bbf900293f44270d651a69813606630217657821270d0adbf4197)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aee129e2c085ca2ee1e5748ae5c9eabffed289f379d1f5ed79fcf846ff739399)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96df45b849dffb72cb0795688cd62965c25ceb98a809e134c0a262efaa5d69b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3d243b0e9fa8d746e8d0949f64dc2c1d917dddeb659fa50bab0721d30140e65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5b1be2d8c3af832eeba24663494c3c0f8c1f7aa0f6a262c6d3c383a6d5af0ec)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCodeRepository")
    def put_code_repository(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33386a28d2e118405dc296048a9b76d1d39c51ad0f0951bb71831ec12d9ec478)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCodeRepository", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCodeRepository")
    def reset_code_repository(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeRepository", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="codeRepository")
    def code_repository(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryList:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryList, jsii.get(self, "codeRepository"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="codeRepositoryInput")
    def code_repository_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]]], jsii.get(self, "codeRepositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78ce63533120cb80fe129e041b944e052d79b8fa66f54a3429bde29061aaabb5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2738a464945ad0c2878106b456f3d1c6c02bdcbad32bf4bc28628f3a024817fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
        "lifecycle_config_arns": "lifecycleConfigArns",
    },
)
class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings:
    def __init__(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6a3b7c8db8be02fa278abb574a9e0f9dbcd26e324d0da8d3203d4180a3d5668)
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument lifecycle_config_arns", value=lifecycle_config_arns, expected_type=type_hints["lifecycle_config_arns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if lifecycle_config_arns is not None:
            self._values["lifecycle_config_arns"] = lifecycle_config_arns

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec"], result)

    @builtins.property
    def lifecycle_config_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.'''
        result = self._values.get("lifecycle_config_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ff0cc30b023a7813a01851e053b50d8893d26cc0cbaf9422ded7599cf7522c3)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1d0db4e0033c9064da70bb6cd20a1e98a0ad3f4f8c22e31518ed5c9a5418694)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9f87516619b194d06ba8660dd4807e8e7d174f73a074b7a9bd4b0afc70899f3)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__766ffae5faa766dd868f7348e05541f1947a9e9129b79678c0945eee48e2b813)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__846e7a350491e3bc797bb47235ef22f89d6c8bc31c9d0777e52309077deacd3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbc3a60ed214d9b3fe94b9dba5f753e563749969b4af3ce9df81d43439ddc19b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb16e97a1819148defab0847a8ac1f81c401dbbd1d5757f00f9f01e0f766679c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1ba8ea2754d1eff60f813b433820e23805dac7e8a636a923a8f920e37b4169a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8456de51e3989c8aefd592e10db5b0704e620a67567a370958a1236a2423a08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4be6a7bfd022b9068dab153a91de2e0eeba968ff5a441f0bcf55652a02ec48d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdd6518514c76069e8c6dfcbdba9b17ad5b4d156a5b305a5ded127bd809e7a02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33dc4f06485e1b938f98433a6fa114ed98fbe6576002904dcd363eb88a860c82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74501287e7f051cfb7d7ddcca02805824b05c2d039e0b6e413dfe302079a3664)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dcce5aad63435c14cdf9bfec3cb3c817f515710935e18da396f29a8cb9e8d4a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d2ac76429464f78f028ac44e955be671e18a705a67859ec70cbf2a2d2efde3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7659dcfb2311cee5f2f1b0d7dc82e6df8598ce7502712c5456a9fd536e0b4af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4de8129c2330eb6480c6e5571ae98df2fe437ea0fc3d45afb9c1046e0a4623d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8edd65962364ca1ea71d363d3767ff36d4cbbbf1d52d393f5a14cbbfb8650066)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a85832a99fb1fd65f66257f19d5c1a4a2d1ba156ebfe140e35492de2c0581cfc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f34cb3b1138a263f38d1ca2de66345019b202fccfb44d13c03e752f9eea22eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23f8def9f258b052df25aa6c10a32761e7cdccf9b30811041ea25bf9e68c3777)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__785b2b993e39c1e5a110b67ee6bee7339620e64db42be783673b1d23d9bdb10f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetLifecycleConfigArns")
    def reset_lifecycle_config_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArns", []))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList:
        return typing.cast(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnsInput")
    def lifecycle_config_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "lifecycleConfigArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArns")
    def lifecycle_config_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lifecycleConfigArns"))

    @lifecycle_config_arns.setter
    def lifecycle_config_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51e6c8c1ab8f4a30386f08d2f3a2375c62f3e49eaceb42341eded3ad017cf0fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArns", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__462094efaf00362d128ffa1e1333d78107dd559195ce26b6ff9db68bb42dbd7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2196bae6c2a708f150d469bdc058809e6f17d6cfa64714871f388579d0a1e37)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCanvasAppSettings")
    def put_canvas_app_settings(
        self,
        *,
        direct_deploy_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings, typing.Dict[builtins.str, typing.Any]]] = None,
        emr_serverless_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        generative_ai_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        identity_provider_oauth_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
        kendra_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        model_register_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        time_series_forecasting_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        workspace_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param direct_deploy_settings: direct_deploy_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#direct_deploy_settings SagemakerDomain#direct_deploy_settings}
        :param emr_serverless_settings: emr_serverless_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_serverless_settings SagemakerDomain#emr_serverless_settings}
        :param generative_ai_settings: generative_ai_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#generative_ai_settings SagemakerDomain#generative_ai_settings}
        :param identity_provider_oauth_settings: identity_provider_oauth_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#identity_provider_oauth_settings SagemakerDomain#identity_provider_oauth_settings}
        :param kendra_settings: kendra_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#kendra_settings SagemakerDomain#kendra_settings}
        :param model_register_settings: model_register_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#model_register_settings SagemakerDomain#model_register_settings}
        :param time_series_forecasting_settings: time_series_forecasting_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#time_series_forecasting_settings SagemakerDomain#time_series_forecasting_settings}
        :param workspace_settings: workspace_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#workspace_settings SagemakerDomain#workspace_settings}
        '''
        value = SagemakerDomainDefaultUserSettingsCanvasAppSettings(
            direct_deploy_settings=direct_deploy_settings,
            emr_serverless_settings=emr_serverless_settings,
            generative_ai_settings=generative_ai_settings,
            identity_provider_oauth_settings=identity_provider_oauth_settings,
            kendra_settings=kendra_settings,
            model_register_settings=model_register_settings,
            time_series_forecasting_settings=time_series_forecasting_settings,
            workspace_settings=workspace_settings,
        )

        return typing.cast(None, jsii.invoke(self, "putCanvasAppSettings", [value]))

    @jsii.member(jsii_name="putCodeEditorAppSettings")
    def put_code_editor_app_settings(
        self,
        *,
        app_lifecycle_management: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement, typing.Dict[builtins.str, typing.Any]]] = None,
        built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_lifecycle_management: app_lifecycle_management block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        :param built_in_lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultUserSettingsCodeEditorAppSettings(
            app_lifecycle_management=app_lifecycle_management,
            built_in_lifecycle_config_arn=built_in_lifecycle_config_arn,
            custom_image=custom_image,
            default_resource_spec=default_resource_spec,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putCodeEditorAppSettings", [value]))

    @jsii.member(jsii_name="putCustomFileSystemConfig")
    def put_custom_file_system_config(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d7fe5a2730abd85e849a7f462bd376dcbb2049d9fc7286ed17a64921ce5de33)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomFileSystemConfig", [value]))

    @jsii.member(jsii_name="putCustomPosixUserConfig")
    def put_custom_posix_user_config(
        self,
        *,
        gid: jsii.Number,
        uid: jsii.Number,
    ) -> None:
        '''
        :param gid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#gid SagemakerDomain#gid}.
        :param uid: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#uid SagemakerDomain#uid}.
        '''
        value = SagemakerDomainDefaultUserSettingsCustomPosixUserConfig(
            gid=gid, uid=uid
        )

        return typing.cast(None, jsii.invoke(self, "putCustomPosixUserConfig", [value]))

    @jsii.member(jsii_name="putJupyterLabAppSettings")
    def put_jupyter_lab_app_settings(
        self,
        *,
        app_lifecycle_management: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement, typing.Dict[builtins.str, typing.Any]]] = None,
        built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
        emr_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings, typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param app_lifecycle_management: app_lifecycle_management block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_lifecycle_management SagemakerDomain#app_lifecycle_management}
        :param built_in_lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#built_in_lifecycle_config_arn SagemakerDomain#built_in_lifecycle_config_arn}.
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param emr_settings: emr_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#emr_settings SagemakerDomain#emr_settings}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterLabAppSettings(
            app_lifecycle_management=app_lifecycle_management,
            built_in_lifecycle_config_arn=built_in_lifecycle_config_arn,
            code_repository=code_repository,
            custom_image=custom_image,
            default_resource_spec=default_resource_spec,
            emr_settings=emr_settings,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putJupyterLabAppSettings", [value]))

    @jsii.member(jsii_name="putJupyterServerAppSettings")
    def put_jupyter_server_app_settings(
        self,
        *,
        code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param code_repository: code_repository block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#code_repository SagemakerDomain#code_repository}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultUserSettingsJupyterServerAppSettings(
            code_repository=code_repository,
            default_resource_spec=default_resource_spec,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putJupyterServerAppSettings", [value]))

    @jsii.member(jsii_name="putKernelGatewayAppSettings")
    def put_kernel_gateway_app_settings(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
        lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param lifecycle_config_arns: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arns SagemakerDomain#lifecycle_config_arns}.
        '''
        value = SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings(
            custom_image=custom_image,
            default_resource_spec=default_resource_spec,
            lifecycle_config_arns=lifecycle_config_arns,
        )

        return typing.cast(None, jsii.invoke(self, "putKernelGatewayAppSettings", [value]))

    @jsii.member(jsii_name="putRSessionAppSettings")
    def put_r_session_app_settings(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        value = SagemakerDomainDefaultUserSettingsRSessionAppSettings(
            custom_image=custom_image, default_resource_spec=default_resource_spec
        )

        return typing.cast(None, jsii.invoke(self, "putRSessionAppSettings", [value]))

    @jsii.member(jsii_name="putRStudioServerProAppSettings")
    def put_r_studio_server_pro_app_settings(
        self,
        *,
        access_status: typing.Optional[builtins.str] = None,
        user_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#access_status SagemakerDomain#access_status}.
        :param user_group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#user_group SagemakerDomain#user_group}.
        '''
        value = SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings(
            access_status=access_status, user_group=user_group
        )

        return typing.cast(None, jsii.invoke(self, "putRStudioServerProAppSettings", [value]))

    @jsii.member(jsii_name="putSharingSettings")
    def put_sharing_settings(
        self,
        *,
        notebook_output_option: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
        s3_output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notebook_output_option: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#notebook_output_option SagemakerDomain#notebook_output_option}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.
        :param s3_output_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_output_path SagemakerDomain#s3_output_path}.
        '''
        value = SagemakerDomainDefaultUserSettingsSharingSettings(
            notebook_output_option=notebook_output_option,
            s3_kms_key_id=s3_kms_key_id,
            s3_output_path=s3_output_path,
        )

        return typing.cast(None, jsii.invoke(self, "putSharingSettings", [value]))

    @jsii.member(jsii_name="putSpaceStorageSettings")
    def put_space_storage_settings(
        self,
        *,
        default_ebs_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_ebs_storage_settings: default_ebs_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_storage_settings SagemakerDomain#default_ebs_storage_settings}
        '''
        value = SagemakerDomainDefaultUserSettingsSpaceStorageSettings(
            default_ebs_storage_settings=default_ebs_storage_settings
        )

        return typing.cast(None, jsii.invoke(self, "putSpaceStorageSettings", [value]))

    @jsii.member(jsii_name="putStudioWebPortalSettings")
    def put_studio_web_portal_settings(
        self,
        *,
        hidden_app_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        hidden_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        hidden_ml_tools: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param hidden_app_types: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_app_types SagemakerDomain#hidden_app_types}.
        :param hidden_instance_types: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_instance_types SagemakerDomain#hidden_instance_types}.
        :param hidden_ml_tools: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_ml_tools SagemakerDomain#hidden_ml_tools}.
        '''
        value = SagemakerDomainDefaultUserSettingsStudioWebPortalSettings(
            hidden_app_types=hidden_app_types,
            hidden_instance_types=hidden_instance_types,
            hidden_ml_tools=hidden_ml_tools,
        )

        return typing.cast(None, jsii.invoke(self, "putStudioWebPortalSettings", [value]))

    @jsii.member(jsii_name="putTensorBoardAppSettings")
    def put_tensor_board_app_settings(
        self,
        *,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        value = SagemakerDomainDefaultUserSettingsTensorBoardAppSettings(
            default_resource_spec=default_resource_spec
        )

        return typing.cast(None, jsii.invoke(self, "putTensorBoardAppSettings", [value]))

    @jsii.member(jsii_name="resetAutoMountHomeEfs")
    def reset_auto_mount_home_efs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoMountHomeEfs", []))

    @jsii.member(jsii_name="resetCanvasAppSettings")
    def reset_canvas_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCanvasAppSettings", []))

    @jsii.member(jsii_name="resetCodeEditorAppSettings")
    def reset_code_editor_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCodeEditorAppSettings", []))

    @jsii.member(jsii_name="resetCustomFileSystemConfig")
    def reset_custom_file_system_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomFileSystemConfig", []))

    @jsii.member(jsii_name="resetCustomPosixUserConfig")
    def reset_custom_posix_user_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPosixUserConfig", []))

    @jsii.member(jsii_name="resetDefaultLandingUri")
    def reset_default_landing_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultLandingUri", []))

    @jsii.member(jsii_name="resetJupyterLabAppSettings")
    def reset_jupyter_lab_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJupyterLabAppSettings", []))

    @jsii.member(jsii_name="resetJupyterServerAppSettings")
    def reset_jupyter_server_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJupyterServerAppSettings", []))

    @jsii.member(jsii_name="resetKernelGatewayAppSettings")
    def reset_kernel_gateway_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKernelGatewayAppSettings", []))

    @jsii.member(jsii_name="resetRSessionAppSettings")
    def reset_r_session_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRSessionAppSettings", []))

    @jsii.member(jsii_name="resetRStudioServerProAppSettings")
    def reset_r_studio_server_pro_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRStudioServerProAppSettings", []))

    @jsii.member(jsii_name="resetSecurityGroups")
    def reset_security_groups(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroups", []))

    @jsii.member(jsii_name="resetSharingSettings")
    def reset_sharing_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharingSettings", []))

    @jsii.member(jsii_name="resetSpaceStorageSettings")
    def reset_space_storage_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpaceStorageSettings", []))

    @jsii.member(jsii_name="resetStudioWebPortal")
    def reset_studio_web_portal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStudioWebPortal", []))

    @jsii.member(jsii_name="resetStudioWebPortalSettings")
    def reset_studio_web_portal_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStudioWebPortalSettings", []))

    @jsii.member(jsii_name="resetTensorBoardAppSettings")
    def reset_tensor_board_app_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTensorBoardAppSettings", []))

    @builtins.property
    @jsii.member(jsii_name="canvasAppSettings")
    def canvas_app_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCanvasAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCanvasAppSettingsOutputReference, jsii.get(self, "canvasAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="codeEditorAppSettings")
    def code_editor_app_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsOutputReference, jsii.get(self, "codeEditorAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="customFileSystemConfig")
    def custom_file_system_config(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCustomFileSystemConfigList:
        return typing.cast(SagemakerDomainDefaultUserSettingsCustomFileSystemConfigList, jsii.get(self, "customFileSystemConfig"))

    @builtins.property
    @jsii.member(jsii_name="customPosixUserConfig")
    def custom_posix_user_config(
        self,
    ) -> SagemakerDomainDefaultUserSettingsCustomPosixUserConfigOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsCustomPosixUserConfigOutputReference, jsii.get(self, "customPosixUserConfig"))

    @builtins.property
    @jsii.member(jsii_name="jupyterLabAppSettings")
    def jupyter_lab_app_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsOutputReference, jsii.get(self, "jupyterLabAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettings")
    def jupyter_server_app_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference, jsii.get(self, "jupyterServerAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettings")
    def kernel_gateway_app_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference, jsii.get(self, "kernelGatewayAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="rSessionAppSettings")
    def r_session_app_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsRSessionAppSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsRSessionAppSettingsOutputReference", jsii.get(self, "rSessionAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="rStudioServerProAppSettings")
    def r_studio_server_pro_app_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsRStudioServerProAppSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsRStudioServerProAppSettingsOutputReference", jsii.get(self, "rStudioServerProAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="sharingSettings")
    def sharing_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference", jsii.get(self, "sharingSettings"))

    @builtins.property
    @jsii.member(jsii_name="spaceStorageSettings")
    def space_storage_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsSpaceStorageSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsSpaceStorageSettingsOutputReference", jsii.get(self, "spaceStorageSettings"))

    @builtins.property
    @jsii.member(jsii_name="studioWebPortalSettings")
    def studio_web_portal_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsStudioWebPortalSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsStudioWebPortalSettingsOutputReference", jsii.get(self, "studioWebPortalSettings"))

    @builtins.property
    @jsii.member(jsii_name="tensorBoardAppSettings")
    def tensor_board_app_settings(
        self,
    ) -> "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference":
        return typing.cast("SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference", jsii.get(self, "tensorBoardAppSettings"))

    @builtins.property
    @jsii.member(jsii_name="autoMountHomeEfsInput")
    def auto_mount_home_efs_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoMountHomeEfsInput"))

    @builtins.property
    @jsii.member(jsii_name="canvasAppSettingsInput")
    def canvas_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettings], jsii.get(self, "canvasAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="codeEditorAppSettingsInput")
    def code_editor_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettings], jsii.get(self, "codeEditorAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="customFileSystemConfigInput")
    def custom_file_system_config_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]]], jsii.get(self, "customFileSystemConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="customPosixUserConfigInput")
    def custom_posix_user_config_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsCustomPosixUserConfig]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsCustomPosixUserConfig], jsii.get(self, "customPosixUserConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultLandingUriInput")
    def default_landing_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultLandingUriInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleInput")
    def execution_role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="jupyterLabAppSettingsInput")
    def jupyter_lab_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettings], jsii.get(self, "jupyterLabAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="jupyterServerAppSettingsInput")
    def jupyter_server_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings], jsii.get(self, "jupyterServerAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="kernelGatewayAppSettingsInput")
    def kernel_gateway_app_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings], jsii.get(self, "kernelGatewayAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="rSessionAppSettingsInput")
    def r_session_app_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsRSessionAppSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsRSessionAppSettings"], jsii.get(self, "rSessionAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="rStudioServerProAppSettingsInput")
    def r_studio_server_pro_app_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings"], jsii.get(self, "rStudioServerProAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupsInput")
    def security_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="sharingSettingsInput")
    def sharing_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsSharingSettings"], jsii.get(self, "sharingSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="spaceStorageSettingsInput")
    def space_storage_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsSpaceStorageSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsSpaceStorageSettings"], jsii.get(self, "spaceStorageSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="studioWebPortalInput")
    def studio_web_portal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "studioWebPortalInput"))

    @builtins.property
    @jsii.member(jsii_name="studioWebPortalSettingsInput")
    def studio_web_portal_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsStudioWebPortalSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsStudioWebPortalSettings"], jsii.get(self, "studioWebPortalSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="tensorBoardAppSettingsInput")
    def tensor_board_app_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettings"], jsii.get(self, "tensorBoardAppSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="autoMountHomeEfs")
    def auto_mount_home_efs(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoMountHomeEfs"))

    @auto_mount_home_efs.setter
    def auto_mount_home_efs(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ecc94e916f271539e78359612a7f747a2fd59890215ee12d44ee6e7a9c545a0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMountHomeEfs", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="defaultLandingUri")
    def default_landing_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultLandingUri"))

    @default_landing_uri.setter
    def default_landing_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e81faf6853cf4f5b569e334ed0f6d59cfec6a770914827a7710830b81f7652bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultLandingUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="executionRole")
    def execution_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRole"))

    @execution_role.setter
    def execution_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14c0da10af71ea964d7cf22301f2e6fc38707307321f82c336b6b067c809cd9b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRole", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d11fab3b5d64d156cbb158e9a44595253ac85b0f3d274fc8b1d30d4ea5b5c4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="studioWebPortal")
    def studio_web_portal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "studioWebPortal"))

    @studio_web_portal.setter
    def studio_web_portal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de815de7c4cd8d230694fe7ad862a32629ecace783e214fa46b1120e4be8c2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "studioWebPortal", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerDomainDefaultUserSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83a7d299b4926eb6e063e10bd481bdc114762cbf1dbb95427b69d3ba95035f3b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRSessionAppSettings",
    jsii_struct_bases=[],
    name_mapping={
        "custom_image": "customImage",
        "default_resource_spec": "defaultResourceSpec",
    },
)
class SagemakerDomainDefaultUserSettingsRSessionAppSettings:
    def __init__(
        self,
        *,
        custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage", typing.Dict[builtins.str, typing.Any]]]]] = None,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param custom_image: custom_image block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4be75f1e2c32f7edf88a5f8928e635d81ddf3fba6344d7f4998a3e98160accb2)
            check_type(argname="argument custom_image", value=custom_image, expected_type=type_hints["custom_image"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if custom_image is not None:
            self._values["custom_image"] = custom_image
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec

    @builtins.property
    def custom_image(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage"]]]:
        '''custom_image block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#custom_image SagemakerDomain#custom_image}
        '''
        result = self._values.get("custom_image")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage"]]], result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsRSessionAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage",
    jsii_struct_bases=[],
    name_mapping={
        "app_image_config_name": "appImageConfigName",
        "image_name": "imageName",
        "image_version_number": "imageVersionNumber",
    },
)
class SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage:
    def __init__(
        self,
        *,
        app_image_config_name: builtins.str,
        image_name: builtins.str,
        image_version_number: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param app_image_config_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.
        :param image_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.
        :param image_version_number: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c9a3bfbfceb4d1fddb17c577dba8c693912517c0a4128ba062797249459bcb4)
            check_type(argname="argument app_image_config_name", value=app_image_config_name, expected_type=type_hints["app_image_config_name"])
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument image_version_number", value=image_version_number, expected_type=type_hints["image_version_number"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "app_image_config_name": app_image_config_name,
            "image_name": image_name,
        }
        if image_version_number is not None:
            self._values["image_version_number"] = image_version_number

    @builtins.property
    def app_image_config_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#app_image_config_name SagemakerDomain#app_image_config_name}.'''
        result = self._values.get("app_image_config_name")
        assert result is not None, "Required property 'app_image_config_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_name SagemakerDomain#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def image_version_number(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#image_version_number SagemakerDomain#image_version_number}.'''
        result = self._values.get("image_version_number")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageList",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__986ea9a3720dcc6dddb31aec49afdbe86040d38fe751bffb0c43369f1e929d3e)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d15697e0d4d158bdbee5e25baac3d602e45b6ee1dca363d0b1009f457b95def)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8725bb989159b1d0e98fff637603dbbef7b16478ec6118d38fb88b14d98a6f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> _cdktf_9a9027ec.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(_cdktf_9a9027ec.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: _cdktf_9a9027ec.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0031306dcb2f45401c27f138a6d29527db5978fbf34a9a29ffba384ab97e9db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f39c47a2a22b70e9d19ff765ebb3e2c9ca56bf241e3e466381389738b1a28d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d37da9af65a2229669e54fd5587b9f13f98e6581c3efef370f757de224047b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9d8e62c0f90bee9f3ddbed2100562481eddff1c78b2afaacdc54321d2c19018)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetImageVersionNumber")
    def reset_image_version_number(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageVersionNumber", []))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigNameInput")
    def app_image_config_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "appImageConfigNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumberInput")
    def image_version_number_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "imageVersionNumberInput"))

    @builtins.property
    @jsii.member(jsii_name="appImageConfigName")
    def app_image_config_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appImageConfigName"))

    @app_image_config_name.setter
    def app_image_config_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ec4d740891a4ab16f1c51d74912b30b5aa0128044af5ba6646eb6dee51ad554)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "appImageConfigName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f701dd20fa53e7d54a1294df48d16535c2ab31b1b92f55113eb888232d1684d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="imageVersionNumber")
    def image_version_number(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "imageVersionNumber"))

    @image_version_number.setter
    def image_version_number(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f881dbcfdbe8ada778f0c14808ba5be3c318c2165105e53dec686f34136a859a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageVersionNumber", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47867b2883b90fa884c7914b61026cd3077816daf3c011f9827f1843eef6bd46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34592cbcd4b5da12cb6ae4e68fdffbac4eac34503dffef7a02ada211a2eb79f2)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6f0ae5748781dfedeed19d08a0984df73e046b50f233769590189f544c8d566)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d830c6ee69eeb763aada91a0881b2b0677e6de3e6b4bff649904cedc5fcdc5e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f38c93f2d9fe2160a21f953cd9ca2f31ed1a54b61021c7fd5a5bbdddad0ce9c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc66e8890eb3f05b3d29b9a1596ab97f84ef1899ca0221c6b745f3fabe6459af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de08041ea6a4ad69a2bd45e673f50b1facbea79a2415e6350689716ef2df179f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0395692746b6a338738352c2e80e1b4bd47a3de1f5d599a21102dc117f6a2cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2d041ec557f299ea184b774d63f36641f3f1a0c931a847a93eedd2e8828f371)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsRSessionAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRSessionAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d363104dd1cfb96de81276109f4f75e5b1e9e99cac00e4cdf74bbe162b0746dc)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCustomImage")
    def put_custom_image(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05e4cd0f287785b693d5605772ecd5d3ccd284fa3f6dd0464821eddb92c4649b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomImage", [value]))

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetCustomImage")
    def reset_custom_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomImage", []))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @builtins.property
    @jsii.member(jsii_name="customImage")
    def custom_image(
        self,
    ) -> SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageList:
        return typing.cast(SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageList, jsii.get(self, "customImage"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="customImageInput")
    def custom_image_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]]], jsii.get(self, "customImageInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf719d6922d73c12647d2cbef17fa633a0ee8a7c6608a37ae135a0432156fc1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings",
    jsii_struct_bases=[],
    name_mapping={"access_status": "accessStatus", "user_group": "userGroup"},
)
class SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings:
    def __init__(
        self,
        *,
        access_status: typing.Optional[builtins.str] = None,
        user_group: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_status: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#access_status SagemakerDomain#access_status}.
        :param user_group: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#user_group SagemakerDomain#user_group}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__448ca41396707bad570b73c95bbb51c88010ec5fbe5731f8aa6b753e53035d02)
            check_type(argname="argument access_status", value=access_status, expected_type=type_hints["access_status"])
            check_type(argname="argument user_group", value=user_group, expected_type=type_hints["user_group"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_status is not None:
            self._values["access_status"] = access_status
        if user_group is not None:
            self._values["user_group"] = user_group

    @builtins.property
    def access_status(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#access_status SagemakerDomain#access_status}.'''
        result = self._values.get("access_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_group(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#user_group SagemakerDomain#user_group}.'''
        result = self._values.get("user_group")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsRStudioServerProAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsRStudioServerProAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af22b009af573074d171938c47cc8f65de0c5426c00d6ba67b755b17c77c8b40)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccessStatus")
    def reset_access_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessStatus", []))

    @jsii.member(jsii_name="resetUserGroup")
    def reset_user_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserGroup", []))

    @builtins.property
    @jsii.member(jsii_name="accessStatusInput")
    def access_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="userGroupInput")
    def user_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="accessStatus")
    def access_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessStatus"))

    @access_status.setter
    def access_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__577ebaa4d6e9f7a16f08aed72e3a77d471c184e45502f7c093360283a81fa784)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessStatus", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="userGroup")
    def user_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userGroup"))

    @user_group.setter
    def user_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2b9888400a2845b121141286e2ffca45e730fe8ea9a447c0d861792b96bd8e44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userGroup", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d4c27dfdd043c8984cf80fc3125aa3ec4eca091432a8278cbd9b523a3ab0d16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSharingSettings",
    jsii_struct_bases=[],
    name_mapping={
        "notebook_output_option": "notebookOutputOption",
        "s3_kms_key_id": "s3KmsKeyId",
        "s3_output_path": "s3OutputPath",
    },
)
class SagemakerDomainDefaultUserSettingsSharingSettings:
    def __init__(
        self,
        *,
        notebook_output_option: typing.Optional[builtins.str] = None,
        s3_kms_key_id: typing.Optional[builtins.str] = None,
        s3_output_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param notebook_output_option: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#notebook_output_option SagemakerDomain#notebook_output_option}.
        :param s3_kms_key_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.
        :param s3_output_path: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_output_path SagemakerDomain#s3_output_path}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4dd634ac30050b1726764ae6971d1a9565819738f081476b3fe307c4c5dde7)
            check_type(argname="argument notebook_output_option", value=notebook_output_option, expected_type=type_hints["notebook_output_option"])
            check_type(argname="argument s3_kms_key_id", value=s3_kms_key_id, expected_type=type_hints["s3_kms_key_id"])
            check_type(argname="argument s3_output_path", value=s3_output_path, expected_type=type_hints["s3_output_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if notebook_output_option is not None:
            self._values["notebook_output_option"] = notebook_output_option
        if s3_kms_key_id is not None:
            self._values["s3_kms_key_id"] = s3_kms_key_id
        if s3_output_path is not None:
            self._values["s3_output_path"] = s3_output_path

    @builtins.property
    def notebook_output_option(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#notebook_output_option SagemakerDomain#notebook_output_option}.'''
        result = self._values.get("notebook_output_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_kms_key_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_kms_key_id SagemakerDomain#s3_kms_key_id}.'''
        result = self._values.get("s3_kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_output_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#s3_output_path SagemakerDomain#s3_output_path}.'''
        result = self._values.get("s3_output_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsSharingSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a80a9baefe36496342db09902861e529ae4fd9815be6baada02db150a973f865)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNotebookOutputOption")
    def reset_notebook_output_option(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotebookOutputOption", []))

    @jsii.member(jsii_name="resetS3KmsKeyId")
    def reset_s3_kms_key_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3KmsKeyId", []))

    @jsii.member(jsii_name="resetS3OutputPath")
    def reset_s3_output_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3OutputPath", []))

    @builtins.property
    @jsii.member(jsii_name="notebookOutputOptionInput")
    def notebook_output_option_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notebookOutputOptionInput"))

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyIdInput")
    def s3_kms_key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3KmsKeyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3OutputPathInput")
    def s3_output_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "s3OutputPathInput"))

    @builtins.property
    @jsii.member(jsii_name="notebookOutputOption")
    def notebook_output_option(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notebookOutputOption"))

    @notebook_output_option.setter
    def notebook_output_option(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b5504187e12070e4e28071809148f404eff4b32cb520e3814cb026f07dcc89a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notebookOutputOption", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="s3KmsKeyId")
    def s3_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3KmsKeyId"))

    @s3_kms_key_id.setter
    def s3_kms_key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__510dd34b64dd0595b894164f8e21ece274e1195c1ed5cbebefba7abe3dd8af16)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3KmsKeyId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="s3OutputPath")
    def s3_output_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "s3OutputPath"))

    @s3_output_path.setter
    def s3_output_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb1a1eba1d87b94a52115e393aa806f64b9f0453625de737b372944347071e1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3OutputPath", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsSharingSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsSharingSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsSharingSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__656654d7743273c5214479068c2ee0573f66b63a5aff32ea778fa44860c5ba5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSpaceStorageSettings",
    jsii_struct_bases=[],
    name_mapping={"default_ebs_storage_settings": "defaultEbsStorageSettings"},
)
class SagemakerDomainDefaultUserSettingsSpaceStorageSettings:
    def __init__(
        self,
        *,
        default_ebs_storage_settings: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_ebs_storage_settings: default_ebs_storage_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_storage_settings SagemakerDomain#default_ebs_storage_settings}
        '''
        if isinstance(default_ebs_storage_settings, dict):
            default_ebs_storage_settings = SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings(**default_ebs_storage_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c88e748c8a35da0aa0708526ddd017b3241a9642b82962a7c9e8aa474bec9113)
            check_type(argname="argument default_ebs_storage_settings", value=default_ebs_storage_settings, expected_type=type_hints["default_ebs_storage_settings"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_ebs_storage_settings is not None:
            self._values["default_ebs_storage_settings"] = default_ebs_storage_settings

    @builtins.property
    def default_ebs_storage_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings"]:
        '''default_ebs_storage_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_storage_settings SagemakerDomain#default_ebs_storage_settings}
        '''
        result = self._values.get("default_ebs_storage_settings")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsSpaceStorageSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings",
    jsii_struct_bases=[],
    name_mapping={
        "default_ebs_volume_size_in_gb": "defaultEbsVolumeSizeInGb",
        "maximum_ebs_volume_size_in_gb": "maximumEbsVolumeSizeInGb",
    },
)
class SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings:
    def __init__(
        self,
        *,
        default_ebs_volume_size_in_gb: jsii.Number,
        maximum_ebs_volume_size_in_gb: jsii.Number,
    ) -> None:
        '''
        :param default_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_volume_size_in_gb SagemakerDomain#default_ebs_volume_size_in_gb}.
        :param maximum_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#maximum_ebs_volume_size_in_gb SagemakerDomain#maximum_ebs_volume_size_in_gb}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cadd3c78a350e28a86ac0116c5467b207548669eaea32e4ee66145a76e1f8eb3)
            check_type(argname="argument default_ebs_volume_size_in_gb", value=default_ebs_volume_size_in_gb, expected_type=type_hints["default_ebs_volume_size_in_gb"])
            check_type(argname="argument maximum_ebs_volume_size_in_gb", value=maximum_ebs_volume_size_in_gb, expected_type=type_hints["maximum_ebs_volume_size_in_gb"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_ebs_volume_size_in_gb": default_ebs_volume_size_in_gb,
            "maximum_ebs_volume_size_in_gb": maximum_ebs_volume_size_in_gb,
        }

    @builtins.property
    def default_ebs_volume_size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_volume_size_in_gb SagemakerDomain#default_ebs_volume_size_in_gb}.'''
        result = self._values.get("default_ebs_volume_size_in_gb")
        assert result is not None, "Required property 'default_ebs_volume_size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def maximum_ebs_volume_size_in_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#maximum_ebs_volume_size_in_gb SagemakerDomain#maximum_ebs_volume_size_in_gb}.'''
        result = self._values.get("maximum_ebs_volume_size_in_gb")
        assert result is not None, "Required property 'maximum_ebs_volume_size_in_gb' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd31c8b3e0b98f158ed32611675a45f49a727d878eca0d9c2aaced9e49756af7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultEbsVolumeSizeInGbInput")
    def default_ebs_volume_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "defaultEbsVolumeSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumEbsVolumeSizeInGbInput")
    def maximum_ebs_volume_size_in_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumEbsVolumeSizeInGbInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultEbsVolumeSizeInGb")
    def default_ebs_volume_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "defaultEbsVolumeSizeInGb"))

    @default_ebs_volume_size_in_gb.setter
    def default_ebs_volume_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aad279260efb6952d449aee0acc88369a1dd45f78c5fc0558999239e0c43b1e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultEbsVolumeSizeInGb", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="maximumEbsVolumeSizeInGb")
    def maximum_ebs_volume_size_in_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumEbsVolumeSizeInGb"))

    @maximum_ebs_volume_size_in_gb.setter
    def maximum_ebs_volume_size_in_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__602580b5f3032bcaa3e9f8e5de3b7b82e7f8ef791758a628e88d302d7f3c46dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumEbsVolumeSizeInGb", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0fd02ea27d2b4246fb6eed9fbae7a794329e2270bdfb1b787f3ff72ec4e9c57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsSpaceStorageSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsSpaceStorageSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb758851f95dc3a2e4d1a2c467f4ae95543058daff8309be5eddab3a69afc91b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultEbsStorageSettings")
    def put_default_ebs_storage_settings(
        self,
        *,
        default_ebs_volume_size_in_gb: jsii.Number,
        maximum_ebs_volume_size_in_gb: jsii.Number,
    ) -> None:
        '''
        :param default_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_ebs_volume_size_in_gb SagemakerDomain#default_ebs_volume_size_in_gb}.
        :param maximum_ebs_volume_size_in_gb: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#maximum_ebs_volume_size_in_gb SagemakerDomain#maximum_ebs_volume_size_in_gb}.
        '''
        value = SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings(
            default_ebs_volume_size_in_gb=default_ebs_volume_size_in_gb,
            maximum_ebs_volume_size_in_gb=maximum_ebs_volume_size_in_gb,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultEbsStorageSettings", [value]))

    @jsii.member(jsii_name="resetDefaultEbsStorageSettings")
    def reset_default_ebs_storage_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultEbsStorageSettings", []))

    @builtins.property
    @jsii.member(jsii_name="defaultEbsStorageSettings")
    def default_ebs_storage_settings(
        self,
    ) -> SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference, jsii.get(self, "defaultEbsStorageSettings"))

    @builtins.property
    @jsii.member(jsii_name="defaultEbsStorageSettingsInput")
    def default_ebs_storage_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings], jsii.get(self, "defaultEbsStorageSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc0e60c6fdde83d14d7a933e1974bc2eac70a2eaed1d326feebd1a198f6d46e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsStudioWebPortalSettings",
    jsii_struct_bases=[],
    name_mapping={
        "hidden_app_types": "hiddenAppTypes",
        "hidden_instance_types": "hiddenInstanceTypes",
        "hidden_ml_tools": "hiddenMlTools",
    },
)
class SagemakerDomainDefaultUserSettingsStudioWebPortalSettings:
    def __init__(
        self,
        *,
        hidden_app_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        hidden_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        hidden_ml_tools: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param hidden_app_types: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_app_types SagemakerDomain#hidden_app_types}.
        :param hidden_instance_types: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_instance_types SagemakerDomain#hidden_instance_types}.
        :param hidden_ml_tools: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_ml_tools SagemakerDomain#hidden_ml_tools}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f7076d0a03619e746a951338e9ff705b97696b960ef4a7fa2b8cd3d23825615)
            check_type(argname="argument hidden_app_types", value=hidden_app_types, expected_type=type_hints["hidden_app_types"])
            check_type(argname="argument hidden_instance_types", value=hidden_instance_types, expected_type=type_hints["hidden_instance_types"])
            check_type(argname="argument hidden_ml_tools", value=hidden_ml_tools, expected_type=type_hints["hidden_ml_tools"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hidden_app_types is not None:
            self._values["hidden_app_types"] = hidden_app_types
        if hidden_instance_types is not None:
            self._values["hidden_instance_types"] = hidden_instance_types
        if hidden_ml_tools is not None:
            self._values["hidden_ml_tools"] = hidden_ml_tools

    @builtins.property
    def hidden_app_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_app_types SagemakerDomain#hidden_app_types}.'''
        result = self._values.get("hidden_app_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hidden_instance_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_instance_types SagemakerDomain#hidden_instance_types}.'''
        result = self._values.get("hidden_instance_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def hidden_ml_tools(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#hidden_ml_tools SagemakerDomain#hidden_ml_tools}.'''
        result = self._values.get("hidden_ml_tools")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsStudioWebPortalSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsStudioWebPortalSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsStudioWebPortalSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91a541c3c0e87c6e88e9a560a08b884e3d716e4bd5f4787468f344edb450dc59)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHiddenAppTypes")
    def reset_hidden_app_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiddenAppTypes", []))

    @jsii.member(jsii_name="resetHiddenInstanceTypes")
    def reset_hidden_instance_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiddenInstanceTypes", []))

    @jsii.member(jsii_name="resetHiddenMlTools")
    def reset_hidden_ml_tools(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiddenMlTools", []))

    @builtins.property
    @jsii.member(jsii_name="hiddenAppTypesInput")
    def hidden_app_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hiddenAppTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="hiddenInstanceTypesInput")
    def hidden_instance_types_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hiddenInstanceTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="hiddenMlToolsInput")
    def hidden_ml_tools_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hiddenMlToolsInput"))

    @builtins.property
    @jsii.member(jsii_name="hiddenAppTypes")
    def hidden_app_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hiddenAppTypes"))

    @hidden_app_types.setter
    def hidden_app_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c44630597acc0cddb89e185371fdadbea8171ac434bcfb884c96c8603a5c2e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hiddenAppTypes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hiddenInstanceTypes")
    def hidden_instance_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hiddenInstanceTypes"))

    @hidden_instance_types.setter
    def hidden_instance_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5145ab98ccd3ed4096eb671033a0293e6829ffca9da9b549f49ee6fff55bb09f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hiddenInstanceTypes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="hiddenMlTools")
    def hidden_ml_tools(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hiddenMlTools"))

    @hidden_ml_tools.setter
    def hidden_ml_tools(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6eded293e1853af0fe2fbf86c9b3f0da4c4eeabd023fc335c5fdea2b99c8dde7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hiddenMlTools", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsStudioWebPortalSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsStudioWebPortalSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsStudioWebPortalSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e43a2d6d1475efd1041b94e6197d9c1a1369edcb8a41135760f4864695c99d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettings",
    jsii_struct_bases=[],
    name_mapping={"default_resource_spec": "defaultResourceSpec"},
)
class SagemakerDomainDefaultUserSettingsTensorBoardAppSettings:
    def __init__(
        self,
        *,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0fc26081fd95e16183d03a085de090d85d9a2df3787989380beac7ef716d821)
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsTensorBoardAppSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9310f350c8c55a499e2ced4c9d1329474bed2ae5da1e27f7f8c99ec9c50b3f78)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71acb789fa6bdc95af11c0cfe2f99e59ed5853d19c86be28931c3ff06cd4c704)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d61cf21cffb52ab4b57a09534068d349fdfb2438b220f3d0bfd045d14e9cafcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1f2fdea534b4a7d72e02527780c1b702a8f872a52ce59a6c96891511847bb74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__976c5cffa5917b799083dbb8a0d9d23ee2a6342f1113bef13be13e8f5e38813b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3639396b56161d2561ed75ba1f3c0e2665b038f36fe4ba8f50dea4ccfa8ca65c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aeb0ff9183e88e8e3878c687f743bd5bc9c61472cffd7f461a1e6231817cc44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f09402a83b7c35dbdbc0e0426f51a01f76349d33fa0fedbb9705fa30a03025a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1446f7e41501e74faa24bd93d3928cf49fa0faaab7bfafa14865575c23726f9)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b374a77b78eab0c915399d041820a394172c1828c1e3f38c86fc76c6c5f1dcc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettings",
    jsii_struct_bases=[],
    name_mapping={
        "docker_settings": "dockerSettings",
        "execution_role_identity_config": "executionRoleIdentityConfig",
        "r_studio_server_pro_domain_settings": "rStudioServerProDomainSettings",
        "security_group_ids": "securityGroupIds",
    },
)
class SagemakerDomainDomainSettings:
    def __init__(
        self,
        *,
        docker_settings: typing.Optional[typing.Union["SagemakerDomainDomainSettingsDockerSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        execution_role_identity_config: typing.Optional[builtins.str] = None,
        r_studio_server_pro_domain_settings: typing.Optional[typing.Union["SagemakerDomainDomainSettingsRStudioServerProDomainSettings", typing.Dict[builtins.str, typing.Any]]] = None,
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param docker_settings: docker_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#docker_settings SagemakerDomain#docker_settings}
        :param execution_role_identity_config: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_identity_config SagemakerDomain#execution_role_identity_config}.
        :param r_studio_server_pro_domain_settings: r_studio_server_pro_domain_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_server_pro_domain_settings SagemakerDomain#r_studio_server_pro_domain_settings}
        :param security_group_ids: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_group_ids SagemakerDomain#security_group_ids}.
        '''
        if isinstance(docker_settings, dict):
            docker_settings = SagemakerDomainDomainSettingsDockerSettings(**docker_settings)
        if isinstance(r_studio_server_pro_domain_settings, dict):
            r_studio_server_pro_domain_settings = SagemakerDomainDomainSettingsRStudioServerProDomainSettings(**r_studio_server_pro_domain_settings)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3778d9e111123821d8c1e9f616676628f0e9f0ce4d31c3e2521880bae1efedc)
            check_type(argname="argument docker_settings", value=docker_settings, expected_type=type_hints["docker_settings"])
            check_type(argname="argument execution_role_identity_config", value=execution_role_identity_config, expected_type=type_hints["execution_role_identity_config"])
            check_type(argname="argument r_studio_server_pro_domain_settings", value=r_studio_server_pro_domain_settings, expected_type=type_hints["r_studio_server_pro_domain_settings"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if docker_settings is not None:
            self._values["docker_settings"] = docker_settings
        if execution_role_identity_config is not None:
            self._values["execution_role_identity_config"] = execution_role_identity_config
        if r_studio_server_pro_domain_settings is not None:
            self._values["r_studio_server_pro_domain_settings"] = r_studio_server_pro_domain_settings
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids

    @builtins.property
    def docker_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDomainSettingsDockerSettings"]:
        '''docker_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#docker_settings SagemakerDomain#docker_settings}
        '''
        result = self._values.get("docker_settings")
        return typing.cast(typing.Optional["SagemakerDomainDomainSettingsDockerSettings"], result)

    @builtins.property
    def execution_role_identity_config(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#execution_role_identity_config SagemakerDomain#execution_role_identity_config}.'''
        result = self._values.get("execution_role_identity_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def r_studio_server_pro_domain_settings(
        self,
    ) -> typing.Optional["SagemakerDomainDomainSettingsRStudioServerProDomainSettings"]:
        '''r_studio_server_pro_domain_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_server_pro_domain_settings SagemakerDomain#r_studio_server_pro_domain_settings}
        '''
        result = self._values.get("r_studio_server_pro_domain_settings")
        return typing.cast(typing.Optional["SagemakerDomainDomainSettingsRStudioServerProDomainSettings"], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#security_group_ids SagemakerDomain#security_group_ids}.'''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDomainSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettingsDockerSettings",
    jsii_struct_bases=[],
    name_mapping={
        "enable_docker_access": "enableDockerAccess",
        "vpc_only_trusted_accounts": "vpcOnlyTrustedAccounts",
    },
)
class SagemakerDomainDomainSettingsDockerSettings:
    def __init__(
        self,
        *,
        enable_docker_access: typing.Optional[builtins.str] = None,
        vpc_only_trusted_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enable_docker_access: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#enable_docker_access SagemakerDomain#enable_docker_access}.
        :param vpc_only_trusted_accounts: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#vpc_only_trusted_accounts SagemakerDomain#vpc_only_trusted_accounts}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48542167f4d863eed9187c5560cdb6a2a47940b037f4ba1fbdd76936d7525b98)
            check_type(argname="argument enable_docker_access", value=enable_docker_access, expected_type=type_hints["enable_docker_access"])
            check_type(argname="argument vpc_only_trusted_accounts", value=vpc_only_trusted_accounts, expected_type=type_hints["vpc_only_trusted_accounts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if enable_docker_access is not None:
            self._values["enable_docker_access"] = enable_docker_access
        if vpc_only_trusted_accounts is not None:
            self._values["vpc_only_trusted_accounts"] = vpc_only_trusted_accounts

    @builtins.property
    def enable_docker_access(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#enable_docker_access SagemakerDomain#enable_docker_access}.'''
        result = self._values.get("enable_docker_access")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_only_trusted_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#vpc_only_trusted_accounts SagemakerDomain#vpc_only_trusted_accounts}.'''
        result = self._values.get("vpc_only_trusted_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDomainSettingsDockerSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDomainSettingsDockerSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettingsDockerSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fd4c24eedf755ee04692a561b595163784beafcfb4b2aec16fcd3b8b126b088)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableDockerAccess")
    def reset_enable_docker_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableDockerAccess", []))

    @jsii.member(jsii_name="resetVpcOnlyTrustedAccounts")
    def reset_vpc_only_trusted_accounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpcOnlyTrustedAccounts", []))

    @builtins.property
    @jsii.member(jsii_name="enableDockerAccessInput")
    def enable_docker_access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "enableDockerAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcOnlyTrustedAccountsInput")
    def vpc_only_trusted_accounts_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcOnlyTrustedAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableDockerAccess")
    def enable_docker_access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "enableDockerAccess"))

    @enable_docker_access.setter
    def enable_docker_access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8d93f13ac452dfe38ce435e32cd215d1d889df32f0d509ad560113bd5ecd7b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableDockerAccess", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="vpcOnlyTrustedAccounts")
    def vpc_only_trusted_accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vpcOnlyTrustedAccounts"))

    @vpc_only_trusted_accounts.setter
    def vpc_only_trusted_accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f5e51020c021544c476b9232fb0a98ac9acde6d145849f87850bb199a61fa47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcOnlyTrustedAccounts", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDomainSettingsDockerSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDomainSettingsDockerSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDomainSettingsDockerSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__088cf46bb0d04deaa06d5134c80a9c6af7f964e95cc1c3dfc6426f2fd86bb786)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDomainSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ba29ecbae06a14349a5ae5e53779ed3c882e3b880aa67e3f36f1533183f1e1)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDockerSettings")
    def put_docker_settings(
        self,
        *,
        enable_docker_access: typing.Optional[builtins.str] = None,
        vpc_only_trusted_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param enable_docker_access: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#enable_docker_access SagemakerDomain#enable_docker_access}.
        :param vpc_only_trusted_accounts: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#vpc_only_trusted_accounts SagemakerDomain#vpc_only_trusted_accounts}.
        '''
        value = SagemakerDomainDomainSettingsDockerSettings(
            enable_docker_access=enable_docker_access,
            vpc_only_trusted_accounts=vpc_only_trusted_accounts,
        )

        return typing.cast(None, jsii.invoke(self, "putDockerSettings", [value]))

    @jsii.member(jsii_name="putRStudioServerProDomainSettings")
    def put_r_studio_server_pro_domain_settings(
        self,
        *,
        domain_execution_role_arn: builtins.str,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        r_studio_connect_url: typing.Optional[builtins.str] = None,
        r_studio_package_manager_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_execution_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_execution_role_arn SagemakerDomain#domain_execution_role_arn}.
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param r_studio_connect_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_connect_url SagemakerDomain#r_studio_connect_url}.
        :param r_studio_package_manager_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_package_manager_url SagemakerDomain#r_studio_package_manager_url}.
        '''
        value = SagemakerDomainDomainSettingsRStudioServerProDomainSettings(
            domain_execution_role_arn=domain_execution_role_arn,
            default_resource_spec=default_resource_spec,
            r_studio_connect_url=r_studio_connect_url,
            r_studio_package_manager_url=r_studio_package_manager_url,
        )

        return typing.cast(None, jsii.invoke(self, "putRStudioServerProDomainSettings", [value]))

    @jsii.member(jsii_name="resetDockerSettings")
    def reset_docker_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerSettings", []))

    @jsii.member(jsii_name="resetExecutionRoleIdentityConfig")
    def reset_execution_role_identity_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExecutionRoleIdentityConfig", []))

    @jsii.member(jsii_name="resetRStudioServerProDomainSettings")
    def reset_r_studio_server_pro_domain_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRStudioServerProDomainSettings", []))

    @jsii.member(jsii_name="resetSecurityGroupIds")
    def reset_security_group_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecurityGroupIds", []))

    @builtins.property
    @jsii.member(jsii_name="dockerSettings")
    def docker_settings(
        self,
    ) -> SagemakerDomainDomainSettingsDockerSettingsOutputReference:
        return typing.cast(SagemakerDomainDomainSettingsDockerSettingsOutputReference, jsii.get(self, "dockerSettings"))

    @builtins.property
    @jsii.member(jsii_name="rStudioServerProDomainSettings")
    def r_studio_server_pro_domain_settings(
        self,
    ) -> "SagemakerDomainDomainSettingsRStudioServerProDomainSettingsOutputReference":
        return typing.cast("SagemakerDomainDomainSettingsRStudioServerProDomainSettingsOutputReference", jsii.get(self, "rStudioServerProDomainSettings"))

    @builtins.property
    @jsii.member(jsii_name="dockerSettingsInput")
    def docker_settings_input(
        self,
    ) -> typing.Optional[SagemakerDomainDomainSettingsDockerSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDomainSettingsDockerSettings], jsii.get(self, "dockerSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleIdentityConfigInput")
    def execution_role_identity_config_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "executionRoleIdentityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="rStudioServerProDomainSettingsInput")
    def r_studio_server_pro_domain_settings_input(
        self,
    ) -> typing.Optional["SagemakerDomainDomainSettingsRStudioServerProDomainSettings"]:
        return typing.cast(typing.Optional["SagemakerDomainDomainSettingsRStudioServerProDomainSettings"], jsii.get(self, "rStudioServerProDomainSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="securityGroupIdsInput")
    def security_group_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="executionRoleIdentityConfig")
    def execution_role_identity_config(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "executionRoleIdentityConfig"))

    @execution_role_identity_config.setter
    def execution_role_identity_config(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d59617e1e8766a5083c6a2b520ba16c17f97f71a0c89be642d0b66eb56d1b48a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleIdentityConfig", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5409b4ea48f5457cc516524dead92222991a795d00a427fef43af1a94d4036c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerDomainDomainSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDomainSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDomainSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1caacfc8bf2230b6e2ba7ce6603c0eb3811887c47c11957a4be88b6d2a9133ea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettingsRStudioServerProDomainSettings",
    jsii_struct_bases=[],
    name_mapping={
        "domain_execution_role_arn": "domainExecutionRoleArn",
        "default_resource_spec": "defaultResourceSpec",
        "r_studio_connect_url": "rStudioConnectUrl",
        "r_studio_package_manager_url": "rStudioPackageManagerUrl",
    },
)
class SagemakerDomainDomainSettingsRStudioServerProDomainSettings:
    def __init__(
        self,
        *,
        domain_execution_role_arn: builtins.str,
        default_resource_spec: typing.Optional[typing.Union["SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec", typing.Dict[builtins.str, typing.Any]]] = None,
        r_studio_connect_url: typing.Optional[builtins.str] = None,
        r_studio_package_manager_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_execution_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_execution_role_arn SagemakerDomain#domain_execution_role_arn}.
        :param default_resource_spec: default_resource_spec block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        :param r_studio_connect_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_connect_url SagemakerDomain#r_studio_connect_url}.
        :param r_studio_package_manager_url: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_package_manager_url SagemakerDomain#r_studio_package_manager_url}.
        '''
        if isinstance(default_resource_spec, dict):
            default_resource_spec = SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec(**default_resource_spec)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31c2866bf7197adc71305e3b209c625cd74b321542511ea5a99e43016408da1c)
            check_type(argname="argument domain_execution_role_arn", value=domain_execution_role_arn, expected_type=type_hints["domain_execution_role_arn"])
            check_type(argname="argument default_resource_spec", value=default_resource_spec, expected_type=type_hints["default_resource_spec"])
            check_type(argname="argument r_studio_connect_url", value=r_studio_connect_url, expected_type=type_hints["r_studio_connect_url"])
            check_type(argname="argument r_studio_package_manager_url", value=r_studio_package_manager_url, expected_type=type_hints["r_studio_package_manager_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_execution_role_arn": domain_execution_role_arn,
        }
        if default_resource_spec is not None:
            self._values["default_resource_spec"] = default_resource_spec
        if r_studio_connect_url is not None:
            self._values["r_studio_connect_url"] = r_studio_connect_url
        if r_studio_package_manager_url is not None:
            self._values["r_studio_package_manager_url"] = r_studio_package_manager_url

    @builtins.property
    def domain_execution_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#domain_execution_role_arn SagemakerDomain#domain_execution_role_arn}.'''
        result = self._values.get("domain_execution_role_arn")
        assert result is not None, "Required property 'domain_execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_resource_spec(
        self,
    ) -> typing.Optional["SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec"]:
        '''default_resource_spec block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#default_resource_spec SagemakerDomain#default_resource_spec}
        '''
        result = self._values.get("default_resource_spec")
        return typing.cast(typing.Optional["SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec"], result)

    @builtins.property
    def r_studio_connect_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_connect_url SagemakerDomain#r_studio_connect_url}.'''
        result = self._values.get("r_studio_connect_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def r_studio_package_manager_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#r_studio_package_manager_url SagemakerDomain#r_studio_package_manager_url}.'''
        result = self._values.get("r_studio_package_manager_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDomainSettingsRStudioServerProDomainSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec",
    jsii_struct_bases=[],
    name_mapping={
        "instance_type": "instanceType",
        "lifecycle_config_arn": "lifecycleConfigArn",
        "sagemaker_image_arn": "sagemakerImageArn",
        "sagemaker_image_version_alias": "sagemakerImageVersionAlias",
        "sagemaker_image_version_arn": "sagemakerImageVersionArn",
    },
)
class SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec:
    def __init__(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__221369be8f4fcc14bc6faa969766986649cbf51dab7f9c720cf17b9d3ae54dac)
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument lifecycle_config_arn", value=lifecycle_config_arn, expected_type=type_hints["lifecycle_config_arn"])
            check_type(argname="argument sagemaker_image_arn", value=sagemaker_image_arn, expected_type=type_hints["sagemaker_image_arn"])
            check_type(argname="argument sagemaker_image_version_alias", value=sagemaker_image_version_alias, expected_type=type_hints["sagemaker_image_version_alias"])
            check_type(argname="argument sagemaker_image_version_arn", value=sagemaker_image_version_arn, expected_type=type_hints["sagemaker_image_version_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if lifecycle_config_arn is not None:
            self._values["lifecycle_config_arn"] = lifecycle_config_arn
        if sagemaker_image_arn is not None:
            self._values["sagemaker_image_arn"] = sagemaker_image_arn
        if sagemaker_image_version_alias is not None:
            self._values["sagemaker_image_version_alias"] = sagemaker_image_version_alias
        if sagemaker_image_version_arn is not None:
            self._values["sagemaker_image_version_arn"] = sagemaker_image_version_arn

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.'''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lifecycle_config_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.'''
        result = self._values.get("lifecycle_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.'''
        result = self._values.get("sagemaker_image_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_alias(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.'''
        result = self._values.get("sagemaker_image_version_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sagemaker_image_version_arn(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.'''
        result = self._values.get("sagemaker_image_version_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6250026fe092b4b923f8f1da7c0415f1dfeaf66c21bc71ced2f4ed85690123b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceType")
    def reset_instance_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceType", []))

    @jsii.member(jsii_name="resetLifecycleConfigArn")
    def reset_lifecycle_config_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleConfigArn", []))

    @jsii.member(jsii_name="resetSagemakerImageArn")
    def reset_sagemaker_image_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageArn", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionAlias")
    def reset_sagemaker_image_version_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionAlias", []))

    @jsii.member(jsii_name="resetSagemakerImageVersionArn")
    def reset_sagemaker_image_version_arn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSagemakerImageVersionArn", []))

    @builtins.property
    @jsii.member(jsii_name="instanceTypeInput")
    def instance_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArnInput")
    def lifecycle_config_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "lifecycleConfigArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArnInput")
    def sagemaker_image_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageArnInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAliasInput")
    def sagemaker_image_version_alias_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionAliasInput"))

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArnInput")
    def sagemaker_image_version_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sagemakerImageVersionArnInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4947aa7bc93f0828de69c6808ea053f7c87fd3071a27dcc06040c482bc6fff08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfigArn")
    def lifecycle_config_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "lifecycleConfigArn"))

    @lifecycle_config_arn.setter
    def lifecycle_config_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7f14ff50d9a5138bbb2a1f734e0099f7f50ed55b019bfc32129fe8c80e45b41)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfigArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageArn")
    def sagemaker_image_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageArn"))

    @sagemaker_image_arn.setter
    def sagemaker_image_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68e0b6e0571c9a320b4768bda0526f7f6473e6738c6314a26816a77f836cc582)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionAlias")
    def sagemaker_image_version_alias(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionAlias"))

    @sagemaker_image_version_alias.setter
    def sagemaker_image_version_alias(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9e4fea411b3d5f0d142d84253174d402ddf5bd5ebd53364d29f6c318941b78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionAlias", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="sagemakerImageVersionArn")
    def sagemaker_image_version_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sagemakerImageVersionArn"))

    @sagemaker_image_version_arn.setter
    def sagemaker_image_version_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03624d077856b6ef40a23afde6c5e20892320695952d09d120bce8254b95d081)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sagemakerImageVersionArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9072d5d5566a2d205b3d10803d0fad806b515ded2717ae4a344b7af1108ce9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class SagemakerDomainDomainSettingsRStudioServerProDomainSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainDomainSettingsRStudioServerProDomainSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b8b271edacd6da35b116f03ae7ee19e415d482cf66b0a43a14f92c7d2aed858)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultResourceSpec")
    def put_default_resource_spec(
        self,
        *,
        instance_type: typing.Optional[builtins.str] = None,
        lifecycle_config_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_arn: typing.Optional[builtins.str] = None,
        sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
        sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param instance_type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#instance_type SagemakerDomain#instance_type}.
        :param lifecycle_config_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#lifecycle_config_arn SagemakerDomain#lifecycle_config_arn}.
        :param sagemaker_image_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_arn SagemakerDomain#sagemaker_image_arn}.
        :param sagemaker_image_version_alias: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_alias SagemakerDomain#sagemaker_image_version_alias}.
        :param sagemaker_image_version_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#sagemaker_image_version_arn SagemakerDomain#sagemaker_image_version_arn}.
        '''
        value = SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec(
            instance_type=instance_type,
            lifecycle_config_arn=lifecycle_config_arn,
            sagemaker_image_arn=sagemaker_image_arn,
            sagemaker_image_version_alias=sagemaker_image_version_alias,
            sagemaker_image_version_arn=sagemaker_image_version_arn,
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultResourceSpec", [value]))

    @jsii.member(jsii_name="resetDefaultResourceSpec")
    def reset_default_resource_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultResourceSpec", []))

    @jsii.member(jsii_name="resetRStudioConnectUrl")
    def reset_r_studio_connect_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRStudioConnectUrl", []))

    @jsii.member(jsii_name="resetRStudioPackageManagerUrl")
    def reset_r_studio_package_manager_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRStudioPackageManagerUrl", []))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpec")
    def default_resource_spec(
        self,
    ) -> SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecOutputReference:
        return typing.cast(SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecOutputReference, jsii.get(self, "defaultResourceSpec"))

    @builtins.property
    @jsii.member(jsii_name="defaultResourceSpecInput")
    def default_resource_spec_input(
        self,
    ) -> typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec]:
        return typing.cast(typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec], jsii.get(self, "defaultResourceSpecInput"))

    @builtins.property
    @jsii.member(jsii_name="domainExecutionRoleArnInput")
    def domain_execution_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainExecutionRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="rStudioConnectUrlInput")
    def r_studio_connect_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rStudioConnectUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="rStudioPackageManagerUrlInput")
    def r_studio_package_manager_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rStudioPackageManagerUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="domainExecutionRoleArn")
    def domain_execution_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainExecutionRoleArn"))

    @domain_execution_role_arn.setter
    def domain_execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__259d57c8c816f396b1e4a7455132d624c5bd8d5632ae624fe2447476a3b15873)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainExecutionRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rStudioConnectUrl")
    def r_studio_connect_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rStudioConnectUrl"))

    @r_studio_connect_url.setter
    def r_studio_connect_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93af4b730c7a22fce3445512e83e3ff5937d7871203d4615f939bdc222d5667f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rStudioConnectUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="rStudioPackageManagerUrl")
    def r_studio_package_manager_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rStudioPackageManagerUrl"))

    @r_studio_package_manager_url.setter
    def r_studio_package_manager_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e16ccd942f5abd81f22e99e40ad375d0feb6b061036a044a7e65dd14f287bfc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rStudioPackageManagerUrl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettings]:
        return typing.cast(typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__009d334163dfe02a00af4ffff98d4eeaf57424ee80e2acf11f7b51ae6b1985b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.sagemakerDomain.SagemakerDomainRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"home_efs_file_system": "homeEfsFileSystem"},
)
class SagemakerDomainRetentionPolicy:
    def __init__(
        self,
        *,
        home_efs_file_system: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param home_efs_file_system: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#home_efs_file_system SagemakerDomain#home_efs_file_system}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__842e0f9f1d11c737b4429c4627a4c6041a61d335ec50155fa322c3e9949abdc6)
            check_type(argname="argument home_efs_file_system", value=home_efs_file_system, expected_type=type_hints["home_efs_file_system"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if home_efs_file_system is not None:
            self._values["home_efs_file_system"] = home_efs_file_system

    @builtins.property
    def home_efs_file_system(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.98.0/docs/resources/sagemaker_domain#home_efs_file_system SagemakerDomain#home_efs_file_system}.'''
        result = self._values.get("home_efs_file_system")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SagemakerDomainRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class SagemakerDomainRetentionPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.sagemakerDomain.SagemakerDomainRetentionPolicyOutputReference",
):
    def __init__(
        self,
        terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__564bd96b1106203920ba2864ec0041420a13f92c6fb87057bb16130542334984)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHomeEfsFileSystem")
    def reset_home_efs_file_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHomeEfsFileSystem", []))

    @builtins.property
    @jsii.member(jsii_name="homeEfsFileSystemInput")
    def home_efs_file_system_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeEfsFileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="homeEfsFileSystem")
    def home_efs_file_system(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "homeEfsFileSystem"))

    @home_efs_file_system.setter
    def home_efs_file_system(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__259f7b49a8f3d1faaf5ed9d701dc4c13fe5be9414d1b638f48a9cd8d7a7cdedd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeEfsFileSystem", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[SagemakerDomainRetentionPolicy]:
        return typing.cast(typing.Optional[SagemakerDomainRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[SagemakerDomainRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__068db42e7625b19d383f3924b9acb1ed09b4a1542108128c4ba8e0bdd76c583a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "SagemakerDomain",
    "SagemakerDomainConfig",
    "SagemakerDomainDefaultSpaceSettings",
    "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig",
    "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig",
    "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference",
    "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigList",
    "SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigOutputReference",
    "SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig",
    "SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfigOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryList",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepositoryOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageList",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImageOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettingsOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings",
    "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository",
    "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryList",
    "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepositoryOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsOutputReference",
    "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings",
    "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage",
    "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageList",
    "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImageOutputReference",
    "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsOutputReference",
    "SagemakerDomainDefaultSpaceSettingsOutputReference",
    "SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings",
    "SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings",
    "SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference",
    "SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsOutputReference",
    "SagemakerDomainDefaultUserSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsList",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings",
    "SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettings",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementOutputReference",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageList",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImageOutputReference",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsCustomFileSystemConfig",
    "SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig",
    "SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfigOutputReference",
    "SagemakerDomainDefaultUserSettingsCustomFileSystemConfigList",
    "SagemakerDomainDefaultUserSettingsCustomFileSystemConfigOutputReference",
    "SagemakerDomainDefaultUserSettingsCustomPosixUserConfig",
    "SagemakerDomainDefaultUserSettingsCustomPosixUserConfigOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettings",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryList",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepositoryOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageList",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImageOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettings",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryList",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepositoryOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageList",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImageOutputReference",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsRSessionAppSettings",
    "SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage",
    "SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageList",
    "SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImageOutputReference",
    "SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsRSessionAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings",
    "SagemakerDomainDefaultUserSettingsRStudioServerProAppSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsSharingSettings",
    "SagemakerDomainDefaultUserSettingsSharingSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsSpaceStorageSettings",
    "SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings",
    "SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsSpaceStorageSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsStudioWebPortalSettings",
    "SagemakerDomainDefaultUserSettingsStudioWebPortalSettingsOutputReference",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettings",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsOutputReference",
    "SagemakerDomainDomainSettings",
    "SagemakerDomainDomainSettingsDockerSettings",
    "SagemakerDomainDomainSettingsDockerSettingsOutputReference",
    "SagemakerDomainDomainSettingsOutputReference",
    "SagemakerDomainDomainSettingsRStudioServerProDomainSettings",
    "SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec",
    "SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpecOutputReference",
    "SagemakerDomainDomainSettingsRStudioServerProDomainSettingsOutputReference",
    "SagemakerDomainRetentionPolicy",
    "SagemakerDomainRetentionPolicyOutputReference",
]

publication.publish()

def _typecheckingstub__650f7b8434805310d757aaa0d233efacec64617bda5906df5766e3e4e3a6b7cb(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    auth_mode: builtins.str,
    default_user_settings: typing.Union[SagemakerDomainDefaultUserSettings, typing.Dict[builtins.str, typing.Any]],
    domain_name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    app_network_access_type: typing.Optional[builtins.str] = None,
    app_security_group_management: typing.Optional[builtins.str] = None,
    default_space_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_settings: typing.Optional[typing.Union[SagemakerDomainDomainSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    retention_policy: typing.Optional[typing.Union[SagemakerDomainRetentionPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_propagation: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cbc910ae71c114601d9d1c7569efab3b2f2c0de56fa601fdf158184c6d66f1c(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da86f98b35012a6438bc87e6edcbf9ef948efe8749ca8e1bb95332e367e5de6d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e81288f06b5774dda2f36d07735792a84409d8f852a3f827da5151f53f19e47(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efc3541c2d8406aebd8d743b93716cb5e9e8ae1cbfe9591d36570393074cd829(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6192a792e9e6502b90adad646ddb07e164c2229b99b9f32c157bd378205c4d9c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ebfc81a49c9174dd1add3ebe9f51484209c027ef20d548fd3a10d52045b3f7e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8bdc0da6f7f47013770cb4d1d39626195d3d96f0559972fddd3c52300de9b40(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__733c3c6a865d488b9ad38a638497555cb18dbfb01b8e72bc1a7a38d6aaf55fde(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d1391862b19d51601a44b6fd1e98f6dd398ad61c5b5d7657e3c172cf49b0ee7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63ba84d2072211247bd8c7cabc1c60c84c9637c08c86ef38cbdb57f19f07b8ce(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0424b7faa03fd3a1ef81a34474d4ad5ee3200e5faf2efb7f1da1b7eb923a7202(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9128e511f49b5ed158e2dd3840f9205838af10e7a523f9fde45fbc1124c98f02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ac367461aed0b3ecc30172747fccc340b4ee32e6a4d1fbe360c36a7b659b7a2(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    auth_mode: builtins.str,
    default_user_settings: typing.Union[SagemakerDomainDefaultUserSettings, typing.Dict[builtins.str, typing.Any]],
    domain_name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    app_network_access_type: typing.Optional[builtins.str] = None,
    app_security_group_management: typing.Optional[builtins.str] = None,
    default_space_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    domain_settings: typing.Optional[typing.Union[SagemakerDomainDomainSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    id: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    retention_policy: typing.Optional[typing.Union[SagemakerDomainRetentionPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    tag_propagation: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tags_all: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d74e00c91ab3c174f7621417bde6ca95e8f43b9dc078d8e45b7695a26e5dd90b(
    *,
    execution_role: builtins.str,
    custom_file_system_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_posix_user_config: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    jupyter_lab_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    jupyter_server_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    kernel_gateway_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    space_storage_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9583a8ad8ef11574079c180ed61f9aeadbaa09794c12d05535d900e45fefe90e(
    *,
    efs_file_system_config: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3928de76a1d29034baf9be5cf0a4760021e5762239fee4d687ddad6fbb9558(
    *,
    file_system_id: builtins.str,
    file_system_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fff1045f9215d09f90a5d7644d83f84e6cdd13df949704772e7666ca269a647e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66809853d1240f6bf6aa20df0a4d5418073fa2849c47cd2d658e2fd7cc566cf5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f6ccf3227918a8b9e66d3d938d1baee1b3feeee075b557df9b4351289116171(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee208fbacb75c8b41702f810cb469798c4842ba14d8bcfad97a830dafee3174e(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfigEfsFileSystemConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a457e7a6875ef874797e895608206d8d30ee192993f777e878b09978dae6639(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2a2e3f84d08b125013232a04dc217d34e4e0111f3f7f7e0ac39fb20bca6f621(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__135469d197234761a7aec39b668567be77adb3b8e816d430958642ba75a4895e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a257d675195faf2790e2d316adbd312043476d2c7f284d2d9b4e356748f6b4b9(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f9d993162834ae200cc1b6cb7cb5ea0aaef22c9b464d7a2445e6228acf6a8a1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56e37db9ae7e24db5f741032313743fe38c8464d6ad3b8ffbd906d140dd8892e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b09a0ea4ed060a09bfbb38f795d22df2f1c55cd6ac1a6a32eaabbf8f4af80eb2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8c3394136dc5f06c3ac310c54c942285d2e1d2f89a33cb3c79bb3a6dd92318e5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__538cdb15884da460b5fad0da25ece03f898d6d419173e685193ecdeb82fe16c0(
    *,
    gid: jsii.Number,
    uid: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6138000690bf20e7ef60334eada24b5ba7ec528c0ef5488dcebea4fa03a9df7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e61c4f89596fb4270a5d3964e0af151da90cb3afb684d4a1ec3df7ab4b81c24b(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__204ffa67f1a553fc10301e1dc2d0a11c79c76e98add0e005499f743a7a36793f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2f6e0472cc8689a7d1a221d07f16d4fe1b9a103bb9f53cc68b88981f9c71371(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsCustomPosixUserConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__995ec60bbbe3bd48bcffd04f83dcb6883574cc06011e2fe9fbfb4ed4ea39378f(
    *,
    app_lifecycle_management: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement, typing.Dict[builtins.str, typing.Any]]] = None,
    built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
    code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    emr_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__580f11d0210e6bc1aaaa37c57a097504299853dd4470c6fc19f38c2f5d953358(
    *,
    idle_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7afb3319df1de19eb793ffd9d7edf02f031cd7f6d5ea9cb270dede9cd025ec47(
    *,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    lifecycle_management: typing.Optional[builtins.str] = None,
    max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b403f368a8abb768f32efe9e1e0592eed145df7326aad4539896506dc17b2aa8(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b33d4d9581bb6a3ca3dce3aa32933569a705e9fadf2f442a52f7785640782485(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30367fd982a4bd3e9c4b6d36ef7274368964ce3816d7ea57102b11b545d035b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c5471495db964be3932fb1b232c260c61b8a99c6291f80b606d5fb6bfb9300(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8daba92f978d6422f54c1b5bce7eb504cefa5d77586922908a31533da9b6ad1d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__654c4be39b0e9ec2ca918e9b7cf8ee05ea59af7663bad7481ca002c7ab8c080e(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e6551da586deedd11010edaea3e5c593ded2c1668e4abf83b08fe7aedc6e0b6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b34974ac2149421b60a27d7a876813f47cda85a47569903886033603295cb3e(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsAppLifecycleManagement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__930bc7db0f6b5fe7316c642ee7d31513497a2a722262e98aeaca9784339554e4(
    *,
    repository_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8144abd8c9dafbae8aeb5fd5f0678f11796d388073d98745a6cf8ee92e0c438a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28464adfc480be381dc45c7666fb2e896c0eb3358774629212cb5c9d4a4e899e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bc8ebaa8f0dee1551495c0755184d2f894caa14bd02b2d90d7a15ff514cbd19(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef54abfcf10296131d32e2c4dde2526bebe870e695a69f857bfd2983e4712529(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3bb56d9d4bfa2eb2aa5bbe2325ff91f4d55e589df8b07aaab36ccc4c2fc77c5(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45bb5287f63de03edfe5defe595e7d8eacfe4e896e5618227dcd337ec93c7706(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04a9c9882e4d952e70c07834a690e32b942ef8c2ced960d7e16842bf2c22f254(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc0a28b618d87087cc64a9008d775d5b592fce773fd35931bc43c2089a7969dd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dc1deacc2f1a459588b9d00166d332070f9e716b2b3e13326fea5c278a1fb8d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3aca4ff21a9d79440a2cb4b49dba8eeb9fbb829c07ae32d3d7db70ba93014e1(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d2c4518dcf2196966167263cc4b6596a76060916b2fecced0c7b0ebc5f30853(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd6941b02bca3daa850de7f73143b232706d013269ee175e75529f8f61bea95a(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__facc6d3b1cf3928ef092fb2e13efc361ec5da9e882f81152013875fed70c09d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8beb68c98a6f4177d58ff9ec6cb9441057c4b94d0edc5ec41b0e03c4949516f(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676321d6c60638dd9e2dafeafba2b22678ee45880448d9968bbf6905491e4f39(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414695ec925c10118a7496712e3a72626c35c7ccc8a17247573296b9a3f51ca9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e3ea2bc892eddac4596ee9e451050258fc32aeb09a74a3d3ea63ec76028a58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2307771c7c7b70637f5bfa1ec0ec19211013efb78e536a4a3a962968d5ccf11a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e301cc5b19b0227fedebf84711bf81011c16548662735af0871812c6a8dc7c44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1475c8c365d256bb675c82e90d1074b09d6c53e898bad4d57906099098e3d28(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8083f8b0d3d69117265da4336ab010923be26a31f36606e5988fa5a24428231(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73cfc4c0c7d8f5c6d40d98ff9de454e4b47d94281fcdd00b8da9bb32af5d221c(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9970c3e8a8270a9bdcfd0dd23c34fd3408d64a244d057218939c848deddd6c75(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac112f5ba7aad546f955ae1642bd4e227e2cd5a3f1eaf0f938b3598a1b60a9d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__536cc75837d26d7729583548889ad10827cd3b485bf45bbcb7338bf9672605bd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d8c31dea618ad411c6f5351a8218a2566b3949486e110cd9b3706d2136ec4fd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb535c521d3a8668eea2c7f5b50050d03e0923b238af30883b4762fde3f00a5b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b310a01bcde4aec3c655c60b6c6f161d39ed409c48b954b5a1043653279027a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe0542e79c62bd186cd4cd271495483e5ff4dba30cf40fc765bc0c488247c7ea(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8b667429c1bd85283161fb998d67c6b9961b20826a651cf699c2dc1076262a1(
    *,
    assumable_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    execution_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39bd2bd2f4bf047e03156f719cf3e3a6fb571bc490219eca1256f1d83fc988e2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0f25d47018169a701844b2a1b92788174866acf78e684759e6a044788ff791b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6206b0dccd704b95fe47a91a6613b11a87f90a301709459ba82d497deaefaa8(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca0c2fa8f267e6727a2ee572ad9f281e9972c2177be076101fd4d057496cc50(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsEmrSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49dd8a59b066a04f05182ed66dd59a14659757ab94c9b47d466f37eeea29608d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5be887a8fe9be03d7133e1de94290157b715474027d90a94107f6c4bd7b354f7(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32cce408dd6bee51e07d7895a6fd693ca127ea935d300b6231303a2746f57f0e(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaf6d71bcc143bf2d611a13c4d936ea520d03a6b86fc146ec40db20807801f6c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a53b435809e2be1bbd825563644d4c50a3165ff7022b4d416cf0b2bd5ea28a8e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7710bc82623e0c8ed649a66bfa6bafc7dce650c7585ad856479735cfa8f1a3c(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterLabAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5154f237ee2b8507f6421ee32a6539564f23ed763cb38cbaeacc257edc85cca3(
    *,
    code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3254acf9f19ddd5d3bf7cc43b236a82fa035c3fccfcbb4d12e8af9a055b2115(
    *,
    repository_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab6f8a5a42226bbe15fcff88138729fa0e790e2a2477661e1a6257b82fb26f4c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45a2ccc785dc49201afcab1fa3d22b359ac3b755608c491798509a939fc6634d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20b601efc5d3c066ff83dcb8f5c3413ea177645cfb2624799b88ec020bbae99b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe3552e704ab49cadabcac64bc36719ce2c9fdefb21d0ee0d0579cb064566f06(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7be93016f1804dd02d692d9461bce3702bad69cf45a62c1b342ef9c9e48492ed(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5bd1e72746108a85ea60ce50bbb6fe038f50adda179306c2c85c8827f882850(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3bbb68f9753f4e2a3b92b4f8548953d9d80889b69e8406ff205680d11e1b888(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7ecb6401847524a3d4da168758d44d9822d8872115b654f826a36a919d7cecb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e21ee74cf164eb51ab896f739ff2a0474206a82b9098c26cea0e3ffc2539dd(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__609812c3bf3e7cc9fa3ed0fc9bd3e96e4779215025a0d6c47402e25f371a8140(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fdb00443375cf1ee212b6e2241efada44f7fcab25fb1ff06be4ab8ef02a7c33(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37fc018365f9bf0426f9e65769821c321122909157a7c88c53f6d1f9e0f9f774(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0900adfdd391c977541fc0ce3f4154fe6c1a0c883d4938be2192c60f7c1ad2fe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01eaf757b8e8703d72867ff904432ee2d2251f5780d62f23c7f1586a86c54f76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a384686e7f69b12d9a1c352e0b02a3469ecbb369e5b68431b5dad088679fcb6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57f80745fbd9eb14f965c048fd294dcad878a97b7af6b2b0b02b83a5542bb77(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82bb7ec117acaf099e00220e3af66564fe7fb6d2706a7497f56cd44e4644565f(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bda23e5fd96bf833f314326e70ca4ee51ebc25efd4825cd4de1af8acadacfb0(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd02f5259a981dae250a23d8f03b3fc61f03c4cdec1e7840f4c3d4c52f9521bb(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c218637f0bd9a7fbfa39ce6ff70508f543640c1ccba76f1bee5cbce21702c52(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b509518d952b62168889b933b53f917f4771c145cc34f67f70824f4cc78399e3(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsJupyterServerAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc7338cd6ac83eaae60db20cee9d1a20cd295b8830add8f4be630749b8803c0(
    *,
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3273ad019499422dac19ba9ea05a581c473ba498db14f68905cc4f9c5b974253(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46d7df5f1ef05c9304d9d613f8a13d5598be70a33addbb2c9a2041e0d7a20170(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3df185394ab8ae4e5d989c3e563b4f5214014f07b7d9017662b41ebc7ad70114(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f79c5ea60bea0c69f5d2658ea1aa464c9f0d0d9ef225b53b0475a547ff17d93(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8af5a2cec8839fc03027e89066ae4478382f70d11bfde8af695d7ef0bb69d372(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__774d6c26b121152beb5ec1b8c808f32730310d35689e41558d83119b09d19b58(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfe65595b7ca1577c6dd0cf0507c7ee6eb6e31c428dca34bb8ab56bcfb4ae288(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7aff8b411f65329f2e3ea8a475aa5e32b1c84753a5a24e5205c9904f003747d9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b991d28e1c533f3d2cc626eea4b62ff1db378fd9508edc878dfe9b1649f4bff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8893476181e33dad23c8b74754dbd9c00e55312b3705e2d076c86a0567f143ff(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e204cd8fd472639335b9bcdd615111574ba7dee9c4bdaef626d2de52ed799c5(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974b31bc311a86ed66d7ffded809ee9f73ccc4b55334ebc960a611c2140e38f5(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f3d1c2ef281b7851c10c5016c3cbf6fecbda5bd62b03bb5eeaea6f5489f1d9b(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b62d08dffc7b7f84b7ae8b522b8bc2c3c7fbf405c9e3947d741eed11144dfce(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f87d61a95a3611bb64775c2bb130e9c996c39ee5dce9185ffb6eb32e946ac882(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73b8af28877b84469110dc1bc98bcf9ee26607be04c98ee19afb1acb7c875bfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e544c96fb672ba5ce95eeaf549a272c6cab0d1874dc12be479a9b7736db3dac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8adeef9ab41d4b9172bb948f58bd00fbd8a6addbd18ec9136edefff83e3fdc98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98a2b96b8c1b56bf122e90864ca070648e94473cf034262ea15e1dbf221b1bb5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd77160b904b15d1dc31a5d9091be80c4258456aa7bc87e3cc4e43027cc0f97(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66d37a0ec834d50af22c3ff4070fc0d052e0e3f788a247e680ec07a218381c8a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6417ba3d0a5acd1aa737f248d1f3a9d81c5e79321a974a767df24123eeb569ea(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb31eafdac64d3e6e3bfd15f3583bd20ceccf3c68b569c26b90f829240739757(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31b050007d6c6a399a121f781b3bef5f31f06439a10c8822d842333458b5e3e0(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsKernelGatewayAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce6e0894a3843bd3e642bc9d3d758e17bb1c66fa48a4ed96c7757a5772de38cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc80e64d21b3af95625a8f1962ef5a8cfa62aae0ab52399cc27aee2a593bf5de(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultSpaceSettingsCustomFileSystemConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d86f052e667b6a80c5843b8c426e49d78556856863017cfd74068aed90375e5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__430740fe3a75ec98683fa696634abb8a78562846f0f65b5e4b359dda3cf7188c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1baf7357a6a619975f802f0da1e14c7790a16bfd8690c09873915019c3b12f27(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__805edd6253c40f2698faac414884fe288bd743d9dff3c1fda5ad142afb0a92ae(
    *,
    default_ebs_storage_settings: typing.Optional[typing.Union[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa0ee7bec01fb410f270af32f2469c6516e056171b39bb558526178b0478484(
    *,
    default_ebs_volume_size_in_gb: jsii.Number,
    maximum_ebs_volume_size_in_gb: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1a667d234b927a66e7b164b23201c3430b5736e25cfa9b640291cd794a463be(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6b82fa07aec15a069867109c0a50bb87b2be1b519d506aecfb9a531439278ac(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__619834be4c40a9e4739d32f3299306b4c73844dee1ec4cf84d49128b131e79c3(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2877358a825b0ebe24e0c9e23aa9f3c56a066e7c4dc4a00e162390b0499feab3(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettingsDefaultEbsStorageSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__532dc8b3d2c196af721aed9b74e3e72493fe2932d79ffa70a08f84adcaca2475(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1655fdbbdeb55603a7c1c49191308a7aee52c6f77221f6285dca31c80a17febd(
    value: typing.Optional[SagemakerDomainDefaultSpaceSettingsSpaceStorageSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84027cf9e196018ec72042a2255ea078b318e0785b2c0e48697f1db2b8c2c45d(
    *,
    execution_role: builtins.str,
    auto_mount_home_efs: typing.Optional[builtins.str] = None,
    canvas_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    code_editor_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    custom_file_system_config: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_posix_user_config: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCustomPosixUserConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    default_landing_uri: typing.Optional[builtins.str] = None,
    jupyter_lab_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    jupyter_server_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    kernel_gateway_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    r_session_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsRSessionAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    r_studio_server_pro_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    sharing_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsSharingSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    space_storage_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsSpaceStorageSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    studio_web_portal: typing.Optional[builtins.str] = None,
    studio_web_portal_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsStudioWebPortalSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    tensor_board_app_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1c55e9b3a8ce9d4b8d97d76c1ef2b544a58f4b7ec5aff93103dcfe0cae3635a(
    *,
    direct_deploy_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings, typing.Dict[builtins.str, typing.Any]]] = None,
    emr_serverless_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    generative_ai_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    identity_provider_oauth_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    kendra_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    model_register_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    time_series_forecasting_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    workspace_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee3ea0b8df0f858249d51f258619343c9a1ada3a3cc84a047a234b90b8ce556(
    *,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f6cdb96c24b50176c931d7d7b853a47e08eef7af86b9542b134bdfa7b7c5b9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ccb9312bc3deacf6006aa291d6f3e3b13dc6f88eccf84620e7c841957147ab3e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c42b0213addcaf73bc56179be11e0270df6216b3e352a1219a6d8ca172fdc12d(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsDirectDeploySettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__134faa03a2412f9526cd54d6e955d709957e79fd1516dba293bf8417f7d2c66d(
    *,
    execution_role_arn: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb231176fbfb4fe12f151b1dbf4ff898c42a70340ef85b2cc5b80fd035005cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6262795f39d2a6508d91cdd672a3e2c761683db11b323aa71f0396c01fca669f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab0e3ec0c23ff996340c5c91310075cf5a6a9a9d32cc61d5430433216075f26a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f98407e1af4e5e8d23dfbc2fbf565ff4f56d495f491837728032e308096aea65(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsEmrServerlessSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e8b17c93261d812bd8929c408c157796a5f9c5a792832bd121ee0f1b2901e7d(
    *,
    amazon_bedrock_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57bc2595a47a2aa79acb689da2c648638cf59c1cace7e226f53d31bd4c7eee6d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5535603f782a709fea13bb4dc5293d66b1cddbbe297e102800c7afd30b4c87b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cf444632b42c4fc90cf7eab821a61d17203dc2d66f69ef2c16b9a9439592991(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsGenerativeAiSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__345a04f420ca45dd51435f7020612229c10ecd7b71934540ca68c84fb865118c(
    *,
    secret_arn: builtins.str,
    data_source_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69cc747fbf67645e32b1971499bb6073cad1955a34b1618c3150e395a75f87b7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7510efac05f19d62f4b3da82ec52f59cdcbcfb91989a651b83ae44950a86ecf(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__497340397d0357765dd9b809647a09e2cc4dfb94ebcb4d223942b7f07f378ce7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d01b121d82c8db331ea67cfc91c78aba9a7280f1db71fcd68ba726f901b031(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b037f848a4008b1b7957a2cf06ae3de4f224ce72bd5e5ae1eda53a95d43c8ce(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09e36f90def99102856cf5747d5381bd7b2967989e7423b9b836a203b9abc684(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37bfbab9834e3134377f0043e5326a00bc8a4a4aa98f30eed15280ab4ba6429f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddae419aae762c8b0db6cf48ee0c1b9fa2c8027846376b7adb664a150a3c8e10(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59b6457ff17dc410e63eefc27f7cfac399186bb6d4abc672ce037ee6d4c219b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__560692b9020fecb2ed047a9b12acab19eb69905f697349c204c88be63f2d04f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__756eb4094e955a2513336736bba012bb45a7075181ea40771fddc2f1b193a899(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de7fbd340c3001e203d31b5c9db7d28127ff83d7ed1eb5fe1cf23e31131ecc29(
    *,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b760987680e6f4e3b56c5d464e3face5624fcf1e6801c99a08d14dca749b5da(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26143a41d93c41ad15fd41117cbd5c049e11c10c994fd4eadf9da39f7fcf08ac(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__254abb492fca1fe2f7f372fc7bcf5be2698ab7345a8aa92210c3a1abf9d88431(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsKendraSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29dc19ede1e3214e365de2371ac5bbc6fa7dac50c30b3925cb51961232279832(
    *,
    cross_account_model_register_role_arn: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ead584a3bee88661e7fd863a791e674a908006eb31b722d2882dce2699da075(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9005731ad3001e61a45644a6997cd8eaa1c7ebd60852ef3bad4b9c6f5511db04(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac51449ed2a9befdf80f563cdd1e27373db6c7dda8678400b5470e02dd14d5e8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96b809baab14f61f11042fbee9150646c2eb313696c72a1c381b1f787bd63407(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsModelRegisterSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d1a00611932826a10be7923cd7b54717477dd6a75d33786649af12da89712c2(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dac00143b28d3aab1f49f1b1511d6d29970b9094819a83bfbed4fa1416ecf4d(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCanvasAppSettingsIdentityProviderOauthSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc424aa328649e3e07a2ceaf41a05c9ee924e02d55f0df645888da8feddd7c0(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3fe434b6b523c6594fe81696f5b991138396fc0fbb2b0cd9ebce4268b22348e(
    *,
    amazon_forecast_role_arn: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8785365329a3901a4e83e39db5f7881873cf74d3f6a93a99a3b6fd561e399394(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf4b9c61e22b74b4f4957152e45f1ec2d69247f08e7fc32e1f3a2433111212a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa11e7da48d6cea4439133902a85d37feb54f579794dbb15a23889fe73a6ca16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440b9a53353debf15db39bd473678a82cc251fb598dd12c1a9af2646bf309ba7(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsTimeSeriesForecastingSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__718365e39a31f0e791cda0850a95d7420c411016309de3a2ebbc248291d52a13(
    *,
    s3_artifact_path: typing.Optional[builtins.str] = None,
    s3_kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f01af8dada41e3e96f0d327412032343ab4dfa43aeb49a2e36c145865dc38047(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5e2068431661f5d5be9a51df0efe295a873ee02b5d349ed4d1112e15b5cc3a6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00a748cc1d5a90594c32b6a2101dcbd6bad4ff2452a8c4a357858f99f35c4cee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74bf76376ade139f14b8f75153c1b941f519f5ef7d16fe91bcff8d657a7c743c(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCanvasAppSettingsWorkspaceSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f045f1aa18429b3aca2d473eca7ebe46fed1cb27cfc241b9eb9442365845180(
    *,
    app_lifecycle_management: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement, typing.Dict[builtins.str, typing.Any]]] = None,
    built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__455473726a7be0cbb8540fbe73946fb99cd4933b8ae9a342fdb73c9fd8b88ccc(
    *,
    idle_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ef8e395ed19be6bccad7304554562dc124e97f222b702ec5fb22da0d1763248(
    *,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    lifecycle_management: typing.Optional[builtins.str] = None,
    max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47eace57243a4ac86795ff57fb0aa86040ad16a6aa4a317fe5de66ee8a5640cf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3e70e1ac8333195885ae50c4ae2dd6ad5d51df3773ef847a31ddf31e0abbb7(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89947bdf8323558a316343f17c89b30975cf1370bb50e1f7d6d210517b02dd1c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f165fb9ae8b477327f29cb124ab886002b152d8473e18359a954ab21213e61e4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__012fed8790fe8d7f82be038d52a1587b9b920e78f57dd89d5032a0d894319b8d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__362772f29d83c875e12359c1a907d41888f7e91917150521285bfdc4808824b0(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagementIdleSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f37a5be7587dabe2afc474e1234790d90e21062cc3b0ad13c5f7635f149b14c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eef3d25929a1510016d0fc29695ae367886bdf17de247c0c3ad41cebbb8d4ed(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsAppLifecycleManagement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa68764766f52bf75745999485706a17141b2a531757f4f5febc30b4083c5e15(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97634cc73f7afd8ef2e693a144aef2ccca9b9e2ee6516f86ebae2aa7c477238d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d34f70ed27e7a4e23b88284a46acf5b6605fec16c85ac206a8cdbdd42fb60be(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f90231e7040a5caec7cf1820f64c4247967ba071a73b3aa491daecdf4e1f8ee9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__625b628429d02751a097ea58103041e45ad83eb4e322d0d9a953e7c2b5546565(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78d2a36a02e45622437917f1aadba44ee0e2b6d24acc51a2c68804d651ded09(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3eff2aa777c127e42280ab601ab5ce00ffb5ff8ee21e1ce29900aa45c128fd2(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f27c594c4ca76591abc9f39a56752abcd90a35f96b0c67d1d73bad01889fdb(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__419a7b7fc769f6a4c53b53c62064fb2fb969b700940612867f281229dca71815(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b0e1058a31b978ff13d90773af528913cc41433bdea8a7ca989d7dcc40a45d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63a1a1cbfac5d16a4c75939dc6e6c2b938f7c6b7d2ea49fb60fd89f3612e30b2(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f5de024d20ea6ae6fbfe19fdd233dd353c1feadc1c49527578a227bf8d33cf9(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17a79c94351c8b0edf8ca0a2c991eec71c170af7fe9cad5778e0b7c1f84a2e13(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0853b9092d43032aa8dc677c92caacbdcc1c8d75911fee941f0c2a6d432cd77(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd9bfba41c4c9e62bec14249cc8e0333583c40902fa7b057aa7824368266bad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00db2b924fd2d5d39f9ab1c698bf3ff679b31d45aa9321f7a087f1bb855862d4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3306a758d88ce61feeef6794c9226f1c0a3a53779feb523621384cafac242bd5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a2fbbac8b45330bd4aad1c1a8fa675e0dcb9c212e6b569efc388ddc0c1649fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ce79996f13457b20fd79f36a5ee99ace09657f5c90960ba922426504c1d7da3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5eaf06c378f86c3c5f965ce86561a65329cd6e3e9be592a71f8d709c1616ca5(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b4edcadf6988c03541327ee99ef03b5f511381ded284e83e9cd4c3f9607eb98(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a33c86a64cda270b09589b5d793e30a1df8bad754a71fe5cf2fa61fe6efe6a3b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCodeEditorAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff8c4e726b8293b7439363df6b03ea1905f73b4f59a734c7142d6aad201dd7f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89d7c72b9af4981231dd96e913ae7e6890fd4853b36bf645ca60a07829f0415f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5933a3a6433328b17c8bb90d745334c3c02c6d9a1784f4411e80a84e49d63d67(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCodeEditorAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95c0ef8a682bca3e91062c572071a36b4af1b49c1f46974969d26472cc3dcbec(
    *,
    efs_file_system_config: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c600cbab23634e21c38f4bbea3dd4853a0bf9e8e190d8a66ee9306a8b6cec94b(
    *,
    file_system_id: builtins.str,
    file_system_path: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8c2a94b1d65b3fa090ca483b538aa13a29bf51ff2123cfa821dd19c3ddbf692(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dce20950a05ca382329933f167a4c77912a87fea56af61d149f1708e8dd7cf9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bd45546bbbeb154305daa13fef5b6ff0c40b14b8010ab5cf219c2876b1bd2fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__479ebaf6fbb33820c90d306f7ebc864edc0586ff2c7b150d5c448cdd86d68c80(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCustomFileSystemConfigEfsFileSystemConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06df435e7e048bc650c1fbdfa2e80b330c1a33480b806887d425f60fa090715b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65d306ff2ac4ccb3fc6c900d55737656ff7553a0af1a00e639772b1c01fa91bc(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe3bf7b9207cd8c3d8ce4e512ff047a485364903fae4c4a2a06ae84c1b00240(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca29aad4591761237e66883043fc56f8826b5057f087eb56f90d6a78a55132b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35f349e95e1649b8704815cbdd980c74cb04033ff688ebe20f96f39793ba026e(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be93d4cd47442a92c35bc3b9a4f08374224e4265cc98a17476d26248d972671f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd498b283e1b95a98ea8e56924007acb40b499694b989d6fcc956c467b43080a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2f2a142c712fa27a8244446c7295cc4348415cecfcfc4404b6dc89cc2217d01(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsCustomFileSystemConfig]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25df54619d51635ef2b9b5d67c78c1654b7857b621317f8fddc2c8ba368c9ad5(
    *,
    gid: jsii.Number,
    uid: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5900eeb8b2a46b21af00e0afeae2117f21ca28a0246403c58190c92d8a9bf132(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff3a6f385817ddc4597656570ddd1aa1748e042dc8a417fcf291c9c1e0923d5e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a02b1bf5e141f360c327be30f3a8806f2dec2021b6b382792bf649e59b2d7208(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c42382e815d2039497bab8919558ef0e41e8b03536d050b9ac5971861502b88e(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsCustomPosixUserConfig],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a99a5eba778f2a834421178883d1e5f0336b16396708bed7516c3bba58395c88(
    *,
    app_lifecycle_management: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement, typing.Dict[builtins.str, typing.Any]]] = None,
    built_in_lifecycle_config_arn: typing.Optional[builtins.str] = None,
    code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    emr_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c89d00afcb07402713dbb71a02780926ed1556c71d3443e4587b5fb2cd3712c(
    *,
    idle_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a84f3f55d172118ed3b8d33ef3e62862b1f110e7792016262b93d92c69ab046(
    *,
    idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    lifecycle_management: typing.Optional[builtins.str] = None,
    max_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    min_idle_timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2c13da4a3a5fc2c2645e949a245ade3fc000578bc0477b1996d49b0087923ee(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__618938f2ab6a86c1e1f8fef0cf96fcf8a4abc68564e939b5250ae1af7e51bcbd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dceb096b3314bf482eacbd72e4c01412a41f1c7302e55f3c50437e72b1236762(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6f8fa08081e6b1d613228970633027bacfd9e4920db0bfa44e669cadd8a8a3c(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a2ff581882c67c8154190c9edc0928c8e978df0f4d5c74a8c250c5a2d5ce46f(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b578e3bd91b805fd74eec0b5ac9c5370cef3abc7fb070e024837ce5fb6c1bf5b(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagementIdleSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed3d01f350347dec180d1a15d9be20460e9e24464a6d6edb1c8980cfb1fbbcd(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18e71f001bf61b91a13f586d10708f9bf9d2effa344aac9161a7c5b48d3eb27(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsAppLifecycleManagement],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082012904e51873cb6e2b1660533cf0b98add24b443afa87c2cc4075a8754b8a(
    *,
    repository_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3950df25dbcd249436d8ec88537e53f8ef8eaa942a12f86bd65251d7c4a74c52(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb50972ad14a05db448dbe65b28f428d236189dc598cc63aacd795590ad1ebd(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5573606be8469b6bbbea91282d62e54c08deb5e2bf7a089d6ded34b6ed8391d6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00159e2c0f6b087e063bfafc7056077ff9474107d75efb3996f3f88f25f37816(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__55447606a35ea6e173a4dcc048de44582ec589ee877b7b6268f83d63996103f4(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1ea44865713d585997ffe3f0bc26d5a83f5855ef53697e88426ebdcc66a7755(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b29dcf66ae582ca04e1bfe656369efbd2649ca5dbc1c145ef41a035c3482dec7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d2db9f312815c69ea16aa7c11bf4c237da5c2835c5429c2396be00279a02d97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da5c6be67404944b458bd191a36ce81608b01facd78af24f41df0e85abe117b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66b3e2ab27db2eb0157d8f02e1766a363119d026d0218d774bd90c9846d0a18e(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fde686806b6d91ad61ac2940ff6b7f863536538ffdc16944972f9fbb5175d29(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dee072c7e91f7fe7b5a38c6a0a8c8df1ffd6e59ae40acdd7fec394e43cc12e8d(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ca271ce3e06873f2b05c136944cb66de0de5d923a7c9757c235d226c9a69bc2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f96271ca2a89e6ebd1291dbe34c8777e1800e7b41b055ae1a15f0aee17a03670(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9da61823c9e9102d6e5432565840aec6404b132b3d4e8424822108d89e46968c(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2dcf36edd7bfe30d2a8e13fd169dab1dfe092355a93d6673a18e277fd5052a6(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd7bdd188053274b65792a37eee58c7f8691c641861e653783144b1e23b53ec7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04df0d629ccdb101b7ff5032705b9ccfe690fde80ead8d75f5745441cbba6466(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30dbd3465426d516520c17d99e0f6b23e7aa16d60248fd7100bdc52c8d97363(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a4f4c81463e27e19371aa67e34c8a80febdbed037f52ce5a3e80149b53ed2e4(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda1f1ef33d2f883179751bbbaf34f70b2178df7e16e86dc921d52fcbd4ae15e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bfd73f44a0af57a3455e87acebb44e17baee4dec341c5235beae4646652acde(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60ea2cd4faa14099cc14d148aa4d96d3bf136f37ad56f6e1724ce9a09ff2e55c(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ffa8f7fe9d37221bd460e59fbec479651dd539070febc00a3a1059a1f134c8b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b08712bd44c5392a3e1f2fcad8fb06fe5fcf1ae4b6ab7f280ffa4eceb56bf47c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__895292a9bdc21a9a47a993a2a72b508e2c7a03fdb87d37df2057b4f4ffe25d69(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ece5484d37f88cc0d07e8f002c6fb118683978c0598839c27ce82adb48c491af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45148c577319edd334ab59a731853b54fae3aa7a39e9b2f0f56a60bf802afa6b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d30eabce76bb128fb8d1b9e86774a1b19a5c7bf711d59bd723c057b9cc4619e(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a0854eef5e5bfd1a2df83021d701fe6f3bdc4d9834f4c8256f39da8efea89aa(
    *,
    assumable_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    execution_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5e1800d941fd02fe589270bb913ba80834cca41b80d4f806d77b4398e16ea8e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__974af3375823ab7dcbfb030b03c6e5a1afc0b9d831227121651ea2363cb325f2(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25cdfd1d63dbe52f77d28cd8fc0aa9bc3eeeff2cc45ce4e3b90fdb0149537b19(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__500de7810df35edb024ecba3cf4bf6b557022c6b2247e77a27df703129ad834d(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsEmrSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc795a33f4f745d2648dd69ea5cc5dff7089f3b719255d345b0c231f96e243c9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78bb1120f40359022a19272e11680eec6fa3eb33f716bc13c2ba37f202159e6(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3abca97be5e2757ed6b271ed86be15a7f88434633af84ce1eff921380ab2d73f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterLabAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5f0d6ed6081f278fb014ba2bb2c9d61e1f6c7d6ee339bde715dcabb49733afc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__302c6131444dceb3936119a8884a93d214ecaa3f5a1d829d1d75cf73098ff6eb(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beeeb6d1380efc695ee88c91b3b150e1e807223e51eb45a25cee128a3ca2285b(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterLabAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817e2c97fa0ba12bf031cbdf7619416d385df4df97b7d447b1a446a88debbcc0(
    *,
    code_repository: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb74670bb91adb121913daad06d7efb14a46aa43fb2dd44a2ea663da664e7180(
    *,
    repository_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f004e0d2473af3aff20dfabad440d63eaaf7d80bb7e77e0058124765bb4f4cfe(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d59b481190ac279455e03fc3d65ea3165c366b33c1a383e2ee500ecfa69a5eae(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67707054b0bc7228aa532eaaecb1a2709c38ad0e5d851aae446a2226fbaa8eed(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011370d08ceb5edf9a3a784c9085c76909b21102b9f24c804ecf4c7343485836(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5c20d76a226757e994003d170c25fe0d7c6f9d91c387d1666a551f85c5bef17(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c32eb9bd30cb4616c4a3c4e5ebadf996a3a0db14748c797e007dd1c4fc0072b0(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18771d1a266337ec8142f912c1547544c8a292f4898aabb97f5f544c3b57b91e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e033718e628cde7285db5ad0465c0626786322992a8ce5283b2ca9152685da9f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68b96730f80aacf3887f6e66f48205854961775f901184e3dfb7cd5645fc973b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4570b1ffd1e2b95358d2c1696375fbcdf56797a929177261c2fff66cba39a7aa(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2923475a8a915c0644154ab30d9fed5c394f76a5bd538ddbfc2daedad1873da4(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd279439ffaff9b063acca71f9acc438a30a680319ae9488dc14fd204b06baae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a135ce64a875857f563c90cb8089c3a0b0c2d498c06a34b5d4f7df76a3ff228c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bc9a8de409bbf900293f44270d651a69813606630217657821270d0adbf4197(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aee129e2c085ca2ee1e5748ae5c9eabffed289f379d1f5ed79fcf846ff739399(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96df45b849dffb72cb0795688cd62965c25ceb98a809e134c0a262efaa5d69b8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3d243b0e9fa8d746e8d0949f64dc2c1d917dddeb659fa50bab0721d30140e65(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5b1be2d8c3af832eeba24663494c3c0f8c1f7aa0f6a262c6d3c383a6d5af0ec(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33386a28d2e118405dc296048a9b76d1d39c51ad0f0951bb71831ec12d9ec478(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsJupyterServerAppSettingsCodeRepository, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ce63533120cb80fe129e041b944e052d79b8fa66f54a3429bde29061aaabb5(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2738a464945ad0c2878106b456f3d1c6c02bdcbad32bf4bc28628f3a024817fa(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsJupyterServerAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6a3b7c8db8be02fa278abb574a9e0f9dbcd26e324d0da8d3203d4180a3d5668(
    *,
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    lifecycle_config_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff0cc30b023a7813a01851e053b50d8893d26cc0cbaf9422ded7599cf7522c3(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1d0db4e0033c9064da70bb6cd20a1e98a0ad3f4f8c22e31518ed5c9a5418694(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9f87516619b194d06ba8660dd4807e8e7d174f73a074b7a9bd4b0afc70899f3(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__766ffae5faa766dd868f7348e05541f1947a9e9129b79678c0945eee48e2b813(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__846e7a350491e3bc797bb47235ef22f89d6c8bc31c9d0777e52309077deacd3d(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc3a60ed214d9b3fe94b9dba5f753e563749969b4af3ce9df81d43439ddc19b(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb16e97a1819148defab0847a8ac1f81c401dbbd1d5757f00f9f01e0f766679c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1ba8ea2754d1eff60f813b433820e23805dac7e8a636a923a8f920e37b4169a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8456de51e3989c8aefd592e10db5b0704e620a67567a370958a1236a2423a08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4be6a7bfd022b9068dab153a91de2e0eeba968ff5a441f0bcf55652a02ec48d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdd6518514c76069e8c6dfcbdba9b17ad5b4d156a5b305a5ded127bd809e7a02(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33dc4f06485e1b938f98433a6fa114ed98fbe6576002904dcd363eb88a860c82(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74501287e7f051cfb7d7ddcca02805824b05c2d039e0b6e413dfe302079a3664(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dcce5aad63435c14cdf9bfec3cb3c817f515710935e18da396f29a8cb9e8d4a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d2ac76429464f78f028ac44e955be671e18a705a67859ec70cbf2a2d2efde3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7659dcfb2311cee5f2f1b0d7dc82e6df8598ce7502712c5456a9fd536e0b4af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4de8129c2330eb6480c6e5571ae98df2fe437ea0fc3d45afb9c1046e0a4623d7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8edd65962364ca1ea71d363d3767ff36d4cbbbf1d52d393f5a14cbbfb8650066(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a85832a99fb1fd65f66257f19d5c1a4a2d1ba156ebfe140e35492de2c0581cfc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f34cb3b1138a263f38d1ca2de66345019b202fccfb44d13c03e752f9eea22eb(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23f8def9f258b052df25aa6c10a32761e7cdccf9b30811041ea25bf9e68c3777(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__785b2b993e39c1e5a110b67ee6bee7339620e64db42be783673b1d23d9bdb10f(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51e6c8c1ab8f4a30386f08d2f3a2375c62f3e49eaceb42341eded3ad017cf0fc(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462094efaf00362d128ffa1e1333d78107dd559195ce26b6ff9db68bb42dbd7b(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsKernelGatewayAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2196bae6c2a708f150d469bdc058809e6f17d6cfa64714871f388579d0a1e37(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d7fe5a2730abd85e849a7f462bd376dcbb2049d9fc7286ed17a64921ce5de33(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsCustomFileSystemConfig, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ecc94e916f271539e78359612a7f747a2fd59890215ee12d44ee6e7a9c545a0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e81faf6853cf4f5b569e334ed0f6d59cfec6a770914827a7710830b81f7652bc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14c0da10af71ea964d7cf22301f2e6fc38707307321f82c336b6b067c809cd9b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d11fab3b5d64d156cbb158e9a44595253ac85b0f3d274fc8b1d30d4ea5b5c4a(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de815de7c4cd8d230694fe7ad862a32629ecace783e214fa46b1120e4be8c2f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83a7d299b4926eb6e063e10bd481bdc114762cbf1dbb95427b69d3ba95035f3b(
    value: typing.Optional[SagemakerDomainDefaultUserSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4be75f1e2c32f7edf88a5f8928e635d81ddf3fba6344d7f4998a3e98160accb2(
    *,
    custom_image: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]]] = None,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c9a3bfbfceb4d1fddb17c577dba8c693912517c0a4128ba062797249459bcb4(
    *,
    app_image_config_name: builtins.str,
    image_name: builtins.str,
    image_version_number: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__986ea9a3720dcc6dddb31aec49afdbe86040d38fe751bffb0c43369f1e929d3e(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d15697e0d4d158bdbee5e25baac3d602e45b6ee1dca363d0b1009f457b95def(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8725bb989159b1d0e98fff637603dbbef7b16478ec6118d38fb88b14d98a6f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0031306dcb2f45401c27f138a6d29527db5978fbf34a9a29ffba384ab97e9db(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f39c47a2a22b70e9d19ff765ebb3e2c9ca56bf241e3e466381389738b1a28d1(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d37da9af65a2229669e54fd5587b9f13f98e6581c3efef370f757de224047b(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9d8e62c0f90bee9f3ddbed2100562481eddff1c78b2afaacdc54321d2c19018(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ec4d740891a4ab16f1c51d74912b30b5aa0128044af5ba6646eb6dee51ad554(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f701dd20fa53e7d54a1294df48d16535c2ab31b1b92f55113eb888232d1684d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f881dbcfdbe8ada778f0c14808ba5be3c318c2165105e53dec686f34136a859a(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47867b2883b90fa884c7914b61026cd3077816daf3c011f9827f1843eef6bd46(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34592cbcd4b5da12cb6ae4e68fdffbac4eac34503dffef7a02ada211a2eb79f2(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f0ae5748781dfedeed19d08a0984df73e046b50f233769590189f544c8d566(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d830c6ee69eeb763aada91a0881b2b0677e6de3e6b4bff649904cedc5fcdc5e0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f38c93f2d9fe2160a21f953cd9ca2f31ed1a54b61021c7fd5a5bbdddad0ce9c4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc66e8890eb3f05b3d29b9a1596ab97f84ef1899ca0221c6b745f3fabe6459af(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de08041ea6a4ad69a2bd45e673f50b1facbea79a2415e6350689716ef2df179f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0395692746b6a338738352c2e80e1b4bd47a3de1f5d599a21102dc117f6a2cb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2d041ec557f299ea184b774d63f36641f3f1a0c931a847a93eedd2e8828f371(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d363104dd1cfb96de81276109f4f75e5b1e9e99cac00e4cdf74bbe162b0746dc(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05e4cd0f287785b693d5605772ecd5d3ccd284fa3f6dd0464821eddb92c4649b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[SagemakerDomainDefaultUserSettingsRSessionAppSettingsCustomImage, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf719d6922d73c12647d2cbef17fa633a0ee8a7c6608a37ae135a0432156fc1f(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsRSessionAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__448ca41396707bad570b73c95bbb51c88010ec5fbe5731f8aa6b753e53035d02(
    *,
    access_status: typing.Optional[builtins.str] = None,
    user_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af22b009af573074d171938c47cc8f65de0c5426c00d6ba67b755b17c77c8b40(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__577ebaa4d6e9f7a16f08aed72e3a77d471c184e45502f7c093360283a81fa784(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b9888400a2845b121141286e2ffca45e730fe8ea9a447c0d861792b96bd8e44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d4c27dfdd043c8984cf80fc3125aa3ec4eca091432a8278cbd9b523a3ab0d16(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsRStudioServerProAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4dd634ac30050b1726764ae6971d1a9565819738f081476b3fe307c4c5dde7(
    *,
    notebook_output_option: typing.Optional[builtins.str] = None,
    s3_kms_key_id: typing.Optional[builtins.str] = None,
    s3_output_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a80a9baefe36496342db09902861e529ae4fd9815be6baada02db150a973f865(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b5504187e12070e4e28071809148f404eff4b32cb520e3814cb026f07dcc89a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__510dd34b64dd0595b894164f8e21ece274e1195c1ed5cbebefba7abe3dd8af16(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb1a1eba1d87b94a52115e393aa806f64b9f0453625de737b372944347071e1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__656654d7743273c5214479068c2ee0573f66b63a5aff32ea778fa44860c5ba5e(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsSharingSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c88e748c8a35da0aa0708526ddd017b3241a9642b82962a7c9e8aa474bec9113(
    *,
    default_ebs_storage_settings: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cadd3c78a350e28a86ac0116c5467b207548669eaea32e4ee66145a76e1f8eb3(
    *,
    default_ebs_volume_size_in_gb: jsii.Number,
    maximum_ebs_volume_size_in_gb: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd31c8b3e0b98f158ed32611675a45f49a727d878eca0d9c2aaced9e49756af7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad279260efb6952d449aee0acc88369a1dd45f78c5fc0558999239e0c43b1e6(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__602580b5f3032bcaa3e9f8e5de3b7b82e7f8ef791758a628e88d302d7f3c46dd(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0fd02ea27d2b4246fb6eed9fbae7a794329e2270bdfb1b787f3ff72ec4e9c57(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettingsDefaultEbsStorageSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb758851f95dc3a2e4d1a2c467f4ae95543058daff8309be5eddab3a69afc91b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc0e60c6fdde83d14d7a933e1974bc2eac70a2eaed1d326feebd1a198f6d46e3(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsSpaceStorageSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f7076d0a03619e746a951338e9ff705b97696b960ef4a7fa2b8cd3d23825615(
    *,
    hidden_app_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    hidden_instance_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    hidden_ml_tools: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91a541c3c0e87c6e88e9a560a08b884e3d716e4bd5f4787468f344edb450dc59(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c44630597acc0cddb89e185371fdadbea8171ac434bcfb884c96c8603a5c2e3(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5145ab98ccd3ed4096eb671033a0293e6829ffca9da9b549f49ee6fff55bb09f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6eded293e1853af0fe2fbf86c9b3f0da4c4eeabd023fc335c5fdea2b99c8dde7(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e43a2d6d1475efd1041b94e6197d9c1a1369edcb8a41135760f4864695c99d2(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsStudioWebPortalSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0fc26081fd95e16183d03a085de090d85d9a2df3787989380beac7ef716d821(
    *,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9310f350c8c55a499e2ced4c9d1329474bed2ae5da1e27f7f8c99ec9c50b3f78(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71acb789fa6bdc95af11c0cfe2f99e59ed5853d19c86be28931c3ff06cd4c704(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d61cf21cffb52ab4b57a09534068d349fdfb2438b220f3d0bfd045d14e9cafcb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1f2fdea534b4a7d72e02527780c1b702a8f872a52ce59a6c96891511847bb74(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__976c5cffa5917b799083dbb8a0d9d23ee2a6342f1113bef13be13e8f5e38813b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3639396b56161d2561ed75ba1f3c0e2665b038f36fe4ba8f50dea4ccfa8ca65c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aeb0ff9183e88e8e3878c687f743bd5bc9c61472cffd7f461a1e6231817cc44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f09402a83b7c35dbdbc0e0426f51a01f76349d33fa0fedbb9705fa30a03025a(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1446f7e41501e74faa24bd93d3928cf49fa0faaab7bfafa14865575c23726f9(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b374a77b78eab0c915399d041820a394172c1828c1e3f38c86fc76c6c5f1dcc(
    value: typing.Optional[SagemakerDomainDefaultUserSettingsTensorBoardAppSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3778d9e111123821d8c1e9f616676628f0e9f0ce4d31c3e2521880bae1efedc(
    *,
    docker_settings: typing.Optional[typing.Union[SagemakerDomainDomainSettingsDockerSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    execution_role_identity_config: typing.Optional[builtins.str] = None,
    r_studio_server_pro_domain_settings: typing.Optional[typing.Union[SagemakerDomainDomainSettingsRStudioServerProDomainSettings, typing.Dict[builtins.str, typing.Any]]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48542167f4d863eed9187c5560cdb6a2a47940b037f4ba1fbdd76936d7525b98(
    *,
    enable_docker_access: typing.Optional[builtins.str] = None,
    vpc_only_trusted_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fd4c24eedf755ee04692a561b595163784beafcfb4b2aec16fcd3b8b126b088(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8d93f13ac452dfe38ce435e32cd215d1d889df32f0d509ad560113bd5ecd7b5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f5e51020c021544c476b9232fb0a98ac9acde6d145849f87850bb199a61fa47(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088cf46bb0d04deaa06d5134c80a9c6af7f964e95cc1c3dfc6426f2fd86bb786(
    value: typing.Optional[SagemakerDomainDomainSettingsDockerSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ba29ecbae06a14349a5ae5e53779ed3c882e3b880aa67e3f36f1533183f1e1(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d59617e1e8766a5083c6a2b520ba16c17f97f71a0c89be642d0b66eb56d1b48a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5409b4ea48f5457cc516524dead92222991a795d00a427fef43af1a94d4036c9(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1caacfc8bf2230b6e2ba7ce6603c0eb3811887c47c11957a4be88b6d2a9133ea(
    value: typing.Optional[SagemakerDomainDomainSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31c2866bf7197adc71305e3b209c625cd74b321542511ea5a99e43016408da1c(
    *,
    domain_execution_role_arn: builtins.str,
    default_resource_spec: typing.Optional[typing.Union[SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec, typing.Dict[builtins.str, typing.Any]]] = None,
    r_studio_connect_url: typing.Optional[builtins.str] = None,
    r_studio_package_manager_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__221369be8f4fcc14bc6faa969766986649cbf51dab7f9c720cf17b9d3ae54dac(
    *,
    instance_type: typing.Optional[builtins.str] = None,
    lifecycle_config_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_arn: typing.Optional[builtins.str] = None,
    sagemaker_image_version_alias: typing.Optional[builtins.str] = None,
    sagemaker_image_version_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6250026fe092b4b923f8f1da7c0415f1dfeaf66c21bc71ced2f4ed85690123b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4947aa7bc93f0828de69c6808ea053f7c87fd3071a27dcc06040c482bc6fff08(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7f14ff50d9a5138bbb2a1f734e0099f7f50ed55b019bfc32129fe8c80e45b41(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68e0b6e0571c9a320b4768bda0526f7f6473e6738c6314a26816a77f836cc582(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9e4fea411b3d5f0d142d84253174d402ddf5bd5ebd53364d29f6c318941b78(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03624d077856b6ef40a23afde6c5e20892320695952d09d120bce8254b95d081(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9072d5d5566a2d205b3d10803d0fad806b515ded2717ae4a344b7af1108ce9f(
    value: typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettingsDefaultResourceSpec],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b8b271edacd6da35b116f03ae7ee19e415d482cf66b0a43a14f92c7d2aed858(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__259d57c8c816f396b1e4a7455132d624c5bd8d5632ae624fe2447476a3b15873(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93af4b730c7a22fce3445512e83e3ff5937d7871203d4615f939bdc222d5667f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e16ccd942f5abd81f22e99e40ad375d0feb6b061036a044a7e65dd14f287bfc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009d334163dfe02a00af4ffff98d4eeaf57424ee80e2acf11f7b51ae6b1985b2(
    value: typing.Optional[SagemakerDomainDomainSettingsRStudioServerProDomainSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__842e0f9f1d11c737b4429c4627a4c6041a61d335ec50155fa322c3e9949abdc6(
    *,
    home_efs_file_system: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564bd96b1106203920ba2864ec0041420a13f92c6fb87057bb16130542334984(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__259f7b49a8f3d1faaf5ed9d701dc4c13fe5be9414d1b638f48a9cd8d7a7cdedd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__068db42e7625b19d383f3924b9acb1ed09b4a1542108128c4ba8e0bdd76c583a(
    value: typing.Optional[SagemakerDomainRetentionPolicy],
) -> None:
    """Type checking stubs"""
    pass
