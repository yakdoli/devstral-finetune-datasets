```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_089.jpeg
document_name: tools
page_number: 089
page_id: tools#page_089
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:44Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

#### Overview
- The page discusses the properties and methods associated with the `CommandBar` control.
- It covers behavior settings, cursor customization, and code examples for setting the `Cursor` property for the `CommandBar`.

## Content

The method associated with the above properties is given below.

### Table: Method associated with CommandBar Properties

| Method                       | Description                                                                                       |
|------------------------------|---------------------------------------------------------------------------------------------------|
| `CalcCommandBarMaxLength`   | Calculates the `CommandBar`'s maximum length for the specified client width.                     |

### Figure: CommandBar with OccupyFullRow property set to "True"

![](attachment:CommandBar_Sample.png)

> Figure 34: CommandBar with OccupyFullRow property set to "True"

### See Also

- [Interactive Features, Themes And Visual Styles](#interactive-features-themes-and-visual-styles)

### 3.3.3.7 Behavior Settings

The behavior settings of the `CommandBar` control are given below.

#### Cursor

The cursor settings of the `CommandBar` can be customized using the property given below.

### Table: CommandBar Property - Cursor

| CommandBar Property | Description                                          |
|---------------------|------------------------------------------------------|
| `Cursor`           | The mouse cursor used for the `CommandBar`.         |

#### Code Examples

```csharp
this.commandBar1.Cursor = System.Windows.Forms.Cursors.Hand;
```

```vb.net
Me.commandBar1.Cursor = System.Windows.Forms.Cursors.Hand
```

#### Note

> The `ResetCursor()` method can be used to reset the `Cursor` property to its default value.

### API Reference

#### Cursor Property
- **Description**: Specifies the mouse cursor for the **CommandBar**.
- **Default Value**: `System.Windows.Forms.Cursors.Default`

### Code Examples

- **C#:**
  ```csharp
  this.commandBar1.Cursor = System.Windows.Forms.Cursors.Hand;
  ```
  
- **VB.NET:**
  ```vb.net
  Me.commandBar1.Cursor = System.Windows.Forms.Cursors.Hand
  ```

### See Also

- **Interactive Features**: Discuss various interactive elements and theming options available for `CommandBar` customization.

## Page-level Navigation/TOC

- **3.3.3.7 Behavior Settings**
  - Cursor
    - Setting the Cursor Property
    - Resetting the Cursor Property

## Cross References

- [Interactive Features, Themes And Visual Styles](#interactive-features-themes-and-visual-styles)

<!-- tags: [CommandBar, WinForms, Cursor, Behavior Settings, Visual Styles] keywords: [CalcCommandBarMaxLength,occupyfullrow,cursor,resetcursor,commandbar,control,behavior] -->
```