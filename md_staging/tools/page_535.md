```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_535.jpeg
document_name: tools
page_number: 535
page_id: tools#page_535
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

**Note:** To know how to customize a color item, refer to the *Color Items* topic.

## 3.5.4.5.1.2.2 Color Items

### Customizing Color Items

Size of the color items can be set through the `ColorItemSize` property. The default width is 13, and the height is 13.

**Note:** The colors within the groups are clickable at design time, and you can change the color using the property grid as shown in the below image.

![Figure 323: Changing the Color using PropertyGrid](./assets/image.png)

### Figure 323: Changing the Color using PropertyGrid

#### C#
```csharp
this.colorPickerUIAdv1.ColorItemSize = new System.Drawing.Size(20, 20);
```

#### VB.NET
```vb
Me.colorPickerUIAdv1.ColorItemSize = New System.Drawing.Size(20, 20)
```

## API Reference

#### Properties
- `ColorItemSize`: Gets or sets the size of the color items in the Color Picker.

#### Returns: Type: `Size`
The size of the color items in the Color Picker.

#### Exceptions
- None

## Code Examples

#### C#
```csharp
this.colorPickerUIAdv1.ColorItemSize = new System.Drawing.Size(20, 20);
```

#### VB.NET
```vb
Me.colorPickerUIAdv1.ColorItemSize = New System.Drawing.Size(20, 20)
```

## See also
- *Color Items*
- `ColorPickerUIAdv`
<!-- tags: [Syncfusion Winforms, Color Picker, ColorItemSize] keywords: [Color Picker, ColorItemSize, Customizing Color Items, Design Time, Property Grid] -->
```