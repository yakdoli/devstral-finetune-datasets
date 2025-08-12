```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_142.jpeg
document_name: DocIo
page_number: 142
page_id: DocIo#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:36:49Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Describes the WField and WEmbedField classes.
- Details the properties and constructors related to these classes.
- Focuses on the WSeqField class, which represents a sequence field type in a Word document.

## Content

### Public Property

| Name       | Description               |
|------------|----------------------------|
| EntityType | Gets the type of the entity. |

#### 4.4.1.2.3 Seq Field

The **WSeqField** class represents a sequence field type in the Word document. To add a sequence field in Microsoft Word, open the **Insert** menu, click **Field**, and then click **Seq**. You can find more information about the sequence field at the following location: <http://office.microsoft.com/en-us/word/HP051861901033.aspx>.

You can use the **NumberFormat** property to set the numbering format for the fields, and the **CaptionName** property to set the name of the caption.

##### Public Constructor

| Name                                    | Description                                       |
|-----------------------------------------|---------------------------------------------------|
| WSeqField.WSeqField(IWordDocument)     | Initializes a new instance of the WSeqField class. |

##### Public Properties

| Name            | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| CaptionName     | Gets or sets the caption name.                                             |
| EntityType      | Gets the type of the entity.                                               |
| FormattingString| Gets the formatting string.                                                |
| NumberFormat    | Gets or sets the type of caption numbering. It includes the following options:<br>• Number |

## API Reference

### Properties
- **CaptionName**: Gets or sets the caption name.
- **EntityType**: Gets the type of the entity.
- **FormattingString**: Gets the formatting string.
- **NumberFormat**: Gets or sets the type of caption numbering.

### Public Constructor
- **WSeqField.WSeqField(IWordDocument)**: Initializes a new instance of the WSeqField class.

## Code Examples

```csharp
// Example of using WSeqField in a document
using(Syncfusion.DocIO.WDocDocument document = new Syncfusion.DocIO.WDocDocument())
{
    // Open a Word document
    document.Open(@"input.docx");

    // Access the body of the document
    Syncfusion.DocIO.WSection section = document.Sections[0];

    // Create a WSeqField
    Syncfusion.DocIO.WSeqField seqField = new Syncfusion.DocIO.WSeqField(document);

    // Set properties of the sequence field
    seqField.CaptionName = "Figure";
    seqField.NumberFormat = "1";

    // Insert the sequence field into the document
    section.AppendField(seqField);

    // Save the modified document
    document.Save(@"output.docx");
}
```

<!-- tags: [DocIO, WField, WEmbedField, WSeqField, WordDocument, sequence_field, properties, constructors, syncfusion-sdk, version-11.4.0.26] keywords: [WSeqField, EntityType, CaptionName, FormattingString, NumberFormat, WordDocument] -->
```