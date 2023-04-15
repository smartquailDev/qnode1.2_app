#
# Exportamos nuestra key SSH

resource "digitalocean_ssh_key" "qnode12" {
  name       = "qnode12"
  public_key = "${file("id_rsa.pub")}"
}

