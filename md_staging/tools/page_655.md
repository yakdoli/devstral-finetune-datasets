```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_655.jpeg
document_name: tools
page_number: 655
page_id: tools#page_655
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:11Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## GradientPanelExt with Host Primitives

### Overview
- Guide to creating a `GradientPanelExt` using code and including primitives like buttons and progress bars.

### Content

#### Figure 404: GradientPanelExt with Host Primitives
![](attachment:Figure_404_GradientPanelExt_with_Host_Primitives.jpg)

This section details the steps required to create a `GradientPanelExt` through code.

#### Through Code

##### Steps to Create GradientPanelExt Through Code
1. **Create a C# or VB.NET application**:
   - Use Visual Studio to create a new application and switch to the code view.
2. **Add the required Syncfusion assemblies**:
   - Include the following references:
     - Syncfusion.Shared.Base
     - Syncfusion.Shared.Windows
     - Syncfusion.Tools.Base
     - Syncfusion.Tools.Windows
3. **Include the namespace** for the Tools Package.
   - **C#**:
     ```csharp
     using Syncfusion.Windows.Forms.Tools;
     ```
   - **VB.NET**:
     ```vb
     Imports Syncfusion.Windows.Forms.Tools
     ```
4. **Create and configure GradientPanelExt**:
   - Instantiate `GradientPanelExt`, add it to the Windows Form, and define various properties such as docking and corner radius.

##### C# Example
```csharp
// Adding the GradientPanelExt
GradientPanelExt gpe = new GradientPanelExt();
gpe.Dock = DockStyle.Fill;
gradientPanelExt1.CornerRadius = 10;
this.Controls.Add(gpe);
```

### API Reference

#### Namespace: Syncfusion.Windows.Forms.Tools
##### Class: `GradientPanelExt`
- **Properties**:
  - `Dock`: Specifies the docking style of the panel.
  - `CornerRadius`: Defines the corner radius for rounded edges.

### Code Examples

#### C# Example to Create GradientPanelExt
```csharp
using Syncfusion.Windows.Forms.Tools;

// In Form constructor or initialization method
GradientPanelExt gradientPanel = new GradientPanelExt();
gradientPanel.Dock = DockStyle.Fill;
gradientPanel.CornerRadius = 10;
this.Controls.Add(gradientPanel);
```

#### VB.NET Example
```vb
Imports Syncfusion.Windows.Forms.Tools

' In Form constructor or initialization method
Dim gradientPanel As New GradientPanelExt()
gradientPanel.Dock = DockStyle.Fill
gradientPanel.CornerRadius = 10
Me.Controls.Add(gradientPanel)
```

### RAG Annotations
- GradientPanelExt
- Host Primitives
- Code Implementation
- C# Example
- VB.NET Example
- DockStyle.Fill
- CornerRadius

```html
<!-- tags: [Syncfusion, WinForms, GradientPanelExt, HostPrimitives, CodeImplementation] keywords: [GradientPanelExt, HostPrimitives, DockStyle.Fill, CornerRadius, C#Example, VB.NETExample] -->
``` 
```html
