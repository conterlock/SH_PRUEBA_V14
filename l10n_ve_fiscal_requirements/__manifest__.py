# -*- coding: utf-8 -*-
{
    "name": "Requerimientos Fiscales Venezolanos",
    "version": "1.0",
    "author": "Soluciones SoftHard",
    "license": "AGPL-3",
    "category": 'Localization',

    "depends": [
        "base",
        "account",
        'l10n_ve_dpt',
        'sale'
    ],
    'data': [
        'views/partner_view.xml',
        'views/company_view.xml',
        'views/account_invoice_view.xml',
        'views/account_tax_view.xml',
        'reports/invoice_change.xml'
    ],
    'installable': True,
}
