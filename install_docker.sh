echo 'Installing Docker from the convenience script\n'
curl -sSL https://get.docker.com | sh

echo 'Enabling docker\n'
sudo systemctl enable docker
sudo systemctl start docker
sudo docker pull synoniem/pydPiper3
echo 'Testing docker\n'
sudo docker run -rm hello-world
