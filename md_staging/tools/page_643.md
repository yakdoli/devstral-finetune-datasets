```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_643.jpeg
document_name: tools
page_number: 643
page_id: tools#page_643
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section guides you to create a Gradient Panel through designer and programmatic approaches.
- Demonstrates the use of GradientPanel control in Visual Studio .NET.
- Steps to configure GradientPanel properties and customize its appearance.

## Content

### Through Designer

This section will guide you to create a GradientPanel control.

1. **Create a new Visual C# application or VB.NET application in Visual Studio .NET.**

2. **Drag-and-drop a GradientPanel control object from the toolbox onto the form and resize it to the desired dimensions.**

   - The GradientPanel control can be found in the Syncfusion section of the toolbox.
   - Figure 392: GradientPanel Control in Toolbox
   
   ![Figure 392: GradientPanel Control in Toolbox](https://example.com/image_url)
   
3. **Set background color for GradientPanel through property grid.**

   - Open the Properties window for the GradientPanel control.
   - Configure properties such as `BackgroundColor`, `PatternStyle`, `GradientColors`, etc.
   
   ![Properties window for GradientPanel control](https://example.com/image_url)

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** GradientPanel
- **Properties:** `BackgroundColor`, `PatternStyle`, `GradientColors`, etc.

## Code Examples (multi-language supported)

```csharp
// Example of programmatically creating a GradientPanel
using Syncfusion.Windows.Forms.Tools;

public class GradientPanelExample
{
    public void InitializeGradientPanel()
    {
        GradientPanel gradientPanel = new GradientPanel();
        gradientPanel.PatternStyle = GradientPanel.PatternStyle.Percent10;
        gradientPanel.BackColor1 = Color.LightSkyBlue;
        gradientPanel.BackColor2 = Color.LightGray;
        
        // Add the GradientPanel to the form
        this.Controls.Add(gradientPanel);
    }
}
```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, GradientPanel, Designer, Property Grid, Visual Studio .NET] keywords: [GradientPanel control, Windows Forms, Syncfusion library, BackgroundColor, PatternStyle, GradientColors, Visual Studio, designer approach, programmatic approach] -->
```