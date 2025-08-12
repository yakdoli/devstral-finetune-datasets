```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_950.jpeg
document_name: tools
page_number: 950
page_id: tools#page_950
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Save and load the background color information of a GradientLabel using XML serialization.
- Utilize the `XmlSerializer` class to provide serialization support.
- Include necessary namespaces for working with Syncfusion's GradientLabel and XML serialization.

### Contents

#### Serialization

We can save and load the background color information in an XML file to persist the color state of a GradientLabel. The `XmlSerializer` Class can be used for providing serialization support.

##### Code Snippets

- **C#**
```csharp
using System.Drawing;
using Syncfusion.Drawing;
using System.Xml.Serialization;
using System.IO;
```

- **VB.NET**
```vb
Imports System.Drawing
Imports Syncfusion.Drawing
Imports System.Xml.Serialization
Imports System.IO
```

**Code snippet saves the information in a file called `colorinfo.xml`:**

- **C#**
```csharp
private void button1_Click(object sender, System.EventArgs e) 
{ 
    this.gradientLabel1.BackgroundColor = new 
        BrushInfo(GradientStyle.Gradient, Color.ForwardDiagonal , Color.Biege); 
    string xmlFilename = "C:\colorinfo.xml";
    XmlSerializer serializer = new 
        XmlSerializer(typeof(Syncfusion.Drawing.BrushInfo)); 
    FileStream fs= new FileStream(xmlFilename, FileMode.Create); 
    System.Xml.XmlTextWriter writer = new System.Xml.XmlTextWriter(fs, 
        System.Text.Encoding.Default); 
    serializer.Serialize(fs, this.gradientLabel1.BackgroundColor); 
    writer.Close(); 
}
```

- **VB.NET**
```vb
Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
```

### WinForms-specific Conventions

- Use Syncfusion's namespaces and classes to handle GradientLabel properties and serialization.
- Ensure namespaces such as `System.Drawing`, `Syncfusion.Drawing`, `System.Xml.Serialization`, and `System.IO` are included for the code to function correctly.

### API Reference

- `BrushInfo`: Represents the brush information for a gradient style.
- `GradientStyle`: Enumerates the gradient styles available.
- `Color`: Represents the color used in the gradient.

### Code Examples

#### Saving GradientLabel Background Color

- **C#**
```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    this.gradientLabel1.BackgroundColor = new 
        BrushInfo(GradientStyle.Gradient, Color.ForwardDiagonal, Color.Biege);
    string xmlFilename = "C:\colorinfo.xml";
    XmlSerializer serializer = new 
        XmlSerializer(typeof(Syncfusion.Drawing.BrushInfo));
    FileStream fs = new FileStream(xmlFilename, FileMode.Create);
    System.Xml.XmlTextWriter writer = new System.Xml.XmlTextWriter(fs, 
        System.Text.Encoding.Default);
    serializer.Serialize(fs, this.gradientLabel1.BackgroundColor);
    writer.Close();
}
```

#### Loading GradientLabel Background Color

- **C#**
```csharp
private void LoadButton_Click(object sender, EventArgs e)
{
    string xmlFilename = "C:\colorinfo.xml";
    XmlSerializer deserializer = new 
        XmlSerializer(typeof(Syncfusion.Drawing.BrushInfo));
    FileStream fs = new FileStream(xmlFilename, FileMode.Open);
    System.Xml.XmlTextReader reader = new System.Xml.XmlTextReader(fs);
    this.gradientLabel1.BackgroundColor = (BrushInfo)deserializer.Deserialize(reader);
    reader.Close();
    fs.Close();
}
```

### See also

- [GradientLabel Controls](docs.gradients)
- [Serialization in Windows Forms](docs.serialization)
<!-- tags: [Syncfusion Winforms, GradientLabel, Serialization, XmlSerializer, version 11.4.0.26] keywords: [GradientLabel, XmlSerialization, BackgroundColor, Syncfusion.Drawing, System.Xml.Serialization, Windows Forms] -->
```
