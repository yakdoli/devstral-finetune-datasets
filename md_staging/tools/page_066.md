```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_066.jpeg
document_name: tools
page_number: 066
page_id: tools#page_066
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:05Z
fidelity: lossless
-->

## CommandBar Properties and Behaviors

### Table: CommandBar Properties

| CommandBar Property        | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| DisableFloating            | Indicates whether the CommandBar is allowed to float.                      |
| FloatModeWrapping          | Indicates whether the CommandBar should wrap when floating.               |
| FloatBounds                | Gets / sets the bounds of a floating CommandBar.                          |
| Floating                   | Returns the current dock / float state of the CommandBar.                  |

### Floating State of CommandBar

The float state of the CommandBar can be disabled by setting the **DisableFloating** property to 'True'.

#### FloatModeWrapping

Setting the **FloatModeWrapping** property to 'True' wraps a floating CommandBar when it is resized to less than its maximum length. The **DisableFloating** property must be set to 'False' for this behavior.

### Code Examples

#### C#

```csharp
this.commandBar1.DisableFloating = false;
this.commandBar1.FloatModeWrapping = true;
this.commandBar1.FloatBounds = new System.Drawing.Rectangle(419, 303, 183, 47);
```

#### VB.NET

```vb
Me.commandBar1.DisableFloating = False
Me.commandBar1.FloatModeWrapping = True
Me.commandBar1.FloatBounds = New System.Drawing.Rectangle(419, 303, 183, 47)
```

### Visual Representation

![Figure 16: CommandBar in Float State](attachment://figure16.png)

**Figure 16: CommandBar in Float State**

### Sample Installation Path

A sample demonstrating the Floating CommandBar is available in the following sample installation path:

---

<!-- tags: [Syncfusion, WinForms, CommandBar, properties, float, disablefloating, floatmodewrapping, floatbounds] keywords: [float mode, floating state, wrapping, disable floating, commandbar properties] -->
```