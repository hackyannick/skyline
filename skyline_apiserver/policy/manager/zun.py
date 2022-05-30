from . import base

list_rules = (
    base.Rule(
        name="context_is_admin",
        check_str=("role:admin"),
        description="No description",
    ),
    base.Rule(
        name="admin_or_owner",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="No description",
    ),
    base.Rule(
        name="admin_api",
        check_str=("rule:context_is_admin"),
        description="No description",
    ),
    base.Rule(
        name="deny_everybody",
        check_str=("!"),
        description="Default rule for deny everybody.",
    ),
    base.APIRule(
        name="zun:container:create",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Create a new container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:container:create:runtime",
        check_str=("(role:admin)"),
        description="Create a new container with specified runtime.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:container:create:privileged",
        check_str=("(!)"),
        description="Create a new privileged container.Warning: the privileged container has a big security risk so be caution if you want to enable this feature",  # noqa
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:container:create:requested_destination",
        check_str=("(role:admin)"),
        description="Create a container on the requested compute host.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:container:create:image_pull_policy",
        check_str=("(role:admin)"),
        description="Create a new container with specified image pull policy.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:container:delete",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Delete a container.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/containers/{container_ident}"}],
    ),
    base.APIRule(
        name="zun:container:delete_all_projects",
        check_str=("(role:admin)"),
        description="Delete a container from all projects.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/containers/{container_ident}"}],
    ),
    base.APIRule(
        name="zun:container:delete_force",
        check_str=("(role:admin)"),
        description="Forcibly delete a container.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/containers/{container_ident}"}],
    ),
    base.APIRule(
        name="zun:container:get_one",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Retrieve the details of a specific container.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers/{container_ident}"}],
    ),
    base.APIRule(
        name="zun:container:get_one:host",
        check_str=("(role:admin)"),
        description="Retrieve the host field of containers.",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/v1/containers/{container_ident}"},
            {"method": "GET", "path": "/v1/containers"},
            {"method": "POST", "path": "/v1/containers"},
            {"method": "PATCH", "path": "/v1/containers/{container_ident}"},
        ],
    ),
    base.APIRule(
        name="zun:container:get_one:image_pull_policy",
        check_str=("(role:admin)"),
        description="Retrieve the image_pull_policy field of containers.",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/v1/containers/{container_ident}"},
            {"method": "GET", "path": "/v1/containers"},
            {"method": "POST", "path": "/v1/containers"},
            {"method": "PATCH", "path": "/v1/containers/{container_ident}"},
        ],
    ),
    base.APIRule(
        name="zun:container:get_one:privileged",
        check_str=("(role:admin)"),
        description="Retrieve the privileged field of containers.",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/v1/containers/{container_ident}"},
            {"method": "GET", "path": "/v1/containers"},
            {"method": "POST", "path": "/v1/containers"},
            {"method": "PATCH", "path": "/v1/containers/{container_ident}"},
        ],
    ),
    base.APIRule(
        name="zun:container:get_one:runtime",
        check_str=("(role:admin)"),
        description="Retrieve the runtime field of containers.",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/v1/containers/{container_ident}"},
            {"method": "GET", "path": "/v1/containers"},
            {"method": "POST", "path": "/v1/containers"},
            {"method": "PATCH", "path": "/v1/containers/{container_ident}"},
        ],
    ),
    base.APIRule(
        name="zun:container:get_one_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve the details of a specific container from all projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers/{container_ident}"}],
    ),
    base.APIRule(
        name="zun:container:get_all",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Retrieve the details of all containers.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:container:get_all_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve the details of all containers across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:container:update",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Update a container.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/containers/{container_ident}"}],
    ),
    base.APIRule(
        name="zun:container:start",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Start a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/start"}],
    ),
    base.APIRule(
        name="zun:container:stop",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Stop a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/stop"}],
    ),
    base.APIRule(
        name="zun:container:reboot",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Reboot a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/reboot"}],
    ),
    base.APIRule(
        name="zun:container:pause",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Pause a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/pause"}],
    ),
    base.APIRule(
        name="zun:container:unpause",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Unpause a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/unpause"}],
    ),
    base.APIRule(
        name="zun:container:logs",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Get the log of a container",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers/{container_ident}/logs"}],
    ),
    base.APIRule(
        name="zun:container:execute",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Execute command in a running container",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/execute"}],
    ),
    base.APIRule(
        name="zun:container:execute_resize",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Resize the TTY used by an execute command.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/containers/{container_ident}/execute_resize"}
        ],
    ),
    base.APIRule(
        name="zun:container:kill",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Kill a running container",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/kill"}],
    ),
    base.APIRule(
        name="zun:container:rename",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Rename a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/rename"}],
    ),
    base.APIRule(
        name="zun:container:attach",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Attach to a running container",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers/{container_ident}/attach"}],
    ),
    base.APIRule(
        name="zun:container:resize",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Resize a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/resize"}],
    ),
    base.APIRule(
        name="zun:container:top",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Display the running processes inside the container.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers/{container_ident}/top"}],
    ),
    base.APIRule(
        name="zun:container:get_archive",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Get a tar archive of a path of container.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers/{container_ident}/get_archive"}],
    ),
    base.APIRule(
        name="zun:container:put_archive",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Put a tar archive to be extracted to a path of container",
        scope_types=["project"],
        operations=[{"method": "PUT", "path": "/v1/containers/{container_ident}/put_archive"}],
    ),
    base.APIRule(
        name="zun:container:stats",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Display the statistics of a container",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/containers/{container_ident}/stats"}],
    ),
    base.APIRule(
        name="zun:container:commit",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Commit a container",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/commit"}],
    ),
    base.APIRule(
        name="zun:container:add_security_group",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Add a security group to a specific container.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/containers/{container_ident}/add_security_group"}
        ],
    ),
    base.APIRule(
        name="zun:container:network_detach",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Detach a network from a container.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/containers/{container_ident}/network_detach"}
        ],
    ),
    base.APIRule(
        name="zun:container:network_attach",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Attach a network from a container.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/containers/{container_ident}/network_attach"}
        ],
    ),
    base.APIRule(
        name="zun:container:remove_security_group",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Remove security group from a specific container.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/containers/{container_ident}/remove_security_group"}
        ],
    ),
    base.APIRule(
        name="zun:container:rebuild",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Rebuild a container.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers/{container_ident}/rebuild"}],
    ),
    base.APIRule(
        name="zun:container:resize_container",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Resize an existing  container.",
        scope_types=["project"],
        operations=[
            {"method": "POST", "path": "/v1/containers/{container_ident}/resize_container"}
        ],
    ),
    base.APIRule(
        name="zun:image:pull",
        check_str=("(role:admin)"),
        description="Pull an image.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/images"}],
    ),
    base.APIRule(
        name="zun:image:get_all",
        check_str=("(role:admin)"),
        description="Print a list of available images.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/images"}],
    ),
    base.APIRule(
        name="zun:image:get_one",
        check_str=("(role:admin)"),
        description="Retrieve the details of a specific image.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/images/{image_id}"}],
    ),
    base.APIRule(
        name="zun:image:search",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Search an image.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/images/{image_ident}/search"}],
    ),
    base.APIRule(
        name="zun:image:delete",
        check_str=("(role:admin)"),
        description="Delete an image.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/images/{image_ident}"}],
    ),
    base.APIRule(
        name="zun:zun-service:delete",
        check_str=("(role:admin)"),
        description="Delete a service.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/services"}],
    ),
    base.APIRule(
        name="zun:zun-service:disable",
        check_str=("(role:admin)"),
        description="Disable a service.",
        scope_types=["project"],
        operations=[{"method": "PUT", "path": "/v1/services/disable"}],
    ),
    base.APIRule(
        name="zun:zun-service:enable",
        check_str=("(role:admin)"),
        description="Enable a service.",
        scope_types=["project"],
        operations=[{"method": "PUT", "path": "/v1/services/enable"}],
    ),
    base.APIRule(
        name="zun:zun-service:force_down",
        check_str=("(role:admin)"),
        description="Forcibly shutdown a service.",
        scope_types=["project"],
        operations=[{"method": "PUT", "path": "/v1/services/force_down"}],
    ),
    base.APIRule(
        name="zun:zun-service:get_all",
        check_str=("(role:admin)"),
        description="Show the status of a service.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/services"}],
    ),
    base.APIRule(
        name="zun:host:get_all",
        check_str=("(role:admin)"),
        description="List all compute hosts.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/hosts"}],
    ),
    base.APIRule(
        name="zun:host:get",
        check_str=("(role:admin)"),
        description="Show the details of a specific compute host.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/hosts/{host_ident}"}],
    ),
    base.APIRule(
        name="zun:capsule:create",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Create a capsule",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/capsules/"}],
    ),
    base.APIRule(
        name="zun:capsule:delete",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Delete a capsule",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/capsules/{capsule_ident}"}],
    ),
    base.APIRule(
        name="zun:capsule:delete_all_projects",
        check_str=("(role:admin)"),
        description="Delete a container in any project.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/capsules/{capsule_ident}"}],
    ),
    base.APIRule(
        name="zun:capsule:get",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Retrieve the details of a capsule.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/capsules/{capsule_ident}"}],
    ),
    base.APIRule(
        name="zun:capsule:get:host",
        check_str=("(role:admin)"),
        description="Retrieve the host field of a capsule.",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/v1/capsules/{capsule_ident}"},
            {"method": "GET", "path": "/v1/capsules"},
            {"method": "POST", "path": "/v1/capsules"},
        ],
    ),
    base.APIRule(
        name="zun:capsule:get_one_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve the details of a capsule in any project.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/capsules/{capsule_ident}"}],
    ),
    base.APIRule(
        name="zun:capsule:get_all",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="List all capsules.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/capsules/"}],
    ),
    base.APIRule(
        name="zun:capsule:get_all_all_projects",
        check_str=("(role:admin)"),
        description="List all capsules across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/capsules/"}],
    ),
    base.APIRule(
        name="zun:network:attach_external_network",
        check_str=("role:admin"),
        description="Attach an unshared external network to a container",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/containers"}],
    ),
    base.APIRule(
        name="zun:network:create",
        check_str=("role:admin"),
        description="Create a network",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/networks"}],
    ),
    base.APIRule(
        name="zun:network:delete",
        check_str=("role:admin"),
        description="Delete a network",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/networks"}],
    ),
    base.APIRule(
        name="zun:container:actions",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="List actions and show action details for a container",
        scope_types=["project"],
        operations=[
            {"method": "GET", "path": "/v1/containers/{container_ident}/container_actions/"},
            {
                "method": "GET",
                "path": "/v1/containers/{container_ident}/container_actions/{request_id}",
            },
        ],
    ),
    base.APIRule(
        name="zun:container:action:events",
        check_str=("(role:admin)"),
        description="Add events details in action details for a container.",
        scope_types=["project"],
        operations=[
            {
                "method": "GET",
                "path": "/v1/containers/{container_ident}/container_actions/{request_id}",
            }
        ],
    ),
    base.APIRule(
        name="zun:availability_zones:get_all",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="List availability zone",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/availability_zones"}],
    ),
    base.APIRule(
        name="zun:quota:update",
        check_str=("(role:admin)"),
        description="Update quotas for a project",
        scope_types=["project"],
        operations=[{"method": "PUT", "path": "/v1/quotas/{project_id}"}],
    ),
    base.APIRule(
        name="zun:quota:delete",
        check_str=("(role:admin)"),
        description="Delete quotas for a project",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/quotas/{project_id}"}],
    ),
    base.APIRule(
        name="zun:quota:get",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Get quotas for a project",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/quotas/{project_id}"}],
    ),
    base.APIRule(
        name="zun:quota:get_default",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Get default quotas for a project",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/quotas/defaults"}],
    ),
    base.APIRule(
        name="zun:quota_class:update",
        check_str=("(role:admin)"),
        description="Update quotas for specific quota class",
        scope_types=["project"],
        operations=[{"method": "PUT", "path": "/v1/quota_classes/{quota_class_name}"}],
    ),
    base.APIRule(
        name="zun:quota_class:get",
        check_str=("(role:admin)"),
        description="List quotas for specific quota class",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/quota_classes/{quota_class_name}"}],
    ),
    base.APIRule(
        name="zun:registry:create",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Create a new registry.",
        scope_types=["project"],
        operations=[{"method": "POST", "path": "/v1/registries"}],
    ),
    base.APIRule(
        name="zun:registry:delete",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Delete a registry.",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/v1/registries/{registry_ident}"}],
    ),
    base.APIRule(
        name="zun:registry:get_one",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Retrieve the details of a specific registry.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/registries/{registry_ident}"}],
    ),
    base.APIRule(
        name="zun:registry:get_all",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Retrieve the details of all registries.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/registries"}],
    ),
    base.APIRule(
        name="zun:registry:get_all_all_projects",
        check_str=("(role:admin)"),
        description="Retrieve the details of all registries across projects.",
        scope_types=["project"],
        operations=[{"method": "GET", "path": "/v1/registries"}],
    ),
    base.APIRule(
        name="zun:registry:update",
        check_str=("is_admin:True or project_id:%(project_id)s"),
        description="Update a registry.",
        scope_types=["project"],
        operations=[{"method": "PATCH", "path": "/v1/registries/{registry_ident}"}],
    ),
)

__all__ = ("list_rules",)