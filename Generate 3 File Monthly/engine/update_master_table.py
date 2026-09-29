from docx import Document

doc_path = r"C:\Users\901191\Music\Automasi EFS\Generate 3 File Monthly\engine\Template_Master\Master_Template_Notin.docx"
doc = Document(doc_path)

programs = [
    ("BNI GL Laporan Trial Balance Per Currency V2", "180", "{{P99_PROG_1}}"),
    ("BNI GL Laporan Trial Balance", "180", "{{P99_PROG_2}}"),
    ("Gather Schema Statistics", "630", "{{P99_PROG_3}}"),
    ("Accounting Program", "3", "{{P99_PROG_4}}"),
    ("FAH Process", "5", "{{P99_PROG_5}}"),
    ("Create Accounting", "3", "{{P99_PROG_6}}"),
    ("Transfer Journal Entries to GL", "5", "{{P99_PROG_7}}"),
    ("Program - Import Journals", "2", "{{P99_PROG_8}}"), # Often named 'Program - Import Journals' or 'Journal Import'
    ("Report Set", "80", "{{P99_PROG_9}}"),
    ("BNI FAH Journal Reversal", "30", "{{P99_PROG_10}}"),
    ("Validate Application Accounting Definitions", "180", "{{P99_PROG_11}}"),
    ("BNI GL Lap Jurnal Trx Entity", "30", "{{P99_PROG_12}}"),
    ("Subledger Period Close Exceptions Report", "5", "{{P99_PROG_13}}"),
    ("Update Subledger Accounting Balances", "3", "{{P99_PROG_14}}"),
    ("Posting: Single Ledger", "2", "{{P99_PROG_15}}"),
    ("OAM Dashboard Collection", "2", "{{P99_PROG_16}}"),
    ("Workflow Background Process", "8", "{{P99_PROG_17}}"),
    ("BNI GL Interface Kurs Harian", "1", "{{P99_PROG_18}}"),
]

# The target table is Table 3
table = doc.tables[3]

# Remove the 'Status' column (column index 4) if it exists
if len(table.columns) == 5:
    for row in table.rows:
        if len(row.cells) > 4:
            row.cells[4]._tc.getparent().remove(row.cells[4]._tc)

# Remove all rows except header
for i in range(len(table.rows)-1, 0, -1):
    row = table.rows[i]
    row._tr.getparent().remove(row._tr)

# Add the 18 rows
for i, prog in enumerate(programs):
    row = table.add_row()
    row.cells[0].text = str(i + 1)
    row.cells[1].text = prog[0]
    row.cells[2].text = prog[2]
    row.cells[3].text = prog[1]

# Set header text just to be sure
table.rows[0].cells[0].text = "No"
table.rows[0].cells[1].text = "Job Name"
table.rows[0].cells[2].text = "P99 (mins)"
table.rows[0].cells[3].text = "Duration Production"

doc.save(doc_path)
print("Table 3 in Master_Template_Notin updated!")
