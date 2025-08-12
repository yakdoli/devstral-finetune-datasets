```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_170.jpeg
document_name: HTMLUI
page_number: 170
page_id: HTMLUI#page_170
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:13:33Z
fidelity: lossless
--> 

## Overview
- Event handling specific to HTMLUI in Syncfusion Winforms.
- Demonstrates the implementation of custom control functionality for `maskedEditTextBox`, `monthCalendar`, and `dataGrid` controls.
- Focuses on associating user-defined controls with their respective implementations during pre-rendering.

## Content

### Handling Pre-render Event in Syncfusion HTMLUI
To ensure predictable size and layout of controls in an HTML document, Syncfusion provides an event `PreRenderDocument` that can be utilized to delegate the functionality of custom controls to their corresponding elements in the HTML document.

#### C# Implementation
```csharp
// Event that is to be raised when a tree of element has been created and their size and location have
// not been calculated yet.
private void htmluiControl1_PreRenderDocument(object sender, Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs e)
{
    Hashtable hmlelements = new Hashtable();

    // Returns an hash of elements by their User Id.
    hmlelements = e.Document.ElementsByUserID;
    BaseElement maskedEditTextBoxElement1 = hmlelements["maskedEditTextBox1"] as BaseElement;

    // Here the base functionality of the 'this.maskedEditBox1' is implemented to the 'maskedEditTextBoxElement1'.
    new CustomControlBase( maskedEditTextBoxElement1, this.maskedEditBox1  );
    BaseElement monthCalendarElement1 = hmlelements["monthCalendar1"] as BaseElement;

    // Here the base functionality of the 'this.monthCalendar1' is implemented to the 'monthCalendarElement1'.
    new CustomControlBase( monthCalendarElement1, this.monthCalendar1  );
    BaseElement dataGridElement1 = hmlelements["dataGrid1"] as BaseElement;

    // Here the base functionality of the 'this.dataGrid1' is implemented to the 'dataGridElement1'.
    new CustomControlBase( dataGridElement1, this.dataGrid1  );
}
```

#### VB.NET Implementation
```vb
[VB.NET]

Private Sub htmluiControl1_PreRenderDocument(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs)
    Dim hmlelements As Hashtable = New Hashtable()
    hmlelements = e.Document.ElementsByUserID

    Dim maskedEditTextBoxElement1 As BaseElement = CType(IIf(TypeOf hmlelements("maskedEditTextBox1") Is BaseElement, hmlelements("maskedEditTextBox1"), Nothing), BaseElement)
    Dim oTemp1 As CustomControlBase = New CustomControlBase(maskedEditTextBoxElement1, Me.maskedEditBox1)

    Dim monthCalendarElement1 As BaseElement = CType(IIf(TypeOf hmlelements("monthCalendar1") Is BaseElement, hmlelements("monthCalendar1"), Nothing), BaseElement)
    Dim oTemp2 As CustomControlBase = New CustomControlBase(monthCalendarElement1, Me.monthCalendar1)

    Dim dataGridElement1 As BaseElement = CType(IIf(TypeOf hmlelements("dataGrid1") Is BaseElement, hmlelements("dataGrid1"), Nothing), BaseElement)
End Sub
```

### Explanation
- The `PreRenderDocument` event is triggered when the HTML document structure is ready but sizes and positions of elements are still unspecified.
- The event allows customization by associating predefined controls (`maskedEditBox`, `monthCalendar`, `dataGrid`) with their respective HTML elements identified by user IDs.
- The `CustomControlBase` class is used to link the functionality of user-defined controls to these HTML elements.

## API Reference

### Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs
- **Event Arguments**: `PreRenderDocumentArgs`
- **Description**: Provides access to the document to be rendered, including its elements.

### Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentEvent
- **Event Subscription**: Subscribe to this event to implement custom functionality before the document is rendered.

### CustomControlBase
- **Purpose**: Delegate the functionality of a custom control to a specified HTML element in the HTMLUI document.

## Code Examples (Multi-Language)
The examples provided in both C# and VB.NET showcase how to implement custom control functionality during the pre-rendering phase of an HTMLUI document.

## RAG Annotations
<!-- tags: [syncfusion-windows-forms, htmlui, custom-control, user-interface, pre-render-document] keywords: [PreRenderDocument, maskedEditTextBox, monthCalendar, dataGrid, HTMLUI, customControlBase, BaseElement] -->
```