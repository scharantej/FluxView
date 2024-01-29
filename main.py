
# Import necessary modules
from flask import Flask, request, render_template, send_mail

# Create a Flask application
app = Flask(__name__)

# Define the home page route
@app.route('/')
def home():
    """Renders the home page."""
    return render_template('index.html')

# Define the about page route
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

# Define the contact page route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Handles the contact page and form submission."""
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Validate the data
        if not name or not email or not message:
            return render_template('contact.html', error="All fields are required.")

        # Send an email to the developers
        send_mail('noreply@example.com', 'New Contact Form Submission',
                  f'Name: {name}\nEmail: {email}\nMessage: {message}', ['developers@example.com'])

        # Display a success message
        return render_template('contact.html', success="Your message has been sent.")

    return render_template('contact.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
