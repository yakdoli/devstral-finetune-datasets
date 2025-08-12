```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_200.jpeg
document_name: DocIo
page_number: 200
page_id: DocIo#page_200
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:55Z
fidelity: lossless
-->

# Essential DocIO

## Class Hierarchy

- ParagraphItem
  - |  
    - WOleObject

## Object Types

Objects can be either linked to the program or embedded in the program. **Linked Objects** remain as separate files and any changes made to them will be reflected immediately. On the other hand, **Embedded Objects** will be stored in the document that they are inserted and hence changes will not be reflected in them.

If you copy information as an embedded object, the destination file requires more disk space than if you link the information. When the file is opened on another computer, the embedded object can be viewed without having access to the original data. The `OleLinkType` property of `WOleObject` is used to set the object type as Embed or Link.

### Figure 70: Setting the OLE Object Type in the Object Dialog Box

- The object dialog box allows you to set the type of OLE object you want to embed or link.
- The `Object type` dropdown menu includes options such as:
  - Adobe Acrobat Document
  - Bitmap Image
  - Microsoft Equation 3.0
  - Microsoft Graph Chart
  - Microsoft Office Excel 97-2003 Worksheet
  - Microsoft Office Excel Binary Worksheet
  - Microsoft Office Excel Chart
  - Microsoft Office Excel Macro-Enabled Worksheet
- The `Result` section provides a preview of the object being inserted.
- The `Display as icon` checkbox is available for additional options.

## API Reference

- **Namespace:** `Syncfusion.DocIO.Models`
  - **Class:** `WOleObject`
    - **Property:** `OleLinkType`
      - **Type:** `string`
      - **Description:** Specifies whether the OLE object is embedded or linked.
      - **Parameters:**
        - `Embed`
        - `Link`

## Code Examples

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.Models;

// Create a new WOleObject
WOleObject oleObject = new WOleObject();

// Set the OleLinkType to Embed
oleObject.OleLinkType = "Embed";

// Insert the object into the document
document.Insert(oleObject);
```

<!-- tags: [DocIO, WinForms, OLEObjects, ObjectTypes, Syncfusion] keywords: [Display as icon, OleLinkType, WOleObject, Link, Embed, Document, Object Dialog Box] -->
```