```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_365.jpeg
document_name: tools
page_number: 365
page_id: tools#page_365
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:46Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

### Size Settings

We can specify the maximum and minimum size for the ButtonEdit control using **MaximumSize** and **MinimumSize** properties.

| Properties          | Description                       |
|---------------------|-----------------------------------|
| **MaximumSize**     | Sets the maximum size of the ButtonEdit control. |
| **MinimumSize**     | Sets the minimum size of the ButtonEdit control. |

*Note: The Border styles of the child buttons can be controlled using ButtonEditChildButton.BorderStyleAdv property. SeeSee [Button Types and Border Styles](#) topic for details.*

## Foreground Settings

This section discusses the foreground settings available for the ButtonEdit control.

### Font and ForeColor

The font style and the forecolor for the ButtonEdit text can be set using **Font** and **ForeColor** properties. These property settings can be overridden by **TextBox.Font** and **TextBox.ForeColor** respectively.

#### Example: Setting Font and ForeColor (C#)

```csharp
this.buttonEdit3.Font = new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular);
this.buttonEdit3.ForeColor = Color.SteelBlue;
```

#### Example: Setting Font and ForeColor (VB.NET)

```vb
Me.buttonEdit3.Font = New System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Regular)
```

*See Also: [Foreground Settings](#)*

**Figure 175: FlatBorderColor="Red"**

*Note: The Border styles of the child buttons can be controlled using ButtonEditChildButton.BorderStyleAdv property. SeeSee [Button Types and Border Styles](#) topic for details.*

* * *

© 2013 Syncfusion. All rights reserved.
* * *

<!-- tags: [Windows Forms, ButtonEdit, SizeSettings, ForegroundSettings, Font, ForeColor] keywords: [ButtonEdit, MaximumSize, MinimumSize, Font, ForeColor, Foreground Settings, C#, VB.NET, Syncfusion Winforms, version, 11.4.0.26] -->
```