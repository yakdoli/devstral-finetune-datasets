```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_225.jpeg
document_name: DocIo
page_number: 225
page_id: DocIo#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:42:52Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes the customization of bullet styles in document lists.
- Focuses on properties and methods related to bullet list styles.

## Content

### WinForms Customization of Bulleted List

![Figure 76: Bulleted List Style](images/bulleted_list_style.png)

This section explains how to customize bulleted list styles in documents using the provided interface. The interface allows adjustments to bullet characters, positions, and text alignment.

---

### Public Properties

| Name                           | Description                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| **Levels**                     | Gets list levels collection.                                                |
| **ListType**                   | Gets or sets list type.                                                     |
| **Name**                       | Gets style name.                                                           |
| **StyleType**                  | Gets the type of the style.                                                 |
| **ListStyle.ListStyle (IWordDocument, ListType)** | Initializes a new instance of the ListStyle class. |

---

### Public Methods

| Name         | Description           |
|--------------|-----------------------|
| [Method Name Here] | [Method Description Here] |

---

## API Reference

### Namespace: Syncfusion.DocIO

#### Class: ListStyle

##### Properties

- **Levels** (`ListLevelsCollection`)
  - Gets the list levels collection.

- **ListType** (`ListType`)
  - Gets or sets the type of the list.

- **Name** (`string`)
  - Gets or sets the style name.

- **StyleType** (`ListStyleType`)
  - Gets the type of the style.

##### Methods

- **ListStyle(ListStyle listStyle)**:
  - Initializes a new instance of the `ListStyle` class.

---

## Code Examples

### C# Example

```csharp
// Example of creating and setting a bulleted list style
Document doc = new Document();
ListStyle listStyle = new ListStyle(doc.WordDocument, ListType.Bulleted);
listStyle.Name = "CustomBulletStyle";
listStyle.ListLevels[0].NumberFormat = ListNumberFormat.CircleBullet;
doc.AddSection().AddParagraph("List item 1");
doc.LastSection.Paragraphs[0].ListStyle = doc.ListStyles[listStyle.Name];
doc.Save();
```

---

## Cross References

- Refer to the **Document Formatting Guide** for more information on formatting and styling in documents.

<!-- tags: [syncfusion-winforms, document-io, bulleted-list, list-style, api, version-11.4.0.26] keywords: [bulleted list, list style, document formatting, list levels, style properties, document customization] -->
```