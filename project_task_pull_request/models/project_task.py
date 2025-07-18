# Copyright 2017 Specialty Medical Drugstore
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, exceptions, fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    pr_uri = fields.Char(string="PR URI", tracking=True)

    pr_required_states = fields.Many2many(related="project_id.pr_required_states")

    @api.constrains("pr_uri", "stage_id", "project_id")
    def _check_pr_uri_required(self):
        for task in self:
            stages_pr_req = task.project_id.pr_required_states
            is_stage_pr_req = task.stage_id in stages_pr_req
            if not task.pr_uri and stages_pr_req and is_stage_pr_req:
                raise exceptions.ValidationError(
                    self.env._(
                        "Please add the URI for the pull request "
                        "before moving the task to this stage."
                    )
                )
