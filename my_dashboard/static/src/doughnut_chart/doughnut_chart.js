/** @odoo-module */

import {loadJS} from "@web/core/assets";
import {getColor} from "@web/core/colors/colors";
import {Component, onWillStart, useRef, onMounted, onWillUnmount} from "@odoo/owl";

export class DoughnutChart extends Component {
    static template = "my_dashboard.DoughnutChart";
    static props = {
        data: Object,
        color_indexes: {
            type: Array,
            optional: true
        }
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
        const labels = Object.keys(this.props.data);
        const data = Object.values(this.props.data);
        const color = !this.props.color_indexes ?
            labels.map((_, index) => getColor(index)) :
            this.props.color_indexes.map((value, index) => getColor(value));
        this.chart = new Chart(this.canvasRef.el, {
            type: "doughnut",
            data: {
                labels: labels,
                datasets: [
                    {
                        data: data,
                        backgroundColor: color,
                    },
                ],
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'bottom',
                    },
                }
            },
        });
    }
}