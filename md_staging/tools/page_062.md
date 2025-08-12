```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_062.jpeg
document_name: tools
page_number: 062
page_id: tools#page_062
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:52Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Adding a Command Bar to a Command Bar Controller

This section demonstrates how to add a CommandBar to a CommandBarController in a Windows Forms application using both C# and VB.NET. Follow the steps outlined below:

1. **Add the panel control containing the toolbar to the CommandBar:**

   ```vb
   ' Add the panel control containing the toolbar to the CommandBar.
   Me.commandBar1.Controls.AddRange(New System.Windows.Forms.Control() _
   {Me.panel1})
   ```

2. **Add the CommandBar to the CommandBarController through the CommandBars collection property.**

   - **C#:**
     ```csharp
     this.commandBarController1.CommandBars.Add(this.commandBar1);
     // Set the text for the CommandBar.
     this.commandBar1.Text = "commandBar1";
     ```

   - **VB.NET:**
     ```vb
     Me.commandBarController1.CommandBars.Add(Me.commandBar1)
     ' Set the text for the CommandBar.
     Me.commandBar1.Text = "commandBar1"
     ```

3. **Call the CommandBarController's EndInit method to signal the end of initialization.**

   - **C#:**
     ```csharp
     ((System.ComponentModel.ISupportInitialize)(this.commandBarController1)).EndInit();
     ```

   - **VB.NET:**
     ```vb
     CType(Me.commandBarController1, System.ComponentModel.ISupportInitialize).EndInit()
     ```

4. **Run the application.**

### Summary

This guide outlines the steps required to integrate a CommandBar into a CommandBarController in a Windows Forms application. By following these steps, you can effectively manage and organize toolbars and their associated controls within your application.

## References

For more information on CommandBars and CommandBarControllers in Syncfusion Windows Forms, refer to the official documentation or API reference.

<!-- tags: [syncfusion, windows forms, commandbar, commandbarcontroller, integration, initialization] keywords: [commandbar, commandbarcontroller, windows forms, controls, toolbox, design, .NET, C#, VB.NET, initialization, endinit] -->
```