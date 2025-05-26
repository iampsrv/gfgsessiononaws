# Update the package list
sudo apt update

# Install Apache web server (called 'apache2' on Ubuntu)
sudo apt install apache2 -y

# Start the Apache service
sudo systemctl start apache2

# Enable Apache to start on boot
sudo systemctl enable apache2

# Create a test HTML page
echo "Hello from EC2 on Ubuntu!" | sudo tee /var/www/html/index.html
