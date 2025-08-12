<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_299.jpeg
document_name: XlsIO
page_number: 299
page_id: XlsIO#page_299
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:08:30Z
fidelity: lossless
-->

# Essential XlsIO

### Setting Required Shape as an Object

The following set of code sample illustrates the condition when the property is set to any `.png` file image.

#### WinForms-specific conventions

The code snippets below demonstrate how to set an object shape to a `.png` file image.

```csharp
oleObject1.Shape = sheet.Pictures[0];
```

```vb.net
oleObject1.Shape = sheet.Pictures(0)
```

**Run the code. The following output is generated:**

### Figure 102: Word Icon Image

![Example Image](https://unclear-image-url.com)

---

## API Reference

### WinForms-specific conventions

- **oleObject.Shape**:
  - **Type**: Shape
  - **Description**: Represents the shape of the embedded object.

## Code Examples

- **C# Example**:
  ```csharp
  oleObject1.Shape = sheet.Pictures[0];
  ```

- **VB.NET Example**:
  ```vb.net
  oleObject1.Shape = sheet.Pictures(0)
  ```

## Page-level Navigation/TOC (if applicable)

- [Setting Required Shape as an Object]
  - [C# Example]
  - [VB.NET Example]

## Cross References

### See also:

- [XlsIO Documentation](https://unclear-url.com)
- [Syncfusion Developer Center](https://unclear-url.com)

---

<!-- tags: [xlsio, essentialxlsio, winforms, objectshape, csharp, vb.net] keywords: [oleobject, shape, pictures, property, .png, embedded object] -->