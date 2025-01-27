from odoo import models, fields, api

class evaluacion_desempeno(models.Model):
    _name = 'evaluacion.desempeno'
    _descripcion = 'Desempeño del Empleado'

    name = fields.Char(string='Evaluación', required = True)
    fecha_evaluacion = fields.Date(string='Fecha de Evaluación', required=True)
    comentarios = fields.Text(string='Comentarios Evaluador')
    puntuacion = fields.Integer(string='Puntuación', required=True, default=1)
    estado = fields.Selection([
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizado', 'Finalizado')
    ], string="Estado", default='pendiente')

    @api.constrains('score')
    def _check_score(self):
        for record in self:
            if record.score < 1 or record.score > 10:
                raise ValueError("La Puntuación ha de ser entre 1 y 10.")