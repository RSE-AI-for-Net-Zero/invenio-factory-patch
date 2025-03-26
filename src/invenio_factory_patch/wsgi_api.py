# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
from .factory import create_api

application = create_api()
"""
Combined API Flask application.

Replaces :code:`invenio_app` factory function.
"""

