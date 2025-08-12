```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: DocIo
page_number: 097
page_id: DocIo#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:34:32Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Provides information about various document formatting properties and page layout settings.
- Includes details about constructors, properties, and methods for managing document sections.

## Content

### Section Properties

| Property                     | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| DifferentOddAndEvenPages     | True if the document has different headers and footers for odd-numbered and even-numbered pages. |
| FooterDistance               | Gets or sets footer height in points.                                      |
| HeaderDistance               | Gets or sets height of header in points.                                   |
| IsFrontPageBorder            | Gets or sets a value indicating whether this instance is front page border. |
| LineNumberingDistanceFromText | Gets or sets distance from text in lines numbering.                        |
| LineNumberingMode            | Gets or sets line numbering mode.                                          |
| LineNumberingStartValue      | Gets or sets line numbering start value.                                   |
| LineNumberingStep            | Gets or sets line numbering step.                                          |
| Margins                      | Gets or sets page margins in points.                                       |
| Orientation                  | Gets or sets orientation of a page.                                        |
| PageBorderApply              | Gets or sets the value that determines on which pages border is applied.   |
| PageBorderOffsetFrom         | Gets or sets the position of page border.                                  |
| PageBordersApplyType         | Gets or sets the value that determines on which pages border is applied.  |
| PageSize                     | Gets or sets page size in points.                                          |
| VerticalAlignment            | Gets or sets vertical alignment.                                           |

### Public Constructors

| Name                           | Description                                                                                     |
|--------------------------------|-------------------------------------------------------------------------------------------------|
| WSection.WSection (IWordDocument) | Initializes a new instance of the WSection class.                                          |

### Public Properties

| Name | Description                                               |
|------|-----------------------------------------------------------|
| Body | Gets the section body.                                    |

## Code Examples
```csharp
// Example: Create a new section with specific properties
WSection section = new WSection(wordDocument);
section.HeaderDistance = 72; // Set header distance to 1 inch (72 points)
section.FooterDistance = 50; // Set footer distance to 5/7 inches (50 points)
section.PageSize = new SizeF(612, 792); // Set page size to A4 (8.5x11 inches)
section.Margins = new Margins(72, 72, 72, 72); // Set margins to 1 inch on all sides
section.LineNumberingStartValue = 1; // Set line numbering start value
section.LineNumberingStep = 1; // Set line numbering step
section.LineNumberingMode = LineNumberingMode.Document; // Set line numbering mode
section.VerticalAlignment = VerticalAlignment.Center; // Set vertical alignment
```

## Cross References
- See also: Document formatting, Page layout, WSection class, Line numbering, Margins.

<!-- tags: [DocIO, document formatting, page layout, WSection, line numbering, margins] keywords: [different headers, footer distance, header distance, front page border, line numbering mode, margins, page size, vertical alignment] -->
```