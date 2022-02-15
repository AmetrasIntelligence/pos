# Copyright (C) 2017 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'Point Of Sale - Picking Load',
    'summary': "Load and confirm stock pickings via Point Of Sale",
    'version': '13.0.0.0.1',
    'category': 'Point Of Sale',
    'author': 'GRAP,Odoo Community Association (OCA)',
    'website': 'https://www.github.com/OCA/pos',
    'license': 'AGPL-3',
    'maintainers': ['legalsylvain'],
    'development_status': 'Beta',
    'depends': [
        'sale_stock',
        'point_of_sale',
    ],
    'data': [
        'views/view_pos_config.xml',
        'views/view_sale_order.xml',
        'views/view_stock_picking.xml',
        'views/view_stock_picking_type.xml',
        'views/pos_picking_load.xml',
    ],
    'qweb': [
        'static/src/xml/pos_picking_load.xml',
    ],
    'installable': True,
}
