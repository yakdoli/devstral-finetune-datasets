```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_401.jpeg
document_name: tools
page_number: 401
page_id: tools#page_401
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:10:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Calculator Control Color Schemes

### Overview
- Supports all three OfficeColorSchemes.
- Default to blue when ButtonStyle is set to Office2007 style.
- Can be modified using the `Office2007Theme` property.

### Applying OfficeColorSchemes

#### Setting Office2007Theme to Silver

##### C#
```csharp
this.calculatorControl1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Silver;
```

##### VB.NET
```vb
Me.calculatorControl1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Silver
```

#### OfficeColorSchemes Applied to Calculator Control
![Figure 202: OfficeColor Schemes applied to Calculator Control](https://i.imgur.com/QeRp8E3.png)
*Figure 202: OfficeColor Schemes applied to Calculator Control*

### Custom Colors

#### Overview
- Custom colors can be applied to the Calculator control by setting `Office2007Theme` to "Managed."
- Specify custom color using the `ApplyManagedColors` method.

#### Applying Custom Colors

##### C#
```csharp
this.calculatorControl1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Navy);
```

##### VB.NET
```vb
' [VB.NET] implementation placeholder needed.
```

## API Reference

### Properties
- **Office2007Theme**
  - Type: `Office2007Theme`
  - Description: Specifies the color theme for the Calculator control.
  - Possible Values:
    - Blue
    - Silver
    - Black
    - Managed (for custom colors)

### Methods
- **ApplyManagedColors**
  - Parameters:
    - `Control`. Type: `Control` - The control to apply the theme to.
    - `Color`. Type: `Color` - The custom color to apply.
  - Description: Applies a custom color theme to the specified control.

### Code Examples

- **Changing Theme to Silver (C#)**
  ```csharp
  this.calculatorControl1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Silver;
  ```

- **Applying Custom Color (C#)**
  ```csharp
  this.calculatorControl1.Office2007Theme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
  Office2007Colors.ApplyManagedColors(this, Color.Navy);
  ```

<!-- tags: [calculator, color schemes, theming, office2007, custom colors] keywords: [Syncfusion, Windows Forms, Calculator, OfficeColorSchemes, Office2007Theme, ApplyManagedColors, custom color] -->
```