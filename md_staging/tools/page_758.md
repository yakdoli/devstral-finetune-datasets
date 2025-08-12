```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_758.jpeg
document_name: tools
page_number: 758
page_id: tools#page_758
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the application of Themes to the IntegerTextBox control.
- Explains the ThemesEnabled property and how it interacts with BorderStyle.
- Provides code examples in C# and VB.NET for enabling Themes.
- Lists events related to the IntegerTextBox control and their descriptions.

## Content

### 3.5.8.4.3.9 Applying Themes

Themes can be applied to the IntegerTextBox control using the property given below.

| IntegerTextBox Property     | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| ThemesEnabled               | Specifies whether or not to use XP themes, when BorderStyle property is set to 'Fixed3D'. |

#### Note: Refer Border Settings topic to know about the BorderStyle property.

```csharp
this.integerTextBox1.ThemesEnabled = true;
```

```vb
Me.integerTextBox1.ThemesEnabled = true
```

![Figure 480: Themes Applied to IntegerTextBox Control](./image_name.png)

A sample which demonstrates the ThemesEnabled property of the IntegerTextBox control is available in the below sample installation path.

#### Sample installation path:
```
..My Documents\Syncfusion\EssentialStudio\<Version Number>\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

### 3.5.8.4.4 IntegerTextBox Events

The list of events and a detailed explanation about each of them is given in the following sections.

| IntegerTextBox Events       | Description                                                                |
|-----------------------------|----------------------------------------------------------------------------|
| BindableValueChanged        | This event occurs when the BindableValue property is changed.             |

## API Reference

### Properties
- **ThemesEnabled**
  - Specifies whether or not to use XP themes, when BorderStyle property is set to 'Fixed3D'.
  - Type: `bool`

### Events
- **BindableValueChanged**
  - Occurs when the BindableValue property is changed.
  - Signature: `public event EventHandler BindableValueChanged`

## Code Examples

#### Enabling Themes in C#

```csharp
this.integerTextBox1.ThemesEnabled = true;
```

#### Enabling Themes in VB.NET

```vb
Me.integerTextBox1.ThemesEnabled = true
```

## Page-level Navigation/TOC
- **3.5.8.4.3.9 Applying Themes**
- **3.5.8.4.4 IntegerTextBox Events**

## Cross References
See also:
- Border Settings topic
- Sample installation path

<!-- tags: [Syncfusion Winforms, IntegerTextBox, Themes, BorderStyle, Events, WinForms, version:11.4.0.26] keywords: [ThemesEnabled, BorderStyle, Fixed3D, BindableValueChanged, integerTextBox, syncfusion, windows forms, control, property, event] -->
```