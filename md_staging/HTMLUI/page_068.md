```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: HTMLUI
page_number: 068
page_id: HTMLUI#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:42Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

- Methods

  • **InfillFromXMLElement**: Detects the type of control and creates the particular control

## 4.5.26 SPAN Element

The SPAN element is used to group inline elements in the document and create custom character styles. The SPANElementImpl class is used to determine the properties and methods for the span element.

## 4.5.27 STRONG Element

The STRONG element is used to emphasize the specified text, usually in bold. The STRONGElementImpl class is used to define the properties and methods for the strong element.

## 4.5.28 STYLE Element

The STYLE element is used to implement custom style in a document. It occurs inside the head section. An external style sheet is linked by using the `<link>` tag in a HTML document. The StyleElementImpl class is invoked for defining the properties and methods of the style element.

### Properties
- **IsVisible**: Gets / sets a value indicating whether the link is shown / hidden

### [C#]
```csharp
// Gets a value indicating whether the link is visible or not.
Hashtable htmlElements = this.htmluiControl1.Document.GetElementsByUserIdHash();
StyleElementImpl link = htmlElements["style"] as StyleElementImpl;
this.label1.Text = "\nLink(IsVisible): " + link.IsVisible.ToString();
```

### [VB.NET]
```vb
' Gets a value indicating whether the link is visible or not.
```

## Page-level Navigation/TOC (if applicable)
- References are kept as shown in the original document.
- For additional context, see the HTMLUI documentation for further details.

<!-- tags: [product: Syncfusion Winforms, module: HTMLUI, control: HTMLUI elements, api: SPANElementImpl, STRONGElementImpl, StyleElementImpl, version: 11.4.0.26] keywords: [HTMLUI, SPAN element, STRONG element, STYLE element, IsVisible property, HTMLUI control] -->
```