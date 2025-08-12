```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_423.jpeg
document_name: tools
page_number: 423
page_id: tools#page_423
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:12:25Z
fidelity: lossless
-->

## Overview
- The page explains the customization options for the header portion of the MonthCalendarAdv control in Syncfusion Winforms.
- It details the properties for setting a gradient background, including descriptions and sample code in C#.
- The section focuses on configuring the Header settings with detailed explanations and property mappings.

---

## Content

### Header Settings

#### 3.5.3.1.4.2.1.1 Header Settings

This section will walk you through the different properties used to customize the header portion of the MonthCalendarAdv control.

#### Gradient Background

Gradient background can be set for the header using the below properties.

| MonthCalendarAdv Properties          | Description                                                                                                         |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| HeadGradient                          | Specifies whether the header can show a gradient background.                                                    |
| HeaderStartColor                      | Sets the start color of the header gradient when HeaderGradient property is true.                               |
| HeaderEndColor                        | Sets the end color of the header gradient when HeaderGradient property is true.                                 |
| HeaderVerticalGradient                | When HeadGradient property is set to true, vertical gradient style will be applied to the header, by default.<br>To change it to horizontal gradient style, set this property to false. |

---

#### Code Examples

```csharp
this.monthCalendarAdv1.HeadGradient = true;
this.monthCalendarAdv1.HeaderVerticalGradient = true;
this.monthCalendarAdv1.HeaderEndColor = System.Drawing.Color.SteelBlue;
this.monthCalendarAdv1.HeaderStartColor = System.Drawing.Color.AliceBlue;
```

---

## API Reference (if applicable)
- **Properties:**
  - `HeadGradient`: Specifies whether the header can show a gradient background.
  - `HeaderStartColor`: Sets the start color of the header gradient.
  - `HeaderEndColor`: Sets the end color of the header gradient.
  - `HeaderVerticalGradient`: Specifies whether the gradient style should be vertical or horizontal.

---

## Image Caption
**Figure 221:** `GridBackColor = "FloralWhite"; GridLines = "Dashed"`

---

### Notes
- The gradient background for the header can be customized using the properties listed above.
- Detailed C# code examples are provided to demonstrate the usage of these properties.

---

### References
- See also: MonthCalendarAdv control documentation for additional properties and methods.

---

<!-- tags: Syncfusion, Winforms, MonthCalendarAdv, Header Settings, Gradient Background, C# Code Examples, Property Settings -->
``` 
