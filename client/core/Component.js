export class Component {
    constructor(options) {
        const {tagName, className, children, events, ...attrs} = options;

        this.tagName = tagName;
        this.className = className;
        this.children = children;
        this.events = events
        this.attrs = attrs
    }


    toHTML() {
        const element = document.createElement(this.tagName);
    
        element.className = this.className;
    
        if (this.children) element.insertAdjacentHTML("beforeend", this.children);
        
        element.addEventListener("click", this.events);

        for (const key in this.events) {
          const value = this.events[key];
          element.addEventListener(key, value);
        }
    
        return element;
      }
    }