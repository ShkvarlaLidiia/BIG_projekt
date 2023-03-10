import { isArray } from "../utils/isArray";

export function render(parentNode, component) {
    if (isArray(component)) {
        return document.querySelector(parentNode).append(...component);
    }

    document.querySelector(parentNode).append(component);
}
