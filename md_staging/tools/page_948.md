```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_948.jpeg
document_name: tools
page_number: 948
page_id: tools#page_948
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:09Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Focuses on customizing the appearance of the GradientLabel control in Windows Forms.
- Explains how to customize the control's text appearance and background settings.
- Provides details on properties such as `DrawActiveWhenDisabled`, `BackgroundColor`, `Style`, `BackColor`, `ForeColor`, `PatternStyle`, and `GradientStyle`.

---

### DrawActiveWhenDisabled
The `DrawActiveWhenDisabled` property determines whether the text should be drawn as active when the control is disabled.

#### Description
- Gets or sets a value indicating whether the text should be drawn active when the control is disabled.
- The default value is set to `False`.

#### Code Examples
```csharp
this.gradientLabel1.DrawActiveWhenDisabled = true;
```

```vb
Me.gradientLabel1.DrawActiveWhenDisabled = True
```

---

### 3.5.10.2.3.3 Background Settings

#### Overview
This section illustrates the background settings of the GradientLabel control.

#### Description
The GradientLabel control's background can be customized using the `BackgroundColor` property and its related options, which are detailed below.

---

### GradientLabel Properties

| Property              | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `BackgroundColor`     | Gets or sets the background color and other styles.                      |
| `Style`              | Specifies the brush style. <br> Options: `Solid`, `Pattern`, `Gradient`. <br> Default value is `Gradient`. |
| `BackColor`          | Specifies the backcolor of the control.                                  |
| `ForeColor`          | Specifies the forecolor for any text or graphics in the control.         |
| `PatternStyle`       | Specifies the pattern style of the control.                             |
| `GradientStyle`      | Specifies the gradient style of the background.                          |

---

### API Reference (if applicable)
Not explicitly detailed in the current scope of the documentation.

---

### Code Examples (if applicable)
- **C# Example**:
  ```csharp
  this.gradientLabel1.DrawActiveWhenDisabled = true;
  this.gradientLabel1.Style = GradientLabelStyle.Gradient;
  this.gradientLabel1.BackColor = Color.LightBlue;
  this.gradientLabel1.ForeColor = Color.Black;
  this.gradientLabel1.PatternStyle = GradientLabelPatternStyle.Horizontal;
  this.gradientLabel1.GradientStyle = GradientLabelGradientStyle.Linear;
  ```

- **VB.NET Example**:
  ```vb
  Me.gradientLabel1.DrawActiveWhenDisabled = True
  Me.gradientLabel1.Style = GradientLabelStyle.Gradient
  Me.gradientLabel1.BackColor = Color.LightBlue
  Me.gradientLabel1.ForeColor = Color.Black
  Me.gradientLabel1.PatternStyle = GradientLabelPatternStyle.Horizontal
  Me.gradientLabel1.GradientStyle = GradientLabelGradientStyle.Linear
  ```

---

### Cross References
- For more information on the GradientLabel control and its properties, refer to the [Official Syncfusion Documentation](https://www.syncfusion.com/documentation/windowsforms).

---

<!-- tags: [windowsforms, gradientlabel, backgroundsettings, drawactivewhendisabled, properties] keywords: [gradientlabel, background settings, draw active when disabled, style, backcolor, forecolor, patternstyle, gradientstyle] -->
``` 
