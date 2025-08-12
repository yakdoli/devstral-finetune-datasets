```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_253.jpeg
document_name: diagram
page_number: 253
page_id: diagram#page_253
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:24:13Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Provides guidance on adding custom properties to Diagram and displaying them in the Property Editor.
- Illustrates the process using code examples in C#.
- Demonstrates extending the Diagram control by creating custom properties and integrating them into the property editor.

## Content

### 5 Frequently Asked Questions
This section guides you through questions based on very specific tasks in Diagram control.

#### 5.1 How To Add a Custom Property To Diagram And Display It In the Property Editor

The below given code snippet illustrates how you can add a custom property to Diagram and display it in the Property Editor.

```csharp
//Derived Diagram
public class MyDiagram : Syncfusion.Windows.Forms.Diagram.Controls.Diagram
{
    public override Model CreateModel()
    {
        return new QuickStart.MainForm.MyModel();
    }
}

//Derived Model where the new property is added
public class MyModel : Syncfusion.Windows.Forms.Diagram.Model
{
    public override void SetDefaultPropertyValues()
    {
        base.SetDefaultPropertyValues();
        this.SetPropertyValue("MyCustomProperty", 0);
    }
    
    [Browsable(true),
    Category("MyProperties"),
    Description("Description for MyCustomProperty")]
    public int MyCustomProperty
    {
        get
        {
            object value = this.GetPropertyValue("MyCustomProperty");
            if (value != null)
            {
                return (int)value;
            }
            return 0;
        }
    }
}
```

### Explanation:
- **MyDiagram**: Derived from `Syncfusion.Windows.Forms.Diagram.Controls.Diagram`, overrides the `CreateModel` method to use a custom model.
- **MyModel**: Derived from `Syncfusion.Windows.Forms.Diagram.Model`, sets default property values and defines a custom property `MyCustomProperty`.
- **Custom Property**: The `MyCustomProperty` is marked with `Browsable(true)` to ensure it is visible in the property editor. It is categorized under "MyProperties" and has a description "Description for MyCustomProperty".
- **Accessors**: The `get` accessor retrieves the value of `MyCustomProperty` from the model, handling cases where the value might be `null`.

<!-- tags: [Syncfusion, Winforms, Diagram, Custom Properties, Property Editor] keywords: [Diagram, CustomProperty, PropertyEditor, MyCustomProperty, SetDefaultPropertyValues, Model, Browsable, Category, Description, MyDiagram, MyModel] -->
```