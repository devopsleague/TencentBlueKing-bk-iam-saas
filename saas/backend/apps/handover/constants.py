# -*- coding: utf-8 -*-
"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-权限中心(BlueKing-IAM) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from aenum import LowerStrEnum, auto, skip
from django.utils.translation import gettext as _

from backend.util.enum import ChoicesEnum


class HandoverStatus(ChoicesEnum, LowerStrEnum):
    """权限交接的执行状态"""

    RUNNING = auto()
    SUCCEED = auto()
    FAILED = auto()
    PARTIAL_FAILED = auto()

    _choices_labels = skip(
        (
            (RUNNING, _("正在交接")),
            (SUCCEED, _("交接成功")),
            (FAILED, _("交接失败")),
            (PARTIAL_FAILED, _("部分失败")),
        )
    )


class HandoverTaskStatus(ChoicesEnum, LowerStrEnum):
    """权限交接具体任务的执行状态"""

    RUNNING = auto()
    SUCCEED = auto()
    FAILED = auto()

    _choices_labels = skip(
        (
            (RUNNING, _("正在交接")),
            (SUCCEED, _("交接成功")),
            (FAILED, _("交接失败"),),
        )
    )


class HandoverObjectType(ChoicesEnum, LowerStrEnum):
    """交接的权限类型"""

    GROUP = auto()
    CUSTOM = auto()
    SUPER_MANAGER = auto()
    SYSTEM_MANAGER = auto()
    GRADE_MANAGER = auto()

    _choices_labels = skip(
        (
            (GROUP, _("用户组权限")),
            (CUSTOM, _("自定义权限")),
            (SUPER_MANAGER, _("超级管理员权限")),
            (SYSTEM_MANAGER, _("系统管理员权限")),
            (GRADE_MANAGER, _("分级管理员权限")),
        )
    )
