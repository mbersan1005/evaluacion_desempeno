from odoo import models, fields, api

class EvaluacionDesempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _description = 'Desempeño del Empleado'

    name = fields.Char(string='Evaluación', required=True)
    employee_id = fields.Many2one('hr.employee', string="Empleado", required=True)
    fecha_evaluacion = fields.Date(string='Fecha de Evaluación', required=True)
    comentarios = fields.Text(string='Comentarios Evaluador')
    puntuacion = fields.Integer(string='Puntuación', required=True, default=1)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string="Estado", default='pendiente')

    @api.constrains('puntuacion') 
    def _check_puntuacion(self):
        for record in self:
            if record.puntuacion < 1 or record.puntuacion > 10:
                raise ValueError("La puntuación debe estar entre 1 y 10.")
