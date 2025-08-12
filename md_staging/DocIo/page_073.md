```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_073.jpeg
document_name: DocIo
page_number: 073
page_id: DocIo#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:04Z
fidelity: lossless
--> 

## Document Color

### Overview
- The Background class is responsible for managing background color and fill effects in Word documents.
- The fill effect type is determined by the Type property, which returns a value of the BackgroundType enum.

### Content

#### Background Fill Effect Types

The BackgroundType enum supports the following fill effects:

- **NoBackground**: No background fill effect.
- **Gradient**: Gradient fill effect.
- **Picture**: Background picture.
- **Texture**: Texture fill effect.
- **Color**: Color fill effect.

**Note:** Pattern fill effect is not supported.

#### Picture Property

The Picture property defines the picture to be used as the document background when the BackgroundType is set to BackgroundType.Picture. If the BackgroundType is BackgroundType.Texture, the picture will be used as a texture. Therefore, a background picture must be present in such cases.

#### Color Property

The Color property defines the color to be used as the document background when the BackgroundType is set to BackgroundType.Color.

#### Gradient Property

The Gradient property defines the gradient to be used as the document background when the BackgroundType is set to BackgroundType.Grad ed. The Gradient property returns an object of the BackgroundGradient class. For more details on the BackgroundGradient class, refer to the BackgroundGradient documentation.

#### Accessing Document Background

The WordDocument.Background property is used to access the DocIO document background. The Background property of WordDocument is automatically initialized. If there is no background in the default DocIO document, the Type property of the Background is set to NoBackground.

### Public Properties

| Name      | Description                 |
|-----------|-----------------------------|
| Color     | Gets or sets the background color. |
| Gradient  | Gets or sets the background gradient. |
| Picture   | Gets or sets the background picture. |
```