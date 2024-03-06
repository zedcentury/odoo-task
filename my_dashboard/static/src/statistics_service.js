/** @odoo-module */

import {registry} from "@web/core/registry";
import {reactive} from "@odoo/owl";

const statisticsService = {
    dependencies: ["rpc"],
    async start(env, {rpc}) {
        const statistics = reactive({isReady: false});

        const updates = await rpc("/statistics");
        Object.assign(statistics, updates, {isReady: true});

        return statistics;
    },
};

registry.category("services").add("my_dashboard.statistics", statisticsService);