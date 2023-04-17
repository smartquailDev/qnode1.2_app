
resource "digitalocean_droplet" "QNODE12" {
  image     = "ubuntu-22-04-x64"
  name      = "QNODE12"
  region    = "sfo3"
  size      = "s-1vcpu-1gb"
  user_data = "${file("docker.yaml")}"
  ssh_keys  = ["${digitalocean_ssh_key.qnd12.fingerprint}"]
}


