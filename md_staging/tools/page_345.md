```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_345.jpeg
document_name: tools
page_number: 345
page_id: tools#page_345
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:06:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

![Figure 156: Office Color Schemes for ButtonAdv Control](https://via.placeholder.com/300x400?text=Figure%20156:%20Office%20Color%20Schemes%20for%20ButtonAdv%20Control)

## Custom Colors

We can also apply custom colors to the ButtonAdv control by setting `Office2007ColorScheme` to `"Managed"` and specifying the custom color through the `ApplyManagedColors` method as follows.

### Code Examples

#### C#

```csharp
this.buttonAdv1.Office2007ColorScheme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.LightGreen);
```

#### VB.NET

```vbnet
Me.buttonAdv1.Office2007ColorScheme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(this, Color.LightGreen)
```

![Figure 157: CustomColor = "LightGreen"](https://via.placeholder.com/300x400?text=Figure%20157:%20CustomColor=%20%22LightGreen%22)

## See Also

- [Button Types, Image Settings](Button Types, Image Settings)
- [3.5.2.1.3.1.4 Foreground Settings](3.5.2.1.3.1.4 Foreground Settings)

```html
<!-- tags: [Syncfusion Winforms, ButtonAdv, Office2007Theme, Office2007Colors, Managed, ApplyManagedColors, Custom Colors, C#, VB.NET, Foreground Settings] keywords: [ButtonAdv control, Office color schemes, Custom colors, Managed theme, ApplyManagedColors method, LightGreen, Foreground settings] -->
```