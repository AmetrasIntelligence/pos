
[![Runboat](https://img.shields.io/badge/runboat-Try%20me-875A7B.png)](https://runboat.odoo-community.org/builds?repo=OCA/pos&target_branch=16.0)
[![Pre-commit Status](https://github.com/OCA/pos/actions/workflows/pre-commit.yml/badge.svg?branch=16.0)](https://github.com/OCA/pos/actions/workflows/pre-commit.yml?query=branch%3A16.0)
[![Build Status](https://github.com/OCA/pos/actions/workflows/test.yml/badge.svg?branch=16.0)](https://github.com/OCA/pos/actions/workflows/test.yml?query=branch%3A16.0)
[![codecov](https://codecov.io/gh/OCA/pos/branch/16.0/graph/badge.svg)](https://codecov.io/gh/OCA/pos)
[![Translation Status](https://translation.odoo-community.org/widgets/pos-16-0/-/svg-badge.svg)](https://translation.odoo-community.org/engage/pos-16-0/?utm_source=widget)

<!-- /!\ do not modify above this line -->

# Point of Sale

Odoo modules for Point of Sale.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[pos_access_right](pos_access_right/) | 16.0.1.0.1 |  | Point of Sale - Extra Access Right for certain actions
[pos_bypass_global_discount](pos_bypass_global_discount/) | 16.0.1.0.1 |  | POS Bypass Global Discount
[pos_cash_control_override](pos_cash_control_override/) | 16.0.1.0.0 |  | Override bare PoS user cash control restrictions
[pos_config_logo](pos_config_logo/) | 16.0.1.0.0 |  | Set logotypes different from the company's one
[pos_container_deposit](pos_container_deposit/) | 16.0.1.0.0 |  | This module is used to manage container deposits for products in Point of Sale.
[pos_customer_comment](pos_customer_comment/) | 16.0.1.0.3 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Display Customer comment in the PoS front office and allow to edit and save it by the cashier
[pos_customer_tree_view_vat](pos_customer_tree_view_vat/) | 16.0.1.0.1 | [![mileo](https://github.com/mileo.png?size=30px)](https://github.com/mileo) | Point of Sale: Show VAT number at Customer Tree View
[pos_daily_sales_reports_category_only](pos_daily_sales_reports_category_only/) | 16.0.1.0.1 |  | Show Sales Reports by Category
[pos_default_partner](pos_default_partner/) | 16.0.1.0.1 |  | Add a default customer in pos order
[pos_discount_all](pos_discount_all/) | 16.0.1.0.1 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Display discount amount on PoS cashier screen and print it on ticketcalculated from the difference between a sale with default pricelist
[pos_edit_order_line](pos_edit_order_line/) | 16.0.1.0.1 |  | POS Edit Order Line
[pos_escpos_status](pos_escpos_status/) | 16.0.1.0.1 |  | Point of sale: fetch status for 'escpos' driver
[pos_financial_risk](pos_financial_risk/) | 16.0.1.0.1 | [![geomer198](https://github.com/geomer198.png?size=30px)](https://github.com/geomer198) [![CetmixGitDrone](https://github.com/CetmixGitDrone.png?size=30px)](https://github.com/CetmixGitDrone) | Point of Sale Fonancial Risk
[pos_global_discount_in_line](pos_global_discount_in_line/) | 16.0.1.0.1 |  | Order discount in line instead of discount product
[pos_hide_banknote_button](pos_hide_banknote_button/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Hide useless Banknote buttons in the PoS (+10, +20, +50)
[pos_lot_barcode](pos_lot_barcode/) | 16.0.1.0.1 |  | Scan barcode to enter lot/serial numbers
[pos_lot_selection](pos_lot_selection/) | 16.0.1.0.1 |  | POS Lot Selection
[pos_loyalty_exclude](pos_loyalty_exclude/) | 16.0.1.0.1 |  | Exclude products from sale loyalty program in POS
[pos_loyalty_redeem_payment](pos_loyalty_redeem_payment/) | 16.0.1.0.2 |  | Use vouchers as payment method in pos orders
[pos_margin](pos_margin/) | 16.0.1.0.2 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Margin on PoS Order
[pos_membership](pos_membership/) | 16.0.1.0.1 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Implement features of membership module in the Point of sale UI.
[pos_membership_extension](pos_membership_extension/) | 16.0.1.0.1 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Prevent to sale product in the point of sale to customer that don't belong to membership categories
[pos_minimize_menu](pos_minimize_menu/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Reduce size of the main menu of the point of sale.
[pos_order_new_line](pos_order_new_line/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Allow cashier to create a new order line, instead of merging the quantity with a previous line
[pos_order_remove_line](pos_order_remove_line/) | 16.0.1.2.1 | [![robyf70](https://github.com/robyf70.png?size=30px)](https://github.com/robyf70) | Add button to remove POS order line.
[pos_order_reorder](pos_order_reorder/) | 16.0.0.1.2 |  | Simple Re-order in the Point of Sale
[pos_order_to_sale_order](pos_order_to_sale_order/) | 16.0.1.0.11 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | PoS Order To Sale Order
[pos_order_to_sale_order_delivery](pos_order_to_sale_order_delivery/) | 16.0.1.0.1 | [![GabbasovDinar](https://github.com/GabbasovDinar.png?size=30px)](https://github.com/GabbasovDinar) [![CetmixGitDrone](https://github.com/CetmixGitDrone.png?size=30px)](https://github.com/CetmixGitDrone) | Compatibility of pos_order_to_sale_order and delivery modules
[pos_order_to_sale_order_report](pos_order_to_sale_order_report/) | 16.0.1.0.2 |  | Report will be downloaded after the sales order is created.
[pos_order_to_sale_order_sale_financial_risk](pos_order_to_sale_order_sale_financial_risk/) | 16.0.1.0.1 | [![geomer198](https://github.com/geomer198.png?size=30px)](https://github.com/geomer198) [![CetmixGitDrone](https://github.com/CetmixGitDrone.png?size=30px)](https://github.com/CetmixGitDrone) | Sale Financial Risk control for Sales Orders created from POS
[pos_partner_birthdate](pos_partner_birthdate/) | 16.0.1.0.4 | [![ecino](https://github.com/ecino.png?size=30px)](https://github.com/ecino) | Adds the birthdate in the customer screen of POS
[pos_partner_firstname](pos_partner_firstname/) | 16.0.1.0.4 | [![robyf70](https://github.com/robyf70.png?size=30px)](https://github.com/robyf70) | POS Support of partner firstname
[pos_partner_location_abstract](pos_partner_location_abstract/) | 16.0.1.0.1 |  | POS Partner Location Abstract
[pos_partner_location_google_map](pos_partner_location_google_map/) | 16.0.1.0.1 |  | POS Partner Location Google Map
[pos_partner_sale_warning](pos_partner_sale_warning/) | 16.0.1.0.0 |  | Show partner sales warning in POS
[pos_payment_change](pos_payment_change/) | 16.0.1.0.4 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Allow cashier to change order payments, as long as the session is not closed.
[pos_payment_description](pos_payment_description/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Payment description on order tree view
[pos_payment_method_cashdro](pos_payment_method_cashdro/) | 16.0.1.0.0 |  | Allows to pay with CashDro Terminals on the Point of Sale
[pos_payment_method_change_policy](pos_payment_method_change_policy/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Adds alternative way to handle Change in Point of Sale.
[pos_payment_method_image](pos_payment_method_image/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Add images on Payment Methods available in the PoS
[pos_payment_restriction](pos_payment_restriction/) | 16.0.1.0.0 | [![rousseldenis](https://github.com/rousseldenis.png?size=30px)](https://github.com/rousseldenis) | Adds restrictions options on POS payment level
[pos_payment_terminal](pos_payment_terminal/) | 16.0.1.0.3 |  | Point of sale: support generic payment terminal
[pos_payment_usability](pos_payment_usability/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Improve payment screen in the PoS front office
[pos_picking_delayed](pos_picking_delayed/) | 16.0.1.0.1 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Delay the creation of the picking when PoS order is created
[pos_price_to_weight](pos_price_to_weight/) | 16.0.1.0.0 |  | Compute weight based on barcodes with prices
[pos_pricelist_technical](pos_pricelist_technical/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Prevent technical pricelists from being displayed in the Point of Sale front-end UI
[pos_product_display_default_code](pos_product_display_default_code/) | 16.0.1.0.1 |  | pos: display product default code before product name
[pos_product_label](pos_product_label/) | 16.0.1.0.2 | [![ivantodorovich](https://github.com/ivantodorovich.png?size=30px)](https://github.com/ivantodorovich) | Print product labels from the POS
[pos_product_mergeable_line](pos_product_mergeable_line/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Allows to configure at the product level, if an order line can be merged or not.
[pos_product_multi_barcode](pos_product_multi_barcode/) | 16.0.1.0.2 |  | Make product multi barcodes usable in the point of sale
[pos_product_packaging_container_deposit](pos_product_packaging_container_deposit/) | 16.0.1.0.1 |  | Add the container deposit fees in a POS order
[pos_product_packaging_multi_barcode](pos_product_packaging_multi_barcode/) | 16.0.1.0.0 |  | Make product packaging multi barcodes usable in the point of sale
[pos_product_pricelist_alternative](pos_product_pricelist_alternative/) | 16.0.1.0.0 |  | Calculate POS product price based on alternative pricelists
[pos_product_quick_info](pos_product_quick_info/) | 16.0.1.0.2 |  | Display product info by one click in Point of Sale
[pos_receipt_hide_info](pos_receipt_hide_info/) | 16.0.1.0.0 |  | Removes Information from POS receipt.
[pos_receipt_hide_price](pos_receipt_hide_price/) | 16.0.1.0.0 |  | Add button to remove price from receipt.
[pos_receipt_replace_user_by_trigram](pos_receipt_replace_user_by_trigram/) | 16.0.1.0.0 |  | Replace User by Trigram in POS receipt.
[pos_receipt_replace_user_by_trigram_hr](pos_receipt_replace_user_by_trigram_hr/) | 16.0.1.0.1 |  | Link module between pos_receipt_replace_user_by_trigram and pos_hr
[pos_receipt_usability](pos_receipt_usability/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Improve receipt screen in the PoS front office
[pos_receipt_vat_detail](pos_receipt_vat_detail/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Add Vat Details on Receipt (base and vat amounts).
[pos_report_session_summary](pos_report_session_summary/) | 16.0.1.0.0 |  | Adds a Session Summary PDF report on the POS session
[pos_reset_search](pos_reset_search/) | 16.0.1.0.0 | [![fkawala](https://github.com/fkawala.png?size=30px)](https://github.com/fkawala) | Point of Sale - Clear product search when user clicks on a product.
[pos_sale_order_print](pos_sale_order_print/) | 16.0.1.0.2 |  | Print multiple sale orders in POS
[pos_sale_product_config_no_variant](pos_sale_product_config_no_variant/) | 16.0.1.0.1 | [![ursais](https://github.com/ursais.png?size=30px)](https://github.com/ursais) | Manage Point Of Sale via Configurator of no variant
[pos_screen_element_custom_size](pos_screen_element_custom_size/) | 16.0.1.0.0 |  | Set custom size for POS screen elements
[pos_session_pay_invoice](pos_session_pay_invoice/) | 16.0.1.0.0 |  | Pay and receive invoices from PoS Session
[pos_stock_available_online](pos_stock_available_online/) | 16.0.2.0.3 |  | Show the available quantity of products in the Point of Sale
[pos_supplierinfo_search](pos_supplierinfo_search/) | 16.0.1.0.0 | [![eLBati](https://github.com/eLBati.png?size=30px)](https://github.com/eLBati) | Search products by supplier data
[pos_ticket_extra_company_info_l10n_fr](pos_ticket_extra_company_info_l10n_fr/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Add siret company infos on the ticket
[pos_timeout](pos_timeout/) | 16.0.1.0.0 |  | Set the timeout of the point of sale
[pos_to_weight_by_product_uom](pos_to_weight_by_product_uom/) | 16.0.1.0.0 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) | Make 'To Weight' default value depending on product UoM settings

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to Odoo Community Association (OCA)
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----
OCA, or the [Odoo Community Association](http://odoo-community.org/), is a nonprofit
organization whose mission is to support the collaborative development of Odoo features
and promote its widespread use.
