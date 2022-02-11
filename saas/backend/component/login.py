"""
TencentBlueKing is pleased to support the open source community by making 蓝鲸智云-权限中心(BlueKing-IAM) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
from django.conf import settings

from backend.common.error_codes import error_codes
from backend.util.url import url_join

from .http import http_get, logger


def _call_login_api(http_func, url_path, data, timeout=30):
    url = url_join(settings.BK_PAAS_INNER_HOST, url_path)
    kwargs = {"url": url, "data": data, "timeout": timeout}

    ok, data = http_func(**kwargs)

    # process result
    if not ok:
        message = "login api failed, method: %s, info: %s" % (http_func.__name__, kwargs)
        logger.error(message)
        raise error_codes.REMOTE_REQUEST_ERROR.format(f'request login api error: {data["error"]}')

    return data


def verify_bk_token(bk_token: str):
    """验证bk_token"""
    url_path = "/login/accounts/is_login/"
    return _call_login_api(http_get, url_path=url_path, data={"bk_token": bk_token})
