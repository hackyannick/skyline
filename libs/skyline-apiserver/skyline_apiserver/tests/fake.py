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

from dataclasses import dataclass, field
from typing import Any, Dict, List

from mimesis import Generic
from pydantic import StrictBool, StrictInt, StrictStr

FAKER = Generic()


@dataclass
class FakeOptData:
    name: str = field(default_factory=lambda: "_".join(FAKER.text.words()))
    description: str = field(default_factory=lambda: str(FAKER.text.text()))
    schema: Any = field(
        default_factory=lambda: FAKER.random.choice(
            [StrictBool, StrictInt, StrictStr, List, Dict],
        ),
    )
    default: Any = None
    deprecated: bool = False
