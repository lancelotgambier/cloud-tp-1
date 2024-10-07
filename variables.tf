variable "resource_group_name" {
  description = "Le nom du groupe de ressources"
  type        = string
}

variable "location" {
  description = "La localisation pour les ressources Azure"
  type        = string
  default     = "North Europe"  # Localisation par défaut
}

variable "mongo_database_name" {
  description = "Le nom de la base de données MongoDB dans Cosmos DB"
  type        = string
}
