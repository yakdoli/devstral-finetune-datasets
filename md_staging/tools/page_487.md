```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_487.jpeg
document_name: tools
page_number: 487
page_id: tools#page_487
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:16:26Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Provides details about the Office2007Theme, which indicates the office color scheme used when the Style is set to Office2007.
- Offers examples for setting the Office2007 style for a control in both C# and VB.NET.

### Content

| Placeholder for Image or Section Title (language: Office2007Theme) | Availability Options |
| --- | --- |
| - Office2007Theme |
|  | |
| Indicates the office color scheme used, when Style is set to Office2007. |

#### Setting Office2007 Style

##### [C#]
```csharp
// Sample for setting Office2007 style for the control
this.dateTimePickerAdv1.Style =
Syncfusion.Windows.Forms.VisualStyle.Office2007;
```

##### [VB.NET]
```vb
' Sample for setting Office2007 style for the control
Me.dateTimePickerAdv1.Style =
Syncfusion.Windows.Forms.VisualStyle.Office2007
```

#### Style Examples

The following images showcase the different styles of the control:

- **Default**
- **Office 2003**
- **VS 2005**
- **Office XP**
- **Office 2007**

Each style has a distinct visual appearance, as demonstrated below:

![Default](default_image.png)
![Office 2003](office2003_image.png)
![VS 2005](vs2005_image.png)
![Office XP](officeXP_image.png)
![Office 2007](office2007_image.png)

Each style variation is depicted with the corresponding calendar and date selection interface, highlighting the thematic differences in the visuals.

## API Reference

### Namespace: Syncfusion.Windows.Forms

#### Properties

- **Style**
  - Type: `VisualStyle`
  - Description: Specifies the visual style of the control.
  - Default: `VisualStyle.Default`

#### Examples

- **C#**
  ```csharp
  this.dateTimePickerAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2007;
  ```

- **VB.NET**
  ```vb
  Me.dateTimePickerAdv1.Style = Syncfusion.Windows.Forms.VisualStyle.Office2007
  ```

## Code Examples

- **C#**
  ```csharp
  // Example for setting Office2007 style
  this.dateTimePickerAdv1.Style =
  Syncfusion.Windows.Forms.VisualStyle.Office2007;
  ```

- **VB.NET**
  ```vb
  ' Example for setting Office2007 style
  Me.dateTimePickerAdv1.Style =
  Syncfusion.Windows.Forms.VisualStyle.Office2007
  ```

<!-- tags: [Syncfusion, WinForms, DateTimePickerAdv, OfficeThemes, VisualStyles] keywords: [Office2007, VisualStyle, Office2003, VS2005, OfficeXP, DateTimePickerAdv, OfficeThemes, C#, VB.NET] -->
```