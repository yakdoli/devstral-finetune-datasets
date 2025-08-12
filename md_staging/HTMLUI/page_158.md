```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: HTMLUI
page_number: 158
page_id: HTMLUI#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:33Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

Essential Studio includes ten component libraries in one great package. Each of these products has a unique and useful feature set. Syncfusion aims to provide customers with the utmost satisfaction and value in using Syncfusion and Microsoft technologies through our technical consulting and training services.

```html
</p>
</body>
</html>
```

## Overview
- Demonstrates how an image reference can be changed for a page in the HTMLUI at runtime using the `PrerenderDocument` event.
- Provides both C# and VB.NET code examples.

## Content

### Changing Image Reference at Runtime
The following snippet shows how an image reference is changed for a page in the HTMLUI at run time, by using the PrerenderDocument event.

#### C#
```csharp
Hashtable htmlElements = new Hashtable();

// Event Declaration.
this.htmluiControl1.PrerenderDocument += 
new Syncfusion.Windows.Forms.HTMLUI.PrerenderDocumentEventHandler(this.htmluiControl1_PrerenderDocument);

// Event that is to be raised when a tree of element has been created and their
// size and location have not been calculated yet.
private void htmluiControl1_PrerenderDocument(object sender, PrerenderDocumentEventArgs e)
{
    // Create and Return the Hash Table where key is Tag name(Element.Name) and
    // Value is array of elements with Current name.
    this.htmlElements = e.Document.GetElementsByNameHash();
    ArrayList imgs = this.htmlElements["img"] as ArrayList;
    foreach (BaseElement elem in imgs)
    {
        string oldValue = elem.Attributes["src"].Value;
        string newValue = @"C:\MyProjects\ImageHandling\newImage.jpg";

        // Replace or change the value of the attribute in the element at run time.
        elem.Attributes["src"].Value = oldValue.Replace(elem.Attributes["src"].Value, newValue);
        Console.WriteLine(elem.Attributes["src"].Value);
    }
}
```

#### VB.NET
```vb
Private htmlElements As Hashtable = New Hashtable()

' Event Declaration.
Me.htmluiControl1.PrerenderDocument += New
```

## API Reference
### Methods and Events
- `PrerenderDocumentEvent`: Triggered when the HTMLUI control is about to render the document, allowing modifications to elements before rendering.

## Code Examples

### C#
```csharp
Hashtable htmlElements = new Hashtable();
this.htmluiControl1.PrerenderDocument += new Syncfusion.Windows.Forms.HTMLUI.PrerenderDocumentEventHandler(this.htmluiControl1_PrerenderDocument);

private void htmluiControl1_PrerenderDocument(object sender, PrerenderDocumentEventArgs e)
{
    this.htmlElements = e.Document.GetElementsByNameHash();
    ArrayList imgs = this.htmlElements["img"] as ArrayList;
    foreach (BaseElement elem in imgs)
    {
        string oldValue = elem.Attributes["src"].Value;
        string newValue = @"C:\MyProjects\ImageHandling\newImage.jpg";
        elem.Attributes["src"].Value = oldValue.Replace(elem.Attributes["src"].Value, newValue);
        Console.WriteLine(elem.Attributes["src"].Value);
    }
}
```

### VB.NET
```vb
Private htmlElements As Hashtable = New Hashtable()
Me.htmluiControl1.PrerenderDocument += New
```

## Page-level Navigation/TOC
This page provides instructions and code examples for dynamically changing image references in the HTMLUI control using the `PrerenderDocument` event. It includes both C# and VB.NET implementations.

<!-- tags: [Syncfusion, WinForms, HTMLUI, PrerenderDocument, Image Reference, C#, VB.NET, version: 11.4.0.26] keywords: [HTMLUI, PrerenderDocument, Image Reference, C#, VB.NET, runtime changes, event handling, control development] -->
```