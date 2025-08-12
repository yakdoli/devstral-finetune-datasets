```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: diagram
page_number: 126
page_id: diagram#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:12Z
fidelity: lossless
--> 

## Essential Diagram for Windows Forms

The following is a summary of the table detailing the properties and their descriptions for labels in the Essential Diagram for Windows Forms:

- **Name**: Used to specify the name of a label.  
- **FullName**: Used to specify the full name of a label. Label container's name is prefixed with its name.  
- **ReadOnly**: Used to add a flag indicating whether the text object is Read-only or not.  
- **Visible**: Specifies the visibility of the label.  
- **FontColorStyle**: Specifies the font color style.  
- **BackgroundStyle**: Specifies the text background style.  
- **Text**: Gets or sets the label text.  
- **FontStyle**: Specifies the font style.  
- **PropertyBinding**: Binds the text value of the label to the Text property.  
- **Size**: Gets or sets the label text size.  
- **SizeToNode**: Set the node size to label size. This can be enabled if the node has only one label and label's position is specified.  

### Properties Table

| Name             | Description                                                                     | Default | Type             | Remarks |
|------------------|---------------------------------------------------------------------------------|---------|------------------|---------|
| Name             | Used to specify the name of a label.                                           | NA      | string           | NA      |
| FullName         | Used to specify the full name of a label.                                      | NA      | string           | NA      |
| Readonly         | Used to add a flag indicating whether the text object is Read-only or not.   | NA      | Boolean          | NA      |
| Visible          | Specifies the visibility of the label.                                         | NA      | Boolean          | NA      |
| FontColorStyle   | Specifies the font color style.                                               | NA      | FillStyle        | NA      |
| BackgroundStyle  | Specifies the text background style.                                           | NA      | FillStyle        | NA      |
| Text             | Gets or sets the label text.                                                  | NA      | String           | NA      |
| FontStyle        | Specifies the font style.                                                     | NA      | FontStyle        | NA      |
| PropertyBinding  | Binds the text value of the label to the Text property.                       | NA      | LabelPropertyBinding | NA      |
| Size             | Gets or sets the label text size.                                             | NA      | SizeF            | NA      |
| SizeToNode       | Set the node size to label size. This can be enabled if the node has only one label and label's position is specified. | NA      | Boolean          | NA      |

### Source Multiplicity

- The table provides information about the properties of labels in the Essential Diagram for Windows Forms, including their names, descriptions, default values, types, and remarks.

### Features of the WinForms Diagram Control

- **Property Binding**: It allows the text value of the label to be bound to the **Text** property, enabling dynamic updates.
- **Customization Options**: Properties like **FontStyle**, **FontColorStyle**, and **BackgroundStyle** allow for detailed customization of the appearance of the labels.
- **Visibility Control**: The **Visible** property determines whether the label is displayed or not.
- **Sizing and Positioning**: **Size** and **SizeToNode** properties provide control over the dimensions of the label and its alignment within the node.

### Usage Context

- This table is particularly useful for developers working with Syncfusion's WinForms Diagram Control, where fine-tuning the properties of labels is essential for creating visually appealing and functional diagrams.

<!-- tags: [Syncfusion Winforms, Diagram Control, Labels, Property Binding, Font Style, Font Color, Background, Visibility, Size, SizeToNode] keywords: [Windows Forms, property binding, font style, visible property, fill style, size customization, node positioning, diagram control, label properties] -->
```