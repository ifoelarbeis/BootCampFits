# -*- coding: utf-8 -*-

from odoo import models, fields, api

class HrDivisi(models.Model):
	_name = 'hr.divisi'
	_description = 'Divisi'
	

	name = fields.Char(string="Nama Divisi")
	desc = fields.Char(string="Keterangan")

class HrEmployee(models.Model):
	_inherit = 'hr.employee'
	
	devisi_id = fields.Many2one('hr.divisi', string="Divisi")
	
