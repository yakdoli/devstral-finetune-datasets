```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_939.jpeg
document_name: tools
page_number: 939
page_id: tools#page_939
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:44Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### AutoLabel Property and Description

| AutoLabel Property | Description |
|---|---|
| Position | Specifies the relative position of the control and the AutoLabel. <br> The options included are as follows. <br> - Custom, <br> - Left, <br> - Left and <br> - Top. |

When the **Position** property is set to 'Custom', you can drag the label to the required position using the mouse.

#### Code Examples

##### C#

```csharp
this.automLabel1.Position =
    Syncfusion.Windows.Forms.Tools.AutoLabelPosition.Top;
```

##### VB.NET

```vb
Me.autoLabel1.Position =
    Syncfusion.Windows.Forms.Tools.AutoLabelPosition.Top
```

#### Visual Representation

![](attachment:image.png)

**Figure 602: "Position" property in the Properties Grid**

## API Reference

### Position Property

- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Property**: AutoLabelPosition
- **Enum Values**: Custom, Top, Left, Left and Top

## Code Examples (continued)

Example usage in C#:

```csharp
this.automLabel1.Position = Syncfusion.Windows.Forms.Tools.AutoLabelPosition.Top;
```

Example usage in VB.NET:

```vb
Me.autoLabel1.Position = Syncfusion.Windows.Forms.Tools.AutoLabelPosition.Top
```

### Visual Designer

In the Properties Grid, the Position property can be set programmatically or via the Visual Studio designer.

<!-- tags: [AutoLabel, Position, Windows Forms, Syncfusion] keywords: [AutoLabel, Position, Designer, C#, VB.NET, WinForms, Syncfusion, Tools] -->
```