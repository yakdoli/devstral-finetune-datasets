```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_026.jpeg
document_name: diagram
page_number: 026
page_id: diagram#page_026
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:01Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### Step 4: Add a Model to the Diagram Control

#### C#

```csharp
// Create a model
Model model = new Model();

// Add the model to the Diagram control
diagram.Model = model;
```

#### VB

```vb
' Create a model
Dim model As New Model()

' Add the model to the Diagram control
diagram.Model = model
```

### Step 5: Add the Diagram Control to the Diagram Form window

#### C#

```csharp
// Add the Diagram control to Diagram Form
this.Controls.Add(diagram);
```

#### VB

```vb
' Add the Diagram control to the Diagram Form
Me.Controls.Add(diagram)
```

## API Reference (if applicable)

### Code Examples

#### C#

- **Setting Location:**
  ```csharp
  diagram.Location = new Point(20, 5);
  ```

#### VB

- **Setting Location:**
  ```vb
  diagram.Location = New Point(20, 5)
  ```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, Diagram control, Model, Windows Forms, Control placement] keywords: [diagram location, adding a model, diagram control, step-by-step guide, windows forms, essential diagram] -->
```