r'''
# `aws_route53_record`

Refer to the Terraform Registry for docs: [`aws_route53_record`](https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record).
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


class Route53Record(
    _cdktf_9a9027ec.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53Record.Route53Record",
):
    '''Represents a {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record aws_route53_record}.'''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        zone_id: builtins.str,
        alias: typing.Optional[typing.Union["Route53RecordAlias", typing.Dict[builtins.str, typing.Any]]] = None,
        allow_overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cidr_routing_policy: typing.Optional[typing.Union["Route53RecordCidrRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        failover_routing_policy: typing.Optional[typing.Union["Route53RecordFailoverRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        geolocation_routing_policy: typing.Optional[typing.Union["Route53RecordGeolocationRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        health_check_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        latency_routing_policy: typing.Optional[typing.Union["Route53RecordLatencyRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        multivalue_answer_routing_policy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        records: typing.Optional[typing.Sequence[builtins.str]] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        weighted_routing_policy: typing.Optional[typing.Union["Route53RecordWeightedRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
        count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
        depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
        for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
        provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record aws_route53_record} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#name Route53Record#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#type Route53Record#type}.
        :param zone_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#zone_id Route53Record#zone_id}.
        :param alias: alias block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#alias Route53Record#alias}
        :param allow_overwrite: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#allow_overwrite Route53Record#allow_overwrite}.
        :param cidr_routing_policy: cidr_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#cidr_routing_policy Route53Record#cidr_routing_policy}
        :param failover_routing_policy: failover_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#failover_routing_policy Route53Record#failover_routing_policy}
        :param geolocation_routing_policy: geolocation_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#geolocation_routing_policy Route53Record#geolocation_routing_policy}
        :param health_check_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#health_check_id Route53Record#health_check_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#id Route53Record#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latency_routing_policy: latency_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#latency_routing_policy Route53Record#latency_routing_policy}
        :param multivalue_answer_routing_policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#multivalue_answer_routing_policy Route53Record#multivalue_answer_routing_policy}.
        :param records: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#records Route53Record#records}.
        :param set_identifier: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#set_identifier Route53Record#set_identifier}.
        :param ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#ttl Route53Record#ttl}.
        :param weighted_routing_policy: weighted_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#weighted_routing_policy Route53Record#weighted_routing_policy}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__664e46ae2ae9d91aa2572e94dfad7096e79e081d304456651a97255df4d1770c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = Route53RecordConfig(
            name=name,
            type=type,
            zone_id=zone_id,
            alias=alias,
            allow_overwrite=allow_overwrite,
            cidr_routing_policy=cidr_routing_policy,
            failover_routing_policy=failover_routing_policy,
            geolocation_routing_policy=geolocation_routing_policy,
            health_check_id=health_check_id,
            id=id,
            latency_routing_policy=latency_routing_policy,
            multivalue_answer_routing_policy=multivalue_answer_routing_policy,
            records=records,
            set_identifier=set_identifier,
            ttl=ttl,
            weighted_routing_policy=weighted_routing_policy,
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
        '''Generates CDKTF code for importing a Route53Record resource upon running "cdktf plan ".

        :param scope: The scope in which to define this construct.
        :param import_to_id: The construct id used in the generated config for the Route53Record to import.
        :param import_from_id: The id of the existing Route53Record that should be imported. Refer to the {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#import import section} in the documentation of this resource for the id to use
        :param provider: ? Optional instance of the provider where the Route53Record to import is found.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a92041eae178a712f0ccb6d0efa22544096459000db09fb55510735efa249d5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument import_to_id", value=import_to_id, expected_type=type_hints["import_to_id"])
            check_type(argname="argument import_from_id", value=import_from_id, expected_type=type_hints["import_from_id"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
        return typing.cast(_cdktf_9a9027ec.ImportableResource, jsii.sinvoke(cls, "generateConfigForImport", [scope, import_to_id, import_from_id, provider]))

    @jsii.member(jsii_name="putAlias")
    def put_alias(
        self,
        *,
        evaluate_target_health: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        zone_id: builtins.str,
    ) -> None:
        '''
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#evaluate_target_health Route53Record#evaluate_target_health}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#name Route53Record#name}.
        :param zone_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#zone_id Route53Record#zone_id}.
        '''
        value = Route53RecordAlias(
            evaluate_target_health=evaluate_target_health, name=name, zone_id=zone_id
        )

        return typing.cast(None, jsii.invoke(self, "putAlias", [value]))

    @jsii.member(jsii_name="putCidrRoutingPolicy")
    def put_cidr_routing_policy(
        self,
        *,
        collection_id: builtins.str,
        location_name: builtins.str,
    ) -> None:
        '''
        :param collection_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#collection_id Route53Record#collection_id}.
        :param location_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#location_name Route53Record#location_name}.
        '''
        value = Route53RecordCidrRoutingPolicy(
            collection_id=collection_id, location_name=location_name
        )

        return typing.cast(None, jsii.invoke(self, "putCidrRoutingPolicy", [value]))

    @jsii.member(jsii_name="putFailoverRoutingPolicy")
    def put_failover_routing_policy(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#type Route53Record#type}.
        '''
        value = Route53RecordFailoverRoutingPolicy(type=type)

        return typing.cast(None, jsii.invoke(self, "putFailoverRoutingPolicy", [value]))

    @jsii.member(jsii_name="putGeolocationRoutingPolicy")
    def put_geolocation_routing_policy(
        self,
        *,
        continent: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        subdivision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param continent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#continent Route53Record#continent}.
        :param country: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#country Route53Record#country}.
        :param subdivision: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#subdivision Route53Record#subdivision}.
        '''
        value = Route53RecordGeolocationRoutingPolicy(
            continent=continent, country=country, subdivision=subdivision
        )

        return typing.cast(None, jsii.invoke(self, "putGeolocationRoutingPolicy", [value]))

    @jsii.member(jsii_name="putLatencyRoutingPolicy")
    def put_latency_routing_policy(self, *, region: builtins.str) -> None:
        '''
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#region Route53Record#region}.
        '''
        value = Route53RecordLatencyRoutingPolicy(region=region)

        return typing.cast(None, jsii.invoke(self, "putLatencyRoutingPolicy", [value]))

    @jsii.member(jsii_name="putWeightedRoutingPolicy")
    def put_weighted_routing_policy(self, *, weight: jsii.Number) -> None:
        '''
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#weight Route53Record#weight}.
        '''
        value = Route53RecordWeightedRoutingPolicy(weight=weight)

        return typing.cast(None, jsii.invoke(self, "putWeightedRoutingPolicy", [value]))

    @jsii.member(jsii_name="resetAlias")
    def reset_alias(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlias", []))

    @jsii.member(jsii_name="resetAllowOverwrite")
    def reset_allow_overwrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOverwrite", []))

    @jsii.member(jsii_name="resetCidrRoutingPolicy")
    def reset_cidr_routing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCidrRoutingPolicy", []))

    @jsii.member(jsii_name="resetFailoverRoutingPolicy")
    def reset_failover_routing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailoverRoutingPolicy", []))

    @jsii.member(jsii_name="resetGeolocationRoutingPolicy")
    def reset_geolocation_routing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeolocationRoutingPolicy", []))

    @jsii.member(jsii_name="resetHealthCheckId")
    def reset_health_check_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheckId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLatencyRoutingPolicy")
    def reset_latency_routing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatencyRoutingPolicy", []))

    @jsii.member(jsii_name="resetMultivalueAnswerRoutingPolicy")
    def reset_multivalue_answer_routing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMultivalueAnswerRoutingPolicy", []))

    @jsii.member(jsii_name="resetRecords")
    def reset_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRecords", []))

    @jsii.member(jsii_name="resetSetIdentifier")
    def reset_set_identifier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSetIdentifier", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetWeightedRoutingPolicy")
    def reset_weighted_routing_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeightedRoutingPolicy", []))

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
    @jsii.member(jsii_name="alias")
    def alias(self) -> "Route53RecordAliasOutputReference":
        return typing.cast("Route53RecordAliasOutputReference", jsii.get(self, "alias"))

    @builtins.property
    @jsii.member(jsii_name="cidrRoutingPolicy")
    def cidr_routing_policy(self) -> "Route53RecordCidrRoutingPolicyOutputReference":
        return typing.cast("Route53RecordCidrRoutingPolicyOutputReference", jsii.get(self, "cidrRoutingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="failoverRoutingPolicy")
    def failover_routing_policy(
        self,
    ) -> "Route53RecordFailoverRoutingPolicyOutputReference":
        return typing.cast("Route53RecordFailoverRoutingPolicyOutputReference", jsii.get(self, "failoverRoutingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="geolocationRoutingPolicy")
    def geolocation_routing_policy(
        self,
    ) -> "Route53RecordGeolocationRoutingPolicyOutputReference":
        return typing.cast("Route53RecordGeolocationRoutingPolicyOutputReference", jsii.get(self, "geolocationRoutingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="latencyRoutingPolicy")
    def latency_routing_policy(
        self,
    ) -> "Route53RecordLatencyRoutingPolicyOutputReference":
        return typing.cast("Route53RecordLatencyRoutingPolicyOutputReference", jsii.get(self, "latencyRoutingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="weightedRoutingPolicy")
    def weighted_routing_policy(
        self,
    ) -> "Route53RecordWeightedRoutingPolicyOutputReference":
        return typing.cast("Route53RecordWeightedRoutingPolicyOutputReference", jsii.get(self, "weightedRoutingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="aliasInput")
    def alias_input(self) -> typing.Optional["Route53RecordAlias"]:
        return typing.cast(typing.Optional["Route53RecordAlias"], jsii.get(self, "aliasInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOverwriteInput")
    def allow_overwrite_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "allowOverwriteInput"))

    @builtins.property
    @jsii.member(jsii_name="cidrRoutingPolicyInput")
    def cidr_routing_policy_input(
        self,
    ) -> typing.Optional["Route53RecordCidrRoutingPolicy"]:
        return typing.cast(typing.Optional["Route53RecordCidrRoutingPolicy"], jsii.get(self, "cidrRoutingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverRoutingPolicyInput")
    def failover_routing_policy_input(
        self,
    ) -> typing.Optional["Route53RecordFailoverRoutingPolicy"]:
        return typing.cast(typing.Optional["Route53RecordFailoverRoutingPolicy"], jsii.get(self, "failoverRoutingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="geolocationRoutingPolicyInput")
    def geolocation_routing_policy_input(
        self,
    ) -> typing.Optional["Route53RecordGeolocationRoutingPolicy"]:
        return typing.cast(typing.Optional["Route53RecordGeolocationRoutingPolicy"], jsii.get(self, "geolocationRoutingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckIdInput")
    def health_check_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="latencyRoutingPolicyInput")
    def latency_routing_policy_input(
        self,
    ) -> typing.Optional["Route53RecordLatencyRoutingPolicy"]:
        return typing.cast(typing.Optional["Route53RecordLatencyRoutingPolicy"], jsii.get(self, "latencyRoutingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="multivalueAnswerRoutingPolicyInput")
    def multivalue_answer_routing_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "multivalueAnswerRoutingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="recordsInput")
    def records_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "recordsInput"))

    @builtins.property
    @jsii.member(jsii_name="setIdentifierInput")
    def set_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "setIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="weightedRoutingPolicyInput")
    def weighted_routing_policy_input(
        self,
    ) -> typing.Optional["Route53RecordWeightedRoutingPolicy"]:
        return typing.cast(typing.Optional["Route53RecordWeightedRoutingPolicy"], jsii.get(self, "weightedRoutingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOverwrite")
    def allow_overwrite(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "allowOverwrite"))

    @allow_overwrite.setter
    def allow_overwrite(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5ec34689dd271aeef6345b04a76a262c0df1dd5c3857dc5bb6279cc5d09e7b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOverwrite", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="healthCheckId")
    def health_check_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "healthCheckId"))

    @health_check_id.setter
    def health_check_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__656fb4bb7fcadf52af46fe08cb9c6f54000e13b9c0238cff2a8818fb27af3f4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f644522c711d599ec22dad09d31e15cda320228e42a551e48360a29b0325e920)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="multivalueAnswerRoutingPolicy")
    def multivalue_answer_routing_policy(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "multivalueAnswerRoutingPolicy"))

    @multivalue_answer_routing_policy.setter
    def multivalue_answer_routing_policy(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9296ebc655e74ded719c6368f19bee44132296eb930530ab69d1ad6080c2c0e8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multivalueAnswerRoutingPolicy", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57bb60cb53be4ba2cf8557d39b176b706cea7a3110e9ffe66d1cca516824b6c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="records")
    def records(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "records"))

    @records.setter
    def records(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e11e57b1ee072fbad87b819dbef6d4997f91d5d2860a87e303be50d8db55e2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "records", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="setIdentifier")
    def set_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "setIdentifier"))

    @set_identifier.setter
    def set_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a6f1b841e53c9a8145e4bf9e39cd4ebca513e55a8b5b851bb52dd09d9d2228a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setIdentifier", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d53cfddec2ff39eb92f6e5f749e2fb81cfa33134964139dbaae8950b1cf70d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39cc0aadb12cc45667f0c517a27804cf522582fc76ec95dcd613e4c5d299ad83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19628d5f99219d3d6d56a0416947acdcada34389208526a1c0166e5873773376)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.route53Record.Route53RecordAlias",
    jsii_struct_bases=[],
    name_mapping={
        "evaluate_target_health": "evaluateTargetHealth",
        "name": "name",
        "zone_id": "zoneId",
    },
)
class Route53RecordAlias:
    def __init__(
        self,
        *,
        evaluate_target_health: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
        name: builtins.str,
        zone_id: builtins.str,
    ) -> None:
        '''
        :param evaluate_target_health: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#evaluate_target_health Route53Record#evaluate_target_health}.
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#name Route53Record#name}.
        :param zone_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#zone_id Route53Record#zone_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a19501fbae62f64bad0bdcb2bf7258225874304130f2878af3d1e6275440998)
            check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "evaluate_target_health": evaluate_target_health,
            "name": name,
            "zone_id": zone_id,
        }

    @builtins.property
    def evaluate_target_health(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#evaluate_target_health Route53Record#evaluate_target_health}.'''
        result = self._values.get("evaluate_target_health")
        assert result is not None, "Required property 'evaluate_target_health' is missing"
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#name Route53Record#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#zone_id Route53Record#zone_id}.'''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecordAlias(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecordAliasOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53Record.Route53RecordAliasOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__a9aa391b8aa97427d9f83066cbd9cd666f01a3ba66dbb3325ea898bca8da3de6)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealthInput")
    def evaluate_target_health_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], jsii.get(self, "evaluateTargetHealthInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluateTargetHealth")
    def evaluate_target_health(
        self,
    ) -> typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable], jsii.get(self, "evaluateTargetHealth"))

    @evaluate_target_health.setter
    def evaluate_target_health(
        self,
        value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad7d7e9337118f3c3cb6c4bee119b9ac18c3ceaaadeba01ba07ac6cccbb7afc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluateTargetHealth", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3bdb672a0d5e594581b66e2f9ddc0813c0d5ab00bd2dde1cfc48bed1c93fbcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1e395da659ccb739026767af4c1d779c4606f00c89493661bbc66e5114eb1c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Route53RecordAlias]:
        return typing.cast(typing.Optional[Route53RecordAlias], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[Route53RecordAlias]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96082e17a9d4ba1a3c0a11d31004d605cce0e5fe4dc51d8d1863f495a6e71716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.route53Record.Route53RecordCidrRoutingPolicy",
    jsii_struct_bases=[],
    name_mapping={"collection_id": "collectionId", "location_name": "locationName"},
)
class Route53RecordCidrRoutingPolicy:
    def __init__(
        self,
        *,
        collection_id: builtins.str,
        location_name: builtins.str,
    ) -> None:
        '''
        :param collection_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#collection_id Route53Record#collection_id}.
        :param location_name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#location_name Route53Record#location_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d012e0472768894ddf90b511a2cb7da9736e4e8ab0095bb026e11f5ae8864975)
            check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
            check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "collection_id": collection_id,
            "location_name": location_name,
        }

    @builtins.property
    def collection_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#collection_id Route53Record#collection_id}.'''
        result = self._values.get("collection_id")
        assert result is not None, "Required property 'collection_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#location_name Route53Record#location_name}.'''
        result = self._values.get("location_name")
        assert result is not None, "Required property 'location_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecordCidrRoutingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecordCidrRoutingPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53Record.Route53RecordCidrRoutingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__74c4795798136446ed3692d94788f7faf7daf695aaab0e49c1377671d9a9a0ff)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="collectionIdInput")
    def collection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "collectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="locationNameInput")
    def location_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationNameInput"))

    @builtins.property
    @jsii.member(jsii_name="collectionId")
    def collection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "collectionId"))

    @collection_id.setter
    def collection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce2d966865e576a45a9b2b60009c84f916b911a6a778631982170db5ab19fae0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "collectionId", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="locationName")
    def location_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationName"))

    @location_name.setter
    def location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__469539fe0241c5d75ff516839f040590a105c00f676f42d877b3696642832be2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationName", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Route53RecordCidrRoutingPolicy]:
        return typing.cast(typing.Optional[Route53RecordCidrRoutingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecordCidrRoutingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__793922f55c8902ddd5f9acb1fbfd134b5431df6caa965b49969bf476d0d159bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.route53Record.Route53RecordConfig",
    jsii_struct_bases=[_cdktf_9a9027ec.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "type": "type",
        "zone_id": "zoneId",
        "alias": "alias",
        "allow_overwrite": "allowOverwrite",
        "cidr_routing_policy": "cidrRoutingPolicy",
        "failover_routing_policy": "failoverRoutingPolicy",
        "geolocation_routing_policy": "geolocationRoutingPolicy",
        "health_check_id": "healthCheckId",
        "id": "id",
        "latency_routing_policy": "latencyRoutingPolicy",
        "multivalue_answer_routing_policy": "multivalueAnswerRoutingPolicy",
        "records": "records",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weighted_routing_policy": "weightedRoutingPolicy",
    },
)
class Route53RecordConfig(_cdktf_9a9027ec.TerraformMetaArguments):
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
        name: builtins.str,
        type: builtins.str,
        zone_id: builtins.str,
        alias: typing.Optional[typing.Union[Route53RecordAlias, typing.Dict[builtins.str, typing.Any]]] = None,
        allow_overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        cidr_routing_policy: typing.Optional[typing.Union[Route53RecordCidrRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
        failover_routing_policy: typing.Optional[typing.Union["Route53RecordFailoverRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        geolocation_routing_policy: typing.Optional[typing.Union["Route53RecordGeolocationRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        health_check_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        latency_routing_policy: typing.Optional[typing.Union["Route53RecordLatencyRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
        multivalue_answer_routing_policy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
        records: typing.Optional[typing.Sequence[builtins.str]] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[jsii.Number] = None,
        weighted_routing_policy: typing.Optional[typing.Union["Route53RecordWeightedRoutingPolicy", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#name Route53Record#name}.
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#type Route53Record#type}.
        :param zone_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#zone_id Route53Record#zone_id}.
        :param alias: alias block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#alias Route53Record#alias}
        :param allow_overwrite: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#allow_overwrite Route53Record#allow_overwrite}.
        :param cidr_routing_policy: cidr_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#cidr_routing_policy Route53Record#cidr_routing_policy}
        :param failover_routing_policy: failover_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#failover_routing_policy Route53Record#failover_routing_policy}
        :param geolocation_routing_policy: geolocation_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#geolocation_routing_policy Route53Record#geolocation_routing_policy}
        :param health_check_id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#health_check_id Route53Record#health_check_id}.
        :param id: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#id Route53Record#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param latency_routing_policy: latency_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#latency_routing_policy Route53Record#latency_routing_policy}
        :param multivalue_answer_routing_policy: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#multivalue_answer_routing_policy Route53Record#multivalue_answer_routing_policy}.
        :param records: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#records Route53Record#records}.
        :param set_identifier: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#set_identifier Route53Record#set_identifier}.
        :param ttl: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#ttl Route53Record#ttl}.
        :param weighted_routing_policy: weighted_routing_policy block. Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#weighted_routing_policy Route53Record#weighted_routing_policy}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = _cdktf_9a9027ec.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alias, dict):
            alias = Route53RecordAlias(**alias)
        if isinstance(cidr_routing_policy, dict):
            cidr_routing_policy = Route53RecordCidrRoutingPolicy(**cidr_routing_policy)
        if isinstance(failover_routing_policy, dict):
            failover_routing_policy = Route53RecordFailoverRoutingPolicy(**failover_routing_policy)
        if isinstance(geolocation_routing_policy, dict):
            geolocation_routing_policy = Route53RecordGeolocationRoutingPolicy(**geolocation_routing_policy)
        if isinstance(latency_routing_policy, dict):
            latency_routing_policy = Route53RecordLatencyRoutingPolicy(**latency_routing_policy)
        if isinstance(weighted_routing_policy, dict):
            weighted_routing_policy = Route53RecordWeightedRoutingPolicy(**weighted_routing_policy)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a865cb9e9e32756d66d59a4a44de223e69fffff16aa14a5da2d5962d0b81000)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument allow_overwrite", value=allow_overwrite, expected_type=type_hints["allow_overwrite"])
            check_type(argname="argument cidr_routing_policy", value=cidr_routing_policy, expected_type=type_hints["cidr_routing_policy"])
            check_type(argname="argument failover_routing_policy", value=failover_routing_policy, expected_type=type_hints["failover_routing_policy"])
            check_type(argname="argument geolocation_routing_policy", value=geolocation_routing_policy, expected_type=type_hints["geolocation_routing_policy"])
            check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument latency_routing_policy", value=latency_routing_policy, expected_type=type_hints["latency_routing_policy"])
            check_type(argname="argument multivalue_answer_routing_policy", value=multivalue_answer_routing_policy, expected_type=type_hints["multivalue_answer_routing_policy"])
            check_type(argname="argument records", value=records, expected_type=type_hints["records"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weighted_routing_policy", value=weighted_routing_policy, expected_type=type_hints["weighted_routing_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
            "zone_id": zone_id,
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
        if alias is not None:
            self._values["alias"] = alias
        if allow_overwrite is not None:
            self._values["allow_overwrite"] = allow_overwrite
        if cidr_routing_policy is not None:
            self._values["cidr_routing_policy"] = cidr_routing_policy
        if failover_routing_policy is not None:
            self._values["failover_routing_policy"] = failover_routing_policy
        if geolocation_routing_policy is not None:
            self._values["geolocation_routing_policy"] = geolocation_routing_policy
        if health_check_id is not None:
            self._values["health_check_id"] = health_check_id
        if id is not None:
            self._values["id"] = id
        if latency_routing_policy is not None:
            self._values["latency_routing_policy"] = latency_routing_policy
        if multivalue_answer_routing_policy is not None:
            self._values["multivalue_answer_routing_policy"] = multivalue_answer_routing_policy
        if records is not None:
            self._values["records"] = records
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weighted_routing_policy is not None:
            self._values["weighted_routing_policy"] = weighted_routing_policy

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#name Route53Record#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#type Route53Record#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#zone_id Route53Record#zone_id}.'''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias(self) -> typing.Optional[Route53RecordAlias]:
        '''alias block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#alias Route53Record#alias}
        '''
        result = self._values.get("alias")
        return typing.cast(typing.Optional[Route53RecordAlias], result)

    @builtins.property
    def allow_overwrite(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#allow_overwrite Route53Record#allow_overwrite}.'''
        result = self._values.get("allow_overwrite")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def cidr_routing_policy(self) -> typing.Optional[Route53RecordCidrRoutingPolicy]:
        '''cidr_routing_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#cidr_routing_policy Route53Record#cidr_routing_policy}
        '''
        result = self._values.get("cidr_routing_policy")
        return typing.cast(typing.Optional[Route53RecordCidrRoutingPolicy], result)

    @builtins.property
    def failover_routing_policy(
        self,
    ) -> typing.Optional["Route53RecordFailoverRoutingPolicy"]:
        '''failover_routing_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#failover_routing_policy Route53Record#failover_routing_policy}
        '''
        result = self._values.get("failover_routing_policy")
        return typing.cast(typing.Optional["Route53RecordFailoverRoutingPolicy"], result)

    @builtins.property
    def geolocation_routing_policy(
        self,
    ) -> typing.Optional["Route53RecordGeolocationRoutingPolicy"]:
        '''geolocation_routing_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#geolocation_routing_policy Route53Record#geolocation_routing_policy}
        '''
        result = self._values.get("geolocation_routing_policy")
        return typing.cast(typing.Optional["Route53RecordGeolocationRoutingPolicy"], result)

    @builtins.property
    def health_check_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#health_check_id Route53Record#health_check_id}.'''
        result = self._values.get("health_check_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#id Route53Record#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def latency_routing_policy(
        self,
    ) -> typing.Optional["Route53RecordLatencyRoutingPolicy"]:
        '''latency_routing_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#latency_routing_policy Route53Record#latency_routing_policy}
        '''
        result = self._values.get("latency_routing_policy")
        return typing.cast(typing.Optional["Route53RecordLatencyRoutingPolicy"], result)

    @builtins.property
    def multivalue_answer_routing_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#multivalue_answer_routing_policy Route53Record#multivalue_answer_routing_policy}.'''
        result = self._values.get("multivalue_answer_routing_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]], result)

    @builtins.property
    def records(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#records Route53Record#records}.'''
        result = self._values.get("records")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#set_identifier Route53Record#set_identifier}.'''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#ttl Route53Record#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def weighted_routing_policy(
        self,
    ) -> typing.Optional["Route53RecordWeightedRoutingPolicy"]:
        '''weighted_routing_policy block.

        Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#weighted_routing_policy Route53Record#weighted_routing_policy}
        '''
        result = self._values.get("weighted_routing_policy")
        return typing.cast(typing.Optional["Route53RecordWeightedRoutingPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws.route53Record.Route53RecordFailoverRoutingPolicy",
    jsii_struct_bases=[],
    name_mapping={"type": "type"},
)
class Route53RecordFailoverRoutingPolicy:
    def __init__(self, *, type: builtins.str) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#type Route53Record#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__491372d478efae839e8b470b3d809a97c2a4d1f4ba454fb66d6645708336792b)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#type Route53Record#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecordFailoverRoutingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecordFailoverRoutingPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53Record.Route53RecordFailoverRoutingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__91d26d35bcc0ae66caab520854d515b0a4190a4976839c90243612002ae278c3)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fa805482885d2df381aed3ac8f68c8c60741ea0267ef4e550eeac066e00f650)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Route53RecordFailoverRoutingPolicy]:
        return typing.cast(typing.Optional[Route53RecordFailoverRoutingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecordFailoverRoutingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__733938b7ea61961df5df4e314d5c4b3eeae2c84693af3e0c3bd5f6fac4b02c53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.route53Record.Route53RecordGeolocationRoutingPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "continent": "continent",
        "country": "country",
        "subdivision": "subdivision",
    },
)
class Route53RecordGeolocationRoutingPolicy:
    def __init__(
        self,
        *,
        continent: typing.Optional[builtins.str] = None,
        country: typing.Optional[builtins.str] = None,
        subdivision: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param continent: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#continent Route53Record#continent}.
        :param country: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#country Route53Record#country}.
        :param subdivision: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#subdivision Route53Record#subdivision}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca905830db8f40e6622d4d0f29d265295680f688dd2418cddb34088bab7e2a57)
            check_type(argname="argument continent", value=continent, expected_type=type_hints["continent"])
            check_type(argname="argument country", value=country, expected_type=type_hints["country"])
            check_type(argname="argument subdivision", value=subdivision, expected_type=type_hints["subdivision"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if continent is not None:
            self._values["continent"] = continent
        if country is not None:
            self._values["country"] = country
        if subdivision is not None:
            self._values["subdivision"] = subdivision

    @builtins.property
    def continent(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#continent Route53Record#continent}.'''
        result = self._values.get("continent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def country(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#country Route53Record#country}.'''
        result = self._values.get("country")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subdivision(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#subdivision Route53Record#subdivision}.'''
        result = self._values.get("subdivision")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecordGeolocationRoutingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecordGeolocationRoutingPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53Record.Route53RecordGeolocationRoutingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__47e9fdc80af58ce900224a225f8cb9ad191645a3556991f266dd8d4482bb6750)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContinent")
    def reset_continent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinent", []))

    @jsii.member(jsii_name="resetCountry")
    def reset_country(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCountry", []))

    @jsii.member(jsii_name="resetSubdivision")
    def reset_subdivision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubdivision", []))

    @builtins.property
    @jsii.member(jsii_name="continentInput")
    def continent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "continentInput"))

    @builtins.property
    @jsii.member(jsii_name="countryInput")
    def country_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryInput"))

    @builtins.property
    @jsii.member(jsii_name="subdivisionInput")
    def subdivision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdivisionInput"))

    @builtins.property
    @jsii.member(jsii_name="continent")
    def continent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "continent"))

    @continent.setter
    def continent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72cd182c23a1fdc41e660bdc94fd9ed6ffd9325dd780d968a06017682e3dd945)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continent", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="country")
    def country(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "country"))

    @country.setter
    def country(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58929e532a5e826fb503a6c018833f77e55d08ce2ca61ea17bcdb2ec46da19c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "country", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="subdivision")
    def subdivision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subdivision"))

    @subdivision.setter
    def subdivision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd8d13e05205f1e898f6a28edf883224a35e4471e44caf411c5f9801179f8592)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subdivision", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Route53RecordGeolocationRoutingPolicy]:
        return typing.cast(typing.Optional[Route53RecordGeolocationRoutingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecordGeolocationRoutingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baa000fb96f97c49d369317110df09426bb20f5323b4d05352714b03c13e1993)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.route53Record.Route53RecordLatencyRoutingPolicy",
    jsii_struct_bases=[],
    name_mapping={"region": "region"},
)
class Route53RecordLatencyRoutingPolicy:
    def __init__(self, *, region: builtins.str) -> None:
        '''
        :param region: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#region Route53Record#region}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad5359527e015839719601e672c99d34b43997bb519448f0ace25913fdb21aae)
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "region": region,
        }

    @builtins.property
    def region(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#region Route53Record#region}.'''
        result = self._values.get("region")
        assert result is not None, "Required property 'region' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecordLatencyRoutingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecordLatencyRoutingPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53Record.Route53RecordLatencyRoutingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__75d92307ed6a7bf460783cf87d71e3db87165881f1724f2721c345411c3d5337)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44c394fe38eee12ed544356a7b353503da71b5c624eca5e860aaa2a44d3a2672)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Route53RecordLatencyRoutingPolicy]:
        return typing.cast(typing.Optional[Route53RecordLatencyRoutingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecordLatencyRoutingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__322250531e32e778bfa7e35f74d3e4b96d684dd9870dd6683c1b51d202277fa4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


@jsii.data_type(
    jsii_type="aws.route53Record.Route53RecordWeightedRoutingPolicy",
    jsii_struct_bases=[],
    name_mapping={"weight": "weight"},
)
class Route53RecordWeightedRoutingPolicy:
    def __init__(self, *, weight: jsii.Number) -> None:
        '''
        :param weight: Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#weight Route53Record#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69cde6f4272f730dba53130ca129cebce74cdd9b842c9d3b7a40376784df3458)
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "weight": weight,
        }

    @builtins.property
    def weight(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://registry.terraform.io/providers/hashicorp/aws/5.0.0/docs/resources/route53_record#weight Route53Record#weight}.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Route53RecordWeightedRoutingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class Route53RecordWeightedRoutingPolicyOutputReference(
    _cdktf_9a9027ec.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws.route53Record.Route53RecordWeightedRoutingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(_typecheckingstub__6dae6afd7b07d68613808e164c14bcd13848141943d2486b90035d968aaa3fbf)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__598c286b61b02abc73e8c134f78681fc4b15e0e892b8690bfd0a13ecca0a0e7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value) # pyright: ignore[reportArgumentType]

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[Route53RecordWeightedRoutingPolicy]:
        return typing.cast(typing.Optional[Route53RecordWeightedRoutingPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[Route53RecordWeightedRoutingPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__001143ac2817032524d96a261f767cd186236b71d7211f6575014b9ff2aa4437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value) # pyright: ignore[reportArgumentType]


__all__ = [
    "Route53Record",
    "Route53RecordAlias",
    "Route53RecordAliasOutputReference",
    "Route53RecordCidrRoutingPolicy",
    "Route53RecordCidrRoutingPolicyOutputReference",
    "Route53RecordConfig",
    "Route53RecordFailoverRoutingPolicy",
    "Route53RecordFailoverRoutingPolicyOutputReference",
    "Route53RecordGeolocationRoutingPolicy",
    "Route53RecordGeolocationRoutingPolicyOutputReference",
    "Route53RecordLatencyRoutingPolicy",
    "Route53RecordLatencyRoutingPolicyOutputReference",
    "Route53RecordWeightedRoutingPolicy",
    "Route53RecordWeightedRoutingPolicyOutputReference",
]

publication.publish()

def _typecheckingstub__664e46ae2ae9d91aa2572e94dfad7096e79e081d304456651a97255df4d1770c(
    scope: _constructs_77d1e7e8.Construct,
    id_: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    zone_id: builtins.str,
    alias: typing.Optional[typing.Union[Route53RecordAlias, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cidr_routing_policy: typing.Optional[typing.Union[Route53RecordCidrRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    failover_routing_policy: typing.Optional[typing.Union[Route53RecordFailoverRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    geolocation_routing_policy: typing.Optional[typing.Union[Route53RecordGeolocationRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    health_check_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    latency_routing_policy: typing.Optional[typing.Union[Route53RecordLatencyRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    multivalue_answer_routing_policy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    records: typing.Optional[typing.Sequence[builtins.str]] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[jsii.Number] = None,
    weighted_routing_policy: typing.Optional[typing.Union[Route53RecordWeightedRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
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

def _typecheckingstub__1a92041eae178a712f0ccb6d0efa22544096459000db09fb55510735efa249d5(
    scope: _constructs_77d1e7e8.Construct,
    import_to_id: builtins.str,
    import_from_id: builtins.str,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5ec34689dd271aeef6345b04a76a262c0df1dd5c3857dc5bb6279cc5d09e7b1(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__656fb4bb7fcadf52af46fe08cb9c6f54000e13b9c0238cff2a8818fb27af3f4f(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f644522c711d599ec22dad09d31e15cda320228e42a551e48360a29b0325e920(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9296ebc655e74ded719c6368f19bee44132296eb930530ab69d1ad6080c2c0e8(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57bb60cb53be4ba2cf8557d39b176b706cea7a3110e9ffe66d1cca516824b6c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e11e57b1ee072fbad87b819dbef6d4997f91d5d2860a87e303be50d8db55e2b(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a6f1b841e53c9a8145e4bf9e39cd4ebca513e55a8b5b851bb52dd09d9d2228a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d53cfddec2ff39eb92f6e5f749e2fb81cfa33134964139dbaae8950b1cf70d(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39cc0aadb12cc45667f0c517a27804cf522582fc76ec95dcd613e4c5d299ad83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19628d5f99219d3d6d56a0416947acdcada34389208526a1c0166e5873773376(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a19501fbae62f64bad0bdcb2bf7258225874304130f2878af3d1e6275440998(
    *,
    evaluate_target_health: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
    name: builtins.str,
    zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9aa391b8aa97427d9f83066cbd9cd666f01a3ba66dbb3325ea898bca8da3de6(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad7d7e9337118f3c3cb6c4bee119b9ac18c3ceaaadeba01ba07ac6cccbb7afc3(
    value: typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3bdb672a0d5e594581b66e2f9ddc0813c0d5ab00bd2dde1cfc48bed1c93fbcd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1e395da659ccb739026767af4c1d779c4606f00c89493661bbc66e5114eb1c7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96082e17a9d4ba1a3c0a11d31004d605cce0e5fe4dc51d8d1863f495a6e71716(
    value: typing.Optional[Route53RecordAlias],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d012e0472768894ddf90b511a2cb7da9736e4e8ab0095bb026e11f5ae8864975(
    *,
    collection_id: builtins.str,
    location_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74c4795798136446ed3692d94788f7faf7daf695aaab0e49c1377671d9a9a0ff(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce2d966865e576a45a9b2b60009c84f916b911a6a778631982170db5ab19fae0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__469539fe0241c5d75ff516839f040590a105c00f676f42d877b3696642832be2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__793922f55c8902ddd5f9acb1fbfd134b5431df6caa965b49969bf476d0d159bf(
    value: typing.Optional[Route53RecordCidrRoutingPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a865cb9e9e32756d66d59a4a44de223e69fffff16aa14a5da2d5962d0b81000(
    *,
    connection: typing.Optional[typing.Union[typing.Union[_cdktf_9a9027ec.SSHProvisionerConnection, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.WinrmProvisionerConnection, typing.Dict[builtins.str, typing.Any]]]] = None,
    count: typing.Optional[typing.Union[jsii.Number, _cdktf_9a9027ec.TerraformCount]] = None,
    depends_on: typing.Optional[typing.Sequence[_cdktf_9a9027ec.ITerraformDependable]] = None,
    for_each: typing.Optional[_cdktf_9a9027ec.ITerraformIterator] = None,
    lifecycle: typing.Optional[typing.Union[_cdktf_9a9027ec.TerraformResourceLifecycle, typing.Dict[builtins.str, typing.Any]]] = None,
    provider: typing.Optional[_cdktf_9a9027ec.TerraformProvider] = None,
    provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[_cdktf_9a9027ec.FileProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.LocalExecProvisioner, typing.Dict[builtins.str, typing.Any]], typing.Union[_cdktf_9a9027ec.RemoteExecProvisioner, typing.Dict[builtins.str, typing.Any]]]]] = None,
    name: builtins.str,
    type: builtins.str,
    zone_id: builtins.str,
    alias: typing.Optional[typing.Union[Route53RecordAlias, typing.Dict[builtins.str, typing.Any]]] = None,
    allow_overwrite: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    cidr_routing_policy: typing.Optional[typing.Union[Route53RecordCidrRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    failover_routing_policy: typing.Optional[typing.Union[Route53RecordFailoverRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    geolocation_routing_policy: typing.Optional[typing.Union[Route53RecordGeolocationRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    health_check_id: typing.Optional[builtins.str] = None,
    id: typing.Optional[builtins.str] = None,
    latency_routing_policy: typing.Optional[typing.Union[Route53RecordLatencyRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
    multivalue_answer_routing_policy: typing.Optional[typing.Union[builtins.bool, _cdktf_9a9027ec.IResolvable]] = None,
    records: typing.Optional[typing.Sequence[builtins.str]] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[jsii.Number] = None,
    weighted_routing_policy: typing.Optional[typing.Union[Route53RecordWeightedRoutingPolicy, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__491372d478efae839e8b470b3d809a97c2a4d1f4ba454fb66d6645708336792b(
    *,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91d26d35bcc0ae66caab520854d515b0a4190a4976839c90243612002ae278c3(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa805482885d2df381aed3ac8f68c8c60741ea0267ef4e550eeac066e00f650(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__733938b7ea61961df5df4e314d5c4b3eeae2c84693af3e0c3bd5f6fac4b02c53(
    value: typing.Optional[Route53RecordFailoverRoutingPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca905830db8f40e6622d4d0f29d265295680f688dd2418cddb34088bab7e2a57(
    *,
    continent: typing.Optional[builtins.str] = None,
    country: typing.Optional[builtins.str] = None,
    subdivision: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47e9fdc80af58ce900224a225f8cb9ad191645a3556991f266dd8d4482bb6750(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72cd182c23a1fdc41e660bdc94fd9ed6ffd9325dd780d968a06017682e3dd945(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58929e532a5e826fb503a6c018833f77e55d08ce2ca61ea17bcdb2ec46da19c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8d13e05205f1e898f6a28edf883224a35e4471e44caf411c5f9801179f8592(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baa000fb96f97c49d369317110df09426bb20f5323b4d05352714b03c13e1993(
    value: typing.Optional[Route53RecordGeolocationRoutingPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad5359527e015839719601e672c99d34b43997bb519448f0ace25913fdb21aae(
    *,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75d92307ed6a7bf460783cf87d71e3db87165881f1724f2721c345411c3d5337(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44c394fe38eee12ed544356a7b353503da71b5c624eca5e860aaa2a44d3a2672(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322250531e32e778bfa7e35f74d3e4b96d684dd9870dd6683c1b51d202277fa4(
    value: typing.Optional[Route53RecordLatencyRoutingPolicy],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69cde6f4272f730dba53130ca129cebce74cdd9b842c9d3b7a40376784df3458(
    *,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dae6afd7b07d68613808e164c14bcd13848141943d2486b90035d968aaa3fbf(
    terraform_resource: _cdktf_9a9027ec.IInterpolatingParent,
    terraform_attribute: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__598c286b61b02abc73e8c134f78681fc4b15e0e892b8690bfd0a13ecca0a0e7e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__001143ac2817032524d96a261f767cd186236b71d7211f6575014b9ff2aa4437(
    value: typing.Optional[Route53RecordWeightedRoutingPolicy],
) -> None:
    """Type checking stubs"""
    pass
