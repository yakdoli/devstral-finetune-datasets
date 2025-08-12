```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_051.jpeg
document_name: tools
page_number: 051
page_id: tools#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:17:20Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

3. **Add items to the Carousel in either the Properties window or in the Smart Tags of the Carousel control.**

![Adding the Carousel Control to an Application](Carousel Tasks "Adding the Carousel Control to an Application")
*Figure 8: Adding the Carousel Control to an Application*

### 3.2.2.2 Adding through Code
To add the Carousel control to an application through code, include the Windows Forms Tools namespace:

#### [C#]
```csharp
using Syncfusion.Windows.Forms.Tools;
```

#### [VB]
```vb
Imports Syncfusion.Windows.Forms.Tools
```

**Create an instance of the Carousel control and add it to the form as given in the following code:**

#### [C#]
```csharp
Syncfusion.Windows.Forms.Tools.Carousel carousel1;
this.carousel1 = new Syncfusion.Windows.Forms.Tools.Carousel();
this.Controls.Add(carousel1);
```

---

<!-- tags: [syncfusion-winforms, carousel-control, essential-tools, windows-forms, adding-controls] keywords: [syncfusion, winforms, carousel, properties, smart-tags, code, namespace, instance, add-control, controls] -->
```