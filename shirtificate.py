from fpdf import FPDF

# Create a custom class inheriting from FPDF
class Shirtificate(FPDF):
    def header(self):
        # Set font and size for the header
        self.set_font('Arial', 'B', 20)
        # Calculate the width of the text
        title_width = self.get_string_width('CS50 Shirtificate')
        # Calculate the position to center the text horizontally
        title_x = (self.w - title_width) / 2
        # Print the header text
        self.cell(0, 20, 'CS50 Shirtificate', align='C')

    def footer(self):
        # Set font and size for the footer
        self.set_font('Arial', 'I', 8)
        # Print page number centered on the bottom
        self.set_y(-15)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

    def shirtificate(self, name):
        # Set page format to A4 and orientation to portrait
        self.add_page(orientation='P', format='A4')
        self.set_auto_page_break(auto=True, margin=15)
        self.set_margins(20, 20, 20)

        # Add the shirt's image
        self.image('shirtificate.png', x=50, y=60, w=110)

        # Set font and size for the name
        self.set_font('Arial', 'B', 25)
        # Set the text color to white
        self.set_text_color(255, 255, 255)
        # Calculate the width of the name
        name_width = self.get_string_width(name)
        # Calculate the position to center the name horizontally
        name_x = (self.w - name_width) / 2
        # Print the name on top of the shirt
        self.cell(-190, 170, f"{name} took CS50", align="C")

        # Output the PDF to a file named 'shirtificate.pdf'
        self.output('shirtificate.pdf')

# Prompt the user for their name
name = input("Enter your name: ")

# Create an instance of the Shirtificate class
shirtificate = Shirtificate()
# Generate the shirtificate PDF
shirtificate.shirtificate(name)
