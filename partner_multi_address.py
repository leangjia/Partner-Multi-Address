#-*- coding:utf-8 -*-
from openerp.osv import fields,osv

class partner_multi_address(osv.osv):
    _name="res.partner"
    _inherit="res.partner"
    _description="add Partner Multi Address."
    _columns={
            "Address2":fields.text("Address2",size=128),
            }
partner_multi_address()