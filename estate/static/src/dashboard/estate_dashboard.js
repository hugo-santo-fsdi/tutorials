/** @odoo-module **/

import { Component, onWillStart, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { session } from "@web/session";

class EstateDashboard extends Component {
    static template = "estate.EstateDashboard";

    setup() {
        this.action = useService("action");
        this.session = session;
        this.cards = [
            { title: "Properties", value: "24", detail: "Published and draft listings" },
            { title: "Visits", value: "18", detail: "Visits planned this week" },
            { title: "Offers", value: "07", detail: "Offers waiting for review" },
            { title: "Conversion", value: "82%", detail: "Lead to visit ratio" },
        ];
        this.panels = [
            { title: "Recent Activity", items: ["New property intake", "Offer follow-up", "Visit confirmation"] },
            { title: "Upcoming Tasks", items: ["Review contracts", "Prepare viewings", "Check client notes"] },
            { title: "Team Notes", items: ["Keep prices aligned", "Update sold listings", "Share feedback"] },
        ];
    }

    get userName() {
        return session.user_name || "Current User";
    }

    openProfile() {
        this.action.doAction("estate.action_estate_profile");
    }

    openProperties() {
        this.action.doAction("estate.action_estate_property");
    }
}

class EstateProfile extends Component {
    static template = "estate.EstateProfile";

    setup() {
        this.action = useService("action");
        this.orm = useService("orm");
        this.session = session;
        this.state = useState({
            loading: true,
            user: null,
        });

        onWillStart(async () => {
            const [user] = await this.orm.read("res.users", [session.uid], [
                "name",
                "login",
                "email",
                "phone",
                "mobile",
                "tz",
                "lang",
            ]);
            this.state.user = user;
            this.state.loading = false;
        });
    }

    get avatarUrl() {
        return `/web/image/res.users/${session.uid}/avatar_128`;
    }

    backToDashboard() {
        this.action.doAction("estate.action_estate_dashboard");
    }
}

registry.category("actions").add("estate.dashboard", EstateDashboard);
registry.category("actions").add("estate.profile", EstateProfile);
