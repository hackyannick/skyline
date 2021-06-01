# Copyright 2021 99cloud
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

import os
import warnings
from dataclasses import InitVar, dataclass, field
from pathlib import Path, PurePath
from typing import Any, Dict, Iterator, Sequence, Tuple, Type

import yaml
from immutables import Map
from pydantic import BaseModel, create_model

from skyline_apiserver import __version__


@dataclass(frozen=True)
class Opt:
    name: str
    description: str
    schema: Any
    default: Any = None
    deprecated: bool = False
    value: Any = field(init=False, default=None)
    _schema_model: Type[BaseModel] = field(init=False, repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "_schema_model",
            create_model(f"Opt(name='{self.name}')", value=(self.schema, ...)),
        )

    def load(self, value: Any) -> None:
        value = self.default if value is None else value
        self._schema_model(value=value)
        object.__setattr__(self, "value", value)
        if self.deprecated:
            warnings.warn(
                f"The config opt {self.name} is deprecated, will be deleted after the"
                f" {__version__} version",
                DeprecationWarning,
            )


@dataclass(repr=False, frozen=True)
class Group:
    name: str
    init_opts: InitVar[Sequence[Opt]] = tuple()
    _opts: Map[str, Opt] = field(init=False, repr=False)

    def __post_init__(self, init_opts: Sequence[Opt]) -> None:
        object.__setattr__(self, "_opts", Map({opt.name: opt for opt in init_opts}))

    def __getattr__(self, name: str) -> Any:
        if name in self._opts:
            return self._opts[name].value
        raise AttributeError(name)

    def __contains__(self, key: Any) -> bool:
        return self._opts.__contains__(key)

    def __iter__(self) -> Iterator[Any]:
        return self._opts.__iter__()

    def __len__(self) -> int:
        return self._opts.__len__()

    def __repr__(self) -> str:
        items = ", ".join((f"{opt}=Opt(name='{opt}')" for opt in self._opts))
        return f"Group({items})"


@dataclass(repr=False, frozen=True)
class Configuration:
    init_groups: InitVar[Sequence[Group]] = tuple()
    config: Dict[str, Any] = field(init=False, default_factory=dict, repr=False)
    _groups: Map[str, Group] = field(init=False, repr=False)

    def __post_init__(self, init_groups: Sequence[Group]) -> None:
        object.__setattr__(self, "_groups", Map({group.name: group for group in init_groups}))

    @staticmethod
    def _get_config_file(project: str, env: Dict[str, str]) -> Tuple[str, str]:
        config_dir = env.get("OS_CONFIG_DIR", PurePath("/etc", project).as_posix()).strip()

        config_file = env.get(
            "OS_CONFIG_FILE",
            os.path.join(config_dir, f"{project}.yaml"),
        ).strip()

        return (config_dir, config_file)

    def setup(self, project: str, env: Dict[str, str]) -> None:
        config_dir, config_file = self._get_config_file(project, env)
        if not Path(config_file).exists():
            raise ValueError("Not found config file: %s" % config_file)

        with open(config_file) as f:
            try:
                object.__setattr__(self, "config", yaml.safe_load(f))
            except Exception:
                raise ValueError("Load config file error")

        for group in self._groups.values():
            for opt in group._opts.values():
                value = self.config.get(group.name, {}).get(opt.name)
                opt.load(value)

    def cleanup(self) -> None:
        for group in self._groups.values():
            for opt in group._opts.values():
                object.__setattr__(opt, "value", None)
        object.__setattr__(self, "_groups", Map())
        object.__setattr__(self, "config", {})

    def __getattr__(self, name: str) -> Group:
        if name in self._groups:
            return self._groups[name]
        raise AttributeError(name)

    def __call__(self, init_groups: Sequence[Group]) -> Any:
        object.__setattr__(self, "_groups", Map({group.name: group for group in init_groups}))

    def __contains__(self, key: Any) -> bool:
        return self._groups.__contains__(key)

    def __iter__(self) -> Iterator[Any]:
        return self._groups.__iter__()

    def __len__(self) -> int:
        return self._groups.__len__()

    def __repr__(self) -> str:
        items = ", ".join((f"{group}=Group(name='{group}')" for group in self._groups))
        return f"Configuration({items})"


__all__ = ("Opt", "Group", "Configuration")
