```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_439.jpeg
document_name: grid
page_number: 439
page_id: grid#page_439
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:55Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

![Figure 164: Vertical Lines hidden in Grid](grid#page_439#figure-vertical-lines)

### Overview
- **ColHeaders**: Specifies whether column headers are to be displayed. Default value is set to `true`.

### Content
The following code examples can be used to set this property:

1. **Using C\#**
   ```csharp
   // Hiding the column headers.
   this.gridControl1.Properties.ColHeaders = false;
   ```

2. **Using VB.NET**
   ```vb
   ' Hiding the column headers.
   Me.gridControl1.Properties.ColHeaders = False
   ```

The following illustration shows how the Grid in "Figure 1" is transformed when the `Properties.ColHeaders` property is set to `false`.

## API Reference
### WinForms-specific conventions:
- **Properties**:
  - `ColHeaders`: Gets or sets whether column headers are displayed.
    - Type: `bool`
    - Description: Indicates whether column headers are visible in the Grid control.
    - Default: `true`
    - Parameters:
      - None

### Code Examples
- **C\#**
  ```csharp
  this.gridControl1.Properties.ColHeaders = false;
  ```
- **VB.NET**
  ```vb
  Me.gridControl1.Properties.ColHeaders = False
  ```

## Cross References
See also:
- Grid control properties
- Grid display styling
- Column header visibility

<!-- tags: [WinForms, Grid, ColHeaders, Property, Visibility, C#, VB.NET, syncfusion-sdk, Version:11.4.0.26] keywords: [Grid, column headers, display, property, visibility, C#, Visual Basic.NET, Syncfusion, essential grid] -->
```