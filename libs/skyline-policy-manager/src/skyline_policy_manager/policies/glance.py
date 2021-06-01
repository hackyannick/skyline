from . import base

list_rules = (
    base.Rule(
        name="default",
        check_str=(""),
        description="Defines the default rule used for policies that "
        "historically had an empty policy in the supplied "
        "policy.json file.",
    ),
    base.Rule(
        name="context_is_admin",
        check_str=("role:admin"),
        description="Defines the rule for the is_admin:True check.",
    ),
    base.Rule(
        name="manage_image_cache",
        check_str=("role:admin"),
        description="Manage image cache",
    ),
    base.Rule(
        name="metadef_default",
        check_str=(""),
        description="No description",
    ),
    base.Rule(
        name="metadef_admin",
        check_str=("role:admin"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_namespace",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_namespaces",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="modify_metadef_namespace",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="add_metadef_namespace",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="delete_metadef_namespace",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_object",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_objects",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="modify_metadef_object",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="add_metadef_object",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="delete_metadef_object",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="list_metadef_resource_types",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_resource_type",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="add_metadef_resource_type_association",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="remove_metadef_resource_type_association",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_property",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_properties",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="modify_metadef_property",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="add_metadef_property",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="remove_metadef_property",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_tag",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="get_metadef_tags",
        check_str=("rule:metadef_default"),
        description="No description",
    ),
    base.Rule(
        name="modify_metadef_tag",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="add_metadef_tag",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="add_metadef_tags",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="delete_metadef_tag",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.Rule(
        name="delete_metadef_tags",
        check_str=("rule:metadef_admin"),
        description="No description",
    ),
    base.APIRule(
        name="add_image",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Create new image",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v2/images"}],
    ),
    base.APIRule(
        name="delete_image",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Deletes the image",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="get_image",
        check_str=(
            "role:admin or (role:reader and (project_id:%(project_id)s or "
            'project_id:%(member_id)s or "community":%(visibility)s or '
            '"public":%(visibility)s)) '
        ),
        description="Get specified image",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="get_images",
        check_str=("role:admin or (role:reader and project_id:%(project_id)s)"),
        description="Get all available images",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/images"}],
    ),
    base.APIRule(
        name="modify_image",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Updates given image",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="publicize_image",
        check_str=("role:admin"),
        description="Publicize given image",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="communitize_image",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Communitize given image",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="download_image",
        check_str=(
            "role:admin or (role:member and (project_id:%(project_id)s or "
            'project_id:%(member_id)s or "community":%(visibility)s or '
            '"public":%(visibility)s)) '
        ),
        description="Downloads given image",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/images/{image_id}/file"}],
    ),
    base.APIRule(
        name="upload_image",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Uploads data to specified image",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/v2/images/{image_id}/file"}],
    ),
    base.APIRule(
        name="delete_image_location",
        check_str=("role:admin"),
        description="Deletes the location of given image",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="get_image_location",
        check_str=("role:admin or (role:reader and project_id:%(project_id)s)"),
        description="Reads the location of the image",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="set_image_location",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Sets location URI to given image",
        scope_types=["system", "project"],
        operations=[{"method": "PATCH", "path": "/v2/images/{image_id}"}],
    ),
    base.APIRule(
        name="add_member",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Create image member",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v2/images/{image_id}/members"}],
    ),
    base.APIRule(
        name="delete_member",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Delete image member",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/v2/images/{image_id}/members/{member_id}"}],
    ),
    base.APIRule(
        name="get_member",
        check_str=("role:admin or (role:reader and project_id:%(project_id)s)"),
        description="Show image member details",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/images/{image_id}/members/{member_id}"}],
    ),
    base.APIRule(
        name="get_members",
        check_str=("role:admin or (role:reader and project_id:%(project_id)s)"),
        description="List image members",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/images/{image_id}/members"}],
    ),
    base.APIRule(
        name="modify_member",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Update image member",
        scope_types=["system", "project"],
        operations=[{"method": "PUT", "path": "/v2/images/{image_id}/members/{member_id}"}],
    ),
    base.APIRule(
        name="deactivate",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Deactivate image",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v2/images/{image_id}/actions/deactivate"}],
    ),
    base.APIRule(
        name="reactivate",
        check_str=("role:admin or (role:member and project_id:%(project_id)s)"),
        description="Reactivate image",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v2/images/{image_id}/actions/reactivate"}],
    ),
    base.APIRule(
        name="copy_image",
        check_str=("role:admin"),
        description="Copy existing image to other stores",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v2/images/{image_id}/import"}],
    ),
    base.APIRule(
        name="get_task",
        check_str=("rule:default"),
        description="Get an image task.\n#\n#This granular policy controls "
        "access to tasks, both from the tasks API as well\n"
        "#as internal locations in Glance that use tasks "
        "(like import). Practically this\n#cannot be more "
        "restrictive than the policy that controls import or "
        "things will\n#break, and changing it from the default "
        "is almost certainly not what you want.\n#Access to the "
        "external tasks API should be restricted as desired by "
        "the\n#tasks_api_access policy. This may change in the "
        "future.\n#",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/tasks/{task_id}"}],
    ),
    base.APIRule(
        name="get_tasks",
        check_str=("rule:default"),
        description="List tasks for all images.\n#\n#This granular policy "
        "controls access to tasks, both from the tasks API as "
        "well\n#as internal locations in Glance that use tasks ("
        "like import). Practically this\n#cannot be more "
        "restrictive than the policy that controls import or "
        "things will\n#break, and changing it from the default "
        "is almost certainly not what you want.\n#Access to the "
        "external tasks API should be restricted as desired by "
        "the\n#tasks_api_access policy. This may change in the "
        "future.\n#",
        scope_types=["system", "project"],
        operations=[{"method": "GET", "path": "/v2/tasks"}],
    ),
    base.APIRule(
        name="add_task",
        check_str=("rule:default"),
        description="List tasks for all images.\n#\n#This granular policy "
        "controls access to tasks, both from the tasks API as "
        "well\n#as internal locations in Glance that use tasks ("
        "like import). Practically this\n#cannot be more "
        "restrictive than the policy that controls import or "
        "things will\n#break, and changing it from the default "
        "is almost certainly not what you want.\n#Access to the "
        "external tasks API should be restricted as desired by "
        "the\n#tasks_api_access policy. This may change in the "
        "future.\n#",
        scope_types=["system", "project"],
        operations=[{"method": "POST", "path": "/v2/tasks"}],
    ),
    base.APIRule(
        name="modify_task",
        check_str=("rule:default"),
        description="This policy is not used.",
        scope_types=["system", "project"],
        operations=[{"method": "DELETE", "path": "/v2/tasks/{task_id}"}],
    ),
    base.APIRule(
        name="tasks_api_access",
        check_str=("role:admin"),
        description="\n#This is a generic blanket policy for protecting all "
        "task APIs. It is not\n#granular and will not allow you "
        "to separate writable and readable task\n#operations "
        "into different roles.\n#",
        scope_types=["system", "project"],
        operations=[
            {"method": "GET", "path": "/v2/tasks/{task_id}"},
            {"method": "GET", "path": "/v2/tasks"},
            {"method": "POST", "path": "/v2/tasks"},
            {"method": "DELETE", "path": "/v2/tasks/{task_id}"},
        ],
    ),
)

__all__ = ("list_rules",)
