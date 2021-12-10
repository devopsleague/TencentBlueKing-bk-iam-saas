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
from django.urls import path

from . import views

urlpatterns = [
    path("", views.HandoverViewSet.as_view({"post": "create"}), name="handover.handover"),
    path("records/", views.HandoverRecordsViewSet.as_view({"get": "list"}), name="handover.handover_records"),
    path(
        "records/<int:handover_record_id>/tasks/",
        views.HandoverTasksViewSet.as_view({"get": "list"}),
        name="handover.handover_task",
    ),
]
