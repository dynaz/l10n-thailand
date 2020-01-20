# Copyright 2019 Ecosoft Co., Ltd (https://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

{
    "name": "Thailand Localization - Withholding Tax Report",
    "version": "12.0.1.0.1",
    "author": "Ecosoft, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/l10n-thailand",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": [
        "account",
        "excel_import_export",
        "report_xlsx",
        "report_xlsx_helper",
        "date_range",
        "l10n_th_partner",
        "l10n_th_vendor_tax_invoice",
        "l10n_th_withholding_tax_cert",
    ],
    "data": [
        "data/paper_format.xml",
        "data/report_data.xml",
        "report_txt/templates.xml",
        "report_txt/report.xml",
        "wizard/withholding_tax_report_wizard_view.xml",
        "report/templates/layouts.xml",
        "report/templates/report_template.xml",
        "report/templates/report_withholding_tax_pdf.xml",
    ],
    "installable": True,
}
