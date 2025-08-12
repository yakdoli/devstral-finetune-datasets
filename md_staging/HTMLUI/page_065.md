```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_065.jpeg
document_name: HTMLUI
page_number: 065
page_id: HTMLUI#page_065
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:06:31Z
fidelity: lossless
-->

<!-- anchor: HTMLUI#page_065#overview -->
## Overview

- Deals with the HTML User Interface (HTMLUI) for Windows Forms, focusing on the `LİElementImpl`, `LinkElementImpl`, and related functionalities such as detecting control types and handling list elements.

<!-- anchor: HTMLUI#page_065#content -->

## Content

### Methods

- **InfillFromXMLElement**: Detects the type of control from the `type` attribute and creates that control.

#### 4.5.19 LI - List Element

The `LIST` element is used to define a list item. The `LİElementImpl` class is used to determine the properties and methods for this element. There are two types of lists that are supported by HTMLUI:

- **OL Element**: Ordered List Element
- **UL Element**: Unordered List Element

#### 4.5.20 LINK Element

The `LINK` element is used to define links to other documents, style sheets, and so on. The `LinkElementImpl` is used to determine the methods and properties for the link element.

### Properties

- **IsVisible**: Gets / sets a value indicating whether the link is shown / hidden

### Code Examples

#### [C#]

```csharp
// Get the value indicating whether the link is visible or not.
Hashtable htmelements =
    this.htmluiControl.Document.GetElementsByUserIdHash();
LinkElementImpl link = htmelements["link"] as LinkElementImpl;
this.label1.Text = "\nLink(IsVisible): " + this.link.IsVisible.ToString();
```

#### [VB.NET]

```vb
' Get the value indicating whether the link is visible or not.
Private As Hashtable = Me.htmluiControl.Document.GetElementsByUserIdHash()
Private link As LinkElementImpl = CType(IIf(TypeOf HTMLElement("link") Is
LinkElementImpl, htmelements("link"), Nothing), LinkElementImpl)
Me.label1.Text = Constants.vbLf & "Link(IsVisible): " &
Me.link.IsVisible.ToString()
```

<!-- anchor: HTMLUI#page_065#page-level-navigation -->

## Page-Level Navigation/TOC

- Methods
  - InfillFromXMLElement
- LI - List Element
  - Introduction
  - Supported List Types
- LINK Element
  - Overview
  - Properties
  - Code Examples

<!-- Tags and Keywords -->
<!-- tags: [innerHTML, list-elements, link-elements, htmlui, windows-forms, syncfusion] keywords: [list items, ordered list, unordered list, link visibility, html controls] -->
```