```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_440.jpeg
document_name: grid
page_number: 440
page_id: grid#page_440
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

The image illustrates a Grid without Column Headers, as shown below:

| 1 | Row1:Col | Row1:Col | Row1:Col | Row1:Col | Row1:Col |
| --- | --- | --- | --- | --- | --- |
| 2 | Row2:Col | Row2:Col | Row2:Col | Row2:Col | Row2:Col |
| 3 | Row3:Col | Row3:Col | Row3:Col | Row3:Col | Row3:Col |
| 4 | Row4:Col | Row4:Col | Row4:Col | Row4:Col | Row4:Col |
| 5 | Row5:Col | Row5:Col | Row5:Col | Row5:Col | Row5:Col |
| 6 | Row6:Col | Row6:Col | Row6:Col | Row6:Col | Row6:Col |
| 7 | Row7:Col | Row7:Col | Row7:Col | Row7:Col | Row7:Col |
| 8 | Row8:Col | Row8:Col | Row8:Col | Row8:Col | Row8:Col |
| 9 | Row9:Col | Row9:Col | Row9:Col | Row9:Col | Row9:Col |
| 10 | Row10:C | Row10:C | Row10:C | Row10:C | Row10:C |

### Figure 165: Column Headers hidden in Grid

- **RowHeaders**: Specifies whether row headers are to be displayed. Default value is set to `true`.

The following code examples can be used to set this property:

#### 1. Using C#

```csharp
// Hiding the row headers.
this.gridControl1.Properties.RowHeaders = false;
```

#### 2. Using VB.NET

```vb
' Hiding the row headers.
Me.gridControl1.Properties.RowHeaders = False
```

The following illustration shows how the Grid in "Figure 1" is transformed when the `Properties.RowHeaders` property is set to false.

## API Reference

### Properties
- **RowHeaders**: 
  - **Type**: `bool`
  - **Description**: Specifies whether row headers are to be displayed.
  - **Default**: `true`

### Methods

#### `SetRowHeadersVisibility(bool value)`
- **Parameters**:
  - `value`: `bool` - Indicates whether to display row headers.
- **Description**: Sets the visibility of row headers in the grid.

### Events
- **None**

## Code Examples

#### Example: Hiding Row Headers

```csharp
gridControl1.Properties.RowHeaders = false;
```

```vb
gridControl1.Properties.RowHeaders = False
```

## Cross References

- See also: 
  - [Grid Properties Documentation](#grid-properties)
  - [Customizing Grid Appearance](#customizing-grid-appearance)

<!-- tags: [Syncfusion, Windows Forms, Grid, RowHeaders, Properties] keywords: [Syncfusion, Essential Grid, Windows Forms, RowHeaders, Properties, C#, VB.NET, Grid Control, Grid Appearance] -->
```