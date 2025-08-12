```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_147.jpeg
document_name: HTMLUI
page_number: 147
page_id: HTMLUI#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:10:55Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```html
[HTML]

<html>
    <body bgColor="#edf0f7">
        <p>
            <input type="text" id="txt"></input>
        </p>
        <script language="C#">
            using System;
            using System.IO;
            using System.Xml;
            using System.Windows.Forms;
            using System.Drawing;
            using System.Collections;
            using Syncfusion.Windows.Forms.HTMLUI;

            namespace Syncfusion
            {
                public class Script
                {
                    IInputElementImpl scripttext;
                    Hashtable htmllements = new Hashtable();

                    /* Initializes script. */
                    public static Script OnScriptStart()
                    {
                        return new Script();
                    }

                    public Script()
                    {
                        htmllements = Global.Document.GetElementsById_hash();
                        scripttext = htmllements["txt"] as IInputElementImpl;

                        // User control property sets the user control instance for the particular input element declared by the user
                        scripttext.UserControl.CustomControl.Text = "This is a sample for scripting";
                    }
                }
            }
        </script><br />
    </body>
</html>
```

## 4.22.1 HTMLUIScripting Sample

This sample illustrates the support of self-contained HTML documents in HTMLUI.

<!-- tags: [HTMLUI, scripting, sample, self-contained HTML, Windows Forms] keywords: [HTMLUI, scripting, self-contained HTML, Windows Forms, C#, document, input element, user control, custom control, text property] -->
```