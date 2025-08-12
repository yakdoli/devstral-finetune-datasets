```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_175.jpeg
document_name: pdf
page_number: 175
page_id: pdf#page_175
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:55Z
fidelity: lossless
-->

# Essential PDF

## Overview

- The `Pdf3DActivation` class determines when a 3D annotation is active or inactive.
- 3D artwork in a PDF is activated using the `Pdf3DActivationMode` class, with the following activation states:
  - ExplicitActivation: The annotation is initially deactivated. Activation requires explicit interaction (e.g., clicking).
  - PageOpen: The annotation is activated when the PDF page is opened.
  - PageVisible: The annotation is activated when the page becomes visible.

## Detailing 3D Activation Modes

- ExplicitActivation: The annotation is in a deactivated state initially and requires explicit activation by clicking.
- PageOpen: The annotation is activated automatically upon opening the PDF page.
- PageVisible: The annotation becomes active when the page is visible.

## Controlling the Toolbar Visibility

You can show or hide the toolbar by using the `ShowToolbar` property.

### C# Code Example

```csharp
// Creating instance for Pdf3DActivation class
Pdf3DActivation activation = new Pdf3DActivation();

// Setting Activation Mode as PageVisible
activation.ActivationMode = Pdf3DActivationMode.PageVisible;

// Showing the Toolbar
activation.ShowToolbar = true;

// Setting Deactivation Mode as PageVisible
activation.DeactivationMode = Pdf3DDeactivationMode.ExplicitDeactivation;

// Assigning the Activation to the Pdf3DAnotation
annotation.Activation = activation;
```

### VB.NET Code Example

```vb
' Creating instance for Pdf3DActivation class
Dim activation As Syncfusion.Pdf.Interactive.Pdf3DActivation = New Syncfusion.Pdf.Interactive.Pdf3DActivation()

' Setting Activation Mode as PageVisible
activation.ActivationMode = Pdf3DActivationMode.PageVisible

' Showing the Toolbar
activation.ShowToolbar = True

' Setting Deactivation Mode as PageVisible
activation.DeactivationMode = Pdf3DDeactivationMode.ExplicitDeactivation

' Assigning the Activation to the Pdf3DAnotation
```

## Page-Level Navigation/TOC

- Reactivating previous summary points or any local links if they exist.

## Cross References

See also: Any referenced sections or related documentation.
```

<!-- tags: [pdf, essentialpdf, 3d, annotation, activation, winforms, syncfusion] keywords: [pdf3dactivation, explicitactivation, pageopen, pagevisible, showtoolbar, deactivation] -->
```