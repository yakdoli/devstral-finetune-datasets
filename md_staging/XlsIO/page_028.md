```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_028.jpeg
document_name: XlsIO
page_number: 028
page_id: XlsIO#page_028
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:50:02Z
fidelity: lossless
-->

## 3.2 Creating a Platform Application

### Overview
- Step-by-step procedure to create Windows, Web, WPF, Silverlight, and ASP.NET MVC applications.

### Content
#### Creating a Platform Application
This section illustrates the step-by-step procedure to create the following platform applications:

- Windows
- Web
- WPF
- Silverlight
- ASP.NET MVC

#### Windows Application
1. **Open Microsoft Visual Studio**.
2. Go to the **File** menu and click **New Project**.
3. In the **New Project** dialog box, select the **Windows Forms Application** template.
4. Name the project and click **OK**.

![New Project dialog box - Windows Forms Application](https://raw.githubusercontent.com/syncfusion/xlsio-docs/main/images/new-project-winform.png)

#### New Project dialog box - Windows Forms Application

### Appendix

#### Figure: New Project dialog box - Windows Forms Application

## Code Examples

#### Creating a Windows Forms Application
```csharp
using System;
using System.Windows.Forms;

public class MainForm : Form
{
    public MainForm()
    {
        this.Text = "Windows Forms Application";
        this.Size = new System.Drawing.Size(400, 300);
    }

    static void Main()
    {
        Application.EnableVisualStyles();
        Application.SetCompatibleTextRenderingDefault(false);
        Application.Run(new MainForm());
    }
}
```

## API Reference

### `Windows Forms Application`
- **Namespace**: `System.Windows.Forms`
- **Class**: `Form`
- **Properties**:
  - `Text`: Sets the title of the form.
  - `Size`: Sets the dimensions of the form.

### `Application`
- **Namespace**: `System.Windows.Forms`
- **Static Methods**:
  - `EnableVisualStyles()`: Activates visual styles for the application.
  - `SetCompatibleTextRenderingDefault(bool value)`: Sets whether the application should use the system font.
  - `Run(Form form)`: Starts the application with the specified form as the main window.

## RAG Annotations
<!-- tags: [syncfusion, Windows Forms, application creation, Visual Studio, .NET Framework 3.5] keywords: [New Project dialog, Windows Forms, Silverlight, ASP.NET MVC, step-by-step procedure, application development, platform applications] -->
```