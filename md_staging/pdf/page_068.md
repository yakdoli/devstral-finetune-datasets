```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en 
source_filename: page_068.jpeg
document_name: pdf
page_number: 068
page_id: pdf#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:27:35Z
fidelity: lossless
-->

## Content

### Methods

| Method          | Description                                                    |
|-----------------|----------------------------------------------------------------|
| `GetContent`    | Gets the content of the page in form of a PDF template.       |
| `OnBeginSave`   | Raises BeginSave event.                                       |
| `ResetProgress` | Resets the progress.                                          |
| `SetProgress`   | Sets the progress.                                            |
| `SetSection`    | Sets parent section to the page.                              |

### Properties

| Name                 | Description                                               |
|----------------------|-----------------------------------------------------------|
| `Annotations`        | Gets a collection of annotations of the page.             |
| `Contents`           | Gets array of page's content.                             |
| `DefaultLayer`       | Gets the default layer of the page.                       |
| `DefaultLayerIndex`  | Gets or sets index of the default layer.                 |
| `Dictionary`         | Gets the page dictionary.                                 |
| `Document`           | Gets current document.                                    |
| `Graphics`           | Gets the graphics of the DefaultLayer.                    |
| `Layers`             | Gets the collection of the page's layers.                 |
| `Orientation`        | Gets the page orientation.                                |
| `Rotation`           | Gets the page rotation.                                   |
| `Section`            | Gets the parent section of the page.                      |
| `Size`               | Gets the size of the page.                                |

### Events

| Name         | Description                                     |
|--------------|-------------------------------------------------|
| `BeginSave`  | Raises before the page saves.                   |

## API Reference

### Properties

- **Annotations**: Gets a collection of annotations of the page.
- **Contents**: Gets array of page's content.
- **DefaultLayer**: Gets the default layer of the page.
- **DefaultLayerIndex**: Gets or sets index of the default layer.
- **Dictionary**: Gets the page dictionary.
- **Document**: Gets current document.
- **Graphics**: Gets the graphics of the DefaultLayer.
- **Layers**: Gets the collection of the page's layers.
- **Orientation**: Gets the page orientation.
- **Rotation**: Gets the page rotation.
- **Section**: Gets the parent section of the page.
- **Size**: Gets the size of the page.

### Events

- **BeginSave**: Raises before the page saves.

## Code Examples

```csharp
// Example using GetContent method
PdfContentBlock contentBlock = page.GetContent();
```

<!-- tags: [Syncfusion, Winforms, PDF, page, methods, properties, events] keywords: [annotations, contents, defaultLayer, dictionary, document, graphic, layers, orientation, rotation, section, size, beginSave] -->
```