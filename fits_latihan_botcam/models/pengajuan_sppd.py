from odoo import models, fields, api

class PengajuanSppd(models.Model):
	_name = 'report.pengajuan.sppd'
	_description = 'Pengajuan SPPD'
	
	name 			= fields.Char(string="No SPPD")
	wilayah 		= fields.Char(string="Wilayah")
	note			= fields.Text("Maksud Utama")
	user_id 		= fields.Many2one("res.users", string="User")
	date			= fields.Date(string="Tanggal Pengajuan")
	date_from		= fields.Date(string="Date From")
	date_to			= fields.Date(string="Date To")
	employee_id		= fields.Many2one("hr.employee", string="Employee")
	manager_id		= fields.Many2one(string="Manager", related="employee_id.parent_id", store=True)
	sppd_line_ids	= fields.One2many("pengajuan.sppd.line","sppd_id", string="Line Sppd")
	
	
class SppdLine(models.Model):
	_name = 'pengajuan.sppd.line'
	_description = 'Pengajuan SPPD Line'
	
	product_id	= fields.Many2one("product.product", string="Product")
	qty			= fields.Float(string="Quantity")
	amount		= fields.Float(string="Amount")
	sub_total	= fields.Float(string="Subtotal")
	note		= fields.Char(string="Keterangan")
	sppd_id		= fields.Many2one("report.pengajuan.sppd", string="SPPD")
	
	
