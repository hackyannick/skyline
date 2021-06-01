from . import base

list_rules = (
    base.Rule(
        name="context_is_admin",
        check_str=("(role:admin and is_admin_project:True) OR (role:admin and system_scope:all)"),
        description="Decides what is required for the 'is_admin:True' check to succeed.",
    ),
    base.Rule(
        name="project_admin",
        check_str=("role:admin"),
        description="Default rule for project admin.",
    ),
    base.Rule(
        name="deny_stack_user",
        check_str=("not role:heat_stack_user"),
        description="Default rule for deny stack user.",
    ),
    base.Rule(
        name="deny_everybody",
        check_str=("!"),
        description="Default rule for deny everybody.",
    ),
    base.Rule(
        name="allow_everybody",
        check_str=(""),
        description="Default rule for allow everybody.",
    ),
    base.Rule(
        name="cloudformation:ListStacks",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:CreateStack",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:DescribeStacks",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:DeleteStack",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:UpdateStack",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:CancelUpdateStack",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:DescribeStackEvents",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:ValidateTemplate",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:GetTemplate",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:EstimateTemplateCost",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:DescribeStackResource",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and project_id:%(project_id)s) "
            "or (role:heat_stack_user and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:DescribeStackResources",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="cloudformation:ListStackResources",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Nova::Flavor",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Cinder::EncryptedVolumeType",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Cinder::VolumeType",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Cinder::Quota",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Neutron::Quota",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Nova::Quota",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Octavia::Quota",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Manila::ShareType",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Neutron::ProviderNet",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Neutron::QoSPolicy",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Neutron::QoSBandwidthLimitRule",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Neutron::QoSDscpMarkingRule",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Neutron::QoSMinimumBandwidthRule",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Neutron::Segment",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Nova::HostAggregate",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Cinder::QoSSpecs",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Cinder::QoSAssociation",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Keystone::*",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Blazar::Host",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Octavia::Flavor",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="resource_types:OS::Octavia::FlavorProfile",
        check_str=("rule:project_admin"),
        description="No description",
    ),
    base.Rule(
        name="service:index",
        check_str=("role:reader and system_scope:all"),
        description="No description",
    ),
    base.APIRule(
        name="actions:action",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Performs non-lifecycle operations on the stack "
        "(Snapshot, Resume, Cancel update, or check stack "
        "resources). This is the default for all actions but "
        "can be overridden by more specific policies "
        "for individual actions.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions"},
        ],
    ),
    base.APIRule(
        name="actions:snapshot",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create stack snapshot",
        scope_types=["system", "project"],
        operations=[
            {"method": "POST", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions"},
        ],
    ),
    base.APIRule(
        name="actions:suspend",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Suspend a stack.",
        scope_types=["system", "project"],
        operations=[
            {"method": "POST", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions"},
        ],
    ),
    base.APIRule(
        name="actions:resume",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Resume a suspended stack.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "POST",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions",
            },
        ],
    ),
    base.APIRule(
        name="actions:check",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="Check stack resources.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "POST",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions",
            },
        ],
    ),
    base.APIRule(
        name="actions:cancel_update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s) "
        ),
        description="Cancel stack operation and roll back.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "POST",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions",
            },
        ],
    ),
    base.APIRule(
        name="actions:cancel_without_rollback",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s) "
        ),
        description="Cancel stack operation without rolling back.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "POST",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/actions",
            },
        ],
    ),
    base.APIRule(
        name="build_info:build_info",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="Show build information.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/build_info"}],
    ),
    base.APIRule(
        name="events:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="List events.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/events"},
        ],
    ),
    base.APIRule(
        name="events:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Show event.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{"
                "stack_id}/resources/{resource_name}/events/{"
                "event_id}",
            },
        ],
    ),
    base.APIRule(
        name="resource:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="List resources.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/resources",
            },
        ],
    ),
    base.APIRule(
        name="resource:metadata",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) or (role:heat_stack_user and "
            "project_id:%(project_id)s) "
        ),
        description="Show resource metadata.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{"
                "stack_id}/resources/{resource_name}/metadata",
            },
        ],
    ),
    base.APIRule(
        name="resource:signal",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) or (role:heat_stack_user and "
            "project_id:%(project_id)s) "
        ),
        description="Signal resource.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "POST",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{"
                "stack_id}/resources/{resource_name}/signal",
            },
        ],
    ),
    base.APIRule(
        name="resource:mark_unhealthy",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s) "
        ),
        description="Mark resource as unhealthy.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "PATCH",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{"
                "stack_id}/resources/{resource_name_or_physical_id}",
            },
        ],
    ),
    base.APIRule(
        name="resource:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Show resource.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}"
                "/{stack_id}/resources/{resource_name}",
            },
        ],
    ),
    base.APIRule(
        name="software_configs:global_index",
        check_str=("role:reader and system_scope:all"),
        description="List configs globally.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/software_configs"}],
    ),
    base.APIRule(
        name="software_configs:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="List configs.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/software_configs"}],
    ),
    base.APIRule(
        name="software_configs:create",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="Create config.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v1/{tenant_id}/software_configs"}],
    ),
    base.APIRule(
        name="software_configs:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="Show config details.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/software_configs/{config_id}"}],
    ),
    base.APIRule(
        name="software_configs:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete config.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/v1/{tenant_id}/software_configs/{config_id}"}],
    ),
    base.APIRule(
        name="software_deployments:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List deployments.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/software_deployments"}],
    ),
    base.APIRule(
        name="software_deployments:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create deployment.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v1/{tenant_id}/software_deployments"}],
    ),
    base.APIRule(
        name="software_deployments:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Show deployment details.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/v1/{tenant_id}/software_deployments/{deployment_id}"},
        ],
    ),
    base.APIRule(
        name="software_deployments:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update deployment.",
        scope_types=["system", "project"],
        operations=[
            {"method": "PUT", "path": "/v1/{tenant_id}/software_deployments/{deployment_id}"},
        ],
    ),
    base.APIRule(
        name="software_deployments:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete deployment.",
        scope_types=["system", "project"],
        operations=[
            {"method": "DELETE", "path": "/v1/{tenant_id}/software_deployments/{deployment_id}"},
        ],
    ),
    base.APIRule(
        name="software_deployments:metadata",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and project_id:%(project_id)s) "
            "or (role:heat_stack_user and project_id:%(project_id)s)"
        ),
        description="Show server configuration metadata.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/software_deployments/metadata/{server_id}",
            },
        ],
    ),
    base.APIRule(
        name="stacks:abandon",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Abandon stack.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "DELETE",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/abandon",
            },
        ],
    ),
    base.APIRule(
        name="stacks:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Create stack.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v1/{tenant_id}/stacks"}],
    ),
    base.APIRule(
        name="stacks:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete stack.",
        scope_types=["system", "project"],
        operations=[
            {"method": "DELETE", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}"},
        ],
    ),
    base.APIRule(
        name="stacks:detail",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List stacks in detail.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/stacks"}],
    ),
    base.APIRule(
        name="stacks:export",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Export stack.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/export"},
        ],
    ),
    base.APIRule(
        name="stacks:generate_template",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Generate stack template.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/template",
            },
        ],
    ),
    base.APIRule(
        name="stacks:global_index",
        check_str=("role:reader and system_scope:all"),
        description="List stacks globally.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/stacks"}],
    ),
    base.APIRule(
        name="stacks:index",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List stacks.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/stacks"}],
    ),
    base.APIRule(
        name="stacks:list_resource_types",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List resource types.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/resource_types"}],
    ),
    base.APIRule(
        name="stacks:list_template_versions",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List template versions.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/template_versions"}],
    ),
    base.APIRule(
        name="stacks:list_template_functions",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List template functions.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/template_versions/{template_version}/functions",
            },
        ],
    ),
    base.APIRule(
        name="stacks:lookup",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and project_id:%(project_id)s) "
            "or (role:heat_stack_user and project_id:%(project_id)s)"
        ),
        description="Find stack.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/stacks/{stack_identity}"}],
    ),
    base.APIRule(
        name="stacks:preview",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Preview stack.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v1/{tenant_id}/stacks/preview"}],
    ),
    base.APIRule(
        name="stacks:resource_schema",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Show resource type schema.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/resource_types/{type_name}"}],
    ),
    base.APIRule(
        name="stacks:show",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Show stack.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v1/{tenant_id}/stacks/{stack_identity}"}],
    ),
    base.APIRule(
        name="stacks:template",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get stack template.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/template",
            },
        ],
    ),
    base.APIRule(
        name="stacks:environment",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get stack environment.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/environment",
            },
        ],
    ),
    base.APIRule(
        name="stacks:files",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Get stack files.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/files"},
        ],
    ),
    base.APIRule(
        name="stacks:update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update stack.",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}"}],
    ),
    base.APIRule(
        name="stacks:update_patch",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Update stack (PATCH).",
        scope_types=["system", "project"],
        operations=[
            {"method": "PATCH", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}"},
        ],
    ),
    base.APIRule(
        name="stacks:update_no_change",
        check_str=("rule:stacks:update_patch"),
        description="Update stack (PATCH) with no changes.",
        scope_types=["system", "project"],
        operations=[
            {"method": "PATCH", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}"},
        ],
    ),
    base.APIRule(
        name="stacks:preview_update",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Preview update stack.",
        scope_types=["system", "project"],
        operations=[
            {"method": "PUT", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/preview"},
        ],
    ),
    base.APIRule(
        name="stacks:preview_update_patch",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Preview update stack (PATCH).",
        scope_types=["system", "project"],
        operations=[
            {"method": "PATCH", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/preview"},
        ],
    ),
    base.APIRule(
        name="stacks:validate_template",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Validate template.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v1/{tenant_id}/validate"}],
    ),
    base.APIRule(
        name="stacks:snapshot",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Snapshot Stack.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "POST",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/snapshots",
            },
        ],
    ),
    base.APIRule(
        name="stacks:show_snapshot",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="Show snapshot.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/"
                "{stack_id}/snapshots/{snapshot_id}",
            },
        ],
    ),
    base.APIRule(
        name="stacks:delete_snapshot",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s)"
        ),
        description="Delete snapshot.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "DELETE",
                "path": "/v1/{tenant_id}/stacks/{stack_name}"
                "/{stack_id}/snapshots/{snapshot_id}",
            },
        ],
    ),
    base.APIRule(
        name="stacks:list_snapshots",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and project_id:%(project_id)s)"
        ),
        description="List snapshots.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/snapshots",
            },
        ],
    ),
    base.APIRule(
        name="stacks:restore_snapshot",
        check_str=(
            "(role:admin and system_scope:all) or (role:member and project_id:%(project_id)s) "
        ),
        description="Restore snapshot.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "POST",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/"
                "{stack_id}/snapshots/{snapshot_id}/restore",
            },
        ],
    ),
    base.APIRule(
        name="stacks:list_outputs",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="List outputs.",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/outputs"},
        ],
    ),
    base.APIRule(
        name="stacks:show_output",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(project_id)s) "
        ),
        description="Show outputs.",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/{tenant_id}/stacks/{stack_name}/{stack_id}/outputs/{output_key}",
            },
        ],
    ),
)

__all__ = ("list_rules",)
