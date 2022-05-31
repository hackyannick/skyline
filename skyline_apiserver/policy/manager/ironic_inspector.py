# flake8: noqa
# fmt: off

from . import base

list_rules = (
    base.Rule(
        name="is_admin",
        check_str=("role:admin or role:administrator or role:baremetal_admin"),
        description="Full read/write API access",
    ),
    base.Rule(
        name="is_observer",
        check_str=("role:baremetal_observer"),
        description="Read-only API access",
    ),
    base.Rule(
        name="public_api",
        check_str=("is_public_api:True"),
        description="Internal flag for public API routes",
    ),
    base.Rule(
        name="default",
        check_str=("!"),
        description="Default API access policy",
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
        operations=[{"method": "GET", "path": "/introspection"}, {"method": "GET", "path": "/introspection/{node_id}"}],
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
        operations=[{"method": "GET", "path": "/rules"}, {"method": "GET", "path": "/rules/{rule_id}"}],
    ),
    base.APIRule(
        name="introspection:rule:delete",
        check_str=("role:admin and system_scope:all"),
        description="Delete introspection rule(s)",
        scope_types=["project"],
        operations=[{"method": "DELETE", "path": "/rules"}, {"method": "DELETE", "path": "/rules/{rule_id}"}],
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
