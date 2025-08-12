```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: tools
page_number: 060
page_id: tools#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates creating a CommandBar in Windows Forms using designers and programmatic approaches.
- Explains how to set up CommandBars through Syncfusion's API in C# and VB.NET.
- Includes step-by-step instructions for initializing and configuring CommandBars.

## Content

### CommandBar Created Through Designer

![CommandBar Sample](media/CommandBar_Sample.png)
**Figure 12: CommandBar created Through Designer**

#### See Also
- **Through Code**
- **Through XP Menus Framework**

### 3.3.2.2 Through Code

In addition to using the designer for designing the CommandBar layout, it is also feasible to use the CommandBar's programmatic API for creating and setting up the application's CommandBars.

The following section covers the steps involved in creating, initializing, and setting up CommandBars in a Windows Forms application programmatically.

1. **Include the required namespace.**

   **[C#]**
   ```csharp
   using Syncfusion.Windows.Forms.Tools;
   ```

   **[VB.NET]**
   ```vbnet
   Imports Syncfusion.Windows.Forms.Tools
   ```

2. **Create instances of the Essential Tools CommandBarController class and CommandBar control within the application's main form.**

3. **Call the CommandBarController's `BeginInit` method to signal the start of initialization.**

   **[C#]**
   ```csharp
   private Syncfusion.Windows.Forms.Tools.CommandBarController
   ```

### WinForms-specific conventions
- Use Syncfusion.Windows.Forms.Tools namespace for CommandBar functionality.
- Follow initialization steps to properly set up CommandBars in both C# and VB.NET projects.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** CommandBarController
- **Methods:** `BeginInit`

## Code Examples

### C#
```csharp
using Syncfusion.Windows.Forms.Tools;

private Syncfusion.Windows.Forms.Tools.CommandBarController commandBarController;
```

### VB.NET
```vbnet
Imports Syncfusion.Windows.Forms.Tools

Private commandBarController As Syncfusion.Windows.Forms.Tools.CommandBarController
```

## RAG Annotations
<!-- tags: [CommandBarController, Windows Forms, Syncfusion, C#, VB.NET] keywords: [CommandBar, Designer, Programmatic API, Initialization, BeginInit, Syncfusion.Windows.Forms.Tools, controller, C#, VB.NET] -->
```