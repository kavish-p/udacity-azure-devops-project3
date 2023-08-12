resource "azurerm_network_interface" "" {
  name                = ""
  location            = ""
  resource_group_name = ""

  ip_configuration {
    name                          = "internal"
    subnet_id                     = ""
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = ""
  }
}

resource "azurerm_linux_virtual_machine" "" {
  name                = ""
  location            = ""
  resource_group_name = ""
  size                = "Standard_DS2_v2"
  admin_username      = ""
  network_interface_ids = []
  admin_ssh_key {
    username   = "adminuser"
    public_key = file("/home/kavish/.ssh/id_rsa.pub")
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  # source_image_reference {
  #   publisher = "Canonical"
  #   offer     = "UbuntuServer"
  #   sku       = "18.04-LTS"
  #   version   = "latest"
  # }
  source_image_id = "/subscriptions/e85c2d28-e9aa-4775-85de-521be630b9fa/resourceGroups/Azuredevops/providers/Microsoft.Compute/galleries/gallery/images/def/versions/1.0.0"
}
