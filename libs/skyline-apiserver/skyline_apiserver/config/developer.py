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

from pydantic import StrictBool
from skyline_apiserver.config.base import Opt

show_raw_sql = Opt(
    name="show_raw_sql",
    description="Show raw sql",
    schema=StrictBool,
    default=False,
)

GROUP_NAME = __name__.split(".")[-1]
ALL_OPTS = (show_raw_sql,)

__all__ = ("GROUP_NAME", "ALL_OPTS")
