```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_347.jpeg
document_name: tools
page_number: 347
page_id: tools#page_347
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:51Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the customization of ButtonAdv controls in a Windows Forms application.
- Covers both C# and VB.NET implementations for setting font, foreground color, text alignment, and text/image relation.
- Explains the use of Smart Tag features for easier property setting at design time.

## Content

### Setting Foreground Settings for ButtonAdv

```csharp
this.buttonAdv1.Font = new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular);
this.buttonAdv1.ForeColor = System.Drawing.Color.White;
```

```vb
Me.buttonAdv4.Text = "Image above Text"
Me.buttonAdv4.TextAlign = System.Drawing.ContentAlignment.BottomCenter
Me.buttonAdv4.TextImageRelation = TextImageRelation.ImageAboveText

Me.buttonAdv1.Font = New System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular)
Me.buttonAdv1.ForeColor = System.Drawing.Color.White
```

![ButtonAdv with Foreground Settings](image_url)

**Figure 158: ButtonAdv with Foreground Settings**

#### Design Time Features

**ButtonAdv control has Smart Tag, which lets you set the properties easily.**

### Smart Tag Options
- Provides quick access to essential properties through a dropdown menu.
- Streamlines the setup process by offering commonly used settings directly.
- Enhances productivity by reducing the need to navigate through the Properties window.

## API Reference

### Properties
- **Font**: Sets the font of the button text.
  - **Type**: `System.Drawing.Font`
  - **Default**: `null`
- **ForeColor**: Sets the foreground color of the button text.
  - **Type**: `System.Drawing.Color`
  - **Default**: `System.Drawing.SystemColors.ControlText`
- **TextAlign**: Sets the alignment of the button text.
  - **Type**: `System.Drawing.ContentAlignment`
  - **Default**: `System.Drawing.ContentAlignment.MiddleCenter`
- **TextImageRelation**: Sets the relation between text and image.
  - **Type**: `System.Windows.Forms.TextImageRelation`
  - **Default**: `System.Windows.Forms.TextImageRelation.Overlay`

## Code Examples

### C# Example

```csharp
// Setting text, alignment, and image relation
this.buttonAdv1.Text = "Image above Text";
this.buttonAdv1.TextAlign = System.Drawing.ContentAlignment.BottomCenter;
this.buttonAdv1.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText;

// Setting font and foreground color
this.buttonAdv1.Font = new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular);
this.buttonAdv1.ForeColor = System.Drawing.Color.White;
```

### VB.NET Example

```vb
' Setting text, alignment, and image relation
Me.buttonAdv1.Text = "Image above Text"
Me.buttonAdv1.TextAlign = System.Drawing.ContentAlignment.BottomCenter
Me.buttonAdv1.TextImageRelation = System.Windows.Forms.TextImageRelation.ImageAboveText

' Setting font and foreground color
Me.buttonAdv1.Font = New System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular)
Me.buttonAdv1.ForeColor = System.Drawing.Color.White
```

## Cross References

- For more information on ButtonAdv properties, refer to the [Syncfusion WinForms documentation](documentation_url).
- For additional customization techniques, see the related topics section at the end of this chapter.

<!-- tags: [Syncfusion WinForms, ButtonAdv, Smart Tag, Foreground Settings, C#, VB.NET] keywords: [ButtonAdv, Font, ForeColor, TextAlign, TextImageRelation, Design Time Features, Smart Tag, C#, VB.NET] -->
```
