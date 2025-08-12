```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_074.jpeg
document_name: DocIo
page_number: 074
page_id: DocIo#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:08Z
fidelity: lossless
-->

## Background Class Usage Example

### Summary
- Demonstrates how to use the `Background` class to manipulate the background properties of a Word document.
- Includes code examples for copying background styles between two documents.

### Content

#### Background Class Example

The following example illustrates how to use the `Background` class.

```csharp
[C#]

IWordDocument doc1 = new WordDocument();
doc1.Open("Background.doc");
IWordDocument doc2 = new WordDocument();
doc2.EnsureMinimal();

switch (doc1.Background.Type)
{
    case BackgroundType.Gradient:
        doc2.Background.Gradient = doc1.Background.Gradient.Clone();
        break;

    case BackgroundType.Picture:
    case BackgroundType.Texture:
        doc2.Background.Picture = doc1.Background.Picture;
        break;

    case BackgroundType.Color:
        doc2.Background.Color = doc1.Background.Color;
        break;

    default:
        break;
}

doc2.Background.Type = doc1.Background.Type;
doc1.Background.Type = BackgroundType.Color;
doc1.Background.Color = Color.Red;

doc1.Save("Background.doc");
doc2.Save("BackgroundNew.doc");
```

### Explanation
- **Opening an Existing Document**: `doc1` is opened from the file `"Background.doc"`.
- **Creating a New Document**: `doc2` is created as a new and minimal document.
- **Copying Background Style**:
  - The `switch` statement checks the type of background in `doc1` and copies the corresponding style to `doc2`.
  - Different background types (Gradient, Picture/Texture, Color) are handled with specific assignments.
- **Setting Background Color**: `doc1` is explicitly set to have a solid red color as its background.
- **Saving the Documents**: Both `doc1` and `doc2` are saved with their respective modifications.

---

<!-- tags: [DocIO, Background class, WordDocument, Switch statement, Background types, Color, Picture, Gradient, Save, DocIO#page_074] keywords: [background, document, WordDocument, switch statement, gradient, picture, texture, color, save, example] -->
```