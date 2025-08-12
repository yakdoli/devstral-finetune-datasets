```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_027.jpeg
document_name: HTMLUI
page_number: 027
page_id: HTMLUI#page_027
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:04:08Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- This page explains how to handle events and load HTML documents in Syncfusion WinForms HTMLUI controls. It includes code examples for event handling and resource loading.

## Content

### Event Handling in HTMLUI Controls

[C#]

```csharp
this.htmluiControl1.PreRenderDocument += new
Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentEventHandler(this.htmluiControl1_PreRenderDocument);

// Event that is to be raised when a tree of element has been created and their
// size and location have
// not been calculated yet.
private void htmluiControl1_PreRenderDocument(object sender,
Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs e)
{
    Hashtable htmlElements = new Hashtable();
    htmlElements = e.Document.ElementsByUserID;

    BaseElement maskedEditTextBoxElement1 = htmlElements["maskedEditTextBox1"] as BaseElement;

    // Create a new Wrapper object
    new CustomControlBase(maskedEditTextBoxElement1, this.maskedEditBox1);

    BaseElement monthCalendarElement1 = htmlElements["monthCalendar1"] as BaseElement;
    new CustomControlBase(monthCalendarElement1, this.monthCalendar1);

    BaseElement dataGridElement1 = htmlElements["dataGrid1"] as BaseElement;
    new CustomControlBase(dataGridElement1, this.dataGrid1);
}
```

### Loading HTML Resources in the HTMLUI Control

5. Add a handler for the `Load` event and load the HTML document resource into the HTMLUI control.

[C#]

```csharp
this.Load += new System.EventHandler(this.Form1_Load);

private void Form1_Load(object sender, System.EventArgs e)
{
    LoadHTMLResource();
}

private bool LoadHTMLResource()
{
    bool success = false;
    try
    {
        // Gets the Assembly that contains the code that is currently executing
        _assembly = Assembly.GetExecutingAssembly();
    }
```

### API Reference

This section includes information about the methods and events used in the examples, such as:
- `PreRenderDocumentEventHandler`
- `PreRenderDocumentArgs`
- `Document.ElementsByUserID`
- `BaseElement`

### Code Examples

The provided code examples demonstrate how to handle events and load HTML resources in a Windows Forms application using the Syncfusion HTMLUI control.

---

### Related Documents
- For more detailed information on HTMLUI controls, refer to the main documentation.
- For additional event handling examples, see the section on event handling in HTMLUI.

## Note
This example demonstrates the integration of WinForms controls with HTML elements using Syncfusion's HTMLUI control. Ensure that all necessary references and namespaces are included in your project.

<!-- tags: [syncfusion, htmlui, windows forms, pre-render event, load event] keywords: [BaseElement, PreRenderDocumentEventHandler, CustomControlBase, Assembly, HTMLUI, Windows Forms] -->
```