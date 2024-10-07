provider "azurerm" {
  features {}
  subscription_id = "b34e2b74-64a2-4394-8f65-075382a6f762"  # Remplace par ton ID de souscription
}


resource "random_string" "unique" {
  length  = 6
  upper   = false
  lower   = true
  numeric = true
  special = false
}

# Création du groupe de ressources
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location
}

# Création du compte Cosmos DB
resource "azurerm_cosmosdb_account" "main" {
  name                = "mycosmos${random_string.unique.result}"  # Nom Cosmos DB unique
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  offer_type         = "Standard"
  kind                = "MongoDB"

  consistency_policy {
    consistency_level = "Session"  # Niveau de consistance
  }

  geo_location {
    location          = azurerm_resource_group.main.location  # Même région que le groupe de ressources
    failover_priority = 0  # Priorité pour la reprise après sinistre
  }
}

# Création de la base de données MongoDB
resource "azurerm_cosmosdb_mongo_database" "main" {
  name                = var.mongo_database_name
  resource_group_name = azurerm_resource_group.main.name
  account_name        = azurerm_cosmosdb_account.main.name
}

# Création du compte de stockage
resource "azurerm_storage_account" "main" {
  name                     = "myblob${random_string.unique.result}"  # Nom de compte de stockage unique
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier            = "Standard"
  account_replication_type = "LRS"
}
