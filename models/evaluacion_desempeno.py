from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Desempeño del Empleado'

    name = fields.Char(string='Título Evaluación', required=True)
    employee_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    fecha_evaluacion = fields.Date(string='Fecha de Evaluación', required=True)
    comentarios = fields.Text(string='Comentarios Evaluador')
    puntuacion = fields.Integer(string='Puntuación', required=True, default=1)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string="Estado", default='pendiente')

    @api.onchange('puntuacion')
    def _onchange_puntuacion(self):
        for record in self:
            if record.puntuacion < 1:
                record.puntuacion = 1
            elif record.puntuacion > 10:
                record.puntuacion = 10
