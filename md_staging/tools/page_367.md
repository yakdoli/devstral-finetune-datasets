```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_367.jpeg
document_name: tools
page_number: 367
page_id: tools#page_367
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:17Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Button types and styles for ButtonEdit control similar to ButtonAdv control.
- Setting the button types using ButtonEditChildButton1.ButtonType property.
- Configuring border styles through the BorderStyleAdv property.

## Content

### Button Types

The button types for ButtonEdit control are similar to that of ButtonAdv control. Refer [Button Types](Button Types) topic for details.

Use **ButtonEditChildButton1.ButtonType** property for setting the button types of the child buttons.

### Border Styles

The border styles for the child buttons can be set through **BorderStyleAdv** property.

| Property          | Description                                                                                           |
|-------------------|-------------------------------------------------------------------------------------------------------|
| **BorderStyleAdv** | Specifies the border style for child buttons of the ButtonEdit control. The styles are:      |
|                   | - None,                                                                                               |
|                   | - Default,                                                                                            |
|                   | - Dashed,                                                                                            |
|                   | - Dotted,                                                                                            |
|                   | - Inset,                                                                                              |
|                   | - Outset,                                                                                            |
|                   | - Solid,                                                                                              |
|                   | - Bump,                                                                                               |
|                   | - Etched,                                                                                            |
|                   | - Flat,                                                                                               |
|                   | - Raised,                                                                                            |
|                   | - RaisedInner,                                                                                        |
|                   | - RaisedOuter,                                                                                       |
|                   | - Sunken,                                                                                            |
|                   | - SunkenInner,                                                                                       |
|                   | - SunkenOuter.                                                                                       |

## Code Examples

Example of setting the button type and border style:

```csharp
// Setting the button type of the child button
ButtonEditChildButton1.ButtonType = ButtonType.RoundRectangle;

// Setting the border style of the child button
ButtonEditChildButton1.BorderStyleAdv = BorderStyleAdv.Dashed;
```

## Cross References

See also: [Button Types](Button Types) for more details on button types.

<!-- tags: [winforms, buttonedit, buttonadv, buttontypes, borderstyles] keywords: [syncfusion, windows forms, buttonedit, child button, button type, border style] -->
```