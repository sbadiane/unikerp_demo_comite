# -*- encoding: utf-8 -*-
from odoo import models ,api ,fields,_
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

class offre(models.Model):
    _name = "unikerp_offre"

    name = fields.Char(string="nom")

