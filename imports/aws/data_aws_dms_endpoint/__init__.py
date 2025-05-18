r'''
# `data_aws_dms_endpoint`

Refer to the Terraform Registry for docs: [`data_aws_dms_endpoint`](https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint).
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


class DataAwsDmsEndpoint(
    _cdktf_9a9027ec.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpoint",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint aws_dms_endpoint}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        endpoint_id: builtins.str,
        elasticsearch_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointElasticsearchSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kafka_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointKafkaSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mongodb_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointMongodbSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint aws_dms_endpoint} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param endpoint_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#endpoint_id DataAwsDmsEndpoint#endpoint_id}.
        :param elasticsearch_settings: elasticsearch_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#elasticsearch_settings DataAwsDmsEndpoint#elasticsearch_settings}
        :param extra_connection_attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#extra_connection_attributes DataAwsDmsEndpoint#extra_connection_attributes}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#id DataAwsDmsEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka_settings: kafka_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#kafka_settings DataAwsDmsEndpoint#kafka_settings}
        :param mongodb_settings: mongodb_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#mongodb_settings DataAwsDmsEndpoint#mongodb_settings}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#tags DataAwsDmsEndpoint#tags}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f02fac740f13b8142e085aa717e5614e29619445ee26562dd4d5b017a0ac714e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataAwsDmsEndpointConfig(
            endpoint_id=endpoint_id,
            elasticsearch_settings=elasticsearch_settings,
            extra_connection_attributes=extra_connection_attributes,
            id=id,
            kafka_settings=kafka_settings,
            mongodb_settings=mongodb_settings,
            tags=tags,
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
        '''Generates CDKTF code for importing a DataAwsDmsEndpoint resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the DataAwsDmsEndpoint to import.
        :param import_from_id: The id of the existing DataAwsDmsEndpoint that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the DataAwsDmsEndpoint to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cfaf9464bc6960a6c31cecc0d7fac00e5ed27902c181f66245c006c7089a234)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putElasticsearchSettings")
    def put_elasticsearch_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointElasticsearchSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08d6dc810e9ac6604d5bb7028ee204849c7ac360bb6167059e9722c6fba2597b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putElasticsearchSettings", [value]))

    @jsii.member(jsii_name="putKafkaSettings")
    def put_kafka_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointKafkaSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f5af9ff43e0ecd0c180eb4c2cf653ec7eb18beab2b37b03eb0118d60b8d6af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKafkaSettings", [value]))

    @jsii.member(jsii_name="putMongodbSettings")
    def put_mongodb_settings(
        self,
        value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointMongodbSettings", typing.Dict[builtins.str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cff4543676773c01ff508eb52331d1d599ee4e8eb5df4b4477b46d55ce6bf44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMongodbSettings", [value]))

    @jsii.member(jsii_name="resetElasticsearchSettings")
    def reset_elasticsearch_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticsearchSettings", []))

    @jsii.member(jsii_name="resetExtraConnectionAttributes")
    def reset_extra_connection_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConnectionAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKafkaSettings")
    def reset_kafka_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKafkaSettings", []))

    @jsii.member(jsii_name="resetMongodbSettings")
    def reset_mongodb_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMongodbSettings", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseName"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettings")
    def elasticsearch_settings(self) -> "DataAwsDmsEndpointElasticsearchSettingsList":
        return typing.cast("DataAwsDmsEndpointElasticsearchSettingsList", jsii.get(self, "elasticsearchSettings"))

    @builtins.property
    @jsii.member(jsii_name="endpointArn")
    def endpoint_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointArn"))

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @builtins.property
    @jsii.member(jsii_name="engineName")
    def engine_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engineName"))

    @builtins.property
    @jsii.member(jsii_name="kafkaSettings")
    def kafka_settings(self) -> "DataAwsDmsEndpointKafkaSettingsList":
        return typing.cast("DataAwsDmsEndpointKafkaSettingsList", jsii.get(self, "kafkaSettings"))

    @builtins.property
    @jsii.member(jsii_name="kinesisSettings")
    def kinesis_settings(self) -> "DataAwsDmsEndpointKinesisSettingsList":
        return typing.cast("DataAwsDmsEndpointKinesisSettingsList", jsii.get(self, "kinesisSettings"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="mongodbSettings")
    def mongodb_settings(self) -> "DataAwsDmsEndpointMongodbSettingsList":
        return typing.cast("DataAwsDmsEndpointMongodbSettingsList", jsii.get(self, "mongodbSettings"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="redisSettings")
    def redis_settings(self) -> "DataAwsDmsEndpointRedisSettingsList":
        return typing.cast("DataAwsDmsEndpointRedisSettingsList", jsii.get(self, "redisSettings"))

    @builtins.property
    @jsii.member(jsii_name="redshiftSettings")
    def redshift_settings(self) -> "DataAwsDmsEndpointRedshiftSettingsList":
        return typing.cast("DataAwsDmsEndpointRedshiftSettingsList", jsii.get(self, "redshiftSettings"))

    @builtins.property
    @jsii.member(jsii_name="s3Settings")
    def s3_settings(self) -> "DataAwsDmsEndpointS3SettingsList":
        return typing.cast("DataAwsDmsEndpointS3SettingsList", jsii.get(self, "s3Settings"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerAccessRoleArn")
    def secrets_manager_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerAccessRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="secretsManagerArn")
    def secrets_manager_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsManagerArn"))

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRole")
    def service_access_role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRole"))

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslMode"))

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettingsInput")
    def elasticsearch_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointElasticsearchSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointElasticsearchSettings"]]], jsii.get(self, "elasticsearchSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointIdInput")
    def endpoint_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointIdInput"))

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributesInput")
    def extra_connection_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extraConnectionAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kafkaSettingsInput")
    def kafka_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointKafkaSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointKafkaSettings"]]], jsii.get(self, "kafkaSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="mongodbSettingsInput")
    def mongodb_settings_input(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointMongodbSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointMongodbSettings"]]], jsii.get(self, "mongodbSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointId")
    def endpoint_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointId"))

    @endpoint_id.setter
    def endpoint_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ca578a308883e3b4334ff535bab4e540b99959b159d799e25ecfe2a0652cb7d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extraConnectionAttributes"))

    @extra_connection_attributes.setter
    def extra_connection_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad4654df03228580eb0f3188988bdd5fa1dd8fc907fe2d66288022fd6b2a83c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConnectionAttributes", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29733fbc5bb57acc398086248c72c493fcf5d7626868213590841cd8255cf315)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cdb8f83e436327c99d382c504bb0edce8248fde4ab12d929b29547fe2f7b739)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "endpoint_id": "endpointId",
        "elasticsearch_settings": "elasticsearchSettings",
        "extra_connection_attributes": "extraConnectionAttributes",
        "id": "id",
        "kafka_settings": "kafkaSettings",
        "mongodb_settings": "mongodbSettings",
        "tags": "tags",
    },
)
class DataAwsDmsEndpointConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        endpoint_id: builtins.str,
        elasticsearch_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointElasticsearchSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kafka_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointKafkaSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        mongodb_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union["DataAwsDmsEndpointMongodbSettings", typing.Dict[builtins.str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param endpoint_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#endpoint_id DataAwsDmsEndpoint#endpoint_id}.
        :param elasticsearch_settings: elasticsearch_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#elasticsearch_settings DataAwsDmsEndpoint#elasticsearch_settings}
        :param extra_connection_attributes: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#extra_connection_attributes DataAwsDmsEndpoint#extra_connection_attributes}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#id DataAwsDmsEndpoint#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kafka_settings: kafka_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#kafka_settings DataAwsDmsEndpoint#kafka_settings}
        :param mongodb_settings: mongodb_settings block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#mongodb_settings DataAwsDmsEndpoint#mongodb_settings}
        :param tags: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#tags DataAwsDmsEndpoint#tags}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd2e54ad07814f1fe9a7f22dc799610147db86ffd4a3bbd7508b02adefbb7bb0)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument endpoint_id", value=endpoint_id, expected_type=type_hints["endpoint_id"])
            check_type(argname="argument elasticsearch_settings", value=elasticsearch_settings, expected_type=type_hints["elasticsearch_settings"])
            check_type(argname="argument extra_connection_attributes", value=extra_connection_attributes, expected_type=type_hints["extra_connection_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kafka_settings", value=kafka_settings, expected_type=type_hints["kafka_settings"])
            check_type(argname="argument mongodb_settings", value=mongodb_settings, expected_type=type_hints["mongodb_settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_id": endpoint_id,
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
        if elasticsearch_settings is not None:
            self._values["elasticsearch_settings"] = elasticsearch_settings
        if extra_connection_attributes is not None:
            self._values["extra_connection_attributes"] = extra_connection_attributes
        if id is not None:
            self._values["id"] = id
        if kafka_settings is not None:
            self._values["kafka_settings"] = kafka_settings
        if mongodb_settings is not None:
            self._values["mongodb_settings"] = mongodb_settings
        if tags is not None:
            self._values["tags"] = tags

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
    def endpoint_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#endpoint_id DataAwsDmsEndpoint#endpoint_id}.'''
        result = self._values.get("endpoint_id")
        assert result is not None, "Required property 'endpoint_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def elasticsearch_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointElasticsearchSettings"]]]:
        '''elasticsearch_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#elasticsearch_settings DataAwsDmsEndpoint#elasticsearch_settings}
        '''
        result = self._values.get("elasticsearch_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointElasticsearchSettings"]]], result)

    @builtins.property
    def extra_connection_attributes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#extra_connection_attributes DataAwsDmsEndpoint#extra_connection_attributes}.'''
        result = self._values.get("extra_connection_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#id DataAwsDmsEndpoint#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kafka_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointKafkaSettings"]]]:
        '''kafka_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#kafka_settings DataAwsDmsEndpoint#kafka_settings}
        '''
        result = self._values.get("kafka_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointKafkaSettings"]]], result)

    @builtins.property
    def mongodb_settings(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointMongodbSettings"]]]:
        '''mongodb_settings block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#mongodb_settings DataAwsDmsEndpoint#mongodb_settings}
        '''
        result = self._values.get("mongodb_settings")
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List["DataAwsDmsEndpointMongodbSettings"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#tags DataAwsDmsEndpoint#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointElasticsearchSettings",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_uri": "endpointUri",
        "service_access_role_arn": "serviceAccessRoleArn",
    },
)
class DataAwsDmsEndpointElasticsearchSettings:
    def __init__(
        self,
        *,
        endpoint_uri: builtins.str,
        service_access_role_arn: builtins.str,
    ) -> None:
        '''
        :param endpoint_uri: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#endpoint_uri DataAwsDmsEndpoint#endpoint_uri}.
        :param service_access_role_arn: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#service_access_role_arn DataAwsDmsEndpoint#service_access_role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be5779983925d344198ec7ab607f2e90dd5a542088807e3e41deae67182a0d12)
            check_type(argname="argument endpoint_uri", value=endpoint_uri, expected_type=type_hints["endpoint_uri"])
            check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_uri": endpoint_uri,
            "service_access_role_arn": service_access_role_arn,
        }

    @builtins.property
    def endpoint_uri(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#endpoint_uri DataAwsDmsEndpoint#endpoint_uri}.'''
        result = self._values.get("endpoint_uri")
        assert result is not None, "Required property 'endpoint_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_access_role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#service_access_role_arn DataAwsDmsEndpoint#service_access_role_arn}.'''
        result = self._values.get("service_access_role_arn")
        assert result is not None, "Required property 'service_access_role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointElasticsearchSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsDmsEndpointElasticsearchSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointElasticsearchSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__18ff424be0d0ae131579835e54f406047220c68af328781eb80269f11b93f13a)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsDmsEndpointElasticsearchSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00c50fbfb484084be8b33d880b6e36e43650d982e1f853ef6c80edb1b3575c5)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsDmsEndpointElasticsearchSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73258cc2fe9fb4c277467430e6d2c175c1d2d0b8726f23ca6f3c46f69c1db3c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8bff2488fddad7782d5da0553fefe3e678506312437219878bf4adbd987bd804)
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
            type_hints = typing.get_type_hints(_typecheckingstub__58fbc7bb3d432ad6d9314b1a0f0fb7da058b8bfbbec20a2256ebdff3a8634e12)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointElasticsearchSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointElasticsearchSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointElasticsearchSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e37a59ac764bd6bbb54f384e09724a5eee43798f2eb15c92f9a617fed808c60c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class DataAwsDmsEndpointElasticsearchSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointElasticsearchSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9aabad12575c2b2e2035517fb1edb57d271fc25dfb0f9a3893b37e0d0aa3bad7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="errorRetryDuration")
    def error_retry_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "errorRetryDuration"))

    @builtins.property
    @jsii.member(jsii_name="fullLoadErrorPercentage")
    def full_load_error_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "fullLoadErrorPercentage"))

    @builtins.property
    @jsii.member(jsii_name="endpointUriInput")
    def endpoint_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointUriInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArnInput")
    def service_access_role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccessRoleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointUri")
    def endpoint_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointUri"))

    @endpoint_uri.setter
    def endpoint_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19fce281162da0b51b512a3f09e5441960e45d49b4b41265126fc3492116988c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointUri", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @service_access_role_arn.setter
    def service_access_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9f39b91308d9b54144cdf5629e4504326a808d364df4af47da4add74e4e28c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccessRoleArn", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointElasticsearchSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointElasticsearchSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointElasticsearchSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40d3044af496bd7b8ec8e8803d3cfb47ce45adcfe0299ea94c7b18c2f6b6ee03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointKafkaSettings",
    jsii_struct_bases=[],
    name_mapping={"broker": "broker"},
)
class DataAwsDmsEndpointKafkaSettings:
    def __init__(self, *, broker: builtins.str) -> None:
        '''
        :param broker: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#broker DataAwsDmsEndpoint#broker}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9724f4e1f7cbfb35ba6efc9d674526c2226b446f128fcb6bb80009ba168f627)
            check_type(argname="argument broker", value=broker, expected_type=type_hints["broker"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "broker": broker,
        }

    @builtins.property
    def broker(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/data-sources/dms_endpoint#broker DataAwsDmsEndpoint#broker}.'''
        result = self._values.get("broker")
        assert result is not None, "Required property 'broker' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointKafkaSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsDmsEndpointKafkaSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointKafkaSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__2c5e300eba2434e5794afa9dbfb41af74a62d3017dba0ce1c7e593254901e27b)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsDmsEndpointKafkaSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1082054f1d8e151d8ba44b579b2ed3cdb3d58e4828708a3997c8bac26955eb48)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsDmsEndpointKafkaSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29d5d0489bbf1499c4518a47157bfa9a8057e6cba5b57bc0a63a63635ea785bb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f84025fb71461eeebc8e4600d9ad5849d902a0e76862c354c0d1bc2cb781f615)
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
            type_hints = typing.get_type_hints(_typecheckingstub__243652f33ccf7cefbcfbc52482448fd3f2982debdbfadb15e63ddb5421ea1d9a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointKafkaSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointKafkaSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointKafkaSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85773fb21282ff4f2115f06b884d267d58fcffb5b6537a8f05f4029173718b3d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class DataAwsDmsEndpointKafkaSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointKafkaSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a66ef420d1809976ab53184a1298c8e9b85cc8fc42ab002cdf1ee2cbeb6acc7)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="includeControlDetails")
    def include_control_details(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeControlDetails"))

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmpty")
    def include_null_and_empty(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeNullAndEmpty"))

    @builtins.property
    @jsii.member(jsii_name="includePartitionValue")
    def include_partition_value(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includePartitionValue"))

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperations")
    def include_table_alter_operations(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeTableAlterOperations"))

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetails")
    def include_transaction_details(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeTransactionDetails"))

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @builtins.property
    @jsii.member(jsii_name="messageMaxBytes")
    def message_max_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "messageMaxBytes"))

    @builtins.property
    @jsii.member(jsii_name="noHexPrefix")
    def no_hex_prefix(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "noHexPrefix"))

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTable")
    def partition_include_schema_table(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "partitionIncludeSchemaTable"))

    @builtins.property
    @jsii.member(jsii_name="saslPassword")
    def sasl_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saslPassword"))

    @builtins.property
    @jsii.member(jsii_name="saslUsername")
    def sasl_username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "saslUsername"))

    @builtins.property
    @jsii.member(jsii_name="securityProtocol")
    def security_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "securityProtocol"))

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCaCertificateArn"))

    @builtins.property
    @jsii.member(jsii_name="sslClientCertificateArn")
    def ssl_client_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientCertificateArn"))

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyArn")
    def ssl_client_key_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientKeyArn"))

    @builtins.property
    @jsii.member(jsii_name="sslClientKeyPassword")
    def ssl_client_key_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslClientKeyPassword"))

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "topic"))

    @builtins.property
    @jsii.member(jsii_name="brokerInput")
    def broker_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "brokerInput"))

    @builtins.property
    @jsii.member(jsii_name="broker")
    def broker(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "broker"))

    @broker.setter
    def broker(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8917fc3881aa82d9bad913ecce1592876af17aa98b6a72887c1e40a4f8b505f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "broker", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointKafkaSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointKafkaSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointKafkaSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c415d96fd609bbc8578ef6c14facbb9beb36c460461a63403e7f383f5451bd6e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointKinesisSettings",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsDmsEndpointKinesisSettings:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointKinesisSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsDmsEndpointKinesisSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointKinesisSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__9f76b592c31402c1bcc82118075b76d478477b8174efb1bd4222a96235787d4f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsDmsEndpointKinesisSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20031590df7c56cb33255fb725a2d583dcd444c237fd0198af86302d220f7e89)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsDmsEndpointKinesisSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fab751b4510ce5386b3bb399b012f4696458a1a839e3c324e616e9b458b31fec)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad30d6290c15b077701228dd5f67558492df0bcc1beb18e1bc4ac6c10722a952)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d0d5ee5156a0952ee92877843de19f7426a80482b6d29d43fa1cc49c7445943)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]


class DataAwsDmsEndpointKinesisSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointKinesisSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__c124d7fca4038276c969c121a38785e8711105baf48159728552e6cf3296fc57)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="includeControlDetails")
    def include_control_details(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeControlDetails"))

    @builtins.property
    @jsii.member(jsii_name="includeNullAndEmpty")
    def include_null_and_empty(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeNullAndEmpty"))

    @builtins.property
    @jsii.member(jsii_name="includePartitionValue")
    def include_partition_value(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includePartitionValue"))

    @builtins.property
    @jsii.member(jsii_name="includeTableAlterOperations")
    def include_table_alter_operations(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeTableAlterOperations"))

    @builtins.property
    @jsii.member(jsii_name="includeTransactionDetails")
    def include_transaction_details(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeTransactionDetails"))

    @builtins.property
    @jsii.member(jsii_name="messageFormat")
    def message_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "messageFormat"))

    @builtins.property
    @jsii.member(jsii_name="partitionIncludeSchemaTable")
    def partition_include_schema_table(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "partitionIncludeSchemaTable"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="streamArn")
    def stream_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "streamArn"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsDmsEndpointKinesisSettings]:
        return typing.cast(typing.Optional[DataAwsDmsEndpointKinesisSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsDmsEndpointKinesisSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1071a07647905d0d49d2a3a654c9a3bc99da4b90c5616811b3e468af7c6293b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointMongodbSettings",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsDmsEndpointMongodbSettings:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointMongodbSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsDmsEndpointMongodbSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointMongodbSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__abe51328268bcc2986622c7f3d36d098e03259c8f9d8166c35b76ef0b136beff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsDmsEndpointMongodbSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05f74fe601a0b30c0d125572060285f76d8bd90cf514a39e0e34bb0e1ba97ba6)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsDmsEndpointMongodbSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e1cfb57a8fbb94b9b435d8a523c4db280cadf42338ae91e81c27ee5a6683403)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9c78d1dd73b96e70f69ec905bfa0891a931c46ecbb5b612889f7616e1ede4766)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bea14ed5277208cb04e130318566aace01fc0185a8b8299740ec0e2785fa4c46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointMongodbSettings]]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointMongodbSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointMongodbSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__011d7e7e7d110ad0c5bff42264f3b8b460686f1cd325aefe4e95b3c72cc55a7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


class DataAwsDmsEndpointMongodbSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointMongodbSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__f28a1bb9184e202fe43e835db71168e05512ea079b375ce8e150e8f18764cc58)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="authMechanism")
    def auth_mechanism(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authMechanism"))

    @builtins.property
    @jsii.member(jsii_name="authSource")
    def auth_source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authSource"))

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @builtins.property
    @jsii.member(jsii_name="docsToInvestigate")
    def docs_to_investigate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "docsToInvestigate"))

    @builtins.property
    @jsii.member(jsii_name="extractDocId")
    def extract_doc_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "extractDocId"))

    @builtins.property
    @jsii.member(jsii_name="nestingLevel")
    def nesting_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nestingLevel"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointMongodbSettings]]:
        return typing.cast(typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointMongodbSettings]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointMongodbSettings]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1da1c5e607c8a3c7ad3f2d697f142c6586c38d90891b8bf861da7d6ed22f4272)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointRedisSettings",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsDmsEndpointRedisSettings:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointRedisSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsDmsEndpointRedisSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointRedisSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__fb82f2e839c41b4d1a2efcb9cc9da42976b6a3d027dac88570d211b549b855f6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsDmsEndpointRedisSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce2ddeccb551422799a17f0d2664a202c5dd798b4d8dc994a412f69c7d3231e)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsDmsEndpointRedisSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__addd3f525f736fcb7ea7f35d329819764d3f36026f920418f6a87874c8cee688)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df5b4662c4a04acd61a0056f2592fc7537861946419e1e437a1f43b38ea20a2b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7ae929c47c24b1d0a647b618202b2c70fde5fa597bb7ba273699007fdc3c8a37)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]


class DataAwsDmsEndpointRedisSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointRedisSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__4f309068523f2dfeb09d76e3e1fd6d4cb64bddf908f80711b3675f053c08abaa)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="authPassword")
    def auth_password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authPassword"))

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @builtins.property
    @jsii.member(jsii_name="authUserName")
    def auth_user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authUserName"))

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverName"))

    @builtins.property
    @jsii.member(jsii_name="sslCaCertificateArn")
    def ssl_ca_certificate_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslCaCertificateArn"))

    @builtins.property
    @jsii.member(jsii_name="sslSecurityProtocol")
    def ssl_security_protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslSecurityProtocol"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsDmsEndpointRedisSettings]:
        return typing.cast(typing.Optional[DataAwsDmsEndpointRedisSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsDmsEndpointRedisSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7387fcc86374762cf7d64065e0ce5f7adab89fd48ae4cbc9aa8251e9f4e80841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointRedshiftSettings",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsDmsEndpointRedshiftSettings:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointRedshiftSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsDmsEndpointRedshiftSettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointRedshiftSettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__002326dffed9c63ef41ec08491e3f50c63694fbc4f753ee312471ce8f29d2471)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "DataAwsDmsEndpointRedshiftSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d59d53e744bcf972aaab1648d032571ef5dd52353d1641b0a298db92ce48d023)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsDmsEndpointRedshiftSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f119837c390c28da5d16e14e0b6fc152ba7c5a615201f119eed290744d4cddc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__29d1bd8195c489b1f5e7d41661352a414bfdf35c9ad4e6d3bd1d2f42de181bef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3caadcdc07683f279b4f7fbc79cb138b51a64d336213302566ee8b41edfa922a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]


class DataAwsDmsEndpointRedshiftSettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointRedshiftSettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__e1ae2cfce021f7b5b5edb89260d602d5e017f4f3697c2dfd0ac07d4f06587b7f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="bucketFolder")
    def bucket_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketFolder"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideEncryptionKmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsDmsEndpointRedshiftSettings]:
        return typing.cast(typing.Optional[DataAwsDmsEndpointRedshiftSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsDmsEndpointRedshiftSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bafe7b2322682a1239bca61d287db849b4d833e0643e4c484ae74cb7bd64451)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointS3Settings",
    jsii_struct_bases=[],
    name_mapping={},
)
class DataAwsDmsEndpointS3Settings:
    def __init__(self) -> None:
        self._values: typing.Dict[builtins.str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataAwsDmsEndpointS3Settings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataAwsDmsEndpointS3SettingsList(
    _cdktf_9a9027ec.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointS3SettingsList",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a79424d8b595fb0ca5509ef5a0f9ac2c7d73f6fc9f7a025bb5615b48aff1b49d)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DataAwsDmsEndpointS3SettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49755e55cdbd2ae47db676f935d67647501fdc4be2938b59dd922b7c9e34da35)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DataAwsDmsEndpointS3SettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceaa0076d5c500971aac573ff10c2eaefa9d7184b327ad4fd20deca85382fe54)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1bd456a7063af2c6f1acf55c9698f75bae6136bcde05f924d008b8f6d679ade1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__68c6f6a07c5753995bab4e64431fbb0bc5f86242ebb5c60b5ddd500d4538f3ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value) # pyright: ignore[reportArgumentType]


class DataAwsDmsEndpointS3SettingsOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.dataAwsDmsEndpoint.DataAwsDmsEndpointS3SettingsOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cd26da3e6f23688945dbc199a8caf8d688a6d22bb3444cef1df44a2fc8f8a9f)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="addColumnName")
    def add_column_name(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "addColumnName"))

    @builtins.property
    @jsii.member(jsii_name="bucketFolder")
    def bucket_folder(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketFolder"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @builtins.property
    @jsii.member(jsii_name="cannedAclForObjects")
    def canned_acl_for_objects(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cannedAclForObjects"))

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsAndUpdates")
    def cdc_inserts_and_updates(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cdcInsertsAndUpdates"))

    @builtins.property
    @jsii.member(jsii_name="cdcInsertsOnly")
    def cdc_inserts_only(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "cdcInsertsOnly"))

    @builtins.property
    @jsii.member(jsii_name="cdcMaxBatchInterval")
    def cdc_max_batch_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMaxBatchInterval"))

    @builtins.property
    @jsii.member(jsii_name="cdcMinFileSize")
    def cdc_min_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "cdcMinFileSize"))

    @builtins.property
    @jsii.member(jsii_name="cdcPath")
    def cdc_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdcPath"))

    @builtins.property
    @jsii.member(jsii_name="compressionType")
    def compression_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compressionType"))

    @builtins.property
    @jsii.member(jsii_name="csvDelimiter")
    def csv_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvDelimiter"))

    @builtins.property
    @jsii.member(jsii_name="csvNoSupValue")
    def csv_no_sup_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNoSupValue"))

    @builtins.property
    @jsii.member(jsii_name="csvNullValue")
    def csv_null_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvNullValue"))

    @builtins.property
    @jsii.member(jsii_name="csvRowDelimiter")
    def csv_row_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "csvRowDelimiter"))

    @builtins.property
    @jsii.member(jsii_name="dataFormat")
    def data_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFormat"))

    @builtins.property
    @jsii.member(jsii_name="dataPageSize")
    def data_page_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dataPageSize"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionDelimiter")
    def date_partition_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionDelimiter"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionEnabled")
    def date_partition_enabled(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "datePartitionEnabled"))

    @builtins.property
    @jsii.member(jsii_name="datePartitionSequence")
    def date_partition_sequence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datePartitionSequence"))

    @builtins.property
    @jsii.member(jsii_name="dictPageSizeLimit")
    def dict_page_size_limit(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "dictPageSizeLimit"))

    @builtins.property
    @jsii.member(jsii_name="enableStatistics")
    def enable_statistics(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "enableStatistics"))

    @builtins.property
    @jsii.member(jsii_name="encodingType")
    def encoding_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encodingType"))

    @builtins.property
    @jsii.member(jsii_name="encryptionMode")
    def encryption_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionMode"))

    @builtins.property
    @jsii.member(jsii_name="externalTableDefinition")
    def external_table_definition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "externalTableDefinition"))

    @builtins.property
    @jsii.member(jsii_name="ignoreHeaderRows")
    def ignore_header_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreHeaderRows"))

    @builtins.property
    @jsii.member(jsii_name="ignoreHeadersRow")
    def ignore_headers_row(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ignoreHeadersRow"))

    @builtins.property
    @jsii.member(jsii_name="includeOpForFullLoad")
    def include_op_for_full_load(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "includeOpForFullLoad"))

    @builtins.property
    @jsii.member(jsii_name="maxFileSize")
    def max_file_size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFileSize"))

    @builtins.property
    @jsii.member(jsii_name="parquetTimestampInMillisecond")
    def parquet_timestamp_in_millisecond(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "parquetTimestampInMillisecond"))

    @builtins.property
    @jsii.member(jsii_name="parquetVersion")
    def parquet_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parquetVersion"))

    @builtins.property
    @jsii.member(jsii_name="preserveTransactions")
    def preserve_transactions(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "preserveTransactions"))

    @builtins.property
    @jsii.member(jsii_name="rfc4180")
    def rfc4180(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "rfc4180"))

    @builtins.property
    @jsii.member(jsii_name="rowGroupLength")
    def row_group_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "rowGroupLength"))

    @builtins.property
    @jsii.member(jsii_name="serverSideEncryptionKmsKeyId")
    def server_side_encryption_kms_key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serverSideEncryptionKmsKeyId"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccessRoleArn")
    def service_access_role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccessRoleArn"))

    @builtins.property
    @jsii.member(jsii_name="timestampColumnName")
    def timestamp_column_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "timestampColumnName"))

    @builtins.property
    @jsii.member(jsii_name="useCsvNoSupValue")
    def use_csv_no_sup_value(self) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "useCsvNoSupValue"))

    @builtins.property
    @jsii.member(jsii_name="useTaskStartTimeForFullLoadTimestamp")
    def use_task_start_time_for_full_load_timestamp(
        self,
    ) -> _cdktf_9a9027ec.IResolvable:
        return typing.cast(_cdktf_9a9027ec.IResolvable, jsii.get(self, "useTaskStartTimeForFullLoadTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[DataAwsDmsEndpointS3Settings]:
        return typing.cast(typing.Optional[DataAwsDmsEndpointS3Settings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataAwsDmsEndpointS3Settings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e27ca1cae316cc0fc2e8a95453898f67d0cfaf56ed44f076e60718a65232aaec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "DataAwsDmsEndpoint",
    "DataAwsDmsEndpointConfig",
    "DataAwsDmsEndpointElasticsearchSettings",
    "DataAwsDmsEndpointElasticsearchSettingsList",
    "DataAwsDmsEndpointElasticsearchSettingsOutputReference",
    "DataAwsDmsEndpointKafkaSettings",
    "DataAwsDmsEndpointKafkaSettingsList",
    "DataAwsDmsEndpointKafkaSettingsOutputReference",
    "DataAwsDmsEndpointKinesisSettings",
    "DataAwsDmsEndpointKinesisSettingsList",
    "DataAwsDmsEndpointKinesisSettingsOutputReference",
    "DataAwsDmsEndpointMongodbSettings",
    "DataAwsDmsEndpointMongodbSettingsList",
    "DataAwsDmsEndpointMongodbSettingsOutputReference",
    "DataAwsDmsEndpointRedisSettings",
    "DataAwsDmsEndpointRedisSettingsList",
    "DataAwsDmsEndpointRedisSettingsOutputReference",
    "DataAwsDmsEndpointRedshiftSettings",
    "DataAwsDmsEndpointRedshiftSettingsList",
    "DataAwsDmsEndpointRedshiftSettingsOutputReference",
    "DataAwsDmsEndpointS3Settings",
    "DataAwsDmsEndpointS3SettingsList",
    "DataAwsDmsEndpointS3SettingsOutputReference",
]

publication.publish()

def _typecheckingstub__f02fac740f13b8142e085aa717e5614e29619445ee26562dd4d5b017a0ac714e(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    endpoint_id: builtins.str,
    elasticsearch_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointElasticsearchSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kafka_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointKafkaSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mongodb_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointMongodbSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
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

def _typecheckingstub__3cfaf9464bc6960a6c31cecc0d7fac00e5ed27902c181f66245c006c7089a234(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08d6dc810e9ac6604d5bb7028ee204849c7ac360bb6167059e9722c6fba2597b(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointElasticsearchSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f5af9ff43e0ecd0c180eb4c2cf653ec7eb18beab2b37b03eb0118d60b8d6af(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointKafkaSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cff4543676773c01ff508eb52331d1d599ee4e8eb5df4b4477b46d55ce6bf44(
    value: typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointMongodbSettings, typing.Dict[builtins.str, typing.Any]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ca578a308883e3b4334ff535bab4e540b99959b159d799e25ecfe2a0652cb7d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad4654df03228580eb0f3188988bdd5fa1dd8fc907fe2d66288022fd6b2a83c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29733fbc5bb57acc398086248c72c493fcf5d7626868213590841cd8255cf315(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cdb8f83e436327c99d382c504bb0edce8248fde4ab12d929b29547fe2f7b739(
    value: typing.Mapping[builtins.str, builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd2e54ad07814f1fe9a7f22dc799610147db86ffd4a3bbd7508b02adefbb7bb0(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    endpoint_id: builtins.str,
    elasticsearch_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointElasticsearchSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    kafka_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointKafkaSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    mongodb_settings: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.Sequence[typing.Union[DataAwsDmsEndpointMongodbSettings, typing.Dict[builtins.str, typing.Any]]]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be5779983925d344198ec7ab607f2e90dd5a542088807e3e41deae67182a0d12(
    *,
    endpoint_uri: builtins.str,
    service_access_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ff424be0d0ae131579835e54f406047220c68af328781eb80269f11b93f13a(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00c50fbfb484084be8b33d880b6e36e43650d982e1f853ef6c80edb1b3575c5(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73258cc2fe9fb4c277467430e6d2c175c1d2d0b8726f23ca6f3c46f69c1db3c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bff2488fddad7782d5da0553fefe3e678506312437219878bf4adbd987bd804(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58fbc7bb3d432ad6d9314b1a0f0fb7da058b8bfbbec20a2256ebdff3a8634e12(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e37a59ac764bd6bbb54f384e09724a5eee43798f2eb15c92f9a617fed808c60c(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointElasticsearchSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aabad12575c2b2e2035517fb1edb57d271fc25dfb0f9a3893b37e0d0aa3bad7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19fce281162da0b51b512a3f09e5441960e45d49b4b41265126fc3492116988c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9f39b91308d9b54144cdf5629e4504326a808d364df4af47da4add74e4e28c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40d3044af496bd7b8ec8e8803d3cfb47ce45adcfe0299ea94c7b18c2f6b6ee03(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointElasticsearchSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9724f4e1f7cbfb35ba6efc9d674526c2226b446f128fcb6bb80009ba168f627(
    *,
    broker: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5e300eba2434e5794afa9dbfb41af74a62d3017dba0ce1c7e593254901e27b(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1082054f1d8e151d8ba44b579b2ed3cdb3d58e4828708a3997c8bac26955eb48(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d5d0489bbf1499c4518a47157bfa9a8057e6cba5b57bc0a63a63635ea785bb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f84025fb71461eeebc8e4600d9ad5849d902a0e76862c354c0d1bc2cb781f615(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__243652f33ccf7cefbcfbc52482448fd3f2982debdbfadb15e63ddb5421ea1d9a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85773fb21282ff4f2115f06b884d267d58fcffb5b6537a8f05f4029173718b3d(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointKafkaSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a66ef420d1809976ab53184a1298c8e9b85cc8fc42ab002cdf1ee2cbeb6acc7(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8917fc3881aa82d9bad913ecce1592876af17aa98b6a72887c1e40a4f8b505f4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c415d96fd609bbc8578ef6c14facbb9beb36c460461a63403e7f383f5451bd6e(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointKafkaSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f76b592c31402c1bcc82118075b76d478477b8174efb1bd4222a96235787d4f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20031590df7c56cb33255fb725a2d583dcd444c237fd0198af86302d220f7e89(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fab751b4510ce5386b3bb399b012f4696458a1a839e3c324e616e9b458b31fec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad30d6290c15b077701228dd5f67558492df0bcc1beb18e1bc4ac6c10722a952(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d0d5ee5156a0952ee92877843de19f7426a80482b6d29d43fa1cc49c7445943(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c124d7fca4038276c969c121a38785e8711105baf48159728552e6cf3296fc57(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1071a07647905d0d49d2a3a654c9a3bc99da4b90c5616811b3e468af7c6293b(
    value: typing.Optional[DataAwsDmsEndpointKinesisSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe51328268bcc2986622c7f3d36d098e03259c8f9d8166c35b76ef0b136beff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05f74fe601a0b30c0d125572060285f76d8bd90cf514a39e0e34bb0e1ba97ba6(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e1cfb57a8fbb94b9b435d8a523c4db280cadf42338ae91e81c27ee5a6683403(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c78d1dd73b96e70f69ec905bfa0891a931c46ecbb5b612889f7616e1ede4766(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bea14ed5277208cb04e130318566aace01fc0185a8b8299740ec0e2785fa4c46(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011d7e7e7d110ad0c5bff42264f3b8b460686f1cd325aefe4e95b3c72cc55a7f(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, typing.List[DataAwsDmsEndpointMongodbSettings]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f28a1bb9184e202fe43e835db71168e05512ea079b375ce8e150e8f18764cc58(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1da1c5e607c8a3c7ad3f2d697f142c6586c38d90891b8bf861da7d6ed22f4272(
    value: typing.Optional[typing.Union[_cdktf_9a9027ec.IResolvable, DataAwsDmsEndpointMongodbSettings]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb82f2e839c41b4d1a2efcb9cc9da42976b6a3d027dac88570d211b549b855f6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce2ddeccb551422799a17f0d2664a202c5dd798b4d8dc994a412f69c7d3231e(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__addd3f525f736fcb7ea7f35d329819764d3f36026f920418f6a87874c8cee688(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df5b4662c4a04acd61a0056f2592fc7537861946419e1e437a1f43b38ea20a2b(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ae929c47c24b1d0a647b618202b2c70fde5fa597bb7ba273699007fdc3c8a37(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f309068523f2dfeb09d76e3e1fd6d4cb64bddf908f80711b3675f053c08abaa(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7387fcc86374762cf7d64065e0ce5f7adab89fd48ae4cbc9aa8251e9f4e80841(
    value: typing.Optional[DataAwsDmsEndpointRedisSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__002326dffed9c63ef41ec08491e3f50c63694fbc4f753ee312471ce8f29d2471(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d59d53e744bcf972aaab1648d032571ef5dd52353d1641b0a298db92ce48d023(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f119837c390c28da5d16e14e0b6fc152ba7c5a615201f119eed290744d4cddc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29d1bd8195c489b1f5e7d41661352a414bfdf35c9ad4e6d3bd1d2f42de181bef(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3caadcdc07683f279b4f7fbc79cb138b51a64d336213302566ee8b41edfa922a(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ae2cfce021f7b5b5edb89260d602d5e017f4f3697c2dfd0ac07d4f06587b7f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bafe7b2322682a1239bca61d287db849b4d833e0643e4c484ae74cb7bd64451(
    value: typing.Optional[DataAwsDmsEndpointRedshiftSettings],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a79424d8b595fb0ca5509ef5a0f9ac2c7d73f6fc9f7a025bb5615b48aff1b49d(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    wraps_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49755e55cdbd2ae47db676f935d67647501fdc4be2938b59dd922b7c9e34da35(
    index: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceaa0076d5c500971aac573ff10c2eaefa9d7184b327ad4fd20deca85382fe54(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd456a7063af2c6f1acf55c9698f75bae6136bcde05f924d008b8f6d679ade1(
    value: _cdktf_9a9027ec.IInterpolatingParent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68c6f6a07c5753995bab4e64431fbb0bc5f86242ebb5c60b5ddd500d4538f3ad(
    value: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd26da3e6f23688945dbc199a8caf8d688a6d22bb3444cef1df44a2fc8f8a9f(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
    complex_object_index: jsii.Number,
    complex_object_is_from_set: builtins.bool,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27ca1cae316cc0fc2e8a95453898f67d0cfaf56ed44f076e60718a65232aaec(
    value: typing.Optional[DataAwsDmsEndpointS3Settings],
) -> None:
    """Type checking stubs"""
    pass
