```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: tools
page_number: 090
page_id: tools#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:44Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Row Index and Offset

The index and offset settings of rows can be customized using the properties given below.

| CommandBar Property | Description |
|----------------------|-------------|
| RowIndex            | Gets / sets the index of the row or column for the CommandBar. |
| RowOffset           | Gets / sets the linear offset of the CommandBar within a row. |

#### Code Examples

[C#]

```csharp
this.commandBar1.RowIndex = 1;
this.commandBar1.RowOffset = 1;
```

[VB.NET]

```vb
Me.commandBar1.RowIndex = 0
Me.commandBar1.RowOffset = 0
```

### Visible / Hidden CommandBar

The CommandBar control can be hidden using the property given below.

| CommandBar Property | Description |
|----------------------|-------------|
| Visible             | Determines whether the control is visible or hidden. The default value is set to 'True'. |

#### Code Examples

[C#]

```csharp
this.commandBar1.Visible = true;
```

[VB.NET]

```vb
Me.commandBar1.Visible = True
```

### RightToLeft

The elements of the CommandBarController can be aligned from right to left and vice versa using the property given below.

---

## API Reference

### Properties

- **RowIndex**: Gets / sets the index of the row or column for the CommandBar.
- **RowOffset**: Gets / sets the linear offset of the CommandBar within a row.
- **Visible**: Determines whether the control is visible or hidden. The default value is set to 'True'.

---

## Code Examples

#### RowIndex and RowOffset

[C#]

```csharp
this.commandBar1.RowIndex = 1;
this.commandBar1.RowOffset = 1;
```

[VB.NET]

```vb
Me.commandBar1.RowIndex = 0
Me.commandBar1.RowOffset = 0
```

#### Visible CommandBar

[C#]

```csharp
this.commandBar1.Visible = true;
```

[VB.NET]

```vb
Me.commandBar1.Visible = True
```

---

<!-- tags: [syncfusion, windowsforms, tools, rowindex, rowoffset, visible, righttoleft, commandbar] keywords: [RowIndex, RowOffset, Visible, RightToLeft, CommandBar, customization, alignment, visibility, Windows Forms] -->
```