```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_071.jpeg
document_name: HTMLUI
page_number: 071
page_id: HTMLUI#page_071
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:41Z
fidelity: lossless
-->

## Content
### HTML Cells Properties
- `CellsCount`: Gets the number of cells present in the row
- `VirtualCellsCount`: Gets the total number of cells including the Colspan

#### C# Example
```csharp
// Gets the number of cells present in the row and gets total number of cells including the colspan.
Hashtable htmlElements = this.htmluiControl.Document.GetElementsByUserIdHash();
TRElementImpl tr = htmlElements["tr"] as TRElementImpl;
this.label1.Text = "TR(CellsCount and VirtualCellsCount):"+ tr.CellsCount.ToString()+","+ tr.VirtualCellsCount.ToString();
```

#### VB.NET Example
```vbnet
' Gets the number of cells present in the row and gets total number of cells including the colspan.
Private htmlElements As Hashtable = Me.htmluiControl.Document.GetElementsByUserIdHash()
Private tr As TRElementImpl = CType(If(TypeOf htmlElements("tr") Is TRElementImpl, htmlElements("tr"), Nothing), TRElementImpl)
Private Me.label1.Text = "TR(CellsCount and VirtualCellsCount):"+ tr.CellsCount.ToString()+","+ tr.VirtualCellsCount.ToString()
```

### 4.5.34 UL - Unordered List Element
The `UL` element is used in generating an unordered list. The properties and methods of this element are defined in the `ULElementImpl` class.

### 4.5.35 U - Underline Element
The `U` element is used to underline the specified text. The `UElementImpl` class contains the properties and methods for the underline element.

## 4.6 HTML Tags
This section details the HTML tags supported by HTMLUI. Most of the tags conform to the XHTML standard. Some of the tags support additional functionality implemented through custom attributes. Since HTMLUI considers each HTML tag as an XML element, it is recommended to use closing tags for each HTML element at the end. These tags and attributes are also marked and explained in this section.

## Footer
© 2013 Syncfusion. All rights reserved.
```