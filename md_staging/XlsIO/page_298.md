```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_298.jpeg
document_name: XlsIO
page_number: 298
page_id: XlsIO#page_298
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:14Z
fidelity: lossless
-->

## Setting an Image as an Object

The following set of code sample illustrates the condition when the property is set to any .png file image.

### Code Example

```csharp
oleObject1.Picture = Image.FromFile(@"image.png");
```

```vbnet
oleObject1.Picture = Image.FromFile("image.png").Picture = Image.FromFile("image.png")
```

### Output

Run the code. The following output is generated.

### Image Output

![Figure 101: Location](Assets/SampleImage.png)

Figure 101: Location

---

## Summary

- Describes how to set an image as an object in Excel using the XlsIO library.
- Includes C# and VB.NET code examples for setting an image.
- Demonstrates the output when the code is executed, showcasing the embedding of a .png image as an object in Excel.

---

## References

- [Syncfusion Website](https://www.syncfusion.com/)
- [XlsIO Documentation](https://help.syncfusion.com/presentation/xlsio/introduction)

---

<!-- tags: [Syncfusion, XlsIO, Excel, WinForms, Image, Object, Embedding] keywords: [setting image, object embedding, XlsIO, Excel, C#, VB.NET, code sample, output] -->
```