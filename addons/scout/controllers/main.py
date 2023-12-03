# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import http, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.http import request
from werkzeug.exceptions import NotFound


class WebsiteHrRecruitment(http.Controller):
    def sitemap_jobs(env, rule, qs):
        if not qs or qs.lower() in '/jobs':
            yield {'loc': '/jobs'}

    @http.route([
        '/scouts',
    ], type='http', auth="public", website=True)
    def scouts_sections(self, **kwargs):
        env = request.env()

        Section = env['scout.section']

        sections = Section.search([])

        # Render page
        return request.render("scout.index", {
            'sections': sections,
        })
