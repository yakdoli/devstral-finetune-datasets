```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_576.jpeg
document_name: tools
page_number: 576
page_id: tools#page_576
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:51Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- A section discussing the advanced ComboBox (`ComboBoxAdv`) control in Windows Forms.
- Topics include databinding with a `Data Table` and appearance settings, specifically border styles.

## Content

```csharp
Me.comboBoxAdv1.DisplayMember = "place"
```

### Figure 355: ComboBoxAdv databound with Data Table

![](./image.png)

#### 3.5.5.2.3.4 ComboBoxAdv Appearance
This section discusses the below topics.

##### 3.5.5.2.3.4.1 Border Styles
This section discusses the border settings for the `ComboBoxAdv` control.

| ComboBoxAdv Properties | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| **Border3DStyle**       | Specifies the 3D `BorderStyle` for the control. <br> The options are, <br> `RaisedInner`, <br> `RaisedOuter`, <br> `Raised`, <br> `Sunken`, (Default) <br> `SunkenInner`, <br> `SunkenOuter`, <br> `Flat`, <br> `Bump and <br>Adjust`. <br> <br> `FlatStyle` should be set to `"Standard"` to make this property setting effective. |
| **BorderSides**         | Specifies the `BorderSides` of the control.                              |

## API Reference

### ComboBoxAdv Properties
#### Border3DStyle
- Specifies the 3D `BorderStyle` for the control.
- Options include:
  - `RaisedInner`
  - `RaisedOuter`
  - `Raised`
  - `Sunken` (Default)
  - `SunkenInner`
  - `SunkenOuter`
  - `Flat`
  - `Bump and Adjust`
- `FlatStyle` should be set to `"Standard"` to make this setting effective.

#### BorderSides
- Specifies the `BorderSides` of the control.

## Code Examples
```csharp
Me.comboBoxAdv1.DisplayMember = "place"
```

<!-- tags: [ComboBoxAdv, Windows Forms, Border Styles, Data Binding, UI Design] keywords: [ComboBoxAdv, DisplayMember, Border3DStyle, BorderSides, Data Table, Appearance, Styles] -->
```