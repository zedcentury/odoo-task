/** @odoo-module **/
import {Component} from "@odoo/owl";
import {registry} from "@web/core/registry";

export class Dashboard extends Component {
    static template = "my_dashboard.dashboard";
}

registry.category("actions").add("my_dashboard.dashboard", Dashboard);
