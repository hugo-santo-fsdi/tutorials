import { Component, useState, markup } from "@odoo/owl";
import { Counter } from "./counter/counter";
import { Card } from "./card/card";

export class Playground extends Component {
    static template = "awesome_owl.playground";
    static components = { Counter, Card };
    no_markup_value = "<div class='text-primary'>Testing no markup</div>";
    markup_value = markup("<div class='text-primary'>Testing markup</div>");
    setup(){
        this.state = useState({ sum: 2 });
        this.incrementSum = this.incrementSum.bind(this);
    }

    incrementSum(){
        this.state.sum += 1;
    }
}
