```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_066.jpeg
document_name: HTMLUI
page_number: 066
page_id: HTMLUI#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:07:01Z
fidelity: lossless
-->

## Essential HTMLUI for Windows Forms

### Methods

- `GetCssStream`: Returns a stream CSS data of the link element

### 4.5.21 OL - Ordered List Element

The OL element is used in generating an ordered list as specified by the user. The properties and methods of this element are defined in the `OLElementImpl` class.

### 4.5.22 P - Paragraph Element

The P element is used to define a paragraph in the document. The user can determine the properties and methods for the P element by invoking the `PElementImpl` class.

### 4.5.23 PRE - Preformatted Element

The PRE element defines preformatted text. The text enclosed in the pre element usually preserves the spaces and line breaks. The enclosed text appears exactly as in the HTML document. The properties and methods for this element can be determined from the `PREElementImpl` class.

### 4.5.24 SCRIPT Element

The SCRIPT element is used to define scripts to the HTML document. This makes the document self-contained. It does not require any other external ways to define the operation of the document's elements. The `SCRIPTElementImpl` class is used to determine the properties and methods for this element.

#### Properties

- **IsVisible**: Gets / sets a value indicating whether the script is shown / hidden

#### Code Example

```csharp
// Gets or sets a value indicating whether the script  is visible or not.
Hashtable htmlElements = 
this.htmluiControl.Document.GetElementsByUserIdHash();
this.script = htmlElements["script"] as SCRIPTElementImpl;
this.label1.Text = "\nScript(IsVisible):" + this.script.IsVisible.ToString();
```

<!-- tags: [Syncfusion Winforms, HTMLUI, Ordered List, Paragraph, Preformatted, Script, Version 11.4.0.26] keywords: [ordered list element, paragraph element, preformatted text, script element, properties, methods, user guide, htmlui control, scripting] -->
```