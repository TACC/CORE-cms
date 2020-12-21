/**
 * Create an HTML Template element from a given HTML element string
 * @param {string} html - HTML for shadow DOM of custom element
 * @param {string} name - Name of custom element to register
 * @return {Element}
 */
export function fromHTMLString(html, name) {
  let template = document.createElement('template');

  // Never return a text node of whitespace
  html = html.trim();

  template.innerHTML = html;
  template = document.head.appendChild(template);

  return fromTemplate(template, name);
}

/**
 * Populate custom element of givenname with content of a given HTML template
 * @param {HTMLTemplateElement} template - HTML for shadow DOM of custom element
 * @param {string} name - Name of custom element to register
 * @return {Element}
 */
export function fromTemplate(template, name) {

  console.log({template});

  window.customElements.define(name, class extends HTMLElement {
    constructor() {
      super();

      console.log({content: template.content});

      this.attachShadow({ mode: "open" });
      this.shadowRoot.appendChild(template.content.cloneNode(true));
    }
  });
}
