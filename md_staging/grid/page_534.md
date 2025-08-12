```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_534.jpeg
document_name: grid
page_number: 534
page_id: grid#page_534
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:22:59Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

2. When the cell to be zoomed is clicked, handle the CellClick event to display it as a zoomed cell. Here we use a PictureBox to show the magnified view of the cell content.

---

### Note: A PictureBox is a Microsoft's .NET Control used to display an image.

#### C#

```csharp
// Code to show zoom window.
private System.Windows.Forms.PictureBox zoomWindow;
private void gridControl1_CellClick(object sender, GridCellClickEventArgs e)
{
    if (e.RowIndex > 0 && e.ColIndex > 0)
    {
        if (checkBox1.Checked)
        {
            if (!zoomWindow.Visible)
                this.zoomWindow.Visible = true;
            Point pl = new Point(0, 0);
            Size s = new Size(this.gridControl1.ColWidths[e.ColIndex] + 10, this.gridControl1.RowHeights[e.RowIndex] + 5);
            s.Width += 50;
            s.Height += 30;
            Rectangle rect = new Rectangle(pl, s);
            zoomWindow.Size = s;

            Bitmap bmp = new Bitmap(s.Width, s.Height);
            Graphics g = Graphics.FromImage(bmp);
            GridStyleInfo style = gridControl1[e.RowIndex, e.ColIndex];
            float size = style.Font.Size;
            style.Font.Size = 15.5f;
            gridControl1.DrawSingleCell(g, e.RowIndex, e.ColIndex, rect, style, true, true);
            g.Dispose();

            this.zoomWindow.Image = bmp;
            this.zoomWindow.BorderStyle = BorderStyle.FixedSingle;
            this.zoomWindow.Visible = true;
            Point pt = this.gridControl1.ViewLayout.RowColToPoint(e.RowIndex, e.ColIndex, GridCellSizeKind.VisibleSize);
            pt.Y += 60;
            zoomWindow.Location = pt;

            style.Font.Size = size;
        }
    }
}
```

## API Reference

- **Properties**
  - `Visible`: `bool`
  - `Image`: `Image`
  - `BorderStyle`: `BorderSyle`
  - `Location`: `Point`
  - `Size`: `Size`

- **Methods**
  - `DrawSingleCell(Graphics g, int row, int col, Rectangle rect, GridStyleInfo style, bool horzAlign, bool vertAlign)`
  - `RowColToPoint(int row, int col, GridCellSizeKind kind)`

## Code Examples

The provided C# code demonstrates how to zoom a cell in a grid control. It involves creating a PictureBox to display the zoomed view, adjusting the size and location of the PictureBox dynamically based on the clicked cell's dimensions.

---

<!-- tags: [syncfusion, grid, zoom, windowsforms, picturebox] keywords: [cellclick, grid, zoomed, picturebox, magnified view] -->
```