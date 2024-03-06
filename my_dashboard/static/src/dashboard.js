/** @odoo-module */

import {Component, useState, onWillStart} from "@odoo/owl";
import {registry} from "@web/core/registry";
import {useService} from "@web/core/utils/hooks";
import {PieChart} from "./pie_chart/pie_chart";
import {LineChart} from "./line_chart/line_chart";
import {BarChart} from "./bar_chart/bar_chart";
import {DoughnutChart} from "./doughnut_chart/doughnut_chart";

export class Dashboard extends Component {
    static template = "my_dashboard.dashboard";
    static components = {PieChart, LineChart, BarChart, DoughnutChart};

    setup() {
        this.kirim_chiqim = useState({});
        this.period = useState({value: null});
        this.color_indexes = [2, 7];
        this.rpc = useService("rpc");
        onWillStart(async () => {
            await this.getStats();
        });
    }

    async getStats() {
        this.kirim_chiqim = await this.rpc('/statistics', {
            params: {
                period: this.period.value
            }
        });
    }
}

registry.category("actions").add("my_dashboard.dashboard", Dashboard);