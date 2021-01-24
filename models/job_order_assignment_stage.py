class MaintenanceJobOrderAssignmentStage(models.Model):
    _name='maintenance.job.order.assignment.stage'
    _description='Job Order/Assignment Stages'
    x_name = fields.Char('Stage Name', store=True, copy=True, required=True)
    x_studio_sequence = fields.Integer('Sequence', store=True)
