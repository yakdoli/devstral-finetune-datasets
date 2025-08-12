```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_890.jpeg
document_name: tools
page_number: 890
page_id: tools#page_890
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Describes events related to changes in the BorderColor and BorderSides properties of a control.
- Provides examples in C# and VB.NET for handling these events.

## Content

### 3.5.8.9.4.2 BorderColorChanged

#### Overview

This event occurs when the `BorderColor` property is changed. The `BorderColor` property indicates the color of the 2D border.

#### Event Handler

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Example: C#

```csharp
private void numericUpDownExt1_BorderColorChanged(object sender, EventArgs e)
{
    Console.WriteLine(" BorderColorChanged event is raised ");
}
```

#### Code Example: VB.NET

```vbnet
Private Sub numericUpDownExt1_BorderColorChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" BorderColorChanged event is raised ")
End Sub
```

### 3.5.8.9.4.3 BorderSidesChanged

#### Overview

This event occurs when the `BorderSides` property is changed. The `BorderSides` property indicates the border sides of the panel.

#### Event Handler

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Example: C#

```csharp
private void numericUpDownExt1_BorderSidesChanged(object sender, EventArgs e)
{
    Console.WriteLine(" BorderSidesChanged event is raised ");
}
```

#### Code Example: VB.NET

```vbnet
Private Sub numericUpDownExt1_BorderSidesChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" BorderSidesChanged event is raised ")
End Sub
```

## Page-level Navigation/TOC (if applicable)

- **3.5.8.9.4.2 BorderColorChanged**
  - Overview
  - Event Handler
  - Code Example: C#
  - Code Example: VB.NET
- **3.5.8.9.4.3 BorderSidesChanged**
  - Overview
  - Event Handler
  - Code Example: C#
  - Code Example: VB.NET

## Cross References

- For more details on BorderColor and BorderSides properties, see the corresponding control documentation.

<!-- tags: [Syncfusion, Windows Forms, BorderColor, BorderSides, Event Handling, C#, VB.NET] keywords: [Syncfusion, Windows Forms, BorderColorChanged, BorderSidesChanged, EventArgs, Event Handler, C#, VB.NET] -->
```