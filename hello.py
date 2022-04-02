from reportlab.pdfgen import canvas
my_path='G:\\My drive\\testing\\pypdf2\\my_pdf.pdf' 
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
from temp_invoice import my_temp # import the template
from invoice_data import *  # get all data required for invoice

#my_prod={1:['Hard Disk',80,1],2:['RAM',90,2],3:['Monitor',75,2]}
c = canvas.Canvas(my_path,pagesize=letter)
c=my_temp(c) # run the template

c.setFillColorRGB(0,0,1) # font colour
c.setFont("Helvetica", 20)
row_gap=0.6 # gap between each row
line_y=7.9 # location of fist Y position 
total=0
for items in my_sale:
    c.drawString(0.1*inch,line_y*inch,str(my_prod[items][0])) # p Name
    c.drawRightString(4.5*inch,line_y*inch,str(my_prod[items][1])) # p Price
    c.drawRightString(5.5*inch,line_y*inch,str(my_sale[items])) # p Qunt 
    sub_total=my_prod[items][1]*my_sale[items]
    c.drawRightString(7*inch,line_y*inch,str(sub_total)) # Sub Total 
    total=round(total+sub_total,1)
    line_y=line_y-row_gap
c.drawRightString(7*inch,2.1*inch,str(float(total))) # Total 
discount=round((discount_rate/100) * total,1)
c.drawRightString(4*inch,1.8*inch,str(discount_rate)+'%') # discount
c.drawRightString(7*inch,1.8*inch,'-'+str(discount)) # discount
tax=round((tax_rate/100) * (total-discount),1)
c.drawRightString(4*inch,1.2*inch,str(tax_rate)+'%') # tax 
c.drawRightString(7*inch,1.2*inch,str(tax)) # tax 
total_final=total-discount+tax
c.setFont("Times-Bold", 22)
c.setFillColorRGB(1,0,0) # font colour
c.drawRightString(7*inch,0.8*inch,str(total_final)) # tax 
c.showPage()
c.save()
