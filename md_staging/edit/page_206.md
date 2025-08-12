```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_206.jpeg
document_name: edit
page_number: 206
page_id: edit#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:43Z
fidelity: lossless
-->

### Essential Edit for Windows Forms

#### Figure: Edit Control using Windows XP Themes

```markdown
Figure 64: Edit Control using Windows XP Themes
```

A sample based on XP Themes is available in the below sample installation path.

```bash
..\My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Edit.Windows\Samples\2.0\Appearance\XPThemesDemo
```

### 4.9.1.4 Border Style

The border style for the Edit Control can be set by using the below given property.

| Edit Control Property | Description |
|-----------------------|-------------|
| `BorderStyle`        | Gets/sets the border style of the control. The options provided are as follows:<br>- `FixedSingle`<br>- `Fixed3D`<br>- `None` |

## API Reference (if applicable)

- **Namespace**: Syncfusion.Windows.Forms
- **Class**: EditControl
- **Property**:
  - **`BorderStyle`** (Type: `BorderStyle`)
    - **Description**: Gets or sets the border style of the control.
    - **Options**:
      - `FixedSingle`
      - `Fixed3D`
      - `None`
    - **Default**: `FixedSingle`
    - **Required**: No

## Code Examples

### Example: Setting the BorderStyle Property

```csharp
using Syncfusion.Windows.Forms;

EditControl editControl = new EditControl();
editControl.BorderStyle = BorderStyle.None;
```

## Page-level Navigation/TOC (if applicable)

- [ ] 4.9.1.4 Border Style

## Cross References

- See also: XP Themes, Border Style, Edit Control

<!-- tags: [product: Syncfusion Winforms, module: Edit Control, control: EditControl, api: BorderStyle, version: 11.4.0.26] keywords: [EditControl, BorderStyle, XP Themes, FixedSingle, Fixed3D, None] -->
```