```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: pdf
page_number: 123
page_id: pdf#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:31:53Z
fidelity: lossless
-->

# Essential PDF

There are two events provided by the laid out elements: **BeginPageLayout** and **EndPageLayout**. They provide an option to track the current state of the layout, and specify the custom settings for the layout process.

## 4.1.2.2.7 Page Templates

### Overview
- Define similar graphics primitives for a range of pages.
- Each page has two sources of templates that apply sequentially: one on the document holding the section of the page, and another on the section containing the page.
- Each page template has four properties for docked templates and additional elements (stamps).
- Eight additional templates can be added for odd/even pages, overriding the usual templates if set.

### Page Templates

Page Templates define similar graphics primitives for a range of pages. Each page has two sources of the templates (template on the document holding the section of the page, and template on the section containing the page) that apply sequentially.

Each page template has four properties for Left, Right, Top and Bottom docked templates, and a collection of the additional template elements (stamps). Also, there are eight additional templates that you can add to the odd / even pages (EvenTop, OddTop, etc.). If one of these eight templates is set, it overrides its usual template (OddTop overrides Top, etc.); Otherwise, the usual template is used.

#### Note: A PdfPageTemplateElement is added as one template.
It can be assigned to Left, Right, Top or Bottom only once.

### Using the Page Templates

If you want to define some graphics content to all pages of the document, use the **Template** property of the **PdfDocument** class. You can define Left, Top, Right, Bottom templates, as well as arbitrary quantity of the other templates (stamps) that can be used for water marking or stamping of the pages.

If you have decided to use some custom templates for a specified range of the page, use **Template** property of the **PdfSection** class containing these pages. It involves the same functionality as in the **PdfDocument** class. Additionally, you can disable or enable the document templates from the section.

### Default Behavior

Document templates are enabled, by default.

#### Note: Section template, which is printed over the parent template, does not replace document templates.
If you want to insert a watermark or stamp on the page, use **Stamps** property of the **PdfDocumentTemplate** class.

### Behavior

<!-- tags: [product, page templates, pdf layout, docked templates] keywords: [BeginPageLayout, EndPageLayout, PdfPageTemplateElement, stamps, odd/even pages, PdfDocument, PdfSection, Template, Stamps, documento templates, section templates] -->
```