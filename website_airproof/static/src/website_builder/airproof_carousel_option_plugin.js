import {BaseOptionComponent} from "@html_builder/core/utils";
import {BuilderAction} from "@html_builder/core/builder_action";
import {Plugin} from "@html_editor/plugin";
import {registry} from "@web/core/registry";

export class CarouselBubbleOption extends BaseOptionComponent {
    // Declare the template and the selector
    static template = "website_airproof.CarouselBubbleOption";
    static selector = ".x_bubble_item";
}

// We do not need a custom method to handle the Bubble Shadow option
// because the builder uses a standard method to apply/remove the
// right classes (See attribute: classAction in your XML).

export class SetBubbleMarginAction extends BuilderAction {
    // This id is called in the XML
    static id = "setBubbleMargin";

    // Get the current value of the option
    getValue({editingElement}) {
        // Transform the classes list into a string to look after "mb-X" class.
        const match = [...editingElement.classList].join(" ").match(/mb-(\d+)/);

        // If there is a match, return the numeric value
        // mb-2 returns 2
        if (match) {
            return Number(match[1]);
        }

        // Return 0 by default if no match is found.
        return 0;
    }

    apply({editingElement, value}) {
        // Browse all editing elements looking for "mb-" class
        // Then remove the "mb-" class to avoid duplicated classes
        editingElement.classList.forEach((classSelector) => {
            if (classSelector.startsWith("mb-")) {
                editingElement.classList.remove(classSelector);
            }
        });

        // Add the right "mb-" class to the element.
        editingElement.classList.add(`mb-${value}`);
    }
}

class CarouselBubbleOptionPlugin extends Plugin {
    static id = "carouselBubbleOption";
    resources = {
        builder_options: [CarouselBubbleOption],
        // Declare your custom methods related to the options.
        builder_actions: {
            SetBubbleMarginAction,
        },
    };
}

registry.category("website-plugins").add(CarouselBubbleOptionPlugin.id, CarouselBubbleOptionPlugin);
