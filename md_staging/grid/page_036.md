```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_036.jpeg
document_name: grid
page_number: 036
page_id: grid#page_036
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:18:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Installation and Deployment

This section covers information on the install location, samples, licensing, patches update, and updation of the recent version of Essential Studio. It comprises the following subsections:

### 2.1 Installation

For step-by-step installation procedure for the installation of Essential Studio, refer to the Installation topic under Installation and Deployment in the Common UG.

**See Also**

For licensing, patches, and information on adding or removing selective components, refer the following topics in Common UG under Installation and Deployment.

- Licensing
- Patches
- Add/Remove Components

### 2.2 Sample and Location

This section covers the location of the installed samples and describes the procedure to run the samples through the sample browser. It also lists the location of source code.

#### Sample Installation Location

The Grid Windows Forms samples are installed at the following location locally on the disk:

`C:\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Windows\Samples\2.0`

The Grid Grouping Windows Forms samples are installed at the following location locally on the disk:

`C:\Syncfusion\EssentialStudio\[Version Number]\Windows\Grid.Grouping.Windows\Samples\2.0`

---

### API Reference (if applicable)

The API details for this section are not explicitly mentioned in the provided text. However, based on the context, the following elements might be relevant:

- **Namespace**: Syncfusion.Windows.Forms.Grid
- **Class**: GridControl
- **Members**:
  - Methods/Properties: (To be detailed based on specific usage)
  - Events: (To be detailed based on specific usage)

---

### Code Examples (multi-language supported)

Since specific code examples are not provided in the text, here is a generic example of how to integrate the GridControl in a Windows Forms application:

```csharp
using Syncfusion.Windows.Forms.Grid;

public partial class Form1 : Form
{
    public Form1()
    {
        InitializeComponent();

        // Create a new GridControl
        GridControl grid = new GridControl();

        // Add the GridControl to the form
        this.Controls.Add(grid);

        // Set basic properties
        grid.Dock = DockStyle.Fill;
        grid.RowCount = 5;
        grid.ColCount = 5;

        // Set cell values
        grid[0, 0].Text = "Header 1";
        grid[0, 1].Text = "Header 2";
        grid[1, 0].Text = "Row 1";
        grid[1, 1].Text = "Data 1";
    }
}
```

---

### Cross References

See also topics in Common UG under Installation and Deployment:
- Licensing
- Patches
- Add/Remove Components

---

### Page-level Navigation/TOC (if applicable)

- Installation and Deployment
  - 2.1 Installation
  - 2.2 Sample and Location

---

<!-- tags: [Essential Grid, Windows Forms, Installation, Samples, Licensing, Patches, Syncfusion, Windows Forms Installation, Sample Location] keywords: [Essential Grid, Windows Forms, Installation Procedure, Licensing, Patches, Grid Control, Sample Browser, Source Code Location, Grid Windows Forms, Grid Grouping Windows Forms] -->
```