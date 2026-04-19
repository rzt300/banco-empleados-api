output "public_ip" {
  description = "IP publica del servidor"
  value       = aws_instance.banco_server.public_ip
}

output "instance_id" {
  description = "ID de la instancia EC2"
  value       = aws_instance.banco_server.id
}

output "security_group_id" {
  description = "ID del Security Group"
  value       = aws_security_group.banco_sg.id
}

output "url_api" {
  description = "URL de la API en produccion"
  value       = "http://${aws_instance.banco_server.public_ip}:5000/empleados"
}

output "url_health" {
  description = "URL del health check"
  value       = "http://${aws_instance.banco_server.public_ip}:5000/health"
}
