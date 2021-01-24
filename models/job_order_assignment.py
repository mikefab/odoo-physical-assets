# -*- coding: utf-8 -*-

class MaintenanceJobOrderAssignment(models.Model):
    _name='maintenance.job.order.assignment'
    _description='Job Order / Assignment'

    x_active = fields.Boolean('Active', store=True, copy=True)
    x_name = fields.Char('Department/Ward/Area', store=True, copy=True)
    x_studio_stage_id = fields.Many2one('maintenance.job.order.assignment.stage', string='Stage', store=True, copy=True, required=True, ondelete='restrict')
    #x_studio_kanban_state = fields.Selection('Kanban State', "[('normal', 'In progress'), ('done', 'Ready'), ('blocked', 'Blocked')]")
    x_studio_company_id = fields.Many2one('res.company', string="Company", store=True, copy=True, ondelete='Set NULL')
    x_studio_currency_id = fields.Many2one('res.currency', store=True, copy=True, ondelete='Set NULL')
    x_studio_date = fields.Date('Date', store=True, copy=True)
    x_studio_date_start = fields.Datetime('Start Date', store=True, copy=True)
    x_studio_date_stop = fields.Datetime('Stop Date', store=True, copy=True)
    x_studio_image = fields.Binary(store=True, copy=True)

    x_studio_partner_id  = fields.Many2one('res.partner', string='Equipment', store=True, readonly=True, ondelete='Set NULL')
    x_studio_partner_phone = fields.Char('Category', store=True, tracking=True)
    x_studio_value = fields.Float('Value', store=True, copy=True)
    x_studio_notes = fields.Text('Notes', store=True, copy=True)
    x_studio_partner_email = fields.Char('Email', store=True, copy=True)

    x_studio_1 = fields.Char('Work 1', store=True, copy=True)
    x_studio_1_1 = fields.Char('Tool 1', store=True, copy=True)
    x_studio_1_2 = fields.Char('Supp 1', store=True, copy=True)
    x_studio_1_3 = fields.Char('Part 1', store=True, copy=True)


    x_studio_2 = fields.Char('Work 2', store=True, copy=True)
    x_studio_2_1 = fields.Char('Tool 2', store=True, copy=True)
    x_studio_2_2 = fields.Char('Supp 2', store=True, copy=True)
    x_studio_2_3 = fields.Char('Part 2', store=True, copy=True)
    #
    x_studio_3 = fields.Char('Work 4', store=True, copy=True) # S'up?
    x_studio_3_1 = fields.Char('Work 3', store=True, copy=True)
    x_studio_3_2 = fields.Char('Tool 3', store=True, copy=True)
    x_studio_3_3 = fields.Char('Supp 3', store=True, copy=True)
    x_studio_3_4 = fields.Char('Part 3', store=True, copy=True)
    #
    x_studio_4 = fields.Char('Work 5', store=True, copy=True) # S'up?
    x_studio_4_1 = fields.Char('Tool 4', store=True, copy=True)
    x_studio_4_2 = fields.Text('Supp 4', store=True, copy=True)
    x_studio_4_3 = fields.Text('Part 4', store=True, copy=True)
    #
    x_studio_5 = fields.Char('Tool 5', store=True, copy=True)
    x_studio_5_1 = fields.Text('Supp 5', store=True, copy=True)
    #
    x_studio_6 = fields.Char('Work 6', store=True, copy=True)
    x_studio_6_1 = fields.Char('Tool 6', store=True, copy=True)
    x_studio_6_2 = fields.Text('Supp 6', store=True, copy=True)
    #
    # x_studio_char_field_8cSIH = fields.Char('6.', store=True, copy=True)
    # x_studio_char_field_pDvag = fields.Char('New Text', store=True, copy=True)
    #

    # x_studio_description = fields.Char('Description', store=True, copy=True)
    # x_studio_equipment = fields.Char('Equipment', store=True, copy=True)

    # x_studio_equipment = fields.Many2one('maintenance.request', string='Description', store=True, copy=True, ondelete='Set NULL')
    # x_studio_equipment_1 = fields.Many2one('res.partner', store=True, readonly=True, ondelete='Set NULL')
    # x_studio_partner_email = fields.Char('Email', store=True)

    # x_studio_sequence = fields.Integer('Sequence', store=True, copy=True)
    # x_studio_user_id = fields.Many2one('res.users', string='Responsible', store=True, copy=True, ondelete='Set NULL', domain="[('share', '=', False)]")

    x_studio_many2one_field_BZWhr = fields.Many2one('maintenance.equipment', string='Equipment', store=True, readonly=True, ondelete='Set NULL')
    x_studio_many2one_field_GSELf = fields.Many2one('maintenance.request', string='Description of fault', store=True, readonly=True, ondelete='Set NULL')

    x_studio_part_5 = fields.Char('Part 5.', store=True, copy=True)
    x_studio_part_6 = fields.Char('Part 6.', store=True)
    # x_studio_partner_id = fields.Many2one('res.partner', string='Contact', store=True, readonly=True, ondelete='Set NULL')
    # x_studio_priority = fields.Boolean('High Priority')
    # x_studio_related_field_gRR5c= fields.Char('New Related Field', readonly=True)
    # x_studio_sequence = fields.Integer('Sequence', store=True, copy=True)

    x_studio_tag_ids = fields.Many2many('x_job_order_assignment_tag, x_job_order_assignment_tag_rel, x_job_order_assignment_id, x_tag_id', string='Tags', store=True, copy=True)
    # x_studio_text_field_0rnjU = fields.Text('New Multiline Text', store=True, copy=True)
    # x_studio_text_field_4Fb3H = fields.Text('New Multiline Text', store=True, copy=True)
    activity_user_id = fields.Many2one('res.users', string="Responsible Staff")

class MaintenanceStage(models.Model):
    """ Model for case stages. This models the main stages of a Maintenance Request management flow. """

    _name = 'maintenance.stage'
    _description = 'Maintenance Stage'
    _order = 'sequence, id'

    name = fields.Char('Name', required=True, translate=True)
    sequence = fields.Integer('Sequence', default=20)
    fold = fields.Boolean('Folded in Maintenance Pipe')
    done = fields.Boolean('Request Done')
