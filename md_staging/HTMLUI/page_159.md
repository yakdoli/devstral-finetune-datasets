<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_159.jpeg
document_name: HTMLUI
page_number: 159
page_id: HTMLUI#page_159
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:40Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Content

### Handling PreRenderDocument Event

```vb
Syncfusion.Windows.Forms.HTMLUI.PreRenderDocumentEventHandler(Me.htmluiControl1_PreRenderDocument)

' Event that is to be raised when a tree of element has been created and their
' size and location have
' not been calculated yet.
Private Sub htmluiControl1_PreRenderDocument(ByVal sender As Object, ByVal e As PreRenderDocumentArgs)

    ' Create and Return the Hash Table where key is Tag name(Element.Name) and
    ' Value is array of
    ' elements with Current name.
    Me.htmlElements = e.Document.GetElementsByTagName("img")
    Dim imgs As ArrayList = CType(IIf(TypeOf Me.htmlElements("img") Is ArrayList, Me.htmlElements("img"), Nothing), ArrayList)
    For Each elem As BaseElement In imgs
        Dim oldValue As String = elem.Attributes("src").Value
        Dim newValue As String = @"C:\MyProjects\ImageHandling\newImage.jpg";

        ' Replace or change the value of the attribute in the element at run time.
        elem.Attributes("src").Value = oldValue.Replace(oldValue, newValue)
        Console.WriteLine(elem.Attributes("src").Value)
    Next elem
End Sub
```

The following figure illustrates this behavior where the oldImage has been replaced by newValue.

## API Reference

### Event: PreRenderDocument

```vb
Private Sub htmluiControl1_PreRenderDocument(ByVal sender As Object, ByVal e As PreRenderDocumentArgs)
```

This event is raised when a tree of elements has been created and their size and location have not been calculated yet. It allows developers to modify the HTML structure before it is rendered.

### Method: GetElementsByTagName

```vb
Me.htmlElements = e.Document.GetElementsByTagName("img")
```

This method retrieves all elements with the specified tag name.

### Property: Attributes

```vb
elem.Attributes("src").Value
```

This property provides access to the attributes of the element.

## Code Examples

### Example: Replacing Image Sources at Runtime

```vb
Private Sub htmluiControl1_PreRenderDocument(ByVal sender As Object, ByVal e As PreRenderDocumentArgs)
    Me.htmlElements = e.Document.GetElementsByTagName("img")
    Dim imgs As ArrayList = CType(IIf(TypeOf Me.htmlElements("img") Is ArrayList, Me.htmlElements("img"), Nothing), ArrayList)
    For Each elem As BaseElement In imgs
        Dim oldValue As String = elem.Attributes("src").Value
        Dim newValue As String = @"C:\MyProjects\ImageHandling\newImage.jpg";
        elem.Attributes("src").Value = oldValue.Replace(oldValue, newValue)
        Console.WriteLine(elem.Attributes("src").Value)
    Next elem
End Sub
```

## Conclusion

The `PreRenderDocument` event allows developers to manipulate the HTML structure of the `HTMLUI` control before it is rendered. This example demonstrates how to replace `<img>` src attributes dynamically at runtime, ensuring the correct images are displayed in the UI.

<!-- tags: [HTMLUI, Windows Forms, PreRenderDocument, Image, Event, Element, Attribute] keywords: [Syncfusion, HTMLUI, PreRenderDocument, GetElementsByTagName, Attributes] -->