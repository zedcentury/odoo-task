/** @odoo-module */

import {loadJS} from "@web/core/assets";
import {getColor} from "@web/core/colors/colors";
import {Component, onWillStart, useRef, onMounted, onWillUnmount} from "@odoo/owl";

export class BarChart extends Component {
    static template = "my_dashboard.BarChart";
    static props = {
        kirim: Object,
        chiqim: Object,
    };

    setup() {
        this.canvasRef = useRef("canvas");
        onWillStart(() => loadJS(["/web/static/lib/Chart/Chart.js"]));
        onMounted(() => {
            this.renderChart();
        });
        onWillUnmount(() => {
            this.chart.destroy();
        });
    }

    renderChart() {
        // let kirim_data = {
        //     'March': 12500,
        //     'April': 32400,
        //     'May': 19000,
        //     'June': 12000,
        //     'July': 21000,
        // }
        // let chiqim_data = {
        //     'March': 11500,
        //     'April': 22400,
        //     'May': 20200,
        //     'June': 11000,
        //     'July': 40000,
        // }
        // let kirim_labels = Object.keys(kirim_data);
        // let kirim = Object.values(kirim_data);
        // let chiqim_labels = Object.keys(chiqim_data);
        // let chiqim = Object.values(chiqim_labels);
        // const labels = ['March', 'April', 'May', 'June', 'July'];
        // const kirim_data = [12500, 32400, 19000, 12000, 21000];
        // const chiqim_data = [11500, 22400, 20200, 11000, 40000];

        const kirim_labels = Object.keys(this.props.kirim);
        const kirim_data = Object.values(this.props.kirim);
        const chiqim_labels = Object.keys(this.props.chiqim);
        const chiqim_data = Object.values(this.props.chiqim);
        const color1 = getColor(2);
        const color2 = getColor(7);
        this.chart = new Chart(this.canvasRef.el, {
            type: "bar",
            data: {
                labels: kirim_labels.length > chiqim_labels.length ? kirim_labels : chiqim_labels,
                datasets: [
                    {
                        label: 'Kirim',
                        data: kirim_data,
                        backgroundColor: color1,
                    },
                    {
                        label: 'Chiqim',
                        data: chiqim_data,
                        backgroundColor: color2,
                    },
                ],
            },
        });
    }
}