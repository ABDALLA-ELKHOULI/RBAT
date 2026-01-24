# 🐳 Installing Docker

## The Problem

The platform requires Docker to run, but Docker is not installed on your system.

## Solution: Install Docker

### For Ubuntu/Debian Linux

```bash
# Update package index
sudo apt-get update

# Install prerequisites
sudo apt-get install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up the repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Start Docker
sudo systemctl start docker
sudo systemctl enable docker

# Add your user to docker group (to run without sudo)
sudo usermod -aG docker $USER

# Verify installation
docker --version
docker compose version
```

### For Other Systems

- **Windows/Mac**: Download Docker Desktop from https://www.docker.com/products/docker-desktop
- **CentOS/RHEL**: Use `yum install docker-ce`
- **Fedora**: Use `dnf install docker-ce`

### After Installation

```bash
# Test Docker
docker run hello-world

# Navigate to RBAT directory
cd /home/user/RBAT

# Start the platform
docker compose up
```

Note: If you added yourself to the docker group, you may need to log out and log back in for the changes to take effect.

---

## Alternative: Run Without Docker (Manual Setup)

If you can't install Docker, see MANUAL_SETUP.md for running the platform without Docker.
