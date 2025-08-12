```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_061.jpeg
document_name: HTMLUI
page_number: 061
page_id: HTMLUI#page_061
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:18Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Description

The BODY element forms the main section in the HTMLUI because this element contains all the other elements and details regarding their position and properties. The BODYElementImpl class contains the properties and methods for this element.

## BR - Break Element

### Overview

The BR element is used for inserting a line break after a particular line. This is implemented using the `<br>` tag in the HTML document. The BRElementImpl class contains the properties and methods for this element's behavior.

### Properties

- **IsVisible**: Gets / sets a boolean value to indicate whether the control is shown / hidden.

### Code Examples

#### C#

```csharp
// Get the Boolean value to indicate whether the control is visible or not.
Hashtable htmlElements = this.htmluiControl1.Document.GetElementsByIdHash();
BRElementImpl br = htmlElements["br"] as BRElementImpl;
this.label1.Text = "\nBR(IsVisible): " + this.br.IsVisible.ToString();
```

#### VB.NET

```vb
' Get the Boolean value to indicate whether the control is visible or not.
Private htmlElements As Hashtable = Me.HtmluiControl1.Document.GetElementsByIdHash()
Private br As BRElementImpl = CType(IIf(TypeOf htmlElements("br") Is BRElementImpl, htmlElements("br"), Nothing), BRElementImpl)
Me.label1.Text = Constants.vbLf & "BR(IsVisible): " & Me.br.IsVisible.ToString()
```

## CODE Element

### Overview

The CODE element is used in marking the specified text as a computer code, formatted using monospaced font. It uses the CODEElementImpl class which contains the properties and methods determining the element's behavior.

## CUSTOM Element

### Overview

The CUSTOM element is used in creating the custom tags as determined by the user. The CUSTOMElementImpl class is responsible for the custom controls declared by the `<custom>` tag in the HTML document and contains the element's properties and methods.

## Copyright Information

© 2013 Syncfusion. All rights reserved.
Page
```