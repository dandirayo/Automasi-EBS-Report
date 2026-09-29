from docx import Document

doc = Document(r"C:\Users\901191\Music\Automasi EFS\Generate 3 File Monthly\engine\Template_Master\Master_Template_Notin.docx")

for i, table in enumerate(doc.tables):
    print(f"--- Table {i} ---")
    if len(table.rows) > 0:
        row = table.rows[0]
        cells = [c.text.strip() for c in row.cells]
        print("Header:", cells)
        if len(table.rows) > 1:
            row2 = table.rows[1]
            cells2 = [c.text.strip() for c in row2.cells]
            print("Row 1:", cells2)
    print()
