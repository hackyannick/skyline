from . import base

list_rules = (
    base.Rule(
        name="admin_api",
        check_str=("role:admin or role:administrator"),
        description="Legacy rule for cloud admin access",
    ),
    base.Rule(
        name="public_api",
        check_str=("is_public_api:True"),
        description="Internal flag for public API routes",
    ),
    base.Rule(
        name="show_password",
        check_str=("!"),
        description="Show or mask secrets within node driver information in API responses",
    ),
    base.Rule(
        name="show_instance_secrets",
        check_str=("!"),
        description="Show or mask secrets within instance information in API responses",
    ),
    base.Rule(
        name="is_member",
        check_str=(
            "(project_domain_id:default or project_domain_id:None) and "
            "(project_name:demo or project_name:baremetal)"
        ),
        description="May be used to restrict access to specific projects",
    ),
    base.Rule(
        name="is_observer",
        check_str=("rule:is_member and (role:observer or role:baremetal_observer)"),
        description="Read-only API access",
    ),
    base.Rule(
        name="is_admin",
        check_str=("rule:admin_api or (rule:is_member and role:baremetal_admin)"),
        description="Full read/write API access",
    ),
    base.Rule(
        name="is_node_owner",
        check_str=("project_id:%(node.owner)s"),
        description="Owner of node",
    ),
    base.Rule(
        name="is_node_lessee",
        check_str=("project_id:%(node.lessee)s"),
        description="Lessee of node",
    ),
    base.Rule(
        name="is_allocation_owner",
        check_str=("project_id:%(allocation.owner)s"),
        description="Owner of allocation",
    ),
    base.APIRule(
        name="baremetal:node:create",
        check_str=("role:admin and system_scope:all"),
        description="Create Node records",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/nodes"}],
    ),
    base.APIRule(
        name="baremetal:node:list",
        check_str=("role:reader"),
        description="Retrieve multiple Node records, "
        "filtered by an explicit owner or the client project_id",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/nodes"},
            {"method": "GET", "path": "/nodes/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:list_all",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve multiple Node records",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/nodes"},
            {"method": "GET", "path": "/nodes/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:get",
        check_str=(
            "(role:reader and system_scope:all) or "
            "(role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Retrieve a single Node record",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:get:filter_threshold",
        check_str=("role:reader and system_scope:all"),
        description="Filter to allow operators to govern the threshold where "
        "information should be filtered. Non-authorized users "
        "will be subjected to additional API policy checks for "
        "API content response bodies.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:get:last_error",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(node.owner)s) "
        ),
        description="Governs if the node last_error field is masked from "
        "APIclients with insufficent privileges.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:get:reservation",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(node.owner)s) "
        ),
        description="Governs if the node reservation field is masked from "
        "APIclients with insufficent privileges.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:get:driver_internal_info",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(node.owner)s) "
        ),
        description="Governs if the node driver_internal_info field is "
        "masked from API clients with insufficent privileges.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:get:driver_info",
        check_str=(
            "(role:reader and system_scope:all) or (role:reader and "
            "project_id:%(node.owner)s) "
        ),
        description="Governs if the driver_info field is masked from "
        "APIclients with insufficent privileges.",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:driver_info",
        check_str=(
            "(role:member and system_scope:all) or (role:member and "
            "project_id:%(node.owner)s) "
        ),
        description="Governs if node driver_info field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:properties",
        check_str=(
            "(role:member and system_scope:all) or (role:member and "
            "project_id:%(node.owner)s) "
        ),
        description="Governs if node properties field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:chassis_uuid",
        check_str=("role:admin and system_scope:all"),
        description="Governs if node chassis_uuid field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:instance_uuid",
        check_str=(
            "(role:member and system_scope:all) or (role:member and "
            "project_id:%(node.owner)s) "
        ),
        description="Governs if node instance_uuid field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:lessee",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Governs if node lessee field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:owner",
        check_str=("role:member and system_scope:all"),
        description="Governs if node owner field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:driver_interfaces",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Governs if node driver and driver interfaces field "
        "can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:network_data",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Governs if node driver_info field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:conductor_group",
        check_str=("role:member and system_scope:all"),
        description="Governs if node conductor_group field can be updated "
        "via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:name",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Governs if node name field can be updated via the API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update:retired",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Governs if node retired and retired reason can be "
        "updated by API clients.",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Generalized update of node records",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update_extra",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Update Node extra field",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update_instance_info",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Update Node instance_info field",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:update_owner_provisioned",
        check_str=("role:admin and system_scope:all"),
        description="Update Node owner even when Node is provisioned",
        scope_types=["system"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:delete",
        check_str=("role:admin and system_scope:all"),
        description="Delete Node records",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:validate",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Request active validation of Nodes",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}/validate"}],
    ),
    base.APIRule(
        name="baremetal:node:set_maintenance",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Set maintenance flag, taking a Node out of service",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/nodes/{node_ident}/maintenance"}],
    ),
    base.APIRule(
        name="baremetal:node:clear_maintenance",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Clear maintenance flag, placing the Node into service again",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/nodes/{node_ident}/maintenance"}],
    ),
    base.APIRule(
        name="baremetal:node:get_boot_device",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Retrieve Node boot device metadata",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/nodes/{node_ident}/management/boot_device"},
            {"method": "GET", "path": "/nodes/{node_ident}/management/boot_device/supported"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:set_boot_device",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Change Node boot device",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/nodes/{node_ident}/management/boot_device"}],
    ),
    base.APIRule(
        name="baremetal:node:get_indicator_state",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Retrieve Node indicators and their states",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "GET",
                "path": "/nodes/{node_ident}/management/indicators/{component}/{indicator}",
            },
            {"method": "GET", "path": "/nodes/{node_ident}/management/indicators"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:set_indicator_state",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Change Node indicator state",
        scope_types=["system", "project"],
        operations=[
            {
                "method": "PUT",
                "path": "/nodes/{node_ident}/management/indicators/{component}/{indicator}",
            },
        ],
    ),
    base.APIRule(
        name="baremetal:node:inject_nmi",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Inject NMI for a node",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/nodes/{node_ident}/management/inject_nmi"}],
    ),
    base.APIRule(
        name="baremetal:node:get_states",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="View Node power and provision state",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}/states"}],
    ),
    base.APIRule(
        name="baremetal:node:set_power_state",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Change Node power status",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/nodes/{node_ident}/states/power"}],
    ),
    base.APIRule(
        name="baremetal:node:set_provision_state",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Change Node provision status",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/nodes/{node_ident}/states/provision"}],
    ),
    base.APIRule(
        name="baremetal:node:set_raid_state",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Change Node RAID status",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/nodes/{node_ident}/states/raid"}],
    ),
    base.APIRule(
        name="baremetal:node:get_console",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Get Node console connection information",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}/states/console"}],
    ),
    base.APIRule(
        name="baremetal:node:set_console_state",
        check_str=(
            "(role:member and system_scope:all) or (role:member and project_id:%(node.owner)s)"
        ),
        description="Change Node console status",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/nodes/{node_ident}/states/console"}],
    ),
    base.APIRule(
        name="baremetal:node:vif:list",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="List VIFs attached to node",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}/vifs"}],
    ),
    base.APIRule(
        name="baremetal:node:vif:attach",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Attach a VIF to a node",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/nodes/{node_ident}/vifs"}],
    ),
    base.APIRule(
        name="baremetal:node:vif:detach",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Detach a VIF from a node",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/nodes/{node_ident}/vifs/{node_vif_ident}"}],
    ),
    base.APIRule(
        name="baremetal:node:traits:list",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="List node traits",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/nodes/{node_ident}/traits"}],
    ),
    base.APIRule(
        name="baremetal:node:traits:set",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Add a trait to, or replace all traits of, a node",
        scope_types=["system", "project"],
        operations=[
            {"method": "PUT", "path": "/nodes/{node_ident}/traits"},
            {"method": "PUT", "path": "/nodes/{node_ident}/traits/{trait}"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:traits:delete",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Remove one or all traits from a node",
        scope_types=["system", "project"],
        operations=[
            {"method": "DELETE", "path": "/nodes/{node_ident}/traits"},
            {"method": "DELETE", "path": "/nodes/{node_ident}/traits/{trait}"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:bios:get",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Retrieve Node BIOS information",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/nodes/{node_ident}/bios"},
            {"method": "GET", "path": "/nodes/{node_ident}/bios/{setting}"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:disable_cleaning",
        check_str=("role:admin and system_scope:all"),
        description="Disable Node disk cleaning",
        scope_types=["system"],
        operations=[{"method": "PATCH", "path": "/nodes/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:port:get",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Retrieve Port records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/ports/{port_id}"},
            {"method": "GET", "path": "/nodes/{node_ident}/ports"},
            {"method": "GET", "path": "/nodes/{node_ident}/ports/detail"},
            {"method": "GET", "path": "/portgroups/{portgroup_ident}/ports"},
            {"method": "GET", "path": "/portgroups/{portgroup_ident}/ports/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:port:list",
        check_str=("role:reader"),
        description="Retrieve multiple Port records, filtered by owner",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/ports"},
            {"method": "GET", "path": "/ports/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:port:list_all",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve multiple Port records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/ports"},
            {"method": "GET", "path": "/ports/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:port:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Create Port records",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/ports"}],
    ),
    base.APIRule(
        name="baremetal:port:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Delete Port records",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/ports/{port_id}"}],
    ),
    base.APIRule(
        name="baremetal:port:update",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Update Port records",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/ports/{port_id}"}],
    ),
    base.APIRule(
        name="baremetal:portgroup:get",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Retrieve Portgroup records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/portgroups"},
            {"method": "GET", "path": "/portgroups/detail"},
            {"method": "GET", "path": "/portgroups/{portgroup_ident}"},
            {"method": "GET", "path": "/nodes/{node_ident}/portgroups"},
            {"method": "GET", "path": "/nodes/{node_ident}/portgroups/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:portgroup:create",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Create Portgroup records",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/portgroups"}],
    ),
    base.APIRule(
        name="baremetal:portgroup:delete",
        check_str=(
            "(role:admin and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Delete Portgroup records",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/portgroups/{portgroup_ident}"}],
    ),
    base.APIRule(
        name="baremetal:portgroup:update",
        check_str=(
            "(role:member and system_scope:all) or (role:admin and project_id:%(node.owner)s)"
        ),
        description="Update Portgroup records",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/portgroups/{portgroup_ident}"}],
    ),
    base.APIRule(
        name="baremetal:portgroup:list",
        check_str=("role:reader"),
        description="Retrieve multiple Port records, filtered by owner",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/portgroups"},
            {"method": "GET", "path": "/portgroups/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:portgroup:list_all",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve multiple Port records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/portgroups"},
            {"method": "GET", "path": "/portgroups/detail"},
        ],
    ),
    base.APIRule(
        name="baremetal:chassis:get",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve Chassis records",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/chassis"},
            {"method": "GET", "path": "/chassis/detail"},
            {"method": "GET", "path": "/chassis/{chassis_id}"},
        ],
    ),
    base.APIRule(
        name="baremetal:chassis:create",
        check_str=("role:admin and system_scope:all"),
        description="Create Chassis records",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/chassis"}],
    ),
    base.APIRule(
        name="baremetal:chassis:delete",
        check_str=("role:admin and system_scope:all"),
        description="Delete Chassis records",
        scope_types=["system"],
        operations=[{"method": "DELETE", "path": "/chassis/{chassis_id}"}],
    ),
    base.APIRule(
        name="baremetal:chassis:update",
        check_str=("role:member and system_scope:all"),
        description="Update Chassis records",
        scope_types=["system"],
        operations=[{"method": "PATCH", "path": "/chassis/{chassis_id}"}],
    ),
    base.APIRule(
        name="baremetal:driver:get",
        check_str=("role:reader and system_scope:all"),
        description="View list of available drivers",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/drivers"},
            {"method": "GET", "path": "/drivers/{driver_name}"},
        ],
    ),
    base.APIRule(
        name="baremetal:driver:get_properties",
        check_str=("role:reader and system_scope:all"),
        description="View driver-specific properties",
        scope_types=["system"],
        operations=[{"method": "GET", "path": "/drivers/{driver_name}/properties"}],
    ),
    base.APIRule(
        name="baremetal:driver:get_raid_logical_disk_properties",
        check_str=("role:reader and system_scope:all"),
        description="View driver-specific RAID metadata",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/drivers/{driver_name}/raid/logical_disk_properties"},
        ],
    ),
    base.APIRule(
        name="baremetal:node:vendor_passthru",
        check_str=("role:admin and system_scope:all"),
        description="Access vendor-specific Node functions",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "nodes/{node_ident}/vendor_passthru/methods"},
            {"method": "GET", "path": "nodes/{node_ident}/vendor_passthru?method={method_name}"},
            {"method": "PUT", "path": "nodes/{node_ident}/vendor_passthru?method={method_name}"},
            {"method": "POST", "path": "nodes/{node_ident}/vendor_passthru?method={method_name}"},
            {
                "method": "PATCH",
                "path": "nodes/{node_ident}/vendor_passthru?method={method_name}",
            },
            {
                "method": "DELETE",
                "path": "nodes/{node_ident}/vendor_passthru?method={method_name}",
            },
        ],
    ),
    base.APIRule(
        name="baremetal:driver:vendor_passthru",
        check_str=("role:admin and system_scope:all"),
        description="Access vendor-specific Driver functions",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "drivers/{driver_name}/vendor_passthru/methods"},
            {
                "method": "GET",
                "path": "drivers/{driver_name}/vendor_passthru?method={method_name}",
            },
            {
                "method": "PUT",
                "path": "drivers/{driver_name}/vendor_passthru?method={method_name}",
            },
            {
                "method": "POST",
                "path": "drivers/{driver_name}/vendor_passthru?method={method_name}",
            },
            {
                "method": "PATCH",
                "path": "drivers/{driver_name}/vendor_passthru?method={method_name}",
            },
            {
                "method": "DELETE",
                "path": "drivers/{driver_name}/vendor_passthru?method={method_name}",
            },
        ],
    ),
    base.APIRule(
        name="baremetal:node:ipa_heartbeat",
        check_str=(""),
        description="Receive heartbeats from IPA ramdisk",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/heartbeat/{node_ident}"}],
    ),
    base.APIRule(
        name="baremetal:driver:ipa_lookup",
        check_str=(""),
        description="Access IPA ramdisk functions",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/lookup"}],
    ),
    base.APIRule(
        name="baremetal:volume:list_all",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve a list of all Volume connector and target records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/volume/connectors"},
            {"method": "GET", "path": "/volume/targets"},
            {"method": "GET", "path": "/nodes/{node_ident}/volume/connectors"},
            {"method": "GET", "path": "/nodes/{node_ident}/volume/targets"},
        ],
    ),
    base.APIRule(
        name="baremetal:volume:list",
        check_str=("role:reader"),
        description="Retrieve a list of Volume connector and target records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/volume/connectors"},
            {"method": "GET", "path": "/volume/targets"},
            {"method": "GET", "path": "/nodes/{node_ident}/volume/connectors"},
            {"method": "GET", "path": "/nodes/{node_ident}/volume/targets"},
        ],
    ),
    base.APIRule(
        name="baremetal:volume:get",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and (project_id:%(node.owner)s "
            "or project_id:%(node.lessee)s))"
        ),
        description="Retrieve Volume connector and target records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/volume"},
            {"method": "GET", "path": "/volume/connectors"},
            {"method": "GET", "path": "/volume/connectors/{volume_connector_id}"},
            {"method": "GET", "path": "/volume/targets"},
            {"method": "GET", "path": "/volume/targets/{volume_target_id}"},
            {"method": "GET", "path": "/nodes/{node_ident}/volume"},
            {"method": "GET", "path": "/nodes/{node_ident}/volume/connectors"},
            {"method": "GET", "path": "/nodes/{node_ident}/volume/targets"},
        ],
    ),
    base.APIRule(
        name="baremetal:volume:create",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:admin and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Create Volume connector and target records",
        scope_types=["system", "project"],
        operations=[
            {"method": "POST", "path": "/volume/connectors"},
            {"method": "POST", "path": "/volume/targets"},
        ],
    ),
    base.APIRule(
        name="baremetal:volume:delete",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:admin and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Delete Volume connector and target records",
        scope_types=["system", "project"],
        operations=[
            {"method": "DELETE", "path": "/volume/connectors/{volume_connector_id}"},
            {"method": "DELETE", "path": "/volume/targets/{volume_target_id}"},
        ],
    ),
    base.APIRule(
        name="baremetal:volume:update",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(node.owner)s) "
            "or (role:admin and project_id:%(node.lessee)s)"
        ),
        description="Update Volume connector and target records",
        scope_types=["system", "project"],
        operations=[
            {"method": "PATCH", "path": "/volume/connectors/{volume_connector_id}"},
            {"method": "PATCH", "path": "/volume/targets/{volume_target_id}"},
        ],
    ),
    base.APIRule(
        name="baremetal:volume:view_target_properties",
        check_str=("(role:reader and system_scope:all) or (role:admin)"),
        description="Ability to view volume target properties",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/volume/connectors/{volume_connector_id}"},
            {"method": "GET", "path": "/volume/targets/{volume_target_id}"},
        ],
    ),
    base.APIRule(
        name="baremetal:conductor:get",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve Conductor records",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/conductors"},
            {"method": "GET", "path": "/conductors/{hostname}"},
        ],
    ),
    base.APIRule(
        name="baremetal:allocation:get",
        check_str=(
            "(role:reader and system_scope:all) "
            "or (role:reader and project_id:%(allocation.owner)s)"
        ),
        description="Retrieve Allocation records",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/allocations/{allocation_id}"},
            {"method": "GET", "path": "/nodes/{node_ident}/allocation"},
        ],
    ),
    base.APIRule(
        name="baremetal:allocation:list",
        check_str=("role:reader"),
        description="Retrieve multiple Allocation records, filtered by owner",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/allocations"}],
    ),
    base.APIRule(
        name="baremetal:allocation:list_all",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve multiple Allocation records",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/allocations"}],
    ),
    base.APIRule(
        name="baremetal:allocation:create",
        check_str=("(role:member and system_scope:all) or (role:member)"),
        description="Create Allocation records",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/allocations"}],
    ),
    base.APIRule(
        name="baremetal:allocation:create_restricted",
        check_str=("role:member and system_scope:all"),
        description="Create Allocation records with a specific owner.",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/allocations"}],
    ),
    base.APIRule(
        name="baremetal:allocation:delete",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(allocation.owner)s)"
        ),
        description="Delete Allocation records",
        scope_types=["system", "project"],
        operations=[
            {"method": "DELETE", "path": "/allocations/{allocation_id}"},
            {"method": "DELETE", "path": "/nodes/{node_ident}/allocation"},
        ],
    ),
    base.APIRule(
        name="baremetal:allocation:update",
        check_str=(
            "(role:member and system_scope:all) "
            "or (role:member and project_id:%(allocation.owner)s)"
        ),
        description="Change name and extra fields of an allocation",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/allocations/{allocation_id}"}],
    ),
    base.APIRule(
        name="baremetal:allocation:create_pre_rbac",
        check_str=(
            "(rule:is_member and role:baremetal_admin) "
            "or (is_admin_project:True and role:admin)"
        ),
        description="Logical restrictor to prevent legacy allocation rule "
        "missuse - Requires blank allocations to originate from "
        "the legacy baremetal_admin.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/allocations/{allocation_id}"}],
    ),
    base.APIRule(
        name="baremetal:events:post",
        check_str=("role:admin and system_scope:all"),
        description="Post events",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/events"}],
    ),
    base.APIRule(
        name="baremetal:deploy_template:get",
        check_str=("role:reader and system_scope:all"),
        description="Retrieve Deploy Template records",
        scope_types=["system"],
        operations=[
            {"method": "GET", "path": "/deploy_templates"},
            {"method": "GET", "path": "/deploy_templates/{deploy_template_ident}"},
        ],
    ),
    base.APIRule(
        name="baremetal:deploy_template:create",
        check_str=("role:admin and system_scope:all"),
        description="Create Deploy Template records",
        scope_types=["system"],
        operations=[{"method": "POST", "path": "/deploy_templates"}],
    ),
    base.APIRule(
        name="baremetal:deploy_template:delete",
        check_str=("role:admin and system_scope:all"),
        description="Delete Deploy Template records",
        scope_types=["system"],
        operations=[{"method": "DELETE", "path": "/deploy_templates/{deploy_template_ident}"}],
    ),
    base.APIRule(
        name="baremetal:deploy_template:update",
        check_str=("role:admin and system_scope:all"),
        description="Update Deploy Template records",
        scope_types=["system"],
        operations=[{"method": "PATCH", "path": "/deploy_templates/{deploy_template_ident}"}],
    ),
    base.APIRule(
        name="introspection",
        check_str=("rule:public_api"),
        description="Access the API root for available versions information",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/"}],
    ),
    base.APIRule(
        name="introspection:version",
        check_str=("rule:public_api"),
        description="Access the versioned API root for version information",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/{version}"}],
    ),
    base.APIRule(
        name="introspection:continue",
        check_str=("rule:public_api"),
        description="Ramdisk callback to continue introspection",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/continue"}],
    ),
    base.APIRule(
        name="introspection:status",
        check_str=("role:reader and system_scope:all"),
        description="Get introspection status",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/introspection"},
            {"method": "GET", "path": "/introspection/{node_id}"},
        ],
    ),
    base.APIRule(
        name="introspection:start",
        check_str=("role:admin and system_scope:all"),
        description="Start introspection",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/introspection/{node_id}"}],
    ),
    base.APIRule(
        name="introspection:abort",
        check_str=("role:admin and system_scope:all"),
        description="Abort introspection",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/introspection/{node_id}/abort"}],
    ),
    base.APIRule(
        name="introspection:data",
        check_str=("role:admin and system_scope:all"),
        description="Get introspection data",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/introspection/{node_id}/data"}],
    ),
    base.APIRule(
        name="introspection:reapply",
        check_str=("role:admin and system_scope:all"),
        description="Reapply introspection on stored data",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/introspection/{node_id}/data/unprocessed"}],
    ),
    base.APIRule(
        name="introspection:rule:get",
        check_str=("role:admin and system_scope:all"),
        description="Get introspection rule(s)",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/rules"},
            {"method": "GET", "path": "/rules/{rule_id}"},
        ],
    ),
    base.APIRule(
        name="introspection:rule:delete",
        check_str=("role:admin and system_scope:all"),
        description="Delete introspection rule(s)",
        scope_types=["project"],
        operations=[
            {"method": "DELETE", "path": "/rules"},
            {"method": "DELETE", "path": "/rules/{rule_id}"},
        ],
    ),
    base.APIRule(
        name="introspection:rule:create",
        check_str=("role:admin and system_scope:all"),
        description="Create introspection rule",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/rules"}],
    ),
)

__all__ = ("list_rules",)