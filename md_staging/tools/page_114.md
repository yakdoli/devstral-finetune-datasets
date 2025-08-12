```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_114.jpeg
document_name: tools
page_number: 114
page_id: tools#page_114
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:30:32Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Manipulating the size of a toolbar and its parent panel to allow proper layout.
- Handling resizing of a CommandBar based on conditions related to button count and toolbar dimensions.
- Estimating and assigning sizes dynamically based on button width and required button columns.

## Content

### Toolbar Size Adjustment

The code snippet below demonstrates how to adjust the size of a toolbar and its parent panel to allow proper layout based on the toolbar's dimensions:

```csharp
// Set this width to be the toolbar's parent panel width and allow the toolbar to
// layout itself for this width. We then get the toolbar's height and assign this as
// the CommandBar client size.
sznew.Width = nnewwidth;
toolbar.Parent.Width = sznew.Width;
sznew.Height = toolbar.Height;
toolbar.Parent.Width = sztemp.Width;
```

If specific conditions are met, the code then sets the CommandBar's client size to a new size `sznew`:

```csharp
// Set the CommandBar's client size to be equal to this new size.
arg.ClientSize = sznew;
```

### Condition-based Size Assignment

The snippet includes logic to handle different scenarios based on a factor `ffactor`:

- If `ffactor` is greater than 1:
  - The toolbar's parent is assigned the new maximum width, and the CommandBar's client size is set to `sznew`.
  ```csharp
  else
  sznew = szmaxwrap;
  
  // Set the CommandBar's client size to be equal to this new size.
  arg.ClientSize = sznew;
  ```

- If `ffactor` is less than or equal to 1:
  - The CommandBar is extended to the maximum width, and the client size is set accordingly.
  ```csharp
  else if (ffactor <= 1)
  {
  // The CommandBar is extended to the maximum width.
  arg.ClientSize = szminwrap;
  }
  ```

- Otherwise, the client size is directly assigned the toolbar's size:
  ```csharp
  else
  {
  arg.ClientSize = toolbar.Size;
  }
  ```

### Bottom/Top Resizing

The snippet also handles resizing for the Bottom and Top positions of the CommandBar:

```csharp
else if ((arg.CommandBarResizeType == Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Bottom) || (arg.CommandBarResizeType == Syncfusion.Windows.Forms.Tools.CommandBarResizeType.Top)) 
{
  int nfactor = (int)Math.Floor((float)szcurrent.Height / (float)szbtn.Height);
  float ffactor = (float)szcurrent.Height / (float)szbtn.Height;
  
  if (szcurrent.Height > szmaxwrap.Height)
  {
  arg.ClientSize = szmaxwrap;
  }
  else if ((nfactor > 1) && (nfactor == ffactor))
  {
  // The toolbar width is estimated to be equal to the button width + the
  // number of button columns required.
  int nnewwidth = (int)Math.Ceiling((float)nbtncount / (float)nfactor) * szbtn.Width;
  
  Size sznew = Size.Empty;
  }
}
```

### API Reference (if applicable)

This section does not explicitly reference any public APIs but includes the following class and type:

- `Syncfusion.Windows.Forms.Tools.CommandBarResizeType`

### Code Examples

The code examples provided are integrated into the main content, demonstrating how to dynamically adjust the size of the toolbar and CommandBar based on various conditions.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, CommandBar, Toolbar, Resizing, Layout, ClientSize] keywords: [toolbar, parent panel, CommandBarResizeType, Button width, Button columns, Factor, ffactor, nfactor, nbtncount, szcurrent, szbtn] -->
```