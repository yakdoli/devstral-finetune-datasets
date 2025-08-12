```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_283.jpeg
document_name: diagram
page_number: 283
page_id: diagram#page_283
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:53Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### 5.23 How To Prevent the Nodes From Being Rotated

This can be done by raising the `Diagram.Model.EventSink.RotationChanging` event and cancelling the operation.

#### C#

```csharp
this.diagram1.Model.EventSink.RotationChanging += new RotationChangingEventHandler(EventSink_RotationChanging);

void EventSink_RotationChanging(RotationChangingEventArgs evtArgs)
{
    evtArgs.Cancel = true;
}
```

#### VB.NET

```vb
Me.diagram1.Model.EventSink.RotationChanging += New RotationChangingEventHandler(EventSink_RotationChanging)

Private Sub EventSink_RotationChanging(ByVal evtArgs As Syncfusion.Windows.Forms.Diagram.RotationChangingEventArgs)
    evtArgs.Cancel = True
End Sub
```

### 5.24 How To Print a Diagram In a Single Page

Essential Diagram uses the size of your diagram model and the printer page settings for calculating the number of pages to be rendered while printing. Even though you might have only one page worth of nodes in your diagram model, if the model bounds are larger, the Diagram control will attempt to paginate and print the entire model.

To print the diagram in a single page, you have to temporarily modify the size of the model.

#### C#

```csharp
// The desired page size is 21 x 29.7 centimeters.
```

---

## Page-level Navigation/TOC (if applicable)
- 5.23 How To Prevent the Nodes From Being Rotated
- 5.24 How To Print a Diagram In a Single Page

## Cross References
See also: **Diagram.Model.EventSink.RotationChanging**, **Diagram.Printing**.

---
<!-- tags: [syncfusion winforms, essential diagram, rotationchanging event, printing, single page printing] keywords: [Diagram, EventSink, RotationChanging, Print] -->
```