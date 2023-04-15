# Creamos un dominio nuevo
resource "digitalocean_domain" "islafloreana" {
  name = "islafloreanagalapagos.com"
  ip_address = digitalocean_droplet.QNODE12.ipv4_address
}

# Add a record to the domain
resource "digitalocean_record" "www" {
  domain = "${digitalocean_domain.islafloreana.name}"
  type   = "A"
  name   = "islafloreana"
  ttl    = "50"
  value  = "${digitalocean_droplet.QNODE12.ipv4_address}"
}

