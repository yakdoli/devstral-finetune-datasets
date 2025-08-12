```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_202.jpeg
document_name: DocIo
page_number: 202
page_id: DocIo#page_202
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:40:44Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Initially, DocIO-generated documents display an icon in place of the embedded OLE object.
- The `DisplayAsIcon` property determines whether the icon will be updated after opening or editing the OLE object in MS Word.
- Setting `DisplayAsIcon` to `true` prevents updates, while setting it to `false` allows dynamic updates of the icons with the content after opening or editing the OLE object.

## Content

### Public Constructor
| Name | Description |
|------|-------------|
| `WOleObject.WOleObject(IWordDocument)` | Gets the type of the entity. |

### Public Properties
| Name | Description |
|------|-------------|
| `OleLinkType` | Gets the OLE link type (Embed or Link). |
| `OlePicture` | Gets the OLE picture. |
| `EntityType` | Gets the type of the entity. |
| `Container` | Gets the OLE container. |
| `OleStorageName` | Gets or sets the name of the OLE Object storage. |
| `LinkPath` | Gets or sets the link path. |
| `LinkType` | Gets the type of the OLE object. |
| `NativeData` | Gets the native data of embedded OLE object. |
| `PackageFileName` | Gets the name of the file embedded in the package (only if OleType is "Package"). |
| `ObjectType` | Gets or sets the type of the OLE object. |
| `DisplayAsIcon` | Gets or sets the value indicating whether the OLE object is displayed as an icon or content. |

### Example: Inserting an OLE Object in Disk to a Word Document
The following code example illustrates how to insert an OLE object in disk to a Word document.

---

## API Reference
### Class: WOleObject
#### Properties
- **`OleLinkType`**  
  Gets the OLE link type (Embed or Link).
  
- **`OlePicture`**  
  Gets the OLE picture.
  
- **`EntityType`**  
  Gets the type of the entity.
  
- **`Container`**  
  Gets the OLE container.
  
- **`OleStorageName`**  
  Gets or sets the name of the OLE Object storage.
  
- **`LinkPath`**  
  Gets or sets the link path.
  
- **`LinkType`**  
  Gets the type of the OLE object.
  
- **`NativeData`**  
  Gets the native data of embedded OLE object.
  
- **`PackageFileName`**  
  Gets the name of the file embedded in the package (only if OleType is "Package").
  
- **`ObjectType`**  
  Gets or sets the type of the OLE object.
  
- **`DisplayAsIcon`**  
  Gets or sets the value indicating whether the OLE object is displayed as an icon or content.

---

## Code Examples
The exact code for inserting an OLE object in disk to a Word document is not provided here. For complete implementation details, refer to the endpoint documentation or examples provided in the Syncfusion Winforms SDK.

---

## Cross References
See also:
- DocIO documentation for detailed usage of OLE objects in Word documents.

<!-- tags: [DocIO, OLE Object, WordDocument, MS Word, Syncfusion Winforms, 11.4.0.26] keywords: [DisplayAsIcon, Embed, Link, EntityType, OleStorageName, PackageFileName, NativeData, Object Types] -->
```