```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_094.jpeg
document_name: tools
page_number: 094
page_id: tools#page_094
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the various themes supported by Windows Forms UI controls.
- Provides code examples in C# and VB.NET for implementing Office 2007 themes.
- Explains the Office 2010 styles and their application in Windows Forms applications.

## Content

### Themes

#### Office 2007 Themes
The Windows Forms UI controls support themes similar to those found in Office 2007. These include:

- Blue
- Silver
- Black
- Managed

Here is an example of how to set the Office 2007 theme in both C# and VB.NET:

```csharp
this.commandBarController1.Style =
    Syncfusion.Windows.Forms.VisualStudio.Office2007Outlook;
this.commandBarController1.Office2007Theme =
    Syncfusion.Windows.Forms.Office2007ColorScheme.Blue;
```

```vb.NET
Me.commandBarController1.Style =
    Syncfusion.Windows.Forms.VisualStudio.Office2007Outlook
Me.commandBarController1.Office2007Theme =
    Syncfusion.Windows.Forms.Office2007ColorScheme.Blue
```

**Figure 37: Office 2007 Themes**

![Office 2007 Themes](https://example.com/office2007_themes_image.png)

**Note:** The `Style` property must be set to 'Office2007' or 'Office2007Outlook' to get the Office 2007 theme effect.

#### Office 2010 Styles
This feature provides Office 2010-like themes for Windows Forms UI controls. These themes add the Office 2010-like look and feel to your application. This feature enables you to easily apply uniform style to all of the child controls in the application. Windows Forms UI controls support three themes found in Office 2010. They are:

- Blue
- Black
- Silver

There is also a user-managed theme called Managed.

## References

- For more information on themes, refer to the official Syncfusion documentation.
- Example images and additional styles can be viewed in the Documentation Center.

## Page-level Navigation/TOC
- **3.3.3.8.4 Office 2010 Styles**

## Code Examples
- C# and VB.NET examples for setting Office 2007 themes are provided above.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, themes, Office2007, Office2010, C#, VB.NET] keywords: [themes, Office 2007, Office 2010, style settings, user-managed theme, managed theme, commandBarController, Windows Forms UI controls] -->
```