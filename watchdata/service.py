# Copyright (c) 2013 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import time

from oslo_log import log as logging
from oslo_service import service

from watchdata.common import config

CONF = config.CONF

LOG = logging.getLogger(__name__)


class watchdata(service.Service):
    def __init__(self):
        super(watchdata, self).__init__()

    def start(self):
        self._load()
        while True:
            try:
                self._run()
            except Exception as ex:
                LOG.exception(ex)
                time.sleep(5)

    def _run(self):
        try:
            LOG.info("Runing!")
        except Exception as ex:
            LOG.exception('Error running execution plan')
