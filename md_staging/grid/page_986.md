```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_986.jpeg
document_name: grid
page_number: 986
page_id: grid#page_986
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:56:49Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Configuring the record navigation bar visibility and tooltip behavior in the Essential Grid for Windows Forms.

## Content

### Navigation Bar Settings

The following table describes the settings for controlling the visibility and behavior of the record navigation bar:

| Setting                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| ShowNavigationBar        | Specifies whether to show the record navigation bar.                       |
| ShowNavigationBarToolTips | Specifies whether to show tooltips when the user hovers the mouse over the elements of the RecordNavigationBar. |

### Code Examples

The following code examples illustrate the above settings.

#### Using C#

```csharp
this.gridGroupingControl1.ShowNavigationBar = true;
this.gridGroupingControl1.ShowNavigationBarToolTips = true;
```

#### Using VB.NET

```vb.net
Private Me.gridGroupingControl1.ShowNavigationBar = True
Private Me.gridGroupingControl1.ShowNavigationBarToolTips = True
```

### Through Designer

The properties can also be configured through the designer as shown in the figure below:

![Figure 381: ShowNavigationBar = "True" and ShowNavigationBarToolTips = "True"](image.png)

**Figure 381:** ShowNavigationBar = "True" and ShowNavigationBarToolTips = "True"

## Output

- The visual output reflects the configured settings for the record navigation bar.

### API Reference

#### Properties

- **ShowNavigationBar:** Boolean property to specify the visibility of the record navigation bar.
- **ShowNavigationBarToolTips:** Boolean property to specify whether tooltips are shown for the navigation bar elements.

### Code Examples

#### C#

```csharp
// Configuring navigation bar properties
gridGroupingControl1.ShowNavigationBar = true;
gridGroupingControl1.ShowNavigationBarToolTips = true;
```

#### VB.NET

```vb.net
' Configuring navigation bar properties
gridGroupingControl1.ShowNavigationBar = True
gridGroupingControl1.ShowNavigationBarToolTips = True
```

## RAG Annotations

<!-- tags: [Syncfusion, Windows Forms, Grid, Record Navigation Bar, Designer] keywords: [ShowNavigationBar, ShowNavigationBarToolTips, record navigation bar, tooltips, designer configuration] -->
```