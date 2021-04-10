# -*- coding: utf-8 -*-
from odoo import http

# class FitsLatihanBotcam(http.Controller):
#     @http.route('/fits_latihan_botcam/fits_latihan_botcam/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fits_latihan_botcam/fits_latihan_botcam/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fits_latihan_botcam.listing', {
#             'root': '/fits_latihan_botcam/fits_latihan_botcam',
#             'objects': http.request.env['fits_latihan_botcam.fits_latihan_botcam'].search([]),
#         })

#     @http.route('/fits_latihan_botcam/fits_latihan_botcam/objects/<model("fits_latihan_botcam.fits_latihan_botcam"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fits_latihan_botcam.object', {
#             'object': obj
#         })