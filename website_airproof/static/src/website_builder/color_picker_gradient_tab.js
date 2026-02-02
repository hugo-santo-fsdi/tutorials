import {ColorPickerGradientTab} from "@html_editor/main/font/color_picker_gradient_tab";
import {_t} from "@web/core/l10n/translation";
import {registry} from "@web/core/registry";

// Add your gradient to the default list
export class AirproofColorPickerGradientTab extends ColorPickerGradientTab {
    setup() {
        super.setup();
        this.DEFAULT_GRADIENT_COLORS = [
            ...this.DEFAULT_GRADIENT_COLORS,
            "linear-gradient(0deg, rgb(41, 128, 187) 0%, rgb(11, 142, 230) 100%)",
        ];
    }
}

// Get the gradient lists and add the extended class to it.
const colorPickerTabs = registry.category("color_picker_tabs");

colorPickerTabs.remove("html_editor.gradient");
colorPickerTabs.add(
    "html_editor.gradient",
    {
        id: "gradient",
        name: _t("Gradient"),
        component: AirproofColorPickerGradientTab,
    },
    {sequence: 60}
);
