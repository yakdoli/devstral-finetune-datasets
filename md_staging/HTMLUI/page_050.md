```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_050.jpeg
document_name: HTMLUI
page_number: 050
page_id: HTMLUI#page_050
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:57Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```vb
Me.HtmluiControl1.LoadError += New Syncfusion.Windows.Forms.HTMLUI.LoadErrorEventHandler(Me.htmluiControl1_LoadError)

Private Sub htmluiControl1_LoadError(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.HTMLUI.LoadErrorEventArgs)
    Console.WriteLine("Error loading due to" & e.ToString())
End Sub
```

## PreRenderDocument Event

This event is raised when the elements in the HTML document are created in the HTMLUI control, but their size and location are not calculated yet.

### C#

```csharp
// Event that is to be raised when a tree of element has been created and their size and location have not been calculated yet.
this.htmluiControl1.PreRenderDocument += new Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentEventHandler(this.htmluiControl1_PreRenderDocument);

private void htmluiControl1_PreRenderDocument(object sender, Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs e)
{
    Console.WriteLine("This is the Prerender document event");
}
```

### VB.NET

```vb
' Event that is to be raised when a tree of element has been created and their size and location have not been calculated yet.
Me.HtmluiControl1.PreRenderDocument += New Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentEventHandler(Me.htmluiControl1_PreRenderDocument)

Private Sub htmluiControl1_PreRenderDocument(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentArgs)
    Console.WriteLine("This is the Prerender document event")
End Sub
```

## ShowTitleChanged Event

This event is raised after the `ShowTitle` property of the HTMLUI control is changed. The event handler receives its data from the `ValueChangedEventArgs`. The following property is associated with the `ShowTitleChanged` event handling.

- **Empty**: Gets the instance of the class that is found to be empty or having null value

---

<!-- tags: [product, HTMLUI, Windows Forms, events, HTMLUI, version 11.4.0.26] keywords: [PreRenderDocument, ShowTitleChanged, LoadError, event handling, HTMLUI, Windows Forms, Syncfusion, 11.4.0.26] -->
```