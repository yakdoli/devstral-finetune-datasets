```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: DocIo
page_number: 149
page_id: DocIo#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:37:43Z
fidelity: lossless
-->

## Essential DocIO

You can use the `AppendDropDownFormField` function of `WParagraph` to append drop-down form fields to the end of the paragraph.

### Class Hierarchy

- `WTextRange`
  - `WField`
    - `WFormField`
      - `WDropDownFormField`

### Public Constructor

| Name                                                                  | Description                                                         |
|----------------------------------------------------------------------|---------------------------------------------------------------------|
| `WDropDownForm.FieldWDropDownFormField(IWordDocument)`| Initializes a new instance of the `WDropDownFormField` class. |

### Public Properties

| Name               | Description                             |
|--------------------|-----------------------------------------|
| `DropDownItems`    | Gets drop down items.                  |
| `DropDownSelectedIndex` | Gets or sets the selected drop-down index. |

### Code Example

```csharp
IWordDocument doc = new WordDocument();
doc.EnsureMinimal();

IWParagraph par = doc.LastParagraph;
WDropDownFormField dropDown = par.AppendDropDownFormField();
dropDown.DropDownItems.Add("One");
dropDown.DropDownItems.Add("Two");
dropDown.DropDownSelectedIndex = 1;
dropDown.CalculateOnExit = true;
dropDown.Enabled = false;
```

### Notes
This page provides an overview of using the `AppendDropDownFormField` method in DocIO to append drop-down form fields to a paragraph. The class hierarchy and constructors are described along with examples in C# to demonstrate the functionality.
```

<!-- tags: [Essential DocIO, WParagraph, WFormsField, WDropDownFormField, Create FormFields] keywords: [essentials, document manipulation,drop-down form, Word document, paragraphs, form fields, C# examples] -->
```