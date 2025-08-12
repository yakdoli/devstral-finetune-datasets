```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_151.jpeg
document_name: HTMLUI
page_number: 151
page_id: HTMLUI#page_151
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:06Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## 5 Frequently Asked Questions

This section discusses various frequently asked questions with their answers, examples, and code snippets.

### 5.1 How To Access All the Child Elements Of an HTML Element In the HTMLUI Control?

The `IHTMLElement.Children` property of any `IHTMLElement` collects all the child elements of a specified HTML element inside an `IHTMLElementsCollection`. You can access the elements needed for your conditions from this collection.

The following code snippet illustrates how the child elements of the `Body` element in the given HTML document are searched to access elements containing the `OnClick` attribute and how a `Click` event is attached to those elements.

```html
[HTML]

<html>
 <head>
  <style>.nav{background-color:#da5f5}</style>
 </head>
 <body>
 <p/></p>
 <img src="sync.jpg" id="img1" class="nav"/>
 <p/></p>
 <div>This is a sample</div>
 </body>
</html>
```

```csharp
[C#]

private void htmluiControl_LoadFinished(object sender, EventArgs e)
{
    // Getting the body element in the HTML document
    IHTMLElement[] body = this.htmluiControl.Document.GetElementsByName("body");
    // Collecting the children of the body element in a collection
    IHTMLElementsCollection elem = body[0].Children;
    foreach (IHTMLElement child in elem)
    {
        // Searching for the children containing the OnClick attribute
        if (child.Attributes.Contains("OnClick") == true)
        {
            // Click event declaration for current children
        }
    }
}
```

## Page-level Navigation/TOC (if applicable)
- This section covers only FAQs related to accessing child elements in HTMLUI for Windows Forms.

## Cross References
- Refer to the main HTMLUI documentation for more details on working with HTML elements and attributes.

## RAG Annotations
<!-- tags: [Syncfusion, HTMLUI, Windows Forms, IHTMLElement, IHTMLElementsCollection, OnClick, event handler, C#, HTML scripting, child elements] keywords: [child elements, HTMLUI, Windows Forms, IHTMLElement, IHTMLElementsCollection, OnClick, C#, event handling, scripting] -->
```