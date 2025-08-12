```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_171.jpeg
document_name: edit
page_number: 171
page_id: edit#page_171
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:11Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Discusses how to configure the appearance of Context Prompt forms using properties such as `ContextPromptBackgroundBrush`, `ContextPromptBorderColor`, and `ContextPromptSize`.
- Provides examples in both C# and VB.NET for setting these properties.

## Content

### Border Settings

The border color of the Context Prompt form is set by using the `ContextPromptBorderColor` property.

| Edit Control Property          | Description                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------|
| ContextPromptBorderColor       | Specifies the color of the Context Choice form border.                                      |
|                               | Used when `UseXPStyle` property is set to `False`. Otherwise, a 3D border is drawn.          |

**C#**:

```csharp
this.editControl1.ContextPromptBorderColor = System.Drawing.Color.Pink;
```

**VB.NET**:

```vb
Me.editControl1.ContextPromptBorderColor = System.Drawing.Color.Pink
```

### Size Settings

The size of the Context Prompt form can be set by using the below given properties.

| Edit Control Property          | Description                                                                                   |
|-------------------------------|---------------------------------------------------------------------------------------------|
| ContextPromptSize             | Gets / sets the size of the Context Prompt form.                                             |
| UseCustomSizeContextPrompt    | Gets / sets a value indicating whether custom Context Prompt size should be used.          |

**C#**:

```csharp
this.editControl1.ContextPromptSize = new System.Drawing.Size(125, 75);
this.editControl1.UseCustomSizeContextPrompt = true;
```

## API Reference

### Properties

- **ContextPromptBackgroundBrush**: Sets the background gradient of the Context Prompt form.
- **ContextPromptBorderColor**: Sets the border color of the Context Prompt form.
- **ContextPromptSize**: Gets or sets the size of the Context Prompt form.
- **UseCustomSizeContextPrompt**: Indicates whether a custom size for the Context Prompt form is used.

## Code Examples

### Setting Background Gradient

**C#**:

```csharp
this.editControl1.ContextPromptBackgroundBrush = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.PapayaWhip, System.Drawing.Color.LemonChiffon);
```

**VB.NET**:

```vb
Me.editControl1.ContextPromptBackgroundBrush = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.BackwardDiagonal, System.Drawing.Color.PapayaWhip, System.Drawing.Color.LemonChiffon)
```

### Setting Border Color

**C#**:

```csharp
this.editControl1.ContextPromptBorderColor = System.Drawing.Color.Pink;
```

**VB.NET**:

```vb
Me.editControl1.ContextPromptBorderColor = System.Drawing.Color.Pink
```

### Setting Size and Custom Size

**C#**:

```csharp
this.editControl1.ContextPromptSize = new System.Drawing.Size(125, 75);
this.editControl1.UseCustomSizeContextPrompt = true;
```

<!-- tags: [Syncfusion, WinForms, ContextPrompt, Border Settings, Size Settings] keywords: [ContextPromptBackgroundBrush, ContextPromptBorderColor, ContextPromptSize, UseCustomSizeContextPrompt, gradient, border color, form size, custom size] -->
```