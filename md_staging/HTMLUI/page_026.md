```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_026.jpeg
document_name: HTMLUI
page_number: 026
page_id: HTMLUI#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:33Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Introduction to custom tags in HTMLUI for Windows Forms.
- Explanation of the relationship between custom tags and the actual Windows Forms controls.
- Instructions to ensure HTML elements correspond to Windows Forms controls properly.

## Content

### Custom Tags and Control Representation
Note the custom tags `maskededitbox`, `monthcalendar`, and `datagrid`. These tags do not have any relation to the name of the control type they represent. Set the desired size of the custom control by setting the `width` and `height` attributes.

### Adding Custom Controls to the FORM
In the previous step, three custom controls were defined as part of the HTMLUI interface. The actual Windows Forms controls that represent these definitions have to be added to the form.

### Step-by-Step Instructions

1. **Drag a MonthCalendar Control**
   - Drag a `MonthCalendar` control from the toolbox and drop it on the form.
   - The `MonthCalendar` will be named `monthCalendar1` by default.
   - Use this name in the next step to associate it with the appropriate HTML-defined control.

2. **Drag MaskedEditBox and DataGrid Controls**
   - Drag a `MaskedEditBox` control and a `DataGrid` control onto the form.

### Figure: Custom Controls

![Custom Controls](https://example.com/image_path)
*Figure 10: Custom Controls*

### Handling PreRenderDocument Event
4. **Add a handler for the PreRenderDocument event of the HTMLUI control.**
   - This step associates the Windows Forms controls on the form with controls defined in the HTML. This is done in the PreRenderDocument event handler of the HTMLUI control. This event is raised before the control renders the HTML elements (after it has parsed the HTML document into HTML elements).

## API Reference
- No specific API reference is discussed in this section.

## Code Examples
- No code examples are provided in this section.

## Cross References
- Refer to previous steps for adding custom controls and understanding custom tags.

## RAG Annotations
<!-- tags: [HTMLUI, Windows Forms, MonthCalendar, MaskedEditBox, DataGrid] keywords: [custom tags, monthcalendar, datagrid, maskededitbox,,width, height, control representation, PreRenderDocument event] -->
```