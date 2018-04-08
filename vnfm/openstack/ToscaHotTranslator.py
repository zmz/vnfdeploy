# -*- coding: utf-8 -*-
import logging

LOG = logging.getLogger(__name__)

class TOSCAToHOT(object):
    """Convert TOSCA template to HOT template."""
    def __init__(self,vnfd_yaml,heatclient):
        self.vnfd_yaml=vnfd_yaml
        self.heatclient=heatclient
