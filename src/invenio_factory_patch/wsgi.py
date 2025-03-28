# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2017-2018 CERN.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
from .factory import create_app

application = create_app()
"""Combined UI + REST Flask application.

REST API is mounted under ``/api``.

Replaces :code:`invenio_app` factory function.
"""
