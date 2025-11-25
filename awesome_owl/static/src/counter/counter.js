import { Component, useState } from "@odoo/owl";


export class Counter extends Component {
    static template = "awesome_owl.counter";

    setup() {
        this.state = useState({ counter: 0 });
    }

    incrementCounter() {
        this.state.counter++;
    }
}
