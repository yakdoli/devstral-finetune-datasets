```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_357.jpeg
document_name: tools
page_number: 357
page_id: tools#page_357
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:07:17Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page outlines the steps to use the ButtonEditChildButton Collection Editor in Windows Forms.
- It provides instructions on setting properties for buttons, either through the collection editor or directly in the property grid.
- Demonstrates configuring attributes for child buttons within ButtonEdit controls.

## Content

### ButtonEditChildButton Collection Editor

#### Step 1: Opening the Editor
**Description:**
Open the ButtonEditChildButton Collection Editor using the "Button" property.

**Figure:**
**Figure 169:** Opening ButtonEditChildButton Collection Editor using "Button" Property

**Screenshot:**
Displaying the Properties window for `buttonEdit1` with the "Buttons" property highlighted.

#### Step 2: Setting Button Properties
**Description:**
Set properties for buttons using the Editor. You can specify the attributes for any of the child buttons through the collection editor or by clicking any button and then selecting the properties in the property grid, that display the properties for the selected button.

**Figure:**
**ButtonEditChildButton Collection Editor**

**Screenshot:**
The collection editor window showing settings for `buttonEditChildButton1` and `buttonEditChildButton2`. Properties include `TextImageRelation`, `UseMnemonic`, `Appearance - Styles`, and more.

**Steps:**
1. Click the "Buttons" property to open the ButtonEditChildButton Collection Editor.
2. Add or remove buttons as needed.
3. Configure the properties for each button, such as appearance, behavior, and text options.

## API Reference

### Properties
- **Buttons**: Collection of child buttons within the ButtonEdit control.

## Code Examples

### Example: Adding and Configuring Buttons

```csharp
// Adding buttons to the collection
buttonEdit1.Buttons.Add(new ButtonEditChildButton() { Text = "Button 1" });
buttonEdit1.Buttons.Add(new ButtonEditChildButton() { Text = "Button 2" });

// Configuring properties of the first child button
var button1 = buttonEdit1.Buttons[0];
button1.TextImageRelation = TextImageRelation.Overlay;
button1.UseVisualStyle = true;
button1.FlatStyle = FlatStyle.Standard;

// Configuring properties of the second child button
var button2 = buttonEdit1.Buttons[1];
button2.TextImageRelation = TextImageRelation.Overlay;
button2.UseWaitCursor = false;
button2.KeepFocusRectangle = false;
```

## Page-level Navigation/TOC
- Opening the ButtonEditChildButton Collection Editor
- Setting properties for buttons
- Configuring child button attributes

<!-- tags: [syncfusion, windowsforms, buttoneditchildbutton, collectioneditor, properties, configuration] keywords: [buttoneditchildbutton, editor, properties, appearance, behavior, collection, configuration, buttons] -->
```