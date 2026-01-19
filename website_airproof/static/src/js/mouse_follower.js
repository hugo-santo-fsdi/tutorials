import {Interaction} from "@web/public/interaction";
import {registry} from "@web/core/registry";

export class MouseFollower extends Interaction {
    static selector = "#wrapwrap";

    setup() {
        this.mouseX = 0;
        this.mouseY = 0;
        this.xp = 0;
        this.yp = 0;
        this.follower = null;
        this._animationId = null;
    }

    start() {
        this.follower = document.createElement("div");
        this.follower.className =
            "x_mouse_follower o_not_editable position-fixed rounded-circle bg-o-color-1 opacity-50 translate-middle pe-none";
        this.el.append(this.follower);
    }

    onMouseMove(ev) {
        this.mouseX = ev.clientX;
        this.mouseY = ev.clientY;
        this.xp += (this.mouseX - this.xp) * 0.4;
        this.yp += (this.mouseY - this.yp) * 0.4;

        this.follower.setAttribute("style", `top: ${this.yp}px; left: ${this.xp}px;`);
    }

    destroy() {
        if (this.follower) {
            this.follower.remove();
        }

        super.destroy();
    }

    dynamicContent = {
        _document: {
            "t-on-mousemove": this.onMouseMove,
        },
    };
}

registry.category("public.interactions").add("website_airproof.MouseFollower", MouseFollower);
