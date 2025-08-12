```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_052.jpeg
document_name: tools
page_number: 052
page_id: tools#page_052
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:17:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
[VB]
Dim carousel1 As Syncfusion.Windows.Forms.Tools.Carousel
Me.carousel1 = New Syncfusion.Windows.Forms.Tools.Carousel()
Me.Controls.Add(carousel1)
```

## 3.2.3 Features

This section provides details regarding the features supported by the Carousel control and the properties used to add them to an application.

### 3.2.3.1 Path Support

The Carousel control supports arranging items in the following paths:

- Default (elliptical)
- Orbital
- Oval
- Linear

#### 3.2.3.1.1 Default

Items will be arranged in a normal elliptical path.

**C#**
```csharp
this.carousel1.CarouselPath = CarouselPath.Default;
```

**VB**
```vb
Me.carousel1.CarouselPath = CarouselPath.Default
```

#### 3.2.3.1.2 Orbital

Items will be arranged like an orbital curve.

**C#**
```csharp
this.carousel1.CarouselPath = CarouselPath.Orbital;
```

**VB**
```vb
Me.carousel1.CarouselPath = CarouselPath.Orbital
```
```


<!-- tags: [syncfusion, windows-forms, carousel, features, path-support, default, orbital, programming] keywords: [syncfusion windows forms, carousel control, item arrangement, default path, orbital path, programming examples] -->
